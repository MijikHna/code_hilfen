### Introduction
+ LAB: zwei Ubuntu VMS: Server und client
#### Firewall rules with UFW and iptables
+ Remote access erlauben -> Firewall configurieren: ufw und iptables (ufw managed im Hintergrund iptables)
* `sudo ufw allow 22/tcp`
* `sudo ufw enable` - Default behaivour von ufw ist was nicht spezifiziert wurde ablehnen.
* `sudo ufw allow form 10.0.2.0/24 to any port 22` - aus lokalem NW jedem Rechner Zugriff auf Port 22 erlauben, ohne `any` würde allen Maschinen zugriff vom Port 22 erlauben
* `sudo ufw status` - Firewall-rules anschauen.
* `sudo ufw delete 1` - erste Regel löschen oder `sudo ufw delete 22/tcp` - Bestimmte Regel löschen oder `sudo ufw delete allow 22/tcp`
* Komplexe Rules - Iptables
    * Regeln organisiert in Ketten
    + Wenn Regel zutreffend ist, wird die Aktion ausgeführt, sonst wird Standardaktion ausgeführt
    * `sudo iptables -L | more` - Chains/Regels anzeigen; unten sind Regeln, die mit ufw erstellt werden.
    * Regel ändern -> zuerst existierende Regeln abspeichern, verändern und reimportiren
    * `sudo iptables-save > myrules` - Regeln exportieren
    * `nano myrules`
    * `-A` - Regel adden, `-j` - Jump to Chain/Aktion `-p` - Protocol `--dport` - Port
    * `sudo iptables-restore myrules`
### 1 - Remote Console Access
#### 1 - Connecting with telnet
* `nc -l 4000` - netcat im Listening-Mode starten -> printet alles was über Port 4000 kommt
* `telnet 10.0.0.8 4000` -> beenden *SHIFT/^+]*
    * in Telnet-session:
        * `?` - Hilfe
* mit Telnet kann man sich auch den Inhalt der Websites anzeigen
* `telnet serverxyz.com 80`
    * `GET / HTTP1.1` - Get Root Protocol
    * `host serverxyz.com 80`
#### 2 - Configuring SSH Server
* `apt install openssh-server` - SSH-Server installieren - Remote-Connection vom Client erlauben
* in `etc/ssh/sshd_config` - SSH-Server konfigurieren
    * Port setzen, default ist 22 <- Zeile unkommentieren
    * *HostKey* - wo die Keys liegen
    * Logging - wie Login funktioniert
    * Authentication
    * `PermitRootLogin no` setzen ist good Practice
    * `PubkeyAuthentication yes` 
    * `PasswordAuthentication no`
    * `UsePAM yes`
    * `X11Forwarding yes` - damit man per ssh auf GUI benutzen kann
    * Weitere nützliche Zeilen:
        * *AllowUsers, AllowGroups*
        * *DenyUsers, DenyGroups*
* `sudo systemctl restart sshd` - nach Änderung der Config-Datei
* in `etc/ssh/ssh_conig` - SSH-Client konfigurieren
#### 3 - Connecting with SSH
* `apt install openssh-client`
* in `etc/ssh/ssh_conig` - SSH-Client konfigurieren
* `ssh user1@10.0.2.8 -oPort=2222` oder bei default Port 22 `ssh user1@10.0.2.8`
    * zuerst wird man gefragt, ob man Serverskey akzeptieren möchte
* Key Pair:
    + `ssh-keygen`
    * Public Key hat .pub am Ende, Private Key hat keien Extenstion
    * `cat id_rsa.puby`
    * Ausgabe kopieren
    * mit ssh sich auf dem Server anmelden
    * `sudo nano .ssh/authorized_keys`
    * Einfügen
    * exit
    * `ssh user1@10.0.2.8 -i .ssh/id_rsa`
* man kann Configdateien erstellen um sich einfache mit dem Server zu verbinden:
* `nano .ssh/config`
```
Host myserverxyz
Hostname 10.0.2.8
User user1
IdentifyFile ~/.ssh/id_rsa
```
* ssh myserverxyz

### 2 - Remote GUI Access
#### 1 - Desktops
* Desktops laufen auf Windowing software
* in Linux zwei graphische Server: Xorg und Wayland (neuer)
* aus dem Server:
    * `sudo apt install xfce4`
* Zwei möglichkeiten:
    1. X11 forwarding - Applications Windows zu Client schieben
    2. Desktop per Remtoe sharen - VNC (Virtual Network Computing)
#### 2 - Connection with X11
* SSH mit X forwarding benutzen
    * `ssh -Y user@hostname` - alt, nicht sicher
    * Cleint braucht X11 software: Linux - Xorg, Mac - XQuartz, Windows (Xming)
    * Bsp: 
    * `ssh -Y user1@10.0.2.8 -i .ssh/id_rsa`
    * `thunar` - Thunar wird auf dem Client geöffnet
    * `startxfce4` - XFCE auf dem Client starten
#### 3 - Configuring VNS Server
* auf dem Server:
    * `sudo apt isntall tightvncserver`
    * `vncserver`
    * Password max. 8 Zeichen
    * evnetuell only-view-Password setzen
    * Virtualle Dislays laufen auf den Ports: 5901 - 1; 5902 - 2; 5903 - 3
    * Firewall für diese öffnen `sudo ufw allow from 10.0.2.0/24 to any port 5901`
    * nano /home/user1/.vnc/xstartup
    * *export XKL_XMODMAP_DISABLE=1* auskommentieren, da VNC es für GNOME-Kompatibilität eingefügt hat
    * */etc/X11/Xsession* - xfce4 starten
    * `vncserver -kill :1`
    * `vncserver`
#### 4 - Connecting with VNC
* `sudo apt install vinagre`
* es gibt auch Chrome erweitung für VNC
* vinagre starten und eingeben: *10.0.2.8:5901*
    * Screensaver ausmachen + Power-Einstellungen ändern
#### 5 - Oher remote desktop options
* auf Client und Server SW installieren, Account erstellen. Server und Client werden dann über diesen Account kommunizieren.
    * Bomgar, Teamviewer