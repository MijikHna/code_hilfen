### 1 - Getting Help
#### 1 - Learn Linux command syntax
* `command [options] <argument>`
* Wenn Optionen ein Wort ist => `--`
* Wenn Optionen ein Buchstabe ist => `-`
* man kann Optionen zusammenfassen
* Bsp:
    * `ls -s` - Größe der Datei ausgeben
    * `ls -s -1` = `ls -s1` = `ls --size -1` - Pro Zeile nur ein Wort
#### 2 - Get help on the CLI
* `--help` - Dokumentation:
    * `ls --help` 
    * **SHIFT+Bild↓** = im Terminal scrollen
    * für `cd` gibt es kein `--help`, da cd in bash eingebaut ist und ist kein eingeständiges Programm aber es geht `help cd`
* `man ls` - Manual des Befehls
    * `man` ist in Kategorien aufgebaut
    * `man man-pages` - Ansehen für was sind die einzelnen man-Kategorien
    * `man 1 intro` - Intro-Pages für einzelne Kategorien anzeigen
    * `man -f crontab` - alle Kategorien des Befehls ansehen
    * `man 5 crontab` - Bestimmte Kategorie des Befehls ansehen
    * `man -k crontab` - alle Kategorien des Befehls ansehen + erweiterte Kategorien
    * `info crontab` - Info-Page anzeigen. Info-Pages sind umfangreicher + mit Hyperlink (~ Menü)
        * Hyperlink = hat am Ende `::`
        * in Hyperlink reingehen = `Enter`
        * Zurück = `l`
        * `?` - Infor zur Benutzung der Info-Page (wie man sich in Info-Page navigiert)
#### 3 - Get help on the GUI
* `yelp` - GUI-Hilfe für Desktop
* `yelp man:crontab` - Man für des Befehl in GUI anzeigen
* `yelp info:crontab` - Info-Page des Befehls in GUI anzeigen -> man kann sich besser durch Hyperlink durchklicken
* `BROWSER=firefox man -H crontab` - man von Befehl im Browser aufmachen. Per default wird im /tmp angelegt => man kann die HTML aber speichern und z.B Lesezeichen setzen, drucken usw.

#### 4 - Find help online
* ePub-Format = für SW die eReader lesen können. Mit SW Calibre kann man ePub-Dateien zu Mobi-Format konvertieren um z.B auf Kindle die Datei zu lesen
* welche Doku man lesen sollte:
    * Insallation Guide
    * System Adminstrators Guide
    * Networking Guide
    * Storage Administration Gade 
    * Logical Volume Manager Administration Guide
* tlcp.org - Linux Doku
* linux.de.net/man - alle Man für Linux Dateien
* explainshell.com - Hilfe für Befehle

### 2 - Using Basic Commands
#### 1 - Gather operation system information
* LSB = Standardisierungsversuch HW-Info zu sammeln.
* `lsb-base` und `lsb_release` installieren
* `lsb_release -a` - Distro-Info
* `cat /etc/os_release` - Distro-Info
* `hostnamectl` - ist Teil von systemd
* `uname -r` - Kernel-revision anzeigen
* `uname -a` - alle Kernel-Info
* `uptime` - Laufzeit des Systems anzeigen
* `uptime -p` - besserer\pretty Output
* `dmesg` - Nachrichten von Kernel
* `dmesg -H` - besser Lesbare Ausgabe
* `free -m` - Memory in MegaByte
* `cat /proc/meminfo` - Ausführliche Info über Memory
* `gnome-system-monitor` installieren
    * System-Monitor öffnen
#### 2 - Gather hardware information
* `dmidecode` - Systeminfo
    * `sudo dmidecode`
    * `sudo dmidecode --type bios`  - Bios-Info
    * `sudo dmidecode --type system`
    * `sudo dmidecode --type baseboard`
* USB-Geräte:
    * `lsusb`
    * `lsusb -v` - Mehr Info
