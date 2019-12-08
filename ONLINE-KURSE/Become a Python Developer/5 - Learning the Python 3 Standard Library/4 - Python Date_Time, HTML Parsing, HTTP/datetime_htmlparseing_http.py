#1 - Getting the current time with Python
from datetime import datetime  #von datetime-Modul die Klasse datetime importieren

now = datetime.now()

print(now.date())  #Datum ausgeben

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)

print(now.time())  #hh.mm.ss -> mittels Funktion

print()
#2 - Formatting dates and times in Python with datetime
from datetime import datetime

now = datetime.now()

#Formatierte String für Datumausgabe  - strftime():
# %a = Wochentag als kurzer Name
# %A = Wochentag als Name
# %d = Wochentag als Zahl (0-6)
print(now.strftime("%a %A %d"))
# %b = Monatsname kurz
# %B = Monatasname lang
# %m = Monat als Zahl
print(now.strftime("%b %B %m"))

print(now.strftime("%a %B %d"))

# %H = Stunden
# %M = Minuten
# %S = Sekunden
# %p = PM/AM
print(now.strftime("%H:%M:%S %p"))

# %y = Jahr (19)
# %Y = Jahr (2019)
print(now.strftime("%y %Y"))

print()
#3 - Calculating future times and Pyhton calendar
from datetime import datetime, timedelta  #auch noch die Klasse timedelta importieren

now = datetime.now()

testDate = now + timedelta(days=2)  #testDate ist dann vom Typ datetime
myFirstCourse = now - timedelta(weeks=3)

print(testDate.date())  # => kann man Methoden von datetime-Klasse nutzen
print(myFirstCourse.date())

if testDate > myFirstCourse:
    print("Comparison works")

import calendar  #Modul calendar importieren (calendar = Monat im formatierter Kalendarausgabe
cal = calendar.month(2001, 10)
print(cal)
cal2 = calendar.weekday(2001, 10, 11) # welcher Wochentag ist 2001, Nov, 11 (Donnerstag => 3)
print(cal2)

print(calendar.isleap(1999))  # => Fasle
print(calendar.isleap(2000))  # => True

print()
#4 - Create a timer with Python time
import time

#Bsp: Timer 10 Sekunden laufen lassen
run = input("Start? >")
seconds = 0
if run == "yes":
    while seconds != 10:
        print("> ", seconds)
        time.sleep(1)  #für 1. Sekunde schlafen gehen
        seconds += 1
    print("> ", seconds)  #damit am Ende auch die 10 ausgegeben wird



print()
#5 - Pyhton HTML parser
from html.parser import HTMLParser  #HTML-Code parsen => HTMLParser-Klasse importieren

class HTMLParser(HTMLParser):  #eignene HTMLParserklasse, die von Python HTMLParser-Klasse erbt.
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr: ", attr)

    def handle_endtag(self, tag):
        print("End tag: ", tag)

    def handle_comment(self, data):
        print("Comment: ", data)

    def handle_data(self, data):
        print("Data: ", data)

parser = HTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!-- Hi--> I am a coder </h1></body></html>")

input = input("put HTML code")
parser.feed(input)

htmlFile = open("test.html", "r")
s = ""
for line in htmlFile:  #da der Parser html-Code als eine Zeile braucht => muss man zuerst html-Code in .html zu einem String ohne \n machen  <= oder man kann das direkt im handler programmieren, sodass er \n nicht ausgibt
    s += line
parser.feed(s)

print()
#6 - Text wrap module
import textwrap  # Text formatieren

websiteTest = """  Learnin can happen anywhre 
    Das ist nur ein Test
    Ha Ha!
"""

print("No Dedent: ")
print(textwrap.fill(websiteTest))  #ohne Formatierung ausgeben

print("Dedent")
dedentText = textwrap.dedent(websiteTest.strip())  #Leerzeichen am Anfang der Zeile löschen
print("Fill")
print()
print(textwrap.fill(dedentText, width=50))  #Ausgabe ist nur width-Zeichen breit
print("Controlling Indent")
print(textwrap.fill(dedentText, initial_indent="   ", subsequent_indent="           "))  #indent = Abstand der Zeile von linker Seite (initial = erste Zeile, subsequent = weiteren Zeilen
print("Shortening Text")
short = textwrap.shorten("LinkedIn.com is great", width=15, placeholder="...")  #width = wieviele Zeichen ausgegeben werden, placeholder = wie die unterdrückten Zeichen auf Bildschirm ausgegeben werden
print(short)

print()
#7 - Python HTTP package, urllib, and JSON

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
#<- wie googleapis funktioniet => https://developers.google.com/books

#HTML per Python holen
import urllib.request
import json
import textwrap

with urllib.request.urlopen("ttps://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:  # wenn urllib.xxx funtioniert, dann nennen wir ihn f
    text = f.read()  #URL-Request lesen
    decodedText = text.decode("utf-8")  #Text in utf-8 umformen
    print(textwrap.fill(decodedText, width=50))  #formatiet ausgegeben

    print()
    obj = json.loads(decodedText)  #~ parst Json Format in python-Json-Objekt
    print(obj["kind"])
    print(obj["items"][0]["searchInfo"]["textSnippet"])  #auch wenn JSON nur ein Feld hat => mit ["feld][0] ansprechen

