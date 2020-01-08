# 3 - Parsing and processing HTML

# import the HTMLParser module
# in Python 3 you need to import from html.parser

#Bsp = HTML-Parser etstellen

from html.parser import HTMLParser

#Globale Variable um Meta-Tags zu zählen
metacount = 0;

# create a subclass of HTMLParser and override the handler methods
#eigene Klasse von HTMLParser-Klasse ableiten
class MyHTMLParser(HTMLParser):
  # function to handle an opening tag in the doc
  # this will be called when the closing ">" of the tag is reached

  #wird aufgefuen wenn bei <tag> > erreicht wurde 
  def handle_starttag(self, tag, attrs):
    global metacount
    if tag == "meta":
      metacount += 1

    print ("Encountered a start tag:", tag)
    pos = self.getpos() # returns a tuple indication line and character
    print ("\tAt line: ", pos[0], " position ", pos[1])

    if attrs.__len__() > 0: #checken die Länge des Übergabeparam attrs.
      print ("\tAttributes:")
      for a in attrs:
        print ("\t", a[0],"=",a[1])
      
  # function to handle the ending tag
  def handle_endtag(self, tag):
    print ("Encountered an end tag:", tag)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])
    
  # function to handle character and text data (tag contents)
  #gibt Zeilen und Spaltennummer des Inhalts des Tags
  def handle_data(self, data):
    if (data.isspace()):
      return
    print ("Encountered some text data:", data)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])
  
  # function to handle the processing of HTML comments
  #handle_comment von HTMLParser wird überschrieben
  def handle_comment(self, data):
    print ("Encountered comment:", data)
    #gibt Linenummer des Kommentars und Char-Position des Kommentars also Zeile und Spalte
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
    
  # open the sample HTML file and read it
  f = open("samplehtml.html")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)
  
  print ("%d meta tags encountered" % metacount)

if __name__ == "__main__":
  main();
  
