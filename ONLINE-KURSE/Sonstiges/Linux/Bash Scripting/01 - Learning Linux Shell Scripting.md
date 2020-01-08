### 1 - Shell Something out
#### 1 - Printing in the terminal
+ `echo`
    * "" - keine spezial Zeichen
    * ' - mit spezial Zeichen
    * `echo -n` - Enter nicht printen
    * `echo -e "1\t2\t3" - Escape-Seq benutzen sonst alles als String
* `printf`
    * `printf "%-5s %-10s %-4s\n" No Name Mark`
    * `printf "%-5s %-10s %-4.2f\n" 1 Sarath 80.49`
    * `%s` - String
    * `%c` - Char
    * `%d` - Dezimal
    * `%d` - Float
    * `-5` - Left-Alignment
    * `5` - Right-Alignement
* Farben Test Printen:
    * Reset = 0, Black = 30
    * Red = 31, Green = 32, Yellow = 33, Blue = 34, Magenta = 35, Cyan = 36, White = 37
    * Bsp:
        * `echo -e "\e[1;31m This is red text \e[0m"` 
        * `\e[1;31m` - \e - Escape-Seq, 1;31m - Red
        * `\e[om]` - Reset
* Farbe Background Printen:
    * Reset = 0; Black = 40, Red = 41, Green = 42, Yellow = 43, Blue = 44, Magenta = 45, Cyan = 46, White = 47
    * Bsp:
        * `echo -e "\e[1;42m This is red text \e[0m"` 
* <- 3X - Text-Farbe; 4X - Backgroundfarbe
#### 2 - Playing with variables and environment variables
* `env` - Alle mit gerade verwendeten Terminal zugewiesenen/bekannten Variablen anzeigen
* Variable zu bestimmten Prozess anzeigen:
    * `pgrep gedit`
    * `cat /proc/PID/environ`
    * `cat /proc/PID/environ | tr '\0' '\n'` - bei der Ausgabe String-Ende durch Enter ersetzen => Zeilen-weise ausgabe der Env-Variablen
        * `whatis tr` -> Zeichen ersetzen und löschen
* `var = value` - Vergleich
* `var=value` - Zuweisung
+ Variable Printen
    * `echo "$varName"` oder `echo ${var}`
* Env-Var setzen:
    * `varName=LaLa`
    * `export varName` - Env-Variable setzen
* `$PATH` ist in /etc/profile oder so definiert
* `length=${4varName}` - Länge der Variable herausfinden - Anzahl der Chars
* `echo $SHELL` - welche Shell gerade benutzt
* mit `UID` kann man chechen, welcher User gerade angemeldet ist
* Prompt-Text einstellen über `PS1`-Variable. ist in .bashrc gesetzt
    * `cat ~/.bashrc | grep PS1`
    * `PS1="PROMPT>"` 
        * Und dann ähnlich wie es in ./bashrc steht Eingaben machen
#### 3 - Function to prepend (voranstellen) to environment variables
* `prepend { [ -d "$2" ] && eval $1=\"$2':'\$$1\" && export $1; }` - Funktioen definieren
    + `[ -d "$2" ]` - checkt, ob Ordner von Parameter 2 existiert
    + `eval $1=\"$2':'\$$1\"` - Variablenzuweisung
* oder besser, da sonst unschön, wenn $1 leer ist
* ``prepend { [ -d "$2" ] && eval $1=\"\$\{$1:+':'\$$1\}\" && export $1; }`
* `prepend PATH /opt/myapp/bin` - Funktionsaufruf mit 2 Parametern
#### 4 - Math with the shell
* `let` oder `(())` oder `[]` oder `expr`
    * `let result=var1+var2`
    * `let var1+=5`
    * `result=$[ var1 + var2 ]`
    * `result=$[ $var1 + var2 ]`
    * `result=$(( var1 + var2 ))`
    * ```result=`expr 3 + 4` ```
    * `result=$(expr $var1 + 4)`
* `bc` - mit echo String an bc übergeben
    + `echo "$var1 * 1.5" | bc`
    * `echo "scale=2;3/8" | bc` - dabei scale=2 ist Option für bc
    * `echo "obase=2;ibase=2;$var1" | bc` - Dez nach Binär konvertieren
    * `echo "sqrt(100)" | bc`
    * `echo "10^10" | bc`
#### 5 - Playing with file description and redirection
* File Descriptions = Integers, die auf geöffente Files zeigen.
    * 0 - stdin, 1 -stdout, 2 - stderr sind schon reserviert
* Rediraction = Content von einem Destricptor zu anderem schicken
* `echo "Text" > temp.txt`
* `echo "Text" >> temp.txt`
* `ls + > temp.txt` - stdio Redirect
* `ls + 2> temp.txt` - stderr Redirect
* `ls + 2&>1 temp.txt` - stderr nach stdin und stdin nach temp.txt
* `ls + 2> stderr.txt 1>stdout.txt`
* `ls + 2>/dev/null`
* `command | tee Datei1.txt Datei2.txt` - in zwei Dateien gleichzeitig redirekten
    * `cat temp.* | tee out.txt | cat -n` - tee überschreibt 
    * `cat temp.* | tee -a out.txt | cat -n` - Append
    * `echo "who is this | tee -` - stdin als Command-Argument benutzen;
* Redirection-Operatoren: `>`, `>>` - per Default redirekten stdin, sonst kann man den Datei-Deskriptor voranstellen.
* `<` `<<` - stdin redirekten = aus Datei in CLI schreiben
    * `cmd < datei.txt`
    * 
    ```bash
    cat <<EOF>log.txt
    LOG FILE HEADER
    This is a test log file
    Funktion: System stats
    EOF
    ```
* mit `exec` kann man eigene Redirektoren erstellen
    * `exec 3<input.txt` - eignen File Deskriptor für input.txt erstellen/zuweisen
    * `cat<&3` - Lesezugriff auf Deskriptor 3
    * `exec 5>>input.txt` - Screibe-Deskriptor erstellen
    * `exec appended line >&5`
    * `exec 4>output.txt`
    * `echo newline >&4` 
#### 6 - Arrays and associative arrays
* Array definieren
    * `array_var=[1,2,3]`
    * `array_var[0]=1`, `array_var[0]=2`
* Array Zugriff:
    * `echo ${array_var[0]}`, `echo ${array_var[$index]}`
    * `echo ${array_var[*]}` - ganzen Array printen
    * `echo ${#array_var[*]}` - länge des Arrays printen
    * `echo ${!array_var[#]}` oder `echo ${!ass_array[@]}`- alle Indexes des Arrays printen
* Associative Array:
    * `declare -A ass_array`
    * `ass_array=([index1]=var1 [index2]=val2)`
    * `ass_array[index3]=val3`
* Zugriff auf Ass Array:
    * `echo ${ass_array[index1]}` oder 
    * `echo ${!ass_array[*]}` - alle ass Indexes printen
#### 7 - Visiting aliases
* `alias new_command="command sequence"`
* <- in .bashrc eintragen;  `alias new_command="command sequence" >> ~/.bashrc`
* Bsp
    * `alias rm='cp $@ ~/backup && rm $@` - beim rm erst eine Kopie in ~/backup ablegen
* `\command` - die definierten Aliases nicht verwenden => gut Practive auf fremden Systemen 
#### 8 - Grabbing information about the terminal
* `tput` und `stty`
* `tput`:
    * `tput cols` - Anzahl der Reihen
    * `tput lines` - Anzahl der Zeilen
    * `tput longname` - Lange PROMPT
    * `tput cup 100 100` - in Terminal zu diese Position bewegen
    * `tput setb 4` - Background setzen (4 - Orange)
    * `tput setf 6` - Text-Farbe setzen (6 - Gelb)
    * `tput bold` - Text fett
    * `tput rmul` - Unterline
    * `tputed` - Eingabe wie bei Passwrod (Cursor nicht angezeigt)
* `stty`:
    * `stty -echo` - Autoput zu Terminal disablen
    * `sttey echo` - Autput zu Terminal enablen
#### 9 - Getting and setting dates and delays
#### 10 - Debugging the script
* `bash -x scriptName.sh` - Script in Debug-Mode ausführen
* man kann eigene DEBUG-Ausgabe erstellen indem man eigene DEBUG-Variable erstellt
```bash
function DEBUG(){
    [ "$_DEBUG" == "on" ] && $@ || : 
}

for i in ({1..10})
do
    DEBUG echo $i
done
```
* <- diesen Script dann mit `_DEBUG=on ./script.sh` starten. Wenn man den Script so nicht startet, wird kein `echo $i` gemacht
* Also sowas wie `#define` wie in C
* wenn man nur bestimmte Teile Debugen will, dann mit  `set -x/-v/+v` bestimmte Ausgaben an/ausmachen
    + `set -x` - zeigt Commandes an, bevor sie ausgeführt werden
    * `set -x` - Debugging disabeln
    * `set -v` - zeigt Input, wenn dieser gelesen wird
    * `set +v` - Disabled Printing
* man kann Shebang-Tricks benutzen um zu Debuggen
#### 11 - Functions and arguments
#### 12 - Reading the output of a sequence of commands
#### 13 - Reading n characters without pressing the return key
#### 14 - Running a command until it succeeds
#### 15 - Field separators and iterators
#### 16 - Comparisons and tests

### 2 - Have a Good Command
#### 1 - Concatenating with cat
#### 2 - Recording and playing back terminal sessions
#### 3 - Finding files and file listing
#### 4 - Playing with xargs
#### 5 - Translating with tr
#### 6 - Chechsum and verfication
#### 7 - Cryptographic tools and hashes
#### 8 - Sorting unique and duplicates
#### 9 - Temporary file naming and random numbers
#### 10 - Splitting files and data
#### 11 - Slicing filenames and data
#### 12 - Reanming anv moving files in bulk
#### 13 - Spell checking and dictionary manipulation
#### 14 - Automating interactive input
#### 15 - Making commands quicker by running parallel processes

### 3 - File In, File Out
#### 1 - Generating files of any size
#### 2 - The intersection and set difference (A-B) on text files
#### 3 - Finding and deleting duplicates files
#### 4 - Working with file permissions, ownership, and the sticky bit
#### 5 - Making files immutable
#### 6 - Generating blank files in bulk
#### 7 - Finding symbolic links and their targets
#### 8 - Enumerating file type statistics
#### 9 - Using loopback files
#### 10 - Finding the difference between files, and patching
#### 11 - Using head and tail for printing the last or first ten lines
#### 12 - Listing only directories - alternative methods
#### 13 - Fast command-line navigation using pushd and popd
#### 14 - Counting the number of lines, words, and characters in a file
#### 15 - Printing the directory tree
#### 

### 4 - Texting and Driving 
#### 1 - Using regular expressions
#### 2 - Searching and mining text inside a file with grep
#### 3 - Cutting a file column-wise with cut
#### 4 - Using sed to perform text replacement
#### 5 - Using awk for advanced text processing
#### 6 - Finding frequency of words used in a given file
#### 7 - Compressing or decompressing JS
#### 8 - Merging mutliple files as columns
#### 9 - Printing the nth word or column in a file or line
#### 10 - Printing text between line numbers and patterns
#### 11 - Printing lines in the reverse order
#### 12 - Parsing email address and URLs form text
#### 13 - Removing a sentence in a file containing a word
#### 14 - Replacing a pattern with text in all files in a directory
#### 15 - Text slicing and parameter operations

### 5 - Tangled Web? Not a page
#### 1 - Downloading from a web page
#### 2 - Downloading a web page as plain text
#### 3 - A primer on cURL
#### 4 - Parsing data from a website
#### 5 - Image crawler and downloader
#### 6 - Web photo album generator
#### 7 - Creating a define utility by using the web backend
#### 8 - Finding broken links in a website
#### 9 - Tracking changes to a website
#### 10 - Posting to a web page and reading response

### 6 - The Backup Plan
#### 1 - Archiving with tar
#### 2 - Archiving with cpio
#### 3 - Compressing data with gzip
#### 4 - Archiving and compressing with zip
#### 5 - Faster archiving with pbzip2
#### 6 - Creating filesystems with compression
#### 7 - Backup snapshots with rsync
#### 8 - Version control-based backup with Git
#### 9 - Creating entire disk images using FSArchiver

### 7 - The Old-Boy Network
#### 1 - Let us ping
#### 2 - Listing all the machines alive on a network
#### 3 - Running commands on a remote host with SSH
#### 4 - Transferring files through the network
#### 5 - Password-less auto-login with SSH
#### 6 - Port forwarding and mounting remote drives
#### 7 - Network traffic and port analysis
#### 8 - Creating arbitrary sockets

### 8 - Put on the Monitor's Cap
#### 1 - Monitoring disk usage
#### 2 - Calculating the execution time for a command
#### 3 - Collecting information about logged-in users, boot logs, and boot failures
#### 4 - Listing the top ten CPU-consuming processes in an hour
#### 5 - Monitoring commands outputs with watch
#### 6 - Logging access to files and directories
#### 7 - Log file management with logrotate
#### 8 - Logging with syslogd
#### 9 - Monitoring user logins to find intruders
#### 10 - Remote disk usage health monitor
#### 11 - Finding out active user hours on a system
#### 12 - Measuring and optimizing power usage
#### 13 - Monitoring disk activity
#### 14 - Checking disk and filesystems for errors

### 9 - Administration Calls
#### 1 - Gathering information about prcesses
#### 2 - Killing processes and send or respond to signals
#### 3 - Sending messages to user terminals
#### 4 - Gathering system information
#### 5 - Using /proc for gathering information
#### 6 - Scheduling with cron
#### 7 - Writing and reading the MySQL database form Bash
#### 8 - User administration script
#### 9 - Bulk image resizing and format conversion
#### 10 - Taking screenshots from the terminal
#### 11 - Managing multiple terminals from one