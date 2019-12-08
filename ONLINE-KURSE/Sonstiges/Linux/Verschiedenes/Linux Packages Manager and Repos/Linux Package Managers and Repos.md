### 0 - Introduction
#### 2 - What is package management?
* add, remove, update, modify SW
* SW wird als Source oder als Binary geliefert
* heute kommt SW in Package
* Packages haben:
    * Source code
    * Binaries
    * Scripts
    * Metadaten
* Dependencies - wenn ein Package einen anderen Package oder bestimmte Sprache oder tool Chain oder Shared Lib braucht.
    * Depencdency Resolution - kann man manuell machen, aber Package Manager machen das automatisch.
    * manchmal muss man aber manuell engreifen
* Package Manager - mit Package arbeiten
    * behandeln Packages wie Dateien
    * oder downloaden sie aus Repos
* Repositories - Liste von Packages
    * Linux-Distro kommt mit default Repos. SW-Version hängt von Distro ab.
#### 3 - Package naming
* Packet muss für die richtige Distro und Maschinen-Architectur sein
    * *noarch* - hängt nicht von Architektur ab. Kann überall genutzt werden
    * `uname -m` - Arch herausfinden

### 1 - Manage Packages with RPM and YUM
#### 1 - The RPM and YUM package managers
* *RPM* - RedHat Package Manger für CentOS, Fedora 
    * man kann RPM direkt benutzen, wenn man .rpm hat
    * yum - Yellowdog Update, Modifier. sitzt auf Top von RPM. Vorteil von yum gegenüber RPM, dass er Dependencies automatisch managet
* RMP hat DB mit installierten SW (RPM-DB)
* beim Update cached yum die Repos-Inhalte
* `man yum` und `man rpm` 
#### 2 - Searching for a package
* man kann direkt .rpm herunterladen oder mit yum die Repos durchsuchen
    * `yum search tree`- nach tree suchen
    * `yum search all tree` - Treffer wird nicht hervorgeboben
    * `yum -v search all tree` 
    * `yum provides nmcli` - nach SW suchen, dass *nmcli*-Befehl hat
#### 3 - Downloading a package file
* `wget http...` <- davor noch den Link zum Download kopieren
* *npmfind.net* - im Web nach .rpm suchen
*  `yum install --downloadonly uuid` - Pacakge nur downloaden ohne Installation. Landet in */var/cache/yum/..*
#### 4 - Finding package information
* `yum info tree`- Info zu tree anzeigen
* `rpm -qlp uuid...rpm` bzw. `rmp -qlp PackageName`- den Inhalt + Info von .rpm anzeigen `-qlp` - Query,List,PackageFile
    * /usr/bin/.. - sit Binary
    * /usr/lib64/.. - ist Shared Lib
    * /usr/share/doc/.. - ist Doku 
    * /usr/share/man/.. - ist für Man-Page
* `yum -qlpv uuid...rpm --scripts` - mit verbose + `--scritps` zeigt an, welcher Skript bei Installation ausgeführt wird
* `yum -ql uuid` - Info zu den Installierten SW
* `yum -ql uuid --scripts` - Ziegt welcher Skript bei Installation ausgeführt wurde
* `rpm -qf /usr/bin/sed` - nachschein von welchen Packet eine bestimmt Datei kam. `-f` - File
#### 5 - Explore package dependencies
* `yum deplist nano` - Dependencies für *nano* anzeigen
* `yum list bash` - zeigt an ob *bash* installiert ist
* `rpm -qpR uuid...rpm` - Dependencies für .rpm anzeigen. *-R* = Requires
* `rpm -qpRv uuid...rpm`
#### 6 - Installing a package
* `yum install tree` 
* `yum localinstall uuid...rpm` - .rpm installieren
* `rpm -i uuid..rpm` - .rpm isntallieren *-i*-Install
#### 7 - Checking what has installed
* `yum list nano` - schauen, ob nano isntalliert ist
* `yim list installed` - was allgemein installiert ist
    * Fette SW ist alte SW als in Repo, die upgedatet werden
    * Yellow - Version ist neuer als in Repo bekannt
    * red - kein Packet in Repo bekannt
    * blue - Update bekannt
* `yum list all` - zeigt ale SW aus den Repos
    * cyan/blau - Downgrade möglich
    * grün - ist gleich der Repo-Version
#### 8 - Installing groups of packages
* Gruppen = Tool Chains installieren - werden meist für einen bestimmten Service gebraucht
* `yum gouplist` - welche Gruppen in Repo vorhanden sind
* `yum groupinfo "Gruppen Name"` - zeigt alle SW der Gruppe, Optional Group - wird per default nicht installiert, muss man extra sagen
    * `+` - Package ist nicht installiert, also wird gleich installiert
    * `=` - wurde mittel GroupInstall installiert
    * ` ` - wurde installiert
    * `-` - wird nicht installiert
* `yum groupinfo group-aus-z.b.-manadatory-group` - zeigt Packete, die in dieser Gruppe sind
* `yum install "Gruppen Name"` - Gruppe installieren
* `yum --setopt=group_package_types=optional groupinstall "Gruppen Name"` - auch Optional Packages installieren
* `yum groupinstall "Basic Web Server" php` - Default + Basic-Teile installiert + zusätzlich php-Package installiert aus Optional
#### 9 - Removing a package
* `yum remove nano`
* `rpm e- uuid` 
* `yum groupremove "Gruppen Name"`
#### 10 - Upgrading a package
* `yum check-update` - mögliche Updates anzeigen
* `yum update` - Update durchführen
* Updates für bestimmte Packete verweigern
    1. `yum update -x PackageName` - Packet aus dem Update herausnehmen *-x* - Exclude
    2. verionlock plugin für yum installieren und `yum versionlock PackageName` 
        * `yum versionlock` - anzeigen, welche Packet von Update festgehalten werden
        * `yum versionlock delete ausgabezeile_aus_yum_versionlock` - Packet aus Versionlock rausnehmnen
        * `yum versionlock clear` - aus aus Versionlock rausnehmen
