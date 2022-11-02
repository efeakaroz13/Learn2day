#Developed by Efe Akaröz
#2 November 2022
from flask import Flask,render_template,request,redirect
import requests
import json
#from googletrans import Translator
import translators as ts


app = Flask(__name__)
@app.route("/")
def home():
    out = json.loads(requests.get("https://random-word-api.herokuapp.com/word").content)
    out = out[0]
    meaning = ts.google(out,from_language='en', to_language='tr')
    return {"word":out,"meaning":meaning}
    return render_template("index.html")


app.run(debug=True)
