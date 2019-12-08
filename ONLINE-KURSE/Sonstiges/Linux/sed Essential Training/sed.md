* sed = stream editor
* Für Manipulation line-oriented Text, Filter
* 

### 1 - Sed Command-Line Basics
#### 1 - Using the most important sed command
* `sed 's/old/new/' file.txt` - sed = Programm, s = sed Command = substitue, old/new /old durch new ersetzen
* ändert nicht die Original Datei, sondert wie `cat`
    * `sed 's/old/new/' file.txt > neuDatei.txt`
* `sed 's/old//" file.txt` - old löschen
#### 2 - Understanding input, output, files and pipes
* `sed 's/old/new/' file1.txt file2.txt` - geht auch mehrere Dateien bearbeiten
* `sed 's/old/new/'` - File ist dann stdin
    * Beenden: `STRG+D`
* `nl` - cat + gibt noch ZeilenNummern aus
    * `nl | sed 's/old/new/' file1.txt` - Zeilennummer mit nl einfügen diese Ausgabe dann an sed weitergeben
* `sed 's/old/new/' < file1.txt > file2.txt` - Input ist file1.txt, Output ist file2.txt
#### 3 - Qouting command-line arguments
* man sollte `' '` verwenden, falls man im Strin Leerzeichen hat:
    * `sed 's/the/some of the/` file1.txt` - ohne würde Error verursachen
    * `sed 's/the/$1000' fil1.txt` - , ohne `' '`, dann würde es wie '$1' also Variable1 interpretiert
    * sed "s/the/the's" file1.txt` - falls man *'* im String hat
* `" "` - $ wird trotzdem wie Bash-Substitution verwendet
    * man da auch Escape-Zeichen verwenden z.b für *"* selbst mit `\"`
* man kann auch Escapce Zeichen für Leerzeile benutzen, wenn man gar keine Quotes benutzt
#### 4 - Modifying the "s" command
* `sed 's/old/new/' file.txt` - `s` ändern nur das erste Vorkommen von *old* in der Zeile
    * `sed 's/old/new/g' file.txt` - *g* = global, jedes Vorkommen ersetzen
* `sed 's/old/new/2' file.txt` - zweites Vorkommen ersetzen
* man kann statt `/` beliebiges anderes Zeichen benutzen z.B `;` - sinnvoll, falls man im String selbst */* hat
### 2 - Regular Expressions
#### 1 - Introducing regular expressions
* String ist eigentlich auch RegEx
* RegEx sind immer Case-Sensitive
* `.` - ein Buchstabe: `/a.b` 
* `\` - Escape-Seqence: `/a\.c/` = "a.c"; `/a\\c/` = "a\b"; `/a\/c/` = "a/c"
* `^` - Zeile sollte mit xxx beginnen (=Zeilenbeginn): `/^abc/` = "abcxxx" 
* `$` Zeile sollte mit xxx enden (=Zeileende) `/abc$/` = "xxxabc" 
#### 2 - Using character classes and qunatities
* `/a[xyz]c/` = "axc", "axc" usw. - Character-Klasse, `[]` = nur ein Buchstabe
* `/a[a-z]c/` = "aac", "azc"
* `/a[a-zA-Z]c/` = "aac", "azc"
* `/[a-lrxz]/-/g` = *a bis l und r,x,z*
* `/[^a-z]` = nicht a bis z
* `/[^ ]` = keine Leerzeile
* `/ab*c/` = Null oder Mehrfach vom letztem Buchstaben
* `/t.*/` = t dann beliebiges Zeichen Null oder Mehrfach also "txxxx..." Leerzeilen eingeschlossen
    * `/t[a-z]*/` t + Null/Mehrere Buchstaben
    * `/t[a-z][a-z][a-z]*/` - t + mindestens drei Buchstaben
* `/(ab)*c/` - ab-Null/Mehrfach + c
* `s/<.*>/HTML <i>italic text </i>` - ersetzt ganze Zeile mit HTML, da bis zum Ende der Zeile nach dem letztem `>` sucht
* `s/<.*>/HTML <i>italic text </i>` - ersetzt richtig also `<i>` und `</i>` mit HTML 
#### 3 - Using & and \n
* `&` - wird mit gefundemen String ersetzt
    * `sed 's/the/(&)/g` ersetzt jedes `the` mit `(the)`