* `lspci` - PCI-Geräte
* `cat /proc/cpuinfo` - CPU-Info, Flags geben aus, ob CPU bestimmte Features unterstützt
* `lsblk` - Fesplatten-Info
* `lsblk -f` 
#### 3 - Login commands
* `$` - Normaler User; `#` - Superuser
* `whoami` - eingeloggten User anzeigen (Momentan)
* `logname` - eingeloggten User am PC anzeigen
* `su root` - switch user
* `who -H` - mehr Info über eingelogte User
* `w` - 
* `id` - Mehr Info über den User
* `groups`
* `lastlog` - es gibt viele User, die für bestimmte Systemaufgaben erstellt wurden und die bestimmte Systemprogramme starten
* `last -F` - zeigt User, die eigeloggt sind/waren. Die vor kurzerem angemeldeten User werden oben angezeigt
* `last -F | tac` - `tab` wie cat aber Rückwärts
* `lastb` - Fehlerhafte Loggins anzeigen
#### 4 - Time and date
* wenn man NTP einstellt => der Rechner holt sich die Uhrzeit aus Internet, sonst per Interne Uhr.
* `timedatectl` - zeigt die Zeit + Zeiteinstellungen
* `timedatectl list-timezones` - Zeitzonen anzeigen
* `timedatectl list-timezones | grep America` - Zeitzonen spezifizieren
* `timedateclt set-timezone America/Vancouver` - Zeitzone auswählen
* `timedatectl set-time 23:26:00` - eventuell das Befehl zwei Mal eingeben
* `timedatectl set-time 2019-10-20`
* `timedatectl set-time '2010-10-20 12:20:00`
* `timedatectl set-ntp true` - NTP setzen
* `sudo systemctl resatart systemd-timedated` - ZeitDate neustarten, damit NTP synchronisierung
* `sudo apt-get install chrony` - NTP-Client installieren
#### 5 - Locale and date tools
* `localectl` - Locale, Keyboard anzeigen
* `localectl list-locales` - alle Locale anzeigen
* `localectl list-locales | grep ^en` - Locale anzeigen, die mit en beginnen
* `localectl set-locale LANG=en_US.utf8`
* `localectl list-keymaps`
* `localectl list-keymaps | grep ^en`
* `localectl set-keymap us`
* `date` - Datum + Zeit anzeigen (lokale)
* `date --utc` - UTC-Zeit anzeigen
* `date +"%h %d% %Y"` - Date formatiert ausgeben oder `date +%s` - Zeit in Sek ausgeben (um z.B im Skript Zeitdiffs zu bilden)
* `date --date="@153592351` - Gibt Sek als Datum
* `date --date '+10 days'` - Jetzt + 10 Tage
* `date --date 'next thursday'`
* `cal` - Kalendar anzeigen
* `cal -3` - 3 Monate anzeigen
* `cal 3` - 3 Jahre anzeigen
#### 6 - View files
* `journalctl > journal.txt` - Stdout umleiten
* `tac journal.txt` - cat Backwords
* `sort journal.txt` - alphabetisch sortieren
* `more journal.txt` - Pager more verwenden
* `less journal.txt` - ist mächtiger als more
* `journalctl | less` - Ausgabe direkt an anderes Programm weiterleiten 
* `head journal.txt` - ersten 10 Zeilen anzeigen
* `head -n100 journal.txt` - 100 Zeilen anzeigen
* `tail journal.txt` - letzten 10 Zeilen anzeigen
* `sudo tail -f /var/log/messages` tail kann das Ende einer Datei verfolgen -> sehr gut für System Admins = logs verfolgen
* `wc journal.txt` - Wörter zählen
* `wc -l journal.txt` - Zeilen zählen
* `journalctl | head -n100 | tac | less` 
#### 7 - Search within a file
* `journalctl > journal.txt`
* grep-Syngax = `grep [suchkriterien] [datei]`
* `grep kernel journal.txt`
* `grep ^Dec journal.txt` - Zeilen die mit **Dec** beginnen
* `grep Service.$ journal.txt` - alle Zeilen, die mit **Service.** enden
* `grep -c ^Dec journal.txt` - Zählen, wieviele Zeilen mit **Dec** beginnen
#### 8 - Archive files
* in Linux benutzt man Archive um Metadaten zu bewahren (Rechte, Besitz usw.)
* Tar selbst kompremiert die Daten nicht, sondern übergibt die Daeien an weitere Tools
* `sudo tar --xattrs -cvpf etc.tar /etc`  - `--xattrs` - bewahrt die erweiterten Attribute wie Access Control, SELInux security; `-c`=Create Archiv, `-v`=Verbose, `-p`-Besitz übernehmen, `-f`= File name
* `sudo tar --gzip --xattrs -cvpf etc.tar.gz /etc` - als gz Kompremieren
* `sudo tar -bzip2 --xattrs -cvpf etc.tar.bz2 /etc` - als bz2 kompremieren
* `sudo tar --xz --xattrs -cvpf etc.tar.xz /etc`
* `tar -tf etc.tar` - `-t` = zurückkompremieren mit `-t` + anzeigen
* `tar --gzip -tf etc.tar.gz` - gz zurückkomprieren + anzeigen -> als Option das Komprimierungstool angeben
* `sudo tar --xattrs -xvpf etc.tar` - mit `-x` extrahieren 
* `sudo tar --xattrs -xvpf etc.tar -C /home/lala` - mit `-C` den Order zum extrahieren angeben
#### 9 - Compress files
* `cp /etc/services .`
* `gzip services` - existierende Ordner wird kompriemiert und "überschrieben"
* `gunzip services.zp` - Order extrahieren
* `bzip2 services` 
* `bunzip2 services.bz2`
* `xz services`
* `unxz services.xz`
* `zip services.zip services` - Original wird stehen gelassen wird
* `unzip services.zip`

