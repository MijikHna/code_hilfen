* Linux wurde inspiriert auf MINIX/UNIX
* Philosophie - OS und SW sollte frei sein. Unter GNU - freie SW.
* Linux hat Tools aus GNU Projekt (services usw.)
* Distro - Spezifische Gruppe der SW
    * BasisDistros: Debian, Arch, Slackware, Red Had
* Bash ist fast bei allen Distros vorhanden.

### 1 - Setting Up your Environment
#### 1 - Creating a Linux virtual machine
#### 2 - Windows Subsystem for Linux on Windows 10
* Windows Subsystem for Linux installieren
* Läuft direkt in Windows nicht in VirtualBox
* man muss Distro installieren um Bash zu bekommen
* Einrichtung:
    * START -> Windows Features an/ausmachen -> Windows Subsystem für Linux -> Neustarten -> Microsoft Store -> nach Ubuntu suchen -> Ubuntu installieren
    * Ubuntu einrichten - User + Passwort usw.
    * Rechtsklick auf das Fenster -> Settings - kleinere Einstellungen für Bash-Fenster machen

#### 3 - Following along on Mac
* macOS stamm von BSD/UNIX nicht Linux
* hat ähnliche tool chains
* hat bash-Shell 
#### 4 - Following allong on Linux
* `bash` - neue Bash-Session beginnen
#### 5 - Using a cloud provider
* z.B Azure, AWS, GCP, DigitalOcean, Linode, etc
* Ubuntu/Debian wählen
* Verbingund wird dann per ssh aufgebaut
* kosten meisten Geld

### 2 - Command-Line Basics
#### 1 - What is the command line?
* CLI - Command Line - Text based Interface um Befehle einzugeben. Produziert Text-basierten Output.
* Shell - Command Line Interpreter - es gibt verschiedene Shells
#### 2 - How commands are structured
* Syntax: Befehl Option(en) Argument(e)
* Befehl - Programm, das ausgeführt wird
* Optionen - wie das Programm ausgeführt (von Default-Ablauf abweichen)
    * Optionen, die `--` davor haben, können nicht kombiniert werden, müssen einzeln ausgeschrieben werden
* Argument - an welchen Objekte der Befehl/Programm ausgeführt werden soll
#### 3 - Write comamnds in a shell at the prompt
* STRG+SHIFT++ - Terminal vergrößern
* Prompt-String zeigt `User@Hostname:OrdnerName`. Prompt ist auf anderen Platformen sieht unterschiedlich aus. Prompt kann man anpassen.
#### 4 - Heplful keyboard shortcuts in the terminal
* **TAB** - Vervollständigung
* **STRG+C** während der Eingabe eingeben - Eingabe wird verworfen. Ergebnis ist leere Promptzeile
* **TAB TAB** - zeigt mögliche Vervollständigungen.
* **STRG+A** - bewegt den Cursor zum Anfang
* **STRG+E** - bewegt den Cursor zum Ende
* **STRG+->/<-** - den Cursor um ein Word bewegen
* **STRG+U** - löscht vom Cursor bis zu Start
* **STRG+K** - löscht vom Cursor bis zum Ende
* **STRG*SHIFT+C/STRG*SHIFT+Y** - Copy/Paste
* **STRG+R** - Befehl eingeben -> wird das passende Befehl erschienen ~ Suchen in der History
#### 5 - Finding help for commands
* `man` - Manual Page `!= --help`
    * in `man` kann man `h` klicken - `man`-Ausgabe wird in **less** angezeigt. Wenn man `h` eingibt während man in **less** ist, wird Hilfe für **less** angezeigt. Wichtige Tasten für less:
        * f -  forward
        * b - backword
        * z - 
        * w - 
        * Space -
* *Befehl* `--help` - ist Option des Befehls.
* `help` - zeigt alle Bash-Kommandos an
* `apropos wasBefehlMachSoll` z.B `apropos list`