* `\INT` - wird mit dem Text ersetzt der beim INT-ten Suche gefunden wurde mit `\(...\)`
    * `sed 's\(they\) \(were\)\/\2 \1/g` - also Zwei Suchen `they` mit 2 also `were` ersetzen UND `were` mit `they` ersetzen
        * `()` werden bei der Suche nicht berücksichtigt sind nur für die Zuweisung für `\INT`s notwendig.
    + `s/were \([a-z]*\)/\1ed/g file1.txt` - also `were xxx` mit `xxxed` ersetzen
### 3 - Sed Command-Line Flags
#### 1 - Controlling printing with -n and "p" modifier
* `-n` - Zeilenausgabe verhindern
    * `sed -n 's/the/THE/p file1.txt` - mit `p` - wenn Zeile geändert, printe sie
* `-e` - mehrere Befehle gleichzeitig
* `-f` -Datei mit Befehlen
#### 2 - Specifying multiple commands with -e end -f
+ `sed -e 's/up/UP' -e 's/down/DOWN/' file.txt` - mehrere Commandos hintereinander ausführen, mit `-e` sagt man es ist eine Command und keine Datei. Commandos werden per Line ausgeführt. Eventuell kann das erste Command das zweite Command beeinflussen
    +  `sed  'es/up/UP' 'es/down/DOWN/' file.txt`
* auf einigen Distributionen kann man auch `;` bei mehreren Commandos ausführen: `sed 's/up/UP;s/down/DOWN/g' file.txt`
* man kann Commandos aus einer Datei lesen: Bsp:
```bash
cat > script.txt #cat in script.txt umleiten
s/up/UP/g
s/down/DOWN/g
```
* `sed -f script.txt file.txt` - Commandos mit `-f` aud einer Datei einlesen. Eventuell gibt es Fehler wenn man Kommentare im Script hat.
* !! sed auf Linux und MacOS haben unterschiedliche *sed*-Optionen

#### 3 - Challenge/Solution: Change ten thousand men to one woman

### 4 - More sed Commands
#### 1 - Understanding address and address ranges
* Addresse (zu was man sed-Commandos addressiert) kann sein:
    * ZeilenNummer
        * Zeile Drei ändern: `sed 3s/up/UP/ file.txt` nur in Zeile 3 erstetzen
    * `$` - Ende des Files
    * `/.../` - Zeilen, die RegEx entsprechen
    * `,` - Ranges von Addressen
    * `!` - nicht
* Commandos:
    * `p` - (Zeile(n)) printen
    * `d` - (Zeile(n)) löschen
    * `r` - (Zeile(n)) lesen
    * `w` - (Zeile(n)) schreiben
    * `y` - Chars transformieren
#### 2 - Printing lines with "p"
* `sed p file.txt`- jede Zeile wird zwei geprintet, da per Default jede Zeile geprintet wird
* `sed -n p file.txt` - mit `-n` Default-Ausgabe unterbinden
* `sed -n 3p file.txt` - nur 3. Zeile printen
* `sed -n '$p' file.txt` - letzte Zeile drücken, da *$* muss man es in `' '` nehmen
* `sed -n '2,4p' file.txt` oder `sed -n '2,4 p' file.txt` - mehrere Zeilen ausgeben, Leerzeile um lesbarere zu machen
* wenn man mehrere Dateien bearbeitet => zweite Datei ist wie Fortsetzung von erster Dateie => bei Zeilen das beachtet
* `sed -n '/[Tt]he[my]/p' file.txt` - nur Zeilen printen, die The/Them/They haben
* `sed -n '/marched/,/when/p'` - Bereich von RegEx printen. Es wird ab Zeile-*marched* bis *when*-Zeilegeprintet. Wenn mehrere Bereiche gefunden werden, werden mehrere Bereiche ausgegeben
    + z.B. nutzlich wenn man bei C-Programmen Funktionsblöcke ausgeben will: `sed -n '/^}/,/^{/p' cProg.c` - nur Kommentar + Funktions-Rumpfe ausgeben
