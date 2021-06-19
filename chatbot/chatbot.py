from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
'''flask: maps http reqs to python func. 
    Runs python code and shows result in browser'''
#render: retrive content from html file
#request: to req the data
# Corpus trainer: to train the machine, nlp, pair in all our languages
#we are making a self learning chatbot

app=Flask(__name__)

'''this is for storing our data
"Chatterbot" is the username, storage adap is for creating the database'''
eng_bot=ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
#train data
trainer=ChatterBotCorpusTrainer(eng_bot)
#this is for the custom data:
trainer.train("chatterbot.corpus.english")
#making our own data:
trainer.train("data/data.yml")

@app.route("/")
def index():
    return render_template("index.html")  #to send context to html file

@app.route("/get") #to get bot response
def get_bot_response():
    userText=request.args.get("msg") #get data from input where we write js to index.html
    return str(eng_bot.get_response(userText))

if __name__=="__main__":
    app.run(debug=True) 