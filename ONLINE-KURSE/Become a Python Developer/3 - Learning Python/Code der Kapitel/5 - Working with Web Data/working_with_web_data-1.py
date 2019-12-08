# 1 - Fetching Internet data 

#Modul mit Klasse um HTML Request zu machen
import urllib.request # instead of urllib2 like in Python 2.7

def main():
  # open a connection to a URL using urllib2
  #gibt Response-Objekt zurück
  webUrl = urllib.request.urlopen("http://www.google.com")
  
  # get the result code and print it
  #Status des Responses ausgeben .getcode()
  print ("result code: " + str(webUrl.getcode()))
  
  # read the data from the URL and print it
  #HTML-Inahlt auslesen
  data = webUrl.read()
  print (data)

if __name__ == "__main__":
  main()