* Mixen:
    * `sed -n '2,/down/p` - ab Zeile 2 bis *down* Zeile printen
    * `sed -n '/when/,$p'` - ab Zeile *when bis Ende printen
    * `sed -n '2,5!p'` - alle Zeilen außer 2 bis 5 printen
    * `sed -n '/down/!p'` - alle Zeilen, die *down* nicht haben, printen 
#### 3 - Deleting lines with "d"
* `sed '4d'` - Zeile 4 löschen
* `sed '/up/d'` - Zeilen löschen, die *up* haben
* `sed '/thousand/,/down/d` - Zeilen ab *thousand* bis *down* löschen
    * wird oft mit *!* benutzt: `sed '/up/!d*` - alle Zeilen Löschen die kein *up* in der Zeile haben
* man kann z.B zerst mit *p* schauen, welche Zeilen beeinflusst werden, dann diese Zeilen mit *d* löschen 
#### 4 - Reading and writing files with "r" and "w"
+ `sed /down/r file2.txt file.txt` - Datei *file2.txt* lesen, wenn in *file.txt* *down* gefunden wird und direkt ausgegeben
* `sed '1,3 w' file2.txt file.txt` - Zeile 1 bis 3 aus Datei *file.txt* in *file2.txt* schreiben
* man kann *s* und *w* benutzen = veränderten Zeilen in eine Datei schreiben: `sed 's/up/UP/w file2.txt' file.txt`
    * `sed 's/up/UP/gw file2.txt file.txt` - diese Reihenfolge sollte man behandeln, da sonst *g* wie Dateiname behandelt wird
    * also *w* sollte als letztes stehen = wird als letztes Commando asgeführt
* ALLGEMEIN: die Reihenfolge der Befehle ist wichtig
* in einem *sed*-Befehl wird die Datei geöffnet, falls da was ist, wird alles gelöscht, weitere Commands im gleichen *sed* appenden in diese Datei.
#### 5 - Performing transformations with "y"
* ähnlich zu UNIX-`tr`-Commnd - Chars erstetzen
* `sed y/abcdef/ABCDEF/'` - Kleinbuchstaben durch Großbuchstaben ersetzen
* man kann keinen Bereich festlegen z.B `a-z`
#### 6 - Appendng, inserting and changing entire lines with "a", "i", "c"
* Beeinflussen mehrere ganze Zeilen
* `a` - Zeile appenden
* `i` - Zeile inserten
* `c` - Zeile ändern 
* Commandos oben beeinflussen immer nur eine Zeile
* `sed '/down/ a\==> HAHA HE SAID \"DOWN\"' file.txt` ODER `sed '/down/ a\ ==> HAHA HE SAID \"DOWN\"' file.txt` - nach jeder *down*-Zeile *==> HAHA HE SAID "DOWN"* einfügen
* `sed 'a\\n' file.txt` - ein Enter nach jeder Zeile
* `a` wird oft in sed-Scripts verwendet:
```bash
#sedscript.txt
/down/ a\ #erstes Command 
==> HAHA HE SAID "DOWN"
/up/ a\ #zweites Command
==> HEHE HE SAID "UP"
```
* `sed -f sedscript.txt file.txt`
* `i` wie `a` benutzen -> Unterschied, `i` fügt vor der Zeile ein
* sed `/top/,/again/ c\He treated them incosistently\And their moods were vaiable' file.txt` in den Zeilen von *top* bis *again* *He treated ..* durch *And their moods ...* ersetzen
#### 7 - Challenge/Solution: Write the main() function from array.c to file main.c
* `sed -n '/^[a-z]* main *(/,/^}/w' main.c cProg.c`

### 5 - Writing Programms in sed
#### 1 - Grouping commands with { and }
* `{...}` - Gruppen-Commands to Blöcken machen
* `n` - Nächste Zeile bekommen
* `q` - Progamm verlassen
* `#` - Kommentar einfügen
* `=` und `l` - Debugging