* `yum update packet` - bestimmten Packet upgraden
#### 11 - Installing form source
* mit Make
* Makefile wird von *configure* erstellt, *configure* analysiert das System und setzt Variablen in Make anhängig vom System
* Tools = "Development Tools"
    * `yum groupinfo "Development Tools"`
    * `yum groupinstall "Development Tools"`
* Bsp:
    * tar herunterladen
    + `tar -xf lala.tar.bz2`
    + `./configure` - ist eigentlich Shell-Script. Configure kann Error produzieren, wenn es bestimmte SW nicht finden kann. Es wird *MakeFile* erstellt
    * `make`
    * `make -n install` - zeigt den make-Skript an
    * `sudo make install` - von Make erstellten Dateien in richtige Orte kopieren
    * manchmal wird auch uninstall-Skript zur Verfügung gestellt, manchmal muss man alles manuell deinstallieren

### 2 - Manage Packages with dpkg and APT
#### 1 - the dpkg and APT package managers
* *dpkg* - Debian Package - managet Packages
* *apt* - zum Repos Online durchsuchen
* *aptitude* - Text-Interface + CLI
* `man dpkg`, `man apt`, `man apt-get`, `man apt-cache`, `man aptitude`
#### 2 - Searching for a package
* `apt search PackageName` - nach Packet oder nach Text relavant zum Package suchen
* `apt-cache search packageName` - Repo-Infos durchsuchen -> Mehr Infos; mit `apt search` ist besser
#### 3 - Downloading a package
* entweder .deb oder über *apt*
    * .deb - von packages.ubuntu.com + z.B uuid herunterladen; nano von nano-Seite herunterladen
    * `apt-get download packetName` - nur herunterladen, wird in Ordner heruntergeladen, wo man gerade ist
#### 4 - Finding package information
* `apt show packetNamo` - Info zum Packet aus Repo
* `dpkg --info packetName.deb` - Info von .deb
* `dpkg -c packetName.deb` - anzeigen, was wohin installiert wird
* `dpkg -S /usr/bin/nmcli` - anzeigen, welche Packet für die SW zuständig ist
* `dpkg -S pacakgeName` - installierte Version checken
#### 5 - Installing a package
* `apt install packageName`
* `apt-get install packageName`
* `dpkg -i packageName.deb`
* `apt install`:
    * `apt install packageName`
* `dpkg`
    * `dpkg --info packetName.deb` - um z.B Dependencies zu installieren
    * zuerst die Dependecies installieren
    * `dpkg -i packageName.deb`
#### 6 - Checking what has installed
* `apt list` - alle Packages in Repos anzeigen
* `apt list --indstalled` - installierte packages anzeigen
* `dpkg -L packageName` - anzeigen, was hat ein package genau installiert
* `dpkg -s pacakgeName` - checken ob Package installiert ist
* `apt list packageName` - anzeigen ob Pacakge in Repos ist
#### 7 - Exploring aptitude
* `apt install aptitude`
* hat die gleichen Befehel wie apt + weitere
* `aptitude` - Terminal-Menü (C -T = Shift+T) ~ Terminal-Synaptic
    * `/` - nach Package suchen
    * packageNamen eingeben
        * *i* - installed, *p* - not installed, *c* -was deleted und configs sind geblieben, *v* - virtual
    * Klicken:
        * *d* - delete Package, *STRG+U* - zurück/abbrechen, *+* - install
            * Falls dependencies nicht erfüllt wird im Resolver-Teil die Abhängigkeit angezeit:
                * *i* - Dependencies checken 
#### 8 - Removing a package
* *remove* - Package wird entfernt
* *remove purge* - auch Configs-werden gelöscht
* `apt remove pacakgeName`
* `dpkg -r PackageName`
#### 9 - Upgrading a package
* `apt show -a PackageName` - info zu vorhandenen Versionen anzeigen
* `apt show nano` - checkt nur Version auf dem Rechner
* `apt-mark hold packageName` - Package vom update halten
* `apt-mark unhold packageName`
#### 10 - Installing form source
* mit Make - Build automation tool zum Code-Kompilieren. liest Makefile
* Makefile wird von *configure* erstellt, *configure* analysiert das System und setzt Variablen in Make anhängig vom System
* `apt install build-essential` - Make-Tools installieren
* Bsp:
    * tar herunterladen
    + `tar -xf lala.tar.bz2`
    + `./configure` - ist eigentlich Shell-Script. Configure kann Error produzieren, wenn es bestimmte SW nicht finden kann. Es wird *MakeFile* erstellt
    * `make`
    * `make -n install` - zeigt den make-Skript an
    * `sudo make install` - von Make erstellten Dateien in richtige Orte kopieren
    * manchmal wird auch uninstall-Skript zur Verfügung gestellt, manchmal muss man alles manuell deinstallieren
    * apt und dpkg haben dann aber keine Ahnung von dieser SW
