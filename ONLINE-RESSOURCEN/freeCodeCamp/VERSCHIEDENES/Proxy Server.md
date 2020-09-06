### Intro
* Proxy sendet requests weiter
* macht so also ob die Internet Aktivität von anderem Server kam.
+ wird oft für Sicherheit benutzt
+ kann physisch überall stehen (zu Hause oder in der Cloud)
+ verhält sich wie ein IP-Address Filter
### Wie funktioniert Proxy
* oft wie `Forward Proxy` eingerichtet = Mittelmann bei Requests
* Ablauf:
    * Proxy emfängt Request, wandelt die Ziel IP in die IP zum Dienst um and sendet den Request mit eigener IP => eigene IP wird komplett überdeckt
        + oft wird nur Req-Header verändert
    * Emfängt den Response vom eigentlichen Dienst. Schauen nach, ob es mit diesen Daten etwas machen soll z.B checken, ob Response Viren enthält oder so. und sendet die Antwort zurück an wirklciken Anfrager.
### Gründe um Proxy zu benutzen
* Gründe:
    1. Sicherheit + Verschlüsselung verbessern
    2. Verhindert, dass Häcker Info abfangen
    3. Blockiert bestimmte IP/Domains vom tatsächlichem NW
    4. NW-Traffic verbessern durch Cachen der Seiten
    5. Traffic monitoren
    6. Access-Regeln setzen
* Bsp:
    1. Cookie blockieren
    2. Ads blockieren
    3. Deep Web accessen
    4. Suchen/History löschen
    5. Daten scrapen
### Proxy-Typen (14 Typen):
1. `Transparent proxy` die einfachsten: lassen alles passieren, verändern nur die Sender-IP. Reicht um einfachsten IP-Ban zu realisieren
2. `Anonymous Proxy` - meist benutzter Proxy. Der Server erfährt nie die Client-IP. Diese Request = `Proxy Requests`. Browsing Aktivität verstäkt halten. z.B. so vermeiden, dass relevante Ads auf folge-Seiten angezeigt werden.
3. `High anonymity Proxy` - meist sichertste Proxy. Wandeln die Request-IP zu einer random IP (deswegen auch kein Proxy-Request) => Anonymität. TOR-Browser benutzt diese Art von Proxy. Da IP sich ständig ändert => unmöglich zu tracken.
4. `Distorning Proxy` - gibt extra falsche IP weiter. So vorgeben, dass man am anderem Ort ist.
5. `Residental Proxy` - benutz reelle IP => sieht für den Server so aus, als ob der Request nicht kein Proxy-Request ist. Also IP eines Devices. (sind undetectable)
6. `Data Center Proxy` - Gegenteil von `Residental Proxy`:  Data Centren habe IPs die keinem realem Device zugeordnet sind. Also Proxy für Cloud NW. Vorteil ist ihre Geschwindigkeit.
7. `Public proxy` - meist unsichersten. Man benutz sie weil sie kostenlos sind. Es gibt eine Liste mit *free publix proxies*
8. `Private Proxy` - sind vom Provider des Services definiert. Kann nur von einem Client gleichzeitig benutz werden, oder braucht Authentifikation. Also etwas sicherere `Public Proxies`
9. `Dedicated Proxy` - spezielle Art von `Private Proxy`: nur ein Client gleichzeitig. So kann Proxy Provider kontorllieren, wer darf Access haben, wer nicht
10. `Shared Proxy` -  nicht verstanden -> ????
11. `Rotating Proxy` - jedes Mal, wenn Client sich verbinden wird neue IP für diesen Client erstellt. (so funktioniert TOR) => Anonymität
12. `SSL Proxy` - folgen dem gleichen Protokol wie HTTPS-Requests, d.h SSL wird zwei Mal gemacht Anfrage an Proxy, Proxy macht wieder SSL-Anfrage an tatsächlichen Server
13. `Reverse Proxy` - versteckt die IP des Server im Response. Wenn Server geschützt werden muss. Kann man auch Access monitoren

### Proxy-Services
* Liste mit den publc Proxies
    * https://smartproxy.com/
    * https://www.megaproxy.com/
    * https://whoer.net/webproxy
    * https://www.proxysite.com/
    * https://hide.me/en/proxy
    * https://www.kproxy.com/
    * https://www.vpnbook.com/webproxy

### Proxy serve vs VPN
* VPN sichert ganzen NW-Trafic. Proxy nur Intenet-Traffik -- ???
* mit VPN Trafic auch vom ISP verstecken. ISP kann dann nur sehen, dass man zu VPN verbunden war. 

### Pros und Contras:
* Pros:
    * Secure and private internet browsing
    * Ability to get around geo-location restrictions
    * Better network performance
    * Ability to control what websites clients have access to
    * Many types to choose from to suit specific needs
* Contras:
    * Your requests might return really slow
    * Not all proxies encrypt your requests so your information could still leak out
    * Free or cheap proxies could be set up by hackers or government agencies
    * Proxies can disappear at any time
    * All of your requests and information always go through a third party that could be run by anyone

### Proxy aufsetzen
* man kan auf Linux Squid aufsetzen und Proxy-Config erstellen (https://devopscube.com/setup-and-configure-proxy-server/)
* auf Windows oder Mac kann man Proxy mit Python und Google App Engine erstellen. (https://www.hongkiat.com/blog/proxy-with-google-app-engine/)

### mit Proxy verbidnen
1. in den Browser-Einstellungen
2. in den Device-Setting unter Network-Einstellungen