* `sed - e 's/up/UP/g' -e 's/down/DOWN/g' file.txt` oder
```bash
#sedsript.txt
s/up/UP/g
s/down/DOWN/g
```
* `sed -f sedscript file.txt`
* Ersetzung nur in den Zeilen die *when* haben
```bash
#sedsript.txt
/when/ s/up/UP/g
/when/ s/down/DOWN/g
```
* 
```bash
#sedsript.txt
/when/ {
    s/up/UP/g
    s/down/DOWN/g
}
```
* Ersetzung nur in den Zeilen, die kein *when* haben
```bash
#sedsript.txt
/when/ ! {
    s/up/UP/g
    s/down/DOWN/g
}
```
* Ersetzung nur  in den Zeilen von 3 bis 6 und ein *when* haben
```bash
#sedsript.txt
3,6{
    /when/ {
        s/up/UP/g
        s/down/DOWN/g
    }
}
```
#### 2 - Getting the next line with "n"
* ist in Script nutzlich z.B im Blöcken nutzen
* Beginn der Zeile *((* einfügen und am Ende der Zeilen *))* einfügen, wo *marched* vorkommt
```bash
/marched/ {
    n #Zeile printen und zur nächsten Zeile von Input gehen
    s/^/((/
    n
    s/$/))/
}
```
* Ziel eigentlich zur nächsten Zeile springen d.h. Zeilen überspringen, falls notig
#### 3 - Exiting with "q" and "d"
* `q` - printet die (gefundene) Zeile und verlässt den Script => wenn bestimmte Zeile gefunden => alle beenden
    * `sed '/again/q' file.txt` - wenn again gefunden wurde, wird sed beendet
    * 
    ```bash
    /marched/ {
        n
        s/^/((/
        n
        s/$/))/
        q
    }
    ```
    * `sed -f sedScript file.txt`
* d.h Befehle die nach `q` kommen werden nie ausgeführt
* `d` - für Zeile die Ausführung abrechen (im Skript)
* 
```bash
/up/ {
    s/up/UP/
    d
    s/^/==/
}
```
* `sed -f sedScript file.txt`
* d.h. für die Zeile werden die weitere Commands im Skript nicht ausgeführt
#### 4 - Commenting with "#"; debugging with "l" and "="
* Hilfe bei sed-Skripts debuggen
* `#` Kommentar
```bash
# Kommentar 
/marched/ {
    n
    s/^/((/
    n
    s/$/))/
}
```bash
`=` - printet die Zeilennummer
```bash
/marched/ {
    n
    =
    s/^/((/
    n
    =
    s/$/))/
    =
}
```
* hearusfinden wo man gerade im sedSkript befindet
* `l` - printet current Line mit *$*-Zeichen und Sonderzeichen werden mit Escape-Sequenzen ersetzt (z.B. TABs)
* 
```bash
s/ /    /3 # Leerzeichen mit TAB ersetzen wenn man es 3 Mal in der Zeile vokommt
l
```
* 


### 6 - Advanced Programming Concepts
#### 1 - Managing multi-line pattern space with "N", "D", and "P"
* `N, P, D` - Leerzeichen in Multi-Line-Patterns managen
* `:, b, t` - Programm Flow Control managen
* `g, G, H, x` - Hold Buffer managen
* `N` - appendet Neue Zeile und liest nächste Input Line
* `P` - Printet bis zum ersten NewLine-Zeichen
* `D` - deletet die erste Zeile + NewLine-Zeichen dazu
* Wie sed funktioniert:
    1. liest eine Zeile und kopiert es in "Pattern Space"
    2. schauen, ob es Commands im Skript gibt, die ausgeführt werden sollen
    3. führt diese aud Pattern Space
    4. Printet Pattern Space
* `N` - leer nicht den Pattern Space, fügt da ein `\n` und liest die nächste Zeile ein, d.h. im Pattern Space sind jetzt zwei Zeilen die editiert werden können
```bash
/marched/ {
    N
    s/\n/ - /
}
```
`P` und `D` werden meist mit `N` benutzt:
    * `P` - printet Pattern Space bis zum ersten `\n`
    * `D` - deletet im Pattern Space den ersten Teil bis `\n`
