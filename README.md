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

##### Issues:
1. The chatbot uses BERT Models from HuggingFace. When you run inference for the first time, as the custome action is called, the model will downloaded from the internet. They are big models (100s of MB) and due the download, the rasa actions server will timeout for the first time. The model will however save in the cache and should work fine if you close the rasa server and run them again.
2. The chatbot answers questions about the history of the following programming languages: Assembly, Fortran, COBOL, BASIC, LOGO, C, SQL, Python, Lua, Java, JavaScript, Julia, Go, Rust. The bot is designed to choose the languages as intents so try avoiding questions that directly refer to the same 
language in the subsequent questions.
