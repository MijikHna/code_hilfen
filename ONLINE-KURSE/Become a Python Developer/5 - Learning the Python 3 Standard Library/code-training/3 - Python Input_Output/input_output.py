#1 - Command line arguments

#python3 input_output.py 0 1 2
#in CLI ist alles immer ein String
import  sys  #um auf die CLI-Param zugreifen zu können

sys.argv
print("Number of arguments: " + str(len(sys.argv)))
print("Arguments: ", sys.argv)
#<- erstes Argument ist Name (bzw. Pfad der Datei)

sys.argv.remove(sys.argv[0])  #erstes Argument löschen. Funktioniet mit remove, da argv ist eine Liste
print("Arguments: ", sys.argv)

arguments = sys.argv
sum = 0
for i in arguments:
    try:  #hier wird veruch in Zahl zu konvertieren
        number = int(i)
        sum = sum + number
    except e:
        print("Keine Zahl")
print(sum)


print()
#2 - Input and Output
print("Hello !")
color = input("What is your favourite color? ")  #Eingaben aus CLI einlesen
print("Your color: " + color)

print()
#3 - Files and file writing
myFile = open("scores.txt", "w")
#w -> write; r -> read; r+ -> read and write; a -> append

#Eigenschften der Datei
print("Name " + myFile.name)
print(("Mode " + myFile.mode))

myFile.write("GBJ : 100 \nKHD : 99 \nBBB : 89\n")
myFile.close()

myFile = open("scores.txt", "r")
print("Reading ...\n" + myFile.read())
myFile.seek(0, 0)
print("Reading... " + myFile.read(10))  #liest nur 10 Char.
myFile.close()


print()
#4 - File seeking in Python
#Seek-Pointer = zeigt auf Char in Datei, wenn man aus/in Datei liest/schreibt => wird dieser Seek-Pointer verschoben
#Beim öffnen der Datei wird Seek-Pointer auf 0 gesetzt.
myFile = open("scores.txt", "r")
print("Reading... " + myFile.read(10))  #liest nur 10 Char.
myFile.seek(0)
print("Reading... " + myFile.read(10))  #liest nur 10 Char.
myFile.close()

print()
#5 - Iterative files
# = Datei zeilenweise lesen
myFile = open("scores.txt", "r")
print("One line : " + myFile.readline())
myFile.seek(0)
print("One line : " + myFile.readline())

for line in myFile:
    newHeighScorer = line.replace("BBB", "PDJ")  # in der Zeile: BBB durch PDJ ersetzen <- !! nicht in der Datei erstetz sondern im String line
    print(newHeighScorer)
myFile.close()

print()
#6 - Tempfile
import tempfile  # um Temporäre Dateien zu benutzen

tempFile = tempfile.TemporaryFile()
tempFile.write(b"Save this special number for me: 567896")  #in Tempfile schreiben, braucht aber Byte-Object => b davor
tempFile.seek(0)
print(tempFile.read())  #alles aus dem Tempfile lesen

print()
#7 - Manipulate zip files in Python

import zipfile

zip = zipfile.ZipFile("archiv.zip", "r")  #zip-Datei öffnen
print(zip.namelist())

#Metadaten auslesen
for meta in zip.infolist():
    print(meta)

info = zip.getinfo("purchased.txt")  #Metadaten bestimmter Datei
print(info)

print(zip.read("scores.txt"))

with zip.open("scores.txt") as f:  #öffnet wishlist.txt in zip-Datei und konvertiert es zu file (as f)
    print(f.read())

#zip.extract("purchase.txt")  # Datei aus Zip auspacken und speichern
#zip.extractall()

zip.close()