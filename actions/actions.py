from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import wikipediaapi
from transformers import pipeline
from googlesearch import search


page_to_section = {'Assembly language':4, 'Fortran':1, 'COBOL':0, 'BASIC':0, 'Logo (programming language)':0, 
        'C (programming language)':1, 'SQL':0, 'History of Python':1, 'Lua (programming language)':0,
        'Java (software platform)':1, 'JavaScript':0, 'Julia (programming language)':0, 
        'Go (programming language)': 0, 'Rust (programming language)': 0}

entity_to_page = {'assembly':'Assembly language', 'fortran':'Fortran', 'cobol':'COBOL', 
        'basic':'BASIC', 'logo':'Logo (programming language)', 
        'c':'C (programming language)', 'sql':'SQL', 'python':'History of Python', 
        'lua':'Lua (programming language)', 'java':'Java (software platform)', 
        'javascript':'JavaScript', 'julia':'Julia (programming language)', 
        'go':'Go (programming language)', 'rust':'Rust (programming language)'}

class ActionQA(Action):
    def name(self) -> Text:
        return "action_qna"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity = tracker.get_slot("topic")
        page = entity_to_page[entity]
        section = page_to_section[page]
        question = tracker.latest_message.get('text')
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(page)   

        qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')
        answer = qa_pipeline (context = str(page_py.sections[section]), question = question)
        dispatcher.utter_message(text=answer['answer'])
        return []


class ActionSum(Action):
    def name(self) -> Text:
        return "action_sum"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity = tracker.get_slot("topic")
        page = entity_to_page[entity]
        section = page_to_section[page]
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(page)   
        summarizer = pipeline("summarization", model='sshleifer/distilbart-cnn-12-6')
        summary = summarizer(str(page_py.sections[section])[:1024])
        dispatcher.utter_message(text=f"Here is a summary of history of {entity}")
        dispatcher.utter_message(text=summary[0]['summary_text'])
        dispatcher.utter_message(text="------------------------")
        dispatcher.utter_message(text="Here are list of top websites on google for futher study:")
        google_query = f"History of {entity}"
        for j in search(google_query, tld="co.in", num=4, stop=4, pause=2):
            dispatcher.utter_message(text=j)
        
        return []



