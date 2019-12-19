* mit AWK Text manipulieren

### 1 - What is AWK
#### 1 - What is AWK
* auf allen UNIX-Machinen
* zum Daten mainpuliren: 
    * Zeilen
    * Felder in der Zeilen (z.B bei csv)
* nicht gut um Binäre Dateien zu manipulieren, z.B Word/Excel, man kann diese aber zu Text-Dateien konvertieren

### 2 - AWK Command Line Basics
#### 1 - Writing an AWK programm
* `awk '{print $2, $1}' names.txt` - `{ }` - dieses awk-Befehl sollte für jede Zeile angewendet werden (Notes: names.txt: Vorname Name -> $1, $2)
#### 2 - Working with records, fields, patterns, and actions
* AWK-Input sind Records
* Record hat Felder, ist eine Zeile
* Felder werden durch Leerzeile getrennt
* mit `$INT` kann man Felder adressieren, `$0` - ganzes Record
* `awk '{print $2, $1}' names.txt` - `,` in `{ }` sagt einen Fieldseparator einzufügen, Default-Feildseparator ist *Leerzeichen*
    * `awk '{print $2 ", " $1}' names.txt` - richtiges `,` einfügen
* `awk '{print NF, $0}' file.txt` - `NF`= Number Fields => Ausgabe FelderAnzahl *Leerzeichen* Record/Zeile
* `awk '/up/{print NF, $0}' file.txt` - `/up/` ist Pattern=RegEx, Command wird nur auf Zeilen mit Pattern angewendet
`awk 'NF==6{print NF, $0}' file.txt` - Command nur auf Zeilen mit 6 Feldern anwenden
`awk 'NF==6'` - nur Zeilen mit 6 Felder ausgeben, da Default-Command ist print
* `awk '/up/{print "UP:", NF, $0}' /down/{print "DOWN:", NF, $0}` - Mehrere Commands 
#### 3 - Using AWK command-line flags
* `-f FileName` - Filename hat awk-Commandos, wird dann Datei anstelle von Terminal-Eingabe verwendet, Commandos in der Datei müssen nicht in `' '` stehen.
* `-F Separator` - Default-Serparator setzan: `awk -F , '{print $2}` jetzt wird `,` als Feld-Separator gesehe und nicht das Leerzeichen
    * ``awk -F t '{print $2}` - TAB als Separator setzen
* `-v varName=xxx` - AWK-Variable setzen: `awk -v hi=HELLO '{print $1, hi}'` - hier wird die Datei nicht spezifiziert => man muss dann den Text im Terminal eingeben
* man kann mehrere Dateien spezifizieren
    * `awk '{print $1}' < file.txt` 
    * `uptime | awk '{print $1}'`
    * `awk '{print $1}' > file.out` - Ausgabe in Datei umleiten 
    * `awk '{print $1}' | sort -n` - Ausgabe an sort Weiterleiten, soritert wird nach Anzahl der Felder im Record/Zeile
* eventuell muss man Escape-Zeichen, und `"` statt `'` benutzen.
### 3 - Understanding Records and Fields
#### 1 - Exploring basic input-fields separators
* Record besteht aus zwei Teilen
* 1 Zeile = Record
    + Leerzeile + Tab = separieren die Felder, egal wie viele
    * `awk -F , '{print $2}'` - mit -F xx neuen Separator setzen z.B `-F '\t'` - Tab als Separoter setzen.
        * dabei werden mehrfache Separatoren hintereinander ein leeres Field produzieren
        + Fieldsepartor können auch mehre Zeichen oder RegEx sein:
        * `awk -F ABC '{print $2}'` - mehrere Zeichen
        * `awk -F '[,!]' '{print $2}'` - RegEx
#### 2 - Specifying field and record separators with variables
* man kann Fieldseparoter auch per awk-Var setzen: 
    * `awk '{FS=","; print $2}'` - es wird aber nicht ganz richtig arbeiten, da awk zuerst teilt den Text in Records und Fields und dann führt was in { } steht, d.h. es alles mit Default-Einstellungen unterteilt und dann Aktions ausgeführt => BEGIN benutzen - welcher Aktion vor dem Unterteilen stattfinden soll:
        * `awk 'BEGIN={FS=","} {print $2}'`
* Default Record ist eine Zeile => je nachdem welches OS man benutzt wird Ende der Zeile markiert. 
    * Bsp: `!` als Record-Separoter benutzen
    * `awk 'BEGIN{RS="!";FS","} {print $2}'` - RS=Record-Separotr, FS-Field-Separetor
    * Man kann auch Leerstring als RS benutzen => Leere Zeile = RS. Bsp: Wenn Name,Straße,Stadt durch Leerzeile separiert => den Eintrag mit awk als eine Zeile ausgeben:
        * `awk 'BEGIN{RS"";FS="\n"} {name=$1;address=$2;cityzip=$3; print name "," address "," cityzip}'`
    * awk-Output für RS und FS verändern: Deault ist ORS="\n" und OFS=" ":
        * `awk 'BEGIN{OFS=", "; ORS="!"} {print $2, $1} name.txt` - statt Enter ist Ende der Zeile `!` und Leerzeichen = `;`
