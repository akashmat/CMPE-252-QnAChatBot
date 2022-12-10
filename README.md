# CMPE-252-QnAChatBot

Rasa Version: 3.1

#### Running the BOT
Run the following commands in CLI:
1. Clone the Repository
```
git clone https://github.com/akashmat/CMPE-252-QnAChatBot.git
```
2. Create a python environment
```
python3 -m venv env-name
```
3. Activate the environment
```
source env-name/bin/activate
```
5. Move in the repository
```
cd CMPE-252-QnAChatBot
```
7. Install the packages into the environment (Note: the packages are specific to MacOS)
```
pip install -r requirements.txt
```
8. Run Rasa SDK Actions server:
```
rasa run actions
```
9. Open another tab in CLI and activate the environment in the same way as above and move into the repo
10. Run rasa CLI
```
rasa run
```

#### Issues:
1. The chatbot uses BERT Models from HuggingFace. When you run inference for the first time, as the custome action is called, the model will downloaded from the internet. They are big models (100s of MB) and due the download, the rasa actions server will timeout for the first time. The model will however save in the cache and should work fine if you close the rasa server and run them again.
2. The chatbot answers questions about the history of the following programming languages: Assembly, Fortran, COBOL, BASIC, LOGO, C, SQL, Python, Lua, Java, JavaScript, Julia, Go, Rust. The bot is designed to choose the languages as intents so try avoiding questions that directly refer to the same 
language in the subsequent questions.

Conversation Flow 1:
1. Send a greeting: Hi, hey. 
2. Bot: greets back asking which programming language you would be interested in.
3. You: julia
4. Bot: What do you want to know about the history of julia?
5. You: Can ask "ANY FACTUAL" question from the [history](https://en.wikipedia.org/wiki/Julia_(programming_language)#History) section the programming language Julia. Just for e.g., 'What award did the co-creators win?'
6. Bot:James H. Wilkinson Prize for Numerical Software. Did that help you?
7. You: If you answer with an affirmation, the bot will keep asking you to type in the questions. But if no, it will give the summary of the section from wikipedia and give links to google regarding the same topic for further reference. E.g: no
8. Here is a summary of history of julia: 'Work on Julia was started in 2009...'
9. Restart the bot for another conversation.

Conversation Flow 2:
1. You: Hey
2. Bot: Hey! How are you? What language are you interested in?
3. You: rust
4. What do you want to know about the history of rust?
5. Can ask "ANY FACTUAL" question from the [history](https://en.wikipedia.org/wiki/Rust_(programming_language)#History) section the programming language Julia. For e.g., 'who are the founding companies?'
6. Bot: AWS, Huawei, Google, Microsoft, and Mozilla. Did that help you?
7. You: yes
8. Bot: What do you want to know about the history of rust?
9. You: Continue asking questions. For e.g., when did the compiler successfully compile itself?
10. Bot: 2011.  Did that help you?
11. You: yes
12. Bot: What do you want to know about the history of rust?
13. You: what is servo?
14. Bot: a browser engine. Did that help you?
15. You: no
16. Bot: Here is a summary of history of rust: 'Rust grew out of a personal project begun in 2006...."
------------------------
Here are list of top websites on google for futher study:
https://en.wikipedia.org/wiki/Rust_(programming_language)
and other links in google search

17. End
