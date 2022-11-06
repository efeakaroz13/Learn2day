#Author:Efe Akaröz
#5 November 2022

import requests
from bs4 import BeautifulSoup
import random
import json
import multiprocessing

requests_session = requests.Session()
def getwiki():
    while True:
        try:
            oldjson = json.loads(open("out.json","r").read())
            word=  oldjson["word"]
            break 
        except:
            pass

    print(word)
    page = json.loads(requests_session.get("https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json".format(word)).content)
    summary_ = page["query"]["search"][0]["pageid"]
    summary = json.loads(requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&pageids={}".format(summary_)).content)["query"]["pages"][str(summary_)]["extract"]
    oldjson = json.loads(open("out.json","r").read())
    oldjson["summary"] = summary 
    open("out.json","w").write(json.dumps(oldjson,indent=4))


def getimage():
    while True:
        try:
            oldjson = json.loads(open("out.json","r").read())
            word=  oldjson["word"]
            break 
        except:
            pass
    page = requests_session.get("https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X".format(word.replace(" ","+")))
    soup = BeautifulSoup(page.content,"lxml")
    allimages = soup.find_all("img")
    imgout = []
    for l in allimages:
        src= l.get("src")
        try:
            src.split("https")[1]
            imgout.append(src)
        except:
            pass
    oldjson = json.loads(open("out.json","r").read())
    oldjson["images"] = imgout 
    open("out.json","w").write(json.dumps(oldjson,indent=4))

def selectword():
    worder = open("words.txt").readlines()
    word = random.choice(worder).replace("\n","")
    data = {"word":word}
    open("out.json","w").write(json.dumps(data,indent=4))


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=getimage)
    p2 = multiprocessing.Process(target=getwiki)
    p3 = multiprocessing.Process(target=selectword)
    p3.start()
    p1.start()
    p2.start()
    p2.join()
    p3.join()
    p1.join()

