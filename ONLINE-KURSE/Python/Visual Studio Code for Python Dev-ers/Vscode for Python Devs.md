### 0 - Introduction
* Erweiterung *Python* installieren
* Python-Interpreter auswählen::
    1. Befehls-Palette öffnen
    2. python select -> Python:select-Interpeter auswählen

### 1 - Overview for Vs Code
#### 1 - A tour of the user interface
* *STRG+SHIFT+S* - nach Dateien suchen/ersetzen - View
* *STRG+SHIFT*G* - Git-View
* *STRG+SHIFT+X* - Erweiterungen-View
* *STRG+SHIFT*P* - Befehlspalette
+ *STRG+SHIFT*P* - Debug-View
+ Zen-Mode: -> View-> Appeareance -> ... oder *STRG+K+Z* Z
#### 2 - Build HelloWorld.py
* im Editoer -> Rechstklick -> Run in Terminal/Selection/Line in Python Terminal = die Date im Terminal/Python-Interpreter laufen
#### 3 - The Integrated Terminal
* In VS-Code-Terminal -> Rechstklick -Split 
* im Code bash-Command auswählen -> Befehlspalette -> run selected eingeben -> Run Selected Text in Active Terminal => bash-Zeile wird im aktuelem Terminal ausgeführt
* VS-Code-Terminal Einstellungen (Settings -> Terminal Integrated eingeben)

### 2 - Python Code Editing
#### 1 - Editing Python Code
+ Intelecense triggern: *STRG+Leerzeile
* wenn *STRG+Leerzeile* während Intelecense auf ist => Info zu der Funktion/Klasse usw.
* es gibt auch Python-Snippets -> sich mit TABS durch die Teile des Snippets navigieren
#### 2 - Using the Python REPL
* Read Evaluate Python Loop:
* d.h wenn man den Python-Interpreter einmal aufgemacht hat, bleict er offen, bis man ihn selbst schließt.
#### 3 - Formatting Python code
* Format-Standards: www.python.org/dev/peps/pep-0008/
* man kann diesen Standard in VSCode integrieren (mit pip):
    * `pip3 install autopep8` 
    * in VSCode -> Settings -> Pyhton Formatting eingeben -> bei Python>Formatting:Proivider: autopep8 setzen + Formatonsave suchen -> Editor: Format On Save on setzen
* eventuell die Pep8-Regeln lesen
#### 4 - Refactoring Python code
* Code restrukturien, um ihn lesbarer zu machen
* evnteull *rope* davor mit pip3 installieren
* z.B Funktion umbennen:
    1. den Funktionsnamen auswählen -> Rechtsklick -> Rename Symbol
    2. z.B für Debuggen zusammengesetze Ausdrücken auslagern:
        1. Ausdrück auswählen -> Rechtsklick -> Extract Variable -> Variablennamen eingeben.
    3. Teil des Codes in eine Funktion auslagern:
        1. den Code auswählen -> Rechtsklick -> Extract Method -> neuen FunktionsMethod eingeben.
### 3 - Python Code Debugging 
#### 1 - Setting up for Python debugging 
* Zuerst Debugging-Config erstellen -> in launch.json:
    1. Add Configuration klicken - es wird neue launch.json erstellt (eventuell nochmal klicken und Passende Python-Interperter ausäwhlen z.B Remote, Python File usw.)
    2. hier im Beispiel die launch.json folgendermapen bearbeitet:
        1. in *Current File*:
            1. `"stopOnEntry": true` - wenn Debug-Modus angeschmießen wird, wird es an der ersten Zeile pausiert
#### 2 - Stepping through code
+ man kann im Debug-View die Variablen-Werte uberschreiben.
#### 3 - Breakpoints
#### 4 - Conditional breakpoints
* 
    1. Rechstklick beim Breakpoint setzen -> Conditional Breakcpoint auswählen
    2. Expression einfügen: z.B `width > 200 and length > 200` 
    3. Breakpoint wird als *Conditional Breakpoint* markiert
* Breakpoint, wenn bestimmte Ausführung bestimmte Anzahl Mal gemacht wurde:
    1. Rechstklick beim Breakpoint setzen -> Conditional Breakcpoint auswählen
    2. auf *Expression* klicken und *Hit Counter* auswählen
    3. dann die Zahl eingeben.
#### 5 - Logpoints
* statt das Programm pausieren, bestimmte werte Ausgeben:
1. Rechstklick beim Breakpoint setzen -> Conditional Breakcpoint auswählen
    2. auf *Expression* klicken und *Log Message* auswählen
    3. `"parameters: r:{varName}"`
    4. die Ausgaben werden in Debug-Console augegeben
### 4 - Coding Extensions
#### 1 - Python Docstring
* *autodocstring* - Docstring im Code einfügen
    1. `"""` eingeben + *Enter* -> die Erweiterung wird den Kommentar selbständig die Basis-DocStrings erstellen, sich dann mit TABs sich duchklicken und alles eintragen
#### 2 - Better Comments
* die Kommentare richtig schreiben (ist eigentlich für alle Sprachen geeignet)
    * z.B toDos, Serviece-Remiders <- sie sollten dann aber anders aussehen
* *better comments*
    * die Kommentare kann man jetzt Tagen:
        1. `*` vor dem Kommentar => wird FETT
        2. `?` Notiz mit Entscheidung. Text wird Blau
        3. `!` - Wichtig. Text wird Rot
        4. `todo` - Text wird Orange.
    * man kann die Farben über Einstellungen -> Better Comments einstellen. + Man kann eigene Erstellen
#### 3 - REST Client
* hat auch Snippets
* verschiedene HTTP-Request mit `###` trennen
* Man kann den Respose auch Speichern
* Bsp: Snippet erstellen:
    1. z.b POST-Request auswählen
    2. Rechstklick -> Generate Code Snippet -> Python als Sprache auswählen -> Bibiothen auswählen (z.B Python-Default http-Library)
    3. es wird Code für den POST-Request erstellt