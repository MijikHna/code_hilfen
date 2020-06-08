### Mount NTFS
* `sudo mount -t cifs -o defatult,username=userXXXX,password=XXXXX,uid=userXXXX,vers=2.1 //Server/Order /media/ordner`
* `sudo mount -a` - Festplatten aus `/etc/fstab` neueinlesen/verbinden

### chmod
* `chmod -v 777 datei.end`
* `chmod ugo +/-rwx datei.end` - (`ugo` - UserGroupOthers)

### Kernen Header installieren
* `sudo apt-get install linux-headers-$(uname -r)`

### Alle Datien im Ordner löschen
* `rm -r Ordner/*`

### Laufende Programme/Dienste suchen
* `lsof -i | grep programName`

### PC-Info
* `sudo dmicode -t0 -t1`
#### Hardware-Info
* `lspci`
* `lsusb`
* `lsmod`
* `lspci -nnk | grep net -A2` - NW-Hardware (Name und Chipsatz) anzeigen
* `sudo dmidecode | grep -A2 "Bios Information`
#### Audio-Info
* `lspci -nnk | grep -i audio -A2`
* `cat /proc/asound/cards`
#### Grafik
- `lspci -nnk | grep -i VGA -A2`
- `glxinfo | grep "OpenGL version string`
- `xrandr` - Anzeige aktueller Auflösung und Anschlüsse
#### Netzwerk
- `cat /etc/resolv.conf`
- `lspci --nnk | grep -i net -A2`
- `ifconfig`
#### WLAN
- `iwconfig`
- `iwlist chan`
- `iwlist scan`
#### Datein/Festplatte
- `du -hs` - belegter Speicherplatz
- `df -hT` - freier/belegter Festplattenplatz
- `df -h` - verfügbarer Speicherplatz
- `cat /proc/partitions`
- `sudo blkid -o list` - alle verbundenen Laufwerke anzeigen.

### WLAN (RTL8723be)
- `sudo modinfo rtl8723be` bzw. `sudo modinfo rtl873ae`- anstelle von `rtl8723be` Namen des eigenen WLAN-Moduls eingeben
- `echo "options rlt8723au ant_sel=2" | sudo tee /etc/modprobe.d/rtl8723ae_options.conf` - andere Antenne des WLAN-Moduls aufwählen, danach NW-Service neustarten.
### Sonstiges
> zu Grafik:
> * `xrandr --listproviders`
> * `DRI_PRIME=1 glxinfo | grep "OpenGL renderer`
### Distribustionversion
- `uname -a`
- `cat /proc/version`
- `cat /etc/debian_version`
- `cat /etc/issue`
- `lsb_release -a`
### User und Gruppen
> User Anzeigen:
>* `cat -d: -f1 /etc/passwd`
>* `cat /etc/group`
>* `id -nG` 

>User anlegen
>* `sudo adduser userXXX`

>User in eine Gruppe aufnehmen
* `sudo usermod -aG mysql $USER`
* `sudo adduser userName gruppeName`

### Tar
- `tar -zxf /ordner/wo/datei.tar.gz -C /ordner/wohin/`

### Services starten
* `sudo systemctl start/stop/status xxx.service/xxx`
* `service start/stop/status xxx`

### Deb-Pakete über Terminal installieren
>1. zum Verzeichnis mit datei.deb navigieren
>2. `sudo dpkg -i datei.deb`  
>Bei Fehler:
>    1. `sudo apt -f install`  
>
>Eventuell noch Signaturen isntallieren
>1. `wget --no-check-certification https://...`
>2. `sudo apt-get update`
>3. `sudo apt-get upgrade`

### Datei erstellen
- `(sudo) touch /ordner/datei.end`

### Thunderbird-Profil aus Windows in Linux einbinden
1. in `profile.ini` ändern:
    1. `IsRelative=0` statt `1` - (0 - wird absoluter Pfad verwendet, 1 - relativer)
    2. `Path=Pfad` zum Profil in Windows

