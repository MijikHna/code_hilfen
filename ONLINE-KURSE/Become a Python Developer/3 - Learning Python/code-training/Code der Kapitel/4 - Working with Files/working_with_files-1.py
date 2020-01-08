# 1 - Reading and writing files

# Open a file for writing and create it if it doesn't exist
# + = Datei erstellen falls schon existiert
f = open("textfile.txt", "w+")


# write some lines of data to the file
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")
  
# close the file when done
f.close()
  
# Open the file back up and read the contents
f = open("textfile.txt", "r")

if f.mode == "r":
    #wird ganze Datei ausgelesen
    contents = f.read()
    print(contents)
f.close()

f = open("textfile.txt", "r")
if f.mode == 'r':
    fl = f.readlines()
    for x in fl:
        print(x)
f.close()
# Open the file for appending text to the end
f = open("textfile.txt", "a")
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")
f.close()  

# 2 - Working with OS path utilities

#Klassen um mit Verzeichnisse und OS zu arbeiten
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Item exists: " + str(path.exists("textfile.txt")))
print ("Item is a file " + str(path.isfile("textfile.txt")))
print("Item is a directory " + str(path.isdir("textfile.txt")))  
# Work with file paths
print ("Item path: " + str(path.realpath("textfile.txt")))
#trennt Pfad und Dateiname
print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))
  
# Get the modification time
#path.getmtime()  = gibt das Änderungsdatum zurück
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) 
# Calculate how long ago the item was modified
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print("It has been " + str(td) + " since the file was modified")
print("Or, " + str(td.total_seconds()) + "seconds")


# 3 - Using file system shell methods
# = Dateien manipuliren mit Hilfe der Shell-Utilities
from os import path
import shutil
# make a duplicate of an existing file
if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt") 
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    #kopiert nur Inhalt der Datei, Dateieigenschaften nicht
    shutil.copy(src, dst)
        
    # copy over the permissions, modification times, and other info
    #kopiert Inhalt + Dateieigenschaften
    shutil.copystat(src, dst)

    # rename the original file
    os.rename("textfile.txt", "newfile.txt")
    os.rename("newfile.txt", "textfile.txt")
    
    # now put things into a ZIP archive
    from shutil import make_archive
    root_dir, tail = path.split(src)
    shutil.make_archive("arhive", "zip", root_dir)

# more fine-grained control over ZIP files
    from zipfile import ZipFile
    #Konstruktor aufruf für ZipFile() + Name des Objket is dann newzip
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")
