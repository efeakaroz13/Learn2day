#Developed by Efe Akaröz
#2 November 2022
from flask import Flask,render_template,request,redirect
import requests
import json
#from googletrans import Translator
import translators as ts
import wikipedia
from bs4 import BeautifulSoup 

app = Flask(__name__)
@app.route("/")
def home():
    out = json.loads(requests.get("https://random-word-api.herokuapp.com/word").content)
    out = out[0]
    meaning = ts.google(out,from_language='en', to_language='tr')
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(wikipedia.search(out)[0],auto_suggest=False) 
    
    except wikipedia.DisambiguationError as e1:
        summary = wikipedia.summary(e1.options[0])
        
    except Exception as e:
        print(e)
        summary = ""

    summarytr= ts.google(summary,from_language="en",to_language="tr")
    page = requests.get("https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X".format(out.replace(" ","+")))
    soup = BeautifulSoup(page.content,"html.parser")
    allimages = soup.find_all("img")
    imgout = []
    for l in allimages:
        src= l.get("src")
        try:
            src.split("https")[1]
            imgout.append(src)
        except:
            pass

    data =  {"word":out,"meaning":meaning,"summary":summary,"images":imgout,"summarytr":summarytr}
    #return data


    return render_template("index.html",data=data)


app.run(debug=True)