### Pakete neukonfigurieren
* `sudo dpkg --configure -a`

### GPU-Monitoring
1. `sudo apt-get install intel-gpu-tools` - Intel-GPU-Monitoring-Tool installieren
2. `sudo intel_gpu_top` - Intel-GPU-Monitoring-Tool aufrufen
3. `sudo intel_gpu_time PID`

### Prüfen, ob Packet schon isntalliert ist
* `apt-cache policy packet_name`
* `whereis packet_name`

### KDE und Gnome:
* `im-config` -> Eingabemöglichkeit auswähen (IBus, Standard usw.)
* `sudo dpkg-reconfigure gdm3/lightdm/smmd` - Display Manager auswählen

### KDE Tipps:
* Verschiedenens
    * `ALT+F2` - Eingabefeld für Befehle(Anleitung in Krunner)
    * KDE Arbeitsfläche - Miniprogramme(Widgests, Gadgest, Plasmoids)
    * `WIN+TAB` bzw. `WIN+Q`
* Datei-Explorer
    * Dolphin (von KDE)
    * Konqueror
    * Gwenview (Bildbetrachter)
* Fenster
    * `ALT` mit Maus Fenster packen und bewegen` - ganzes Fenster als Angriffsfläche verwenden
    * `STRG+ALT+ESC` - aufgehängte Fenster killen

### 8 Fancy Tricks
1. `sudo !! ` - letzten Befehl mit `sudo` davor noch Mal ausführen.
2. 
    1. Editor auswählen:
    * `sudo update-alternatives --config editor` -> Defaulteditor auswählen  
    ODER
    * `export EDITOR=/bin/nano` in `.bashrc` oder `.zshrc` eingeben
    2. `STRG+X+E` - es wird der Default-Terminal-Editor geöffnet, wenn man sich durch `history` navigiert hat und in der Eingabezeile ein Befehl stand, wird Editor mit diesem Text geöffnent. Wenn man jetzt diese Eingabe im Editor bearbeitet, speichert und beendet, dann wird dieses Befehl im Terminal ausgeführt
3. Schnellen RAM anlegen
    * `mkdir -p /mnt/ram`
    * `mount -t tnpfs tmpfs /mnt/ram -o size=8192M`
    * Test:
        * `dd if=/dev/zero of=test.iso bs=1M count=8000`
4. Befehl nicht in `history` schreiben
    * `SPACE` bevor man Befehl eingibt
5. Letztes Befehl (eventuell wenn falsch eingegeben) im Defalt-Editor bearbeiten und noch Mal ausführen (siehe **2.**)
    * `fc` - wird letztes Befehl im Default-Editor geöffnet. Dann bearbeiten und schließen -> wird der bearbeitete Befehl ausgeführt
6. `ssh -L 3337:127.0.0.1:6379 root@test.org -N` - binde lokalen Port zu remoteHost relativ zur Maschine. Zeige meinen lokalen Port 3337 zu test.org zu 127.0.0.1:6379
7. Mehrere Ordner erstellen
    * `mkdir -p ordner/{1..100}{1..1000}` -  100 Ordner mit je 1000 Ordnern darin erstellen
8. `cat test.txt | tee -a log.txt | cat > /dev/null` - zuerst Ausgabe von **test.txt** in **log.txt**, dann nach **/dev/null**. Vorteil: es wird nichts im Terminal ausgegeben, Ausgabe kann man aber im **log.txt** ansehen
9. `diswon && exit` - wenn Terminal noch Aufgabe(en) am laufen hat, wird(werden) diese dem Terminal abgenommen und Terminal geschlossen und beim beenden des Terminals wird die Aufgabe nicht beendet.

### VIM Encryption
1. Verschlüsseln:
    1. `vim -x /pfad/datei.end` - Datei mit Password schützten
    2. Password zwei Mal eingeben
2. Verschlüsselung aufheben:
    1. `vim /pfad/datei.end`
    2. mit Password entschlüsseln
    3. `:X`
    4. leeres Password zwei mit Enter bestätigen