* Bsp: eine oder mehrere Zeilen finden, die mit *marched* beginnen und mit *up* enden, und diese z.B mit *marched...up* ersetzen
* 
```bash
N
s/marched.*up/marched...up/
P 
D # ohne P und D würde nicht funktionieten, falls marched und up in der gleichen Zeile stehen => da z.B die zweite Zeile angefügt wird, die marched hat, ist die schon im Pattern Space
```
#### 2 - Flow control with ":", "b" and "t" ~ if/while (eher goto von C)
* `:` - definiert einen Label
* `b` - branchet zu definierten Labels
* `t` - branchet nur wenn eine Ersetzung statt gefunden hat
* 
```bash
s/the/THE/g
b next
s/up/UP/g
: next
s/down/DOWN/g
b
s/marched/MARCHED/g
```
* wenn the/THE ausgeführt wird, wird es zu next gesprungen (/down/DOWN), eigentlich wird immer zu next gesprungen
* b -> springt zum Ende des Skripts
* 
```
s/again/again/
t label
s/the/THE/g
: label
s/up/UP/g
``` 
* nur wenn /again/again/ ausgeführt wird, wird the/THE übersprungen
#### 3 - Managing the hold buffer with "g", "G", "h", "H", and "x"
* Hold Buffer - Daten für weitere Operationen speichern
    * `h` - kopiert Pattern nach hold buffer
    * `g` - kopiert hold buffer nach Pattern
    * `H` - hängt `\n` und kopiert Hold Buffer nach Pattern
    * `G` - hängz `\n` und kopiert Pattern nach Hold buffer
    * `x` - ersetzt Patter mit Hold Buffer
* Bsp: h + g 
```bash
#scriptSed
2 { # zweite Zeile
    h # hold
}
$ { #letzte Zeile
    p #print
    g #get
}
```
* `sed -f scriptSed file.txt` -> Ausgabe: Zeite Zeile wird kopiert in Hold Buffer `h` und wird dann nach der letzten Zeile ausgegeben `g`
* Bsp: H + G - sind eigentlich Versionen von h + g für mehrere Zeilen
```bash
#scriptSed
2 { # zweite Zeile
    h # hold
    H
}   
$ { #letzte Zeile
    G #get
}
```
* `sed -f scriptSed file.txt` -> Ausgabe: Zeite Zeile wird kopiert in Hold Buffer `h` + nochmal mit `H` und wird dann nach der letzten Zeile ausgegeben `G`
* * Bsp: x -> alle _ im Text mit `<i>` und `</i>` ersetzen, dabei erstes Vorkommen mit `<i>` zweites Vorkommen mit `</i>`
```bash
#scriptSed
: top # für Loop
/_/ { # wenn _ gefenden wird
    x # Pattern mit Hold Buffer überschreiben
    /ON/ !{ # wenn Pattern nach dem Austauschen ON enthälgt
        s/.*/ON/ # dann alle mit ON erstetzen
        x   #wider in Hold Buffer kopieren
        s;_;<i>; # _ mit <i> ersetzen
    }
    /ON/ { # wenn Pattern nach dem Austauschen ON enthälgt
        s/.*/OFF/ #dann alle mit OFF erstetzen
        x #wider in Hold Buffer kopieren
        s;_;</i>;
    }
    b top
}
```
* `sed -f scriptSed file.txt` -> Ausgabe:
#### 4 - Challenge/Solution: Convert first three words of each line to all caps
* ersten drei Wörter der Zeile zu Großbuchstaben umwandlen:
```sed
s/ /#/3
h
s/#.*$//
y/abcdefghijklmnopqrstuvwxyz/ACDEFGHIJKLMNOPQRSTUVWXYZ
G
s/\n.*#/ /
```

* sed.sourceforge.net - Doku usw. für SEd
* grymoire.com/Unix/Sed.html
* github.com/uuner/sedris - Tetris in SED