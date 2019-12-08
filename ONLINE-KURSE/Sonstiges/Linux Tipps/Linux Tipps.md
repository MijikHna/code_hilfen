### System Basics
* `command \` - Fortseten auf der nächsten Zeile
* `apropos commandEnthält` - Commandos mit commandEnthält-enthaltende anzeigen
* Shortcuts:
    * `STRG+A` - zum Beginn der Zeile
    * `STRG+E` - zum Ende der Zeile
    * `STRG+T` - vertauschen der einzelnen Buchstaben auf den Seiten des Cursors
    * `STRG+Z` - Task in BG schieben
    * `STRG+D` - End des Inputs
    * `STRG+SHIFT+C` - Copy
    * `STRG+SHIFT+X`
    * `STRG+SHIFT+V`
* `sudo visudo` - /etc/sudoers.d öffnen
* `sudo -i` - Benutzer-Shell starten + deren Home öffnen
* `sudo -s` - User-Shell starten
* `sudo -l` - zeigen welche sudo-Rechte der User hat
* `sudo -u` - User auswählen
* `ls /etc/*release` - OS-Info-Dateien anzeigen
* `uptime` - wie lange User online ist
* `free` - Speicher anzeigen
* `who` - Users-TTYs anzeigen
* `systemclt`
    * `systemctl | grep running`
* `echo`
    * `echo h{e,a,u}llo` => hello, hallo, hullo
    * `echo h{a..z}llo`
    * `echo h{0..10}llo`
    * `echo echo h{z..a}llo`
    * `echo h{0..100..5}` - h0 h5 h10 h15 h20
    * `echo {a..z}{a..z}{0..9} >> output.txt`
    * `echo file_{100..0..5}`
* Shebang
    * `#!/usr/bin/env bash`
+ `read -p "What is your name" name` - Nach eingabe fragen
* `auf der Seite *http://bashrcgenerator.com/* kann man das Aussehen der Bash visuell einstellen
* `wc < text.txt` - Wörter zählen
* `alias command` - Alias-Inhalt anzeigen
* `alias newCommand="oldCommand -optionen xxx`
* `unalias command`
* `function greplog () {grep $1 /var/log/syslog; }`, `greplog dhcp` - Funktion für Logging bestimmtes Teils + Aufruf