### 0 - Introduction
### 1 - Trust and browsing securely
* drei Security Areas:
    1. persönliche Info - Passwörter, Phishing Versuche, Malware, Cookies
    2. sichere Verbindung - SSL (HTTPS) 
    3. vertrauenswürdiges NW -
* öffentliche DNS:
    1. google: 8.8.8.8, 8.8.4.4
    2. openDNS: 208.67.222.222, 208.67.220.220
* DNS-Abfrage ist nicht SSL-Verschlüsselt
* Cookies können Info über den Benutzer sammeln
    * Inkognito Mode - verhindert, dass Seiten Cookies von anderen Seiten lesen
    * uBlock Origin, Privacy Badger - tracking verhindern

### 1 - VPN Providers
#### 1 - What's a VPN
* VPN - Virtual Private Network
* setzt NW-Tunnel (Tunnel - wird verschlüsselt) zwischen eigenem PC und Remote Server
    + partial tunnel - nur bestimmte Anfragen laufen durch VPN
    + full tunnel 
+ VPN - Vertrauen wird eigentlich verschoben, von ISP zu VPN-Anbieter
#### 2 - Using a VPN providers app
* VPN-App macht die ganzen technischen Detail bei der Verbindung
* Bsp:
    * Private Internet Access:
        * sich registrieren
        * sich in der PIA-App anmelden -> VPN auswählen
        * www.whatsmyip.com
    * VPN kann einige Seiten verwirren, da IP aus anderem Land aber Daten aus dem anderen Land
    * meisten Apps und Geräte werden die wirkliche Location benutzen
#### 3 - Using an OpenVPN provider
* einige VPN Provider haben keine App, stellen aber config-Datei. Dann muss man Dritte Sortware wie Tunnelblick (MAC), OpenVPN

### 2 - Set Up Your Own VPN Server
#### 1 - VPN Servers
* Self-hosted VPN (z.B Algo)
* man kann ihn zuhause oder im Datazentrum laufen lassen
* Überlegunen: 
    * Traffik geht zuerst nach Hause, also was eigentlich Download ist, wird zum Upload
#### 2 - Installing and using Algo
* Algo sind Scripts, die System zu VPN konfigurieren

### 3 - Tor
#### 1 - What is Tor?
* Tor senden Info durch Serie von Nodes. Pfad ist random. Nodes wissen nicht, welchen Pfad die Daten nehmen
* Tornetwork besteht aus Netzwerk von Rechnern, die Tor installiert haben
* https://www.eff.org/pages/tor-and-https - erklärt wie Tor funktioniert
#### 2 - Browsing with Tor
* ist modifizierter Firefox
* https://fast.com - Geschwindigkeit checken (mit Tor deutlich langsamer)