### 3 - Files, Folders, and Permissions
#### 1 - Files, folders and navigations
* `file datei.end` - Info zu Datei
* `stat datei.end` - Detaliertes Info zu Datei
* `cd` - Change Directory
* `pwd` - Print Working Direktory (Absolut)
* `ls -R Ordner` - Ordner rekursiv auflisten ~ zeigt Baum des Ordners
* 
#### 2 - A little more about ls
* `ls --color=always` - Verschiedene Dateitypen unterschiedlich färben
* `ls -l` - Dateigröße wird in Bytes angezeigt
* `ls -lh` - Dateigrößen mit 1000-er-Kürzel anezgien
#### 3 - Create and remove folders
* `mkdir order1 order2` - mehrere Order erstellen
* `mkdir -p ordner1/ordner2` - mit `-p`- auch ParentOrdner erstellen.
* `rmdir ordner1` - Ordner muss leer sein
#### 4 - Copy, move and delete files and folders
* `cp alt.end neu.end`
* `mv alt.end neu.end` - verschieben und umbennen
* `*` - mehrere Zeichen
* `?` - ein Zeichen
* `mv *.txt ordern\` - alle .txt nach ordner kopieren

#### 5 - find files from the command line
* `find . -name "dateiname"` - dateiname/ordner im aktuellen Verzeichnis suchen, dass *dateiname* enthält
* `find . -name "datei*"`
#### 6 - User roles and sudo
* `su` - switch user
* in Linux gibt es zwei Usertypen: 1) Normaler User, 2)Superuser
* `sudo` - kurz Root-Rechte ausleihen
* `sudo -k` - Root-Rechte-Ausleihe beenden
* `sudo -s` - komplett Root werden
#### 7 - File permissions
* `chmod` 
    * `777` - UserGroupOthers; 4 - Read, 2 - Write 1 - Execute
    * `ugo` oder `a` - UserGroupOthers oder All
        * `+` - dazu. Bsp: `u+rwx`
        * `-` - raus. Bsp: `o-rws`
        * `=` - ~ aktualisieren bzw. mit neuen Rechten überschreiben: `g=r`
* `chown` - change Owner
#### 8 - Create hard and symbolic links
* Hard links - zeigen auf Daten auf dem Diskt (inode)
    * `ln datei.end linkname.end` - eigentlich ist jeder Dateiname ein Hard Link, da er auf die erste Zeile der Datei zeigt.
* Soft links (Symlink) - zeigen auf Datei auf dem Disk (relative path)
    * `ln -s datei.end linkname.end` - wenn man die `datei.end` verschiebt, wird der Link ungültig (da relativ ist)
#### 9 - The linux filesystem

### 4 - Common Command-Line Tasks and Tools
#### 1 - The Unix philosophy
* ein Programm mach EIN Ding
* Input ist Text (String)
#### 2 - Use pipes to connect commands together
* `|` - Pipe Zeichen, Pipe - Output eines Befehls zum anderen senden.
* Bsp:
    * `echo "hello" | wc` - (wc - Word Count: Ausgabe - Zeilen  Wörter Buchstaben, dabei Enterzeichen usw. werden auch gezählt)
#### 3 - View text files with cat, head, tail and less
* `cat` - concatenate
    * `cat datei.end | cat -n` - Zeilennummer anzeigen
    * `cat datei.end | cat -n |tail -n5` - Ausgabe ist 5 letzten Zeilen mit Zeilennummerirung
    `cat datei.end | tail -n5 | cat -n` - Ausgabe ist 5 letzten Zeilen, die Zeilennummerirung beginnt aber bei 1, da Zeilennummeriung nach `tail` angemacht wird.
* `head` - ersten 10 Zeilen der Ausgabe
    * `head -n5 datei.end` - mit `-nX` - wie viele Zeilen angezeigt werden sollen  
* `tail`- letzten 10 Zeilen der Ausgabe
    * `head -n5 datei.end` - mit `-nX` - wie viele Zeilen angezeigt werden sollen 
* `less` - Ausgabe Seitenweise ausgeben
    * `less datei.end` - Datei direkt in `less` aufmachen
    * `cat datei.end | less` - Ausgabe von `cat` nach `less` übergeben 
#### 4 - Search for text in files and streams with grep
* `grep` - gibt Zeilen aus, die einem Pattern enthalten. Ist Casesensitiv
    * `grep -n "pattern" datei.end` - mit `-n` gibt auch Zeilennummer aus
    * `grep -i "pattern" datei.end` - mit `-i` die Casesensitivität ausmachen
     `grep -vi "pattern" datei.end` - mit `-v` Zeilen ausgeben, die den Pattern nicht enthalten
    * `grep -E "[hijk]" datei.end` - mit `-E` RegExp benutzen. Hier RegExp = Zeilen, wo h,i,j,k vorkommen
    * `grep -E "\w{6,}" datei.end` - Wörter, die mindestens 6 Zeichen enthalten
* man-Seite von `grep` checken. Ist ein mächtiges Tool

#### 5 - Manipulate text with awk, sed and sort
* `awk` und `sed` - Text in Streams und Dateien manipulieren
> *beispiel.txt* - Inhalt
>Name  ID Team  
>Scott   314 Purple
>Jian   991 Orange  
>Anne   556 Green  

* `awk`
    * `awk '{print $2}' beispiel.txt` - Ausgabe ist die *ID-Spalte*
    * `awk '{print $2 "\t" $1}' beispiel.txt` - Ausgabe ist ID-Spalte TAB NAME-Spalte
    * `awk '{print $2 "\t" $1}' beispiel.txt | sort -n` - Es wird nach ID-Spalte sortiert (`-n` - nummerisch sortieren)
    * `man` von awk studieren    
* `sed`  
    * `sed "s/Orange/Red/" beispiel.txt` - Alle Orange durch Red ersetzen. `-s/Alt/Neu` - substitute
* `sort`
    * `sort beispiel.txt` - wird nach den Buchstaben der Zeilen sortiert
    * `sort -k2 beispiel.txt` - nach 2-ten Buchstaben der zweiten Spalte sortieren
    * `sort -k2 -n beispiel.txt` - nach 2-ten Spalte (`-k2`), nummerisch (`-n`) sortieren.
    * `sort -u datei.txt` - doppelte Zeilen werden unterdrückt
* Weitere Tools:
    * `rev` - Text rückwärts printen
    * `tac` - Zeilenweise rückwärts printen
    * `tr` - mit individuellen Zeichen arbeiten

#### 6 - Edit text with vim
* `vim` oder `vi`
    * `i` - Eingabemodus, Eingabe nach Cursor
    * `ESC` - Befehlsmodus
    * `SHIFT + i` - Eingabemodus, Eingabe vor Cursor
    * `vim datei.end`
    * `SHIFT+g` - zum Ende der Datei gehen
    * `1+SHIFT+g` - zum Anfang der Datei gehen.
    * `:q!` - Schließen ohne zu Speichern
    * `:wq` - Schließen mit Speichern
#### 7 - Edit text with nano
* `STRG+W` - nach Text suchen; Enter - zum nächsten Treffer
* `STRG+V` - zum Ende der Datei gehen
* `STRG+Y` - zum Anfang der Datei gehen

#### 8 - Working with TAR and ZIP archives
* `tar cvf archivName.tar Ordner/` - `c`=create, `v`=verbose (archivierte Dateien werden ausgegeben)`f`=Datei erstellen, sonst wird Archiv auf dem Screen ausgegeben
* `tar caf archivName.tar.gz Order/` - `a`- Archiv komprieren, Komprimierungsart anhand der Endung herausfidnen (hier `.gz`)
* `tar xf archivName.tar.gz` - `x` = extrachieren
`tar xf archivName.tar.gz -C OrderName` - `-C OrderName` = sagen in welchen Order extrahiert werden soll
* `zip -r archivName.zip Order` - ohne `-r` wird ein leeres Ordner erstellt.

#### 9 - Output redirection
* 0 - stdin; 1 - stdout, 2 - stderr
* `ls 1 > datei.txt` - stdout von ls nach datei.txt umleiten
* `ls notreal 1 > date.txt ` - `notreal` ist nicht existierende Ordern. Da aber stdout umgeleitet wird, wird die Error-Message von `ls` im Terminal angezeigt
* `ls 1 >> datei.txt`  - `>>` - apend, statt überschreiben. 
#### 10 - Exploring environment variables and PATH
* `env` - alle Environment variablen anzeigen
* `PATH="$PATH:/pfad/zu/mytool` 

### 5 - A peek at some more advanced topics
#### 1 - Find distro and kernel info
1. 
    1. `ls -lah /etc/*release`
    2. `cat /etc/*release`
2. 
    1. `uname -a` - Kernelversion erfahren.
#### 2 - Find system HW and disk info
* `free -h` - RAM und SWAP anzeigen
* `cat /proc/cpuinfo`
* `df -h` - Festplattenbelegung anzeigen
* `sudo du / -hd1` - (`du`- disk usage ), (`/` - wo man schauen will ), (`-h` - für Menschen lesbare Größe anzeigen), (`-d1` - Level 1)
* `sudo lshw` - HW auflisten (list HW)
* `ip a` - NW-Info anzeigen
#### 3 - Install and update software with package manager
* `apt search tree` - nach Paket *tree* suchen
* `apt show tree` - mehr Details anzeigen.