#### 3 - Challenge/Solution: Change a CSV file to a tab-separated one
* CSV-Datei, die *,* als Field-Separetor benutzt, TAB als Field-Separator benutzen
* `awk -F, '{print $1 "\t" $2 "\t" $3}' datei.cvs`
* `awk 'BEGIN{FS=","; OFS="\t"} {print $1, $2, $3}' datei.csv`
`awk 'BEGIN{FS=","; OFS="\t"} {print}' datei.csv` - wird aber gleichen Output, da es kompett ganzes Record printet, ohne es zu bearbeiten. 

### 4 - Understanding Variables and Operators
#### 1 - Using build-in variables
* `NF` - Number of Fields: 
    * `awk '{print NF, $0}' datei.txt`
    * `awk 'NF==6 {print NF, $0} datei.txt` - printe nur if NF==6
* `NR` - Number of Records: 
    * `awk '{print NR, $0}' datei.txt`
    `awk 'NR==6 {print NF, $0} datei.txt` - printe nur if NR==6, Nur Zeile 6 wird ausgegeben
* `awk '{print NR, FILENAME, FNR, $0}' datei1.txt datei2.txt` - ZeielenNr DateiNamen FNR-ZeilenNrderDatei
* man kann einige Bild-In-Var überschreiben.
* $0 - ganze Zeile
* $Int - Field  
    * `awk '{print $NF} datei.txt` - letztes Field der Zeile printen
    * `awk '{print $(NF-1)} datei.txt` - vorletzte Zeile printen. `( )`- per RegEx, ohne Klammer würde Mathematik machen d.h `0-1`, da Int-Wert von String wird zu 0
* `awk {print $($1)}` 2 one two three \n 3 one two three; Variablen als Variablen benutzen -> Ausgabe: 
    * one <- printet $2
    * two <- printet $3
* `awk '{$2="TWO"; print}' datei.txt` - Ausgabe verändern -> zwetes Feld wird überschrieben mit *TWO*. Inputfile wird aber nicht überschrieben
    * wenn man $100 macht => wird der Datei Field-Separtor + dieses Field hinzugefügt, wobei alles bis *100* wird mit OFS gefüllt. Es wird also jede Zeile beeinflusst
    * `awk '{$="one two threr"; print NF,$2}' datei.txt` - es wird komplette Zeile/Record überschrieben => Anzahl von Fields + Field2 geprintet
#### 2 - Creating user-defined variables
* Bsp: `awk '{hello=$1; goodbye=$2; print ehllo, goodbye}'` - hello und goodbye sind User-Var, *ehllo* wird Leeresstring
    + in awk sind Var Case-Sensitiv
* `awk '{a=1; b=3; print a+b}'`- Variablen hängen vom Kontext ab, entwder Zahlen oder Strings. Ausgabe: 4
* `awk '{a=1; b=3; print a b}'` - Ausgabe: 13 <- werden als Strings behandelt
    * Strings werden zu 0 konvertiert 
    * Konvertiertung wird an der Operation erkannt
    + Math Operationen werden zuerst behandelt <- sonst Klammern benutzen
        * `awk '{a=1; b=2; c=3; print a b * c}'` - Ausgabe ist `1(2*3)`
        * `awk '{a=1; b=2; c=3; print (a b) * c}'` - Ausgabe ist `12*3`
* `awk '{print "\"" $ 1 "\"+0 = "$1 + 0}'`
    * 123 => Ausgabe: "123"+0 = 123
    * 6.5 => Ausgabe: "6.5"+0 = 6.5
    * 4e3 => Ausgabe: "4e3"+0 = 4000
    * 0021 => Ausgabe: "0021"+0 = 21
    * 66boboo => Ausgabe: "266boboo"+0 = 66
    * boobo66 => Ausgabe: "boobo66"+0 = 0
* man kann in awk auch Scopes definieren. => wie in C/C++ überlagern der Variablen
#### 3 - Working wit operators and arrays
* hier gibt es auch `++`, `--` <- wie in *C*
* gibt es auch `+=`, `/=` usw.
* Vergleiche wie in C: `==`, `!=`
* drei String-Operationen:
    * Vergleiche: ~, !~
* Arrays:
    * `awk '{a[1]=$1; a[2]=$2; a[3]=$3; print a[1], a[2], a[3]}'` 
### 5 - A Quick Introduction to Regular Expressions
#### 1 - Regular expression basics
#### 2 - Working characters classes and quantifiers

### 6 - Using Control Structures
#### 1 - Building control structures
#### 2 - Creating an HTML table
#### 3 - Challenge/Solution: Print only those lines consisting of a complete HTML entity 

### 7 - Formatting the Output
#### 1 - Formatting outpu with printf()
#### 2 - Formatting output with width and precision specifiers
#### 3 - Formatting output with width and precision specifiers

### 8 - Funcitons and Arrays
#### 1 - Manipulating strigns
#### 2 - Using associative arrays
#### 3 - Introducting AWK's math functions

### 9 - Combining AWK with Other Tools
#### 1 - Using pipes
#### 2 - Parsing Excel CSV files: Line endings and quotings
#### 3 - Parsing Excel CSV files: Commas and new lines
#### 4 - Scripting with AWK
#### 5 - Challenge/Solution: Perform a join
