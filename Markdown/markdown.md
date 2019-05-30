# 1 - Markdown Basics
https://guides.github.com/features/mastering-markdown/
### 1 - What is Mardown?
* Markdown = Plaintext, das mit entsprechenden Tools zur Dokumentation konvertiert wird.
* ist sehr leicht zu lesen/schreiben/lernen

  * Headline
    ========
  * `Headline und ======= darunter`
  * __test__ <- mit `__` vor nach test = hervorheben

* Markdown ist leicht konvertierbar in andere Formate
* Es gibt viele Erweiterungen

### 2 - Using Markdown tools
* Fast alle Editoren haben eingebaute MD-Erweiterungen
  * z.B bei Atom => Packages -> Markdown Preview -> ...
* __Stackedit__ = Online-Tool für MD (Online MD-Editor) <- sehr gut auch zum lernen + viele Features z.B Publish, Convert to HTML usw.
* Wichtig zu verstehen, wie es dann nach HTML konvertiert wird (sehr hilfreich dazu __Stackedit__ <- da kann man direkt die konvertierten HTML-Tags anschauen).

### 3 -Basic span elements
* Manchmal funtioniert Parsen nicht richtig => einfach mit Enter und Space spielen

* __Fett__ => `_Fett_`
* **Fett** => `**Fett**`
* _Kursiv_ => `_Kursiv_`
* *Kursiv* => `*Kursiv*`

* => `* ` - ungeordnete Liste
* * `Code snippet` => `` `Code Snippet` `` - Code im Text
* \` => ` \` ` unformaitert ausgeben`
* wenn man MD-Datei später mit bestimmter HTML-Formatierung zu HTML konvertieren möchte => einfach die HTML-Tags mit gewünschten Styles benutzen. Es wird zwar nicht im MD-Betrachter angezeigt. Nach der konvertierung zu HTML wird es aber in HTML vorhanden sein

### 4 - Paragraphs and headers

    Absatz als Code.
* => doppelter TAB oder mehrere Spaces   

* **Space -> Space -> STRG+Enter** = erzwungener Zeilenumbruch
Kopfzeile1
==
* => wenn man unter einer Zeile `==` oder mehr eingibt => wird zur Kopfzeile
Kopfzeile2
--
* => wenn man unter einer Zeile `--` oder mehr eingibt => wird zur Kopfzeile  
__ODER__  
* `# ` ist gleich `<h1>`, `## ` ist gleich `<h2>` usw. Manchmal aus Lesbarkeitsgründen werden auch `#` am Ende hinzugefügt.

### 5 - Blockqoutes

> Blockzitat1

>Blockzitat2

>> Blockzitat2.1

>>Blockzitat2.2

* => am Anfang `>` einfügen => wird zur Blockzitat. Um Blockzitat zu beenden = __Enter -> Enter__
* => am Anfang `>>` einfügen => Blockzitat in Blockzitat
* wird aber oft zur Trennung der Paragraphs benutzt


### 6 - Horizontal rules
---
***
___
* `---` oder `***` oder `___`. Drei ist Minimum. Dazwischen können auch Spaces stehen, hauptsache **DREI**
### Using lists
*
-
+
* `*` oder `-` oder `+` = ungeordnete Liste. Eventuell mit Spaces oder TABs Einrückungen machen.

1. Test 1
2. Test 2
       Test 2 Weiter
* mit `1.`, `2.` = ungeordnete Liste.
* falls in dem Listeneintrag Code stehen sollte => mehr als 4 Spaces eingeben

### 7 - Creating links
* [Link1](http://google.de "Zu Google") => Inline-Link, "Zu Google = title von `<a>`
* <http://google.de> => mit `< ... >` => Rawer Link.
* <kirill@test.de> => wird zu mailto in HTML
* [Link2][1] => Inline-Link, "Zu Google = title von `<a>`
* [Link2][textlabel] => Inline-Link, "Zu Google = title von `<a>`

[1]:http://google.de
[textlabel]:http://google.de
* diese Labels werden dann ganz unten im Dokument erstellt.

### 8 - Adding images
> Inline-Image:
- ![Test1](file:///home/kirill/Bilder/ICONs/telegram.png)
- ![Test1][1]
- also wie bei Links nur mit `!` am Anfang

[1]:file:///home/kirill/Bilder/ICONs/telegram.png "Test Foto"

> Link über Bild
* [![Test1](file:///home/kirill/Bilder/ICONs/telegram.png)](http://google.de)
* Also in `[ ]` einfach den Inline-Image einfügen

* irgendwie muss Image über http erreichbar sein

# 2 -Beyound Markdown

### 1 - GitHub Flavored Markdown
> * GMF ignoriert alle Tags die Unterschrieche haben
* hat zusätzlich Durchgestrichen ~~Test~~ `~~Test~~`
* [x] oder [ ] hat Checkboxen `[x]` bzw. `[ ]`
* https werden automatisch als Links erkannt
* Fenced Codeblock
* hat Tabellen

> * wenn man TAB vor einer Codezeile macht => wird als Code, sonst als Plaintext.
* man kann auch  *\`\`\`* für Code Verwenden <- oft wir direkt nach öffnendem  *\`\`\`* die Sprache angegeben, damit die Syntax etwas angepasst wird.

### 2 - Working with tables
Eins | Zwei | Drei | Vier
---| ---:|:---|:---:
eins | zwei |drei | vier
default|rechts|links|mitte
eins ||| 1

* `---|---` = trennt Kopf vom Inhalt. **!** alle Zeilen müssen gleiche Anzahl von `|` haben
* Es gibt im Web auch Tools, die MD-Tabellen generieren können

### 3 - Other Mardown flavours
* Daring Firebal = 1. MD-Sprache
* auf w3c -> MarkdownSprachen für verschiedene Sprache
* CommonMark = Versuch MD zu standieseren.
* Babelmark 2 -> kann man von verschiedenen MD-Sprachen gerendert werden.

## Next steps
* Listacular = z.B Einkaufsliste in MD schreiben und mitnehmen
* reveal.js = Powerpoint in MD schreiben => wird in HTML umgewandelt.
