import os
import multiprocessing
import requests

def get():
    while True:
        try:
            page = requests.get("https://awazel.com",proxies={"http":"socks5://127.0.0.1:9050","https":"socks5://127.0.0.1:9050"},headers={"User-Agent":"mozilla firefox your mom is hilarious"})
            print("GET | ",str(page.content).split("<title>")[1].split("</title>")[0])
        except:
            print("E")
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=get)
    p2 = multiprocessing.Process(target=get)
    p3 = multiprocessing.Process(target=get)
    p4 = multiprocessing.Process(target=get)
    
    p5 = multiprocessing.Process(target=get)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    
