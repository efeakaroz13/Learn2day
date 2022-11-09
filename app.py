#Developed by Efe Akaröz
#2 November 2022
from flask import Flask,render_template,request,redirect
import requests
import json
#from googletrans import Translator
import translators as ts
import wikipedia
from bs4 import BeautifulSoup 
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    """
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

    """
    data=json.loads(requests.get("http://127.0.0.1:5000/api?lang=tr").content)
    
    return render_template("index.html",data=data)


@app.route("/api")
def api():
    os.system("python3 scraper.py")
    jsonloader = json.loads(open("out.json","r").read())
    try:
        jsonloader["summary"]
    except:
        jsonloader["summary"] = "-"

    language = request.args.get("lang")
    
    summary = jsonloader["summary"]
    if language == None:
        return jsonloader
    if language != None or language != "en":
        try:
            if summary != "-":
                summarytranslated= ts.google(summary,from_language="en",to_language=language)
            else:
                summarytranslated="-"
            
            wordtranslated = ts.google(jsonloader["word"],from_language="en",to_language=language)
            jsonloader["wordtranslated"] = wordtranslated
            jsonloader["summarytranslated"]= summarytranslated
        except Exception as e:
            jsonloader["wordtranslated"] = "-"
            jsonloader["summarytranslated"]= "-"
            jsonloader["supported"] = ['af', 'ak', 'am', 'ar', 'as', 'ay', 'az', 'be', 'bg', 'bho', 'bm', 'bn', 'bs', 'ca', 'ceb', 'ckb', 'co', 'cs', 'cy', 'da', 'de', 'doi', 'dv', 'ee', 'el', 'en', 'en-US', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gn', 'gom', 'gu', 'ha', 'haw', 'hi', 'hmn', 'hr', 'ht', 'hu', 'hy', 'id', 'ig', 'ilo', 'is', 'it', 'iw', 'ja', 'jw', 'ka', 'kk', 'km', 'kn', 'ko', 'kri', 'ku', 'ky', 'la', 'lb', 'lg', 'ln', 'lo', 'lt', 'lus', 'lv', 'mai', 'mg', 'mi', 'mk', 'ml', 'mn', 'mni-Mtei', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'nso', 'ny', 'om', 'or', 'pa', 'pl', 'ps', 'pt', 'qu', 'ro', 'ru', 'rw', 'sa', 'sd', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'ti', 'tk', 'tl', 'tr', 'ts', 'tt', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yi', 'yo', 'zh-CN', 'zh-TW', 'zu']
            jsonloader["docs_warning"] = "You can read the docs from https://github.com/efeakaroz13/Learn2day"
        


    return jsonloader




app.run(debug=True)