### 3 - Navigating File System
#### 1 - List files
* `pwd` - print working direktory
* `ls --color=auto` - Farbe für `ls` in Terminal anschalten
* `alias ls='ls --color==auto'`
* `ls`-Optionen:
    * `-1` - ein Wort pro Zeile
    * `-l` - long list. `-` am Anfang von `rwxrwxrwx` = Datei, `d` = Directory, `c`-character Device, `b`-Block device wie Festplatte, `l`=symbolischer Link
    * `-h` - human readeable size
    * `-R` - rekursive Ausgabe
#### 2 - Understand file system paths
* `sudo apt-get install tree`
* `tree .` -
* `file /etc/services` - Typ der Datei herausfinden
* `cd -` - zu letzen Pfad gehen
#### 3 - Explore the Linux file system
* `/bin` - Command binaries
* `/boot` - Boot loader (Grub + Kernel)
* `/dev` - Device Files
* `/etc` - System config files (als Text gespeichert)
* `/lib` - 32-bit system Libraries
* `/lib64` - 64-bit system Libraries
* `/media` - Mount Points for removable media
* `/mnt` - Temporary mounted filesystems
* `/opt` - optional application software packages
* `/proc` - Virtual system providing process and kernel Info as files. Dateien werden vom Kernen hier reingeschrieben
* `/run` - Rin-time config-Dateien
* `/sbin` - Essential system binaries. Tools für System Admins um PC zu verwalten
* `/srv` - Site-spezific data served by this system z.B Directories für Protokole oder virtuelle Festplatten
* `/sys` - Infor about devices connected to PC
* `/usr` - read-only user Data, contains majority of utilites and apps. OS-Daten + System-Befehle
* `/var` - variabl Files whose content is expected to change during normal operation, z.B log-Dateien. 
#### 4 - Find files with locate
* `locate bzip2`
* `locate -c bzip2` - zählen, wie viel gefunden
* `locoate bzip2 man` - bzip2 oder man suchen
* `locate -A bzip2 man` - bzip und man suchen
* `locate -I High` - Groß-/Kleinschreibung ignorieren
* `locate --regexp '^/usr.*pixmaps.*jpg$'` - Reg Exp in locate verwenden
* `locate --regexp '^/usr.*(pixmaps|backgrounds).*jpg$`
* `locate -S` - Zustand von locoate-DB anzeigen
* `suod updatedb` - locate updaten  
#### 5 - Find files with find
* `find` ist mächtiger als `locate`, obwohl keine DB hat
* `sudo find / -name bzip2` - nach Datei, die **bzip2** hießt suchen, angefangen bei `/`
* `sudo find / -name *bzip2* | sort` - mehr wie locate-Ausgabe
* `sudo find / -user tralala` - nach Datien von tralala suchen
* `sudo find / -group tralala` - nach Dateien von Gruppe tralal suchen
* `sudo find / -size +50k` - nach Dateien die größer als 50k sind suchen
* `find` kann am gefundenem Objekt Operationen ausführen: 
    * `sudo find / -size +1M  -exec stat -c %s %n { } \;`  - `stat` an gefundenen Objekten ausführen  `{}` = Platzhalter für Name, `\;`= keine Behefehle mehr ausführen
    * `sudo find / -size +1M  -exec stat -c %s %n { } \; | sort -n` - Dateien anhand der Größe sortieren
+ `sudo find / -mtime -1` - Dateien die am letzen Tag modifiziert wruden finden
+ `sudo find / -mtime -1` - Dateien die nicht am letzen Tag modifiziert wruden finden
* `sudo find /home -type f` - nur nach Dateien suchen
* `sudo find /home -type d` - nur nach Ordnern(Directory) suchen
### 4 - Editing Text
#### 1 - Nano
* `nano -u datei.txt` - nano mit Undo öffnen
* **STRG+R** = Datei in nano einfügen -> Dateinamen eingeben
* **STRG+K** = Text zum Buffer hinzufügen, nochmal klicken = weitern Text zum Buffer
* **STRG+U** = Einfügen
    * <- steht aber unten
* **STRG+6** = Text markieren
* **ALT+U** = undo
* **ALT+E** = redo
* **STRG+G** = Doku von nano
#### 2 - Vim
* ist sehr powerpull
* 3 Modes
    1. Insert-Mode - `i`
    2. Command-Mode - `esc`
    3. Ex-Mode = Befehle unten eingeben - `esc + :` 
#### 3 - Edit text in Vim
* **ESC + U** - in Command + Undo
* **ESC + STRG+R** - in Command + Redo
* cut:
    1. **C+L** - Cut a letter
    2. **C+W** - Cut a word
    3. **C+C** - Cut a line
* paste (put):
    1. **P** - Paste
* copy (yank)
    1. **Y+L** - Copy a letter
    2. **Y+W** - Copy a word
    3. **Y+Y** - Copy a line
* delete: - 
    1. **D+L** - Cut a letter
    2. **D+W** - Cut a word
    3. **D+D** - Cut a line
#### 4 - Search and replace in Vim
