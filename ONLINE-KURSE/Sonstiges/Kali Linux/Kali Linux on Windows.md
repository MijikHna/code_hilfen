### Introduction
### 1 - Lab Setup:
* Lab Setup:
    * Windows 10
        * Metasploitable Linux virtual machine - Target VM with security vulnerabilites build in <- diese wird getestet mit Kali Linux (NW zu Bridged)
            * Image von hier herunterladen: imformation.rapid7.com/metasploitable-download.html
* 

### 1 - Windows Subsystems for Linux
#### 1 - Understanding and enabling Windows Subsystem for Linux (WSL)
* Compatibility layer for Linux binaries
* WSL ersetzt Linux Kernel
* SW benutzt aber tatsächlich Windwos Kernel
* Linux installiern um Linux binaries in Windows zu laufen
* Fazit: Windows gibt vor Linux zu sein, wurde für Entwickler ausgedacht
* WSL anmachen:
    * Windows Features
    * Windwos Subsystem for Linux
    * Windows neustarten
### 2 - Kali Linux
#### 1 - Kali Linux
* für Security Testing und Analysis enwickelt (keine Alltag OS)
* hat Repos für diese Tools
* für Attackers und Defenders
* Windows Defender kann Kali als Malware identifizieren, da Tools Malware-Signature haben
#### 2 - Installing Kali Linux on Windows 10
* Windows Store:
    1. Kali 
    2. Installieren
    3. Windows Defender settings -> Virus Protection -> Exclusiong -> Add -> Folder -> c\Users\lala\AppData\Local\Packages\Kali...\
    4. Kali starten
    5. User + Passwort 
    6. `cat /etc/*release` 
    7. `cat /etc/apt/sources.list`
    8. keine Eigenen Repos einfügen <- Tipp von Kali-Entwicklern
    9. Man muss Tools selbst installieren, da nur minimale Installation
        * https://tools.kali.org/tools-listing - Liste mit Kali Tools
            * Tool Listing - einzelne Tools oder Metapackages - ganze Packete
    10. `apt list --installed` - installierte Tools
    11. `sudo apt update`
    12. `sudo apt install whatweb` - Whatweb-Tool installieren
    13. `whatweb` - Tool um zu erfahren welches Service auf einem Server läuft. `whatweb https:\\wordpress.com`
    14. `sudo apt install kali-linux-full` - alle Kali-Tools installieren
    15. `dpkg-reconfigure lala` - App neukonfigurieren
#### 3 - Using Kali Linux
* WLS rlaubt nicht den Access zu Raw Sockets (Nmap, WireShark, hping3 usw. werden nicht funktionieren)
* `nikto -host 10.0.2.5` - *nikto* ist Server Vulnerable Scanner. Ausgabe sind Warning oder Alerts. (lese Dokumentaion)
* *John the ripper* - Tool um Passwörter aus Hashes finden. Braucht Datei mit hash-Passwörtern z.B von contest-2012.korelogic.com herunterladen.
    1. `cd /mnt/c/Users/lala/Downloads`
    2. `tar xjf ...tar.bz2`
    3. `mkdir ~/hashfiles`
    4. `mv .. ~/hashfiles`
    5. `john --wordlist hashes-3.dex.txt`
    6. `cat ~/.john/john.pot` - die Eingabe Datei wird in *.john/john.pot* gespeichert 
    7. `msfconsole` - Metasploit-tool
#### 4 - Using graphical tools
* Destktop Manager und X Server installieren um GUI zu haben
    * in WSL Xfce und x.Org und XMing on Windows installieren
        1. `apt install xfce4 xorg`
        2. Xming X server for Windows installieren
        3. XMing starten
        4. `export DISPLAY=:0`
        5. `xeyes` - Test
        6. `xfce4-session` -> Use Default
        7. Application -> Kali Tools:
            * OWASP ZAP -> http://10.0.3.5 - Mashine angreifen (diese Mashine, die VM läuft) -> Alerts anzeigen
        8. *STRG+C* - GUI beenden
#### 5 - Managing and resetting the Kali environment 
* Kaliroot ist in *C:\Users\lala\AppData\Local\Packages\Kali...\LocalStore\rootfs
    + aus Windows sollte man da nicht machen
    * unter Kali mit */mnt/c* ansprechen
* Windows Files exclude z.B bei *find*,
    * `find / -name "*secret*" - print -o -path "/mnt/c" -prune`
+ WSL stopen:
    in cmd: `net stop LxssManager`
+ Kali reseten:
    * Kali löschen und nochmal aus dem Store laden