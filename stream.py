from twython import TwythonStreamer
import time
import json

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            #print(data['lang'])
            tmp = json.dumps(data)
            jfile = open("test034.json","a")
            jfile.write(tmp +'\n')
            print("save")
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print (status_code, data)

# Requires Authentication as of Twitter API v1.1


keys = [["iepKI7tbrRmsOje7rXHhMx3gb", 
    "78yIf9nYz4maCfmOr4iny8bgORNB7jMKyIxwgBgoAhoaVfYL0Z",
    "2745377661-eUIdWW2fKze1n3DHQfeYoYL0O9cp1m04Jl3W5vS", 
    "4lAeJsHTqkcqf3xZgcEBUJyQp5THBH1U74q6ELtSp4UGl"],
    ["1Bhdgk7wmjnl4ERwXqRPLoRiv",
    "T0bCa2LYxvC8pjrZteXgDV1XwxAkisfdI04VAqLfp7ZYJXQfLR",
    "1728020275-apYpd9t9AC97dgloZ63weTsPNDHtV9uAVUQMHae",
    "S4jYFFLcaCEMxdwJ87Me3clT3DSFO17eh1fScRLxs6lzB"],
    ["yKYVhELv1RpAqEun8kjjvlCWM",
    "3bSxheOyKpufuKnRRtyAbbKDRkWlETSd1xsGSQbzbdIZHmXd9u",
    "114558773-mICyqDNtU2GZC11luq2FgesfDj1MsgzJbbOAjTp0",
    "LnpTkBqgcDKcOd2UNJMIiR7Ine2BJoPtHJtWYWo1WLzIj"],
    ["yKYVhELv1RpAqEun8kjjvlCWM",
    "3bSxheOyKpufuKnRRtyAbbKDRkWlETSd1xsGSQbzbdIZHmXd9u",
    "114558773-mICyqDNtU2GZC11luq2FgesfDj1MsgzJbbOAjTp0",
    "LnpTkBqgcDKcOd2UNJMIiR7Ine2BJoPtHJtWYWo1WLzIj"],
    ["LA2vRhqRSgeQyhZJZ1iLoYqud",
    "6lmAfPnJnWDupssWqDmio8LPKR7fbBJBDr97bbh2ZjejYyPeSh",
    "977621309411782657-wZWrLbqfQKxAyR1q6xpyfg8Q0yRsC1p",
    "gB0yULCq9YQUYUJUKdQbv223T550YZutdqt3W0tUjEBUK"],
    ["gsVX1tpgMhUvtogIlyMUQrQWy",
    "65KCx8AKjx1TDlxzBXI7cPv1DvPCH9Qu5z0zigqOkkQwcc3gKo",
    "2430797575-KGIkZxU9tixqfDctb0PjM4q7ia9wlUorTS9Bdle",
    "MIfouMiG0qSuI5TYgSr386MjoOpJF522PXs0Hy4n41Ll2"],
    ["hMNRInIGobzKmPW4LRuXdOdur",
    "4pvs6A549iLgPsKArCVs0IPXPoj9n8El0m5jqZAA7m4TjUpaOh",
    "1096947192-tWvxYYYy1SjBzFZpVsWk4vY3ioJhMzYMS8T8rox",
    "dUbq1QYxibuYoWgICQtiNLiSxB3jCP3lE73DON12rJPVr"]
    ]

words = ['la','el','de','tu','que','del','lo','no','si',
    'un','eres','mi','es','una','se','las','los','por',
    'para','como','sus']


def readBadWords():
    bwfile = open("badWords.txt","r")
    bw = []
    for word in bwfile:
        tmp = word.split('\n')
        bw.append(tmp[0])
    return bw
        


def streamingData():
    for token in keys:
        try:
            stream = MyStreamer(token[0],token[1],token[2],token[3])
            stream.statuses.filter(track=words,languages=['es'])
        except Exception as e:
            print("other tokens")
            continue


def streamingTest():
    for token in keys:
        try:
            stream = MyStreamer(token[0],token[1],token[2],token[3])
            stream.statuses.filter(track=readBadWords(),languages=['es'])
        except Exception as e:
            print("other tokens")
            continue
    
i =0
j = int(input("ingrese el numero de iteraciones: "))
while i < j :
    i+=1
    #streamingData()
    streamingTest()
    time.sleep(30)

#readBadWords()


