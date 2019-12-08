### 1 Firewalls and Ports
#### 1 - Understanding ports
* Port - logischer Space für bestimmte Communication
* Ports sind in Config-Datei spezifiezeit und können dort geändert werden
#### 2 - Exploring open ports
* `ss` - zeigt offene Ports (erstetz `netstat`)
* `ss -t` - aktive TCP-Sockets
* `ss -u` - aktive UDP-Sockets
* `ss -at` 
    * Recv-Q und Send-Q - Packete die bearbeitet werden sollen, oder auf ACK warten
    * Peer Address:Port - der Client
* `ns -l 1124 &` - etwas am Port 1124 listen
    * auf den nicht well-known-Ports laufende Services werden als File-Sharing interpretiert
    * `ss -atn` - `-n` - mit dem Raten von *ss* aufhören, stattdessen Ports anzeigen
* `ns localhost 1124` - etwas aufm Port 1124 starten
* `ss -atnp` - Zeigt Programme/Services die auf dem Port laufen
    * `fd` - File-Deskripro
        * `ls -lh /proc/PID/fd`
* offene Ports am Remote-Maschinen shauen mit nmap:
    * `sudo apt-get install nmap`
    * `nmap -sT -sU localhost` - welche UDP und TCP -Ports sind offen + nmap rät den laufenden Service
* `telnet localhost 22` - mit telnet auf SSH verbinden -> Aber keine Communication möglich, da Telnet nicht ssh kann.
#### 3 - Understanding firewalls
* Kontrolliert inbound and outbound traffic
#### 4 - Managing ufw
* `ufw status`
* `ufw enable`
* `ufw status` 
* `ufw allow 22/tcp` - TCP am Port 22 für SSH erlauben
    * `ufw allow 22` - TCP und UDP am Port 22 erlauben
* `ufw delete 2` - Regel löschen
* `ufw deny 22/tcp` - verbieten
* `ufw delete deny 22/tcp`
* `ufw app list` - Anzeigen welche Apps/programme ufw kennt
* `ufw app info Apache Full` - zeigt, welche Ports die App nutzt, bzw. welche Ports ufw verbieten/erlauben wird
    * `ufw allow from 10.0.2.0/20 to 10.0.2.10 app OpenSSH` - SSH für NW nach 10.0.2.10 erlauben
* Externe DNS blocken:
    * `ufw allow from 10.0.2.0/24 to 10.0.2.10 port 53 proto tcp`
    `ufw allow from 10.0.2.0/24 to 10.0.2.10 port 53 proto udp`
* ufw sitzt auf iptables, die ufw-Befehle werden in iptales übesetzt.
* Manche Sachen kann ufw nicht über Terminal machen (z.B Forwarding oder Chains setzen)-> muss man ufw-Datei bearbeiten 
    * `ls -l /etc/ufw`
    * Regeln mit ufw werden in *user.rules* eingetragen
#### 5 - Managing iptables
* SW, das wie Firewall funktioniert. Complexe Regeln - Chains. Packete werden gegen Regeln vergliechen. Wenn keine Regeln erfüllt, wird default-Aktion ausgeführt
* Chains:
    * INPUT - Packete, die reinkommen
    * FORWARD - Packete die durch das System gehen
    * OUTPUT
* AKTIONS:
    * ALLOW
    * DROP
    * REJECT
* `iptables -L -n`
    * ganz oben die Standard-CHAINS und die deault-Policies dafür
* Um neue Regeln hinzufügen benutzt man `-A INPUT` - Append to Chain INPUT
    * `-A INPUT -i enp0s3 -p tcp --dport 80 -j ACCEPT` - `-i  lala ` - für Pakete am Interface lala, `-p tcp` - Protokoll TCP, `--dport 80` - welcher Port dafür benutzt wird, `-j ACCEPT` - jump to ACCEPT
* `iptabels -A INPUT -i enp0s3 -p tcp --dport 80 -j ACCEPT` - ist aber bis zum Neustart gültig
* Um Regel permanent gelten zu lassen, muss man iptables-Datei exportieren verändern und zurück importieren:
    * `iptables-save > myrules`
    * `nano myrules`
    * vor `#COMMIT` einfügen `-A INPUT -i enp0s3 -p tcp --dport 80 -j ACCEPT`
    * `iptables-restore -myrules`
* `iptables -F` - komplett zurücksetzen
* Optionen:
    * `-s 10.0.2.2/24` - Source 
    * `-m state -state NEW/ESTABLISHED/RELATED` - match a State NEW/ESTABLISHED/RELATED
        * NEW - neue Verbinudng
        * ESTABLISHED/RELATED - z.B bei TCP z.B FTP
* man sollte die Regeln erst über Terminal testen
* Falls nicht funktioniert Regel deleten:
    * `iptables -D [Chain] [number]`
* `iptables -L --line-numbers`
* Reihenfolge ist wichtig, da erster Match ausgeführt wird. Restrictivere Regeln zuerst
### 2 - Security for Common Services
#### 1 - Securing an Apache site with SSL
* TLS (Transport Layer Security) oder SSL -> HTTPS
* zwei Arten:
    * CA-signed
    * self-signed
        * `openssl req -x509` - self-signed vs. CSR 
            * -newkey rsa:2048 - Algorithm + Bits 
            * -keyout key.key - Private Key path
            * -out cert.pem  - Certifikate Path
            * -days 365 
            * -nodes` - NO DES - no password
        * `openssl req  -x509 -newkey rsa:2048 -keyout key.key -out cert.pem -days 365 -node`
            * Country Name, State, Locality Name, Org Name und Orga Unit ausfüllen. 
        * an richtige Orten Kopiren:
        * .key nach `/etc/ssl/private`
        * .pem nach `/etc/ssl/certs`
        * die Orte in Apache eintragen:
        * `nano /etc/apache2/sites-available/default-ssl.conf`
        * `SSLEngine on`
        * `SSLCertificateFile /etc/ssl/certs`
        * `SSLCertificateKeyFile /etc/ssl/certs`
        * `a2ensite default-ssl.conf` - Seite aktivieren
        * `a2enmod ssl` - SSL aktivieren
        * Apache Restarten
#### 2 - Exploring Apache log files
* zwei Logs
    * Access Log (/etc/log/apache2/access.log) - Client Requests
    * Error Log (/etc/log/apache2/error.log) - Service-Related Errors
* die Einstellungen für diese Logs sind in `/etc/apache2/apache2.conf`
    * `LogLevel warn` 
    * `LogFormat ...`
* ebenfalls in `/etc/apache2/sites-available/000-default.conf`
    * hier kann man auch andere Pfade für Logs einstellen
#### 3 - Securing SSH with keys
* Vorgehensweise:
    * Key Pair generieren
    * Public Key zum Server senden
* auf dem Client:
    * `ssh-keygen` - für Art der Verschlüssulung Optionen benutzen
    * `cat ~/.ssh/id_rsa.pub`
    * Ausgabe kopieren
    * per ssh mit dem Server verbinden
    * `mkdir .ssh`
    * `nano .ssh/authorized_keys`
    * Einfügen
    * `nano /etc/ssh/sshd_config`
    * `PubkeyAuthentication yes`
    * `AuthorizedKeysFile ...`
    * `Passsword Authentication no`
    * sshd restarten