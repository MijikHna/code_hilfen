VB hat VBox DHCP und Virtual Router (eventeull VBox DHCP ausmachen)
### 1 - Network Services
#### 1 - Configure a DHCP server
* isc-dhcp-server installieren
* */etc/default/isc-dhcp-server* - Interface  und */etc/dhcp/dhcpd.cond* - Netze usw. modifizieren 
* `sudo apt-install isc-dhcp-server`
* */etc/default/isc-dhcp-server* öffnen
    * `INTERFACE="enp0s3"` - Interface für DHCP setzen
* */etc/dhcp/dhcpd.conf* öffnen (eventuell Datei zuerst backaupen)
    + `authoritative;` - als DHCP Main-Server markieren 
    * `default-lease-time 600` - Wert kleiner, wenn z.B Kafe, da Geräte ständing wechseln, sonst länger, wenn Geräte jedes Mal die gleiche IP bekommen sollen
    * ```
    subnet 10.0.2.0 netmask 255.255.255.0 {
        range 10.0.2.20 10.0.2.220;
        option routers 10.0.2.1; # Router (Gateway)
        option domain-name-servers 10.0.2.1; # DNS-server
        # man kann hier auch noch NTP-Server usw. setzen
    }
    * DHCP resarten `sudo systemctl restart isc-dhcp-server`
    * `sudo dhclient -r` - Lease löschen
    * `sudo dhclient -v` - nach neuer Adresse nachfragen 
* Troubleshouting:
    + `sudo dhclient -v`
    * Logs von *isc-dhcp-server* anschauen
    * Firewall-Problem: DHCP-Server benutzt Port 67(UDP) und Client Port 68(UDP)
#### 2 - Configure a DHCP client
* */etc/network/interfaces* öffnen
* `iface enp0s3 inet dhcp` und weitere auskommentieren
* NW restarten
#### 3 - Configure a PXE boot server
* PXE - Preboot eXecution Environment - Boot over NW - für Installationen, Deployment usw.
* braucht DHCP und TFTP - Travile File Transfer Protocol - Basic File Sharing und Hosting
* Server als PXE einrichten
    1. DHCP-Server aufsetzen
    2. TFTP installieren + Bootble Files kopieren
    3. Configure DHCP Server für NW-Booting einrichten + Cliets zum TFTP-Server weiterleiten
* `sudo apt install tftpd-hpa`
* */etc/default/tftpd-hpa* öffnen
* benutze UDP
* z.B Ubuntu-ISO herunterladen
* `sudo mkdir /mnt/iso`
* `sudo mount ~/Downloads/ubuntu...iso /mnt/iso`
* `sudo cp -R /mnt/iso/install/netboot/* /var/lib/tftpboot/` 
* */etc/dhcp/dhcpd.conf* öffnen
* im passenden subnet-Teil hinzufügen:
    * `allow booting;`
    * `allow bootp;`
    * `next-server 10.0.2.10;` # Adresse des TFTP-Servers
    * `filename "pxelinux.0";` # Datei aus dem Installierer
    * TFTP und DHCP neustarten
    * Client neustarten + F12 
* Weiter Optionen für PXE-Server
    * Host installatin images on NFS/HTTP
    * Host live boot environment
    * Different images for differnt subnets or clients
### 2 - Proxies
### 1 - Configure an HTTP proxy server
* Web Browsing Aktivitäten durch bestimmten Host leiten (Proxy)
    * um Traffic zu kontrollieren, und Files Cachen
    * um Traffic Beschränkungen zu umgehen 
* mit Apache Proxy zu machen => Programm *squid*
    * nimmt Anfragen an und leitet sie weiter und emfängt die angeforderten Sachen vom Remote-Server
* mit Proxies kann man Web Aktivitäten logen und eventuell Zugang blocken
* squid kann Responses für http, https,dns und ftp cachen
* Schritte:
    + `apt isntall squid`
    + `systemctl status squid`
    + läuft per default auf Port 3128 (eventuell Firewall einstellen)
    * Config in */etc/squid//squid.conf*
    * Logs: in */var/log/squid/*
    * In browser: Einstellungen -> Proxy -> HTTP Proxy eingeben (z.B *localhost* + Port: *3128*) -> Häckschen bei für alle Protokolle benutzen
    * in access.log kann man dann die Anfragen/Responses
    * nano /etc/squid/squid.conf
        * `http_access deny !Safe_ports` - HTTP-Zugang für Port nicht in der safe_ports Liste verweigern
        * Nach `cache_dir` suchen
        * `cache_dir ufs /var/spool/squid 100 16 256` - *ufs*-Storage-Format, */var/...* - Speicherort, Größe, wie viele Ornder im ersten Level, wie viele Ordner im zweiten Level
        * squid restarten

### 2 - Control access to an HTTP proxy server
* einstellen, das Proxy nur von bekannten NW und Users benutzt wird
* Squid akzeptiert Traffic nur von sich selber. => einstellen, das andere Systeme ihn benutzen können d.h Client.
* Bsp: Browser:
    * wenn man im Browser einstellen, den Proxy zu benutzen, wrid *Access Denied* kommen
    * */etc/squid/squid.conf* öffnen
    * *acl localnet* finden
    * `acl localnet src 10.0.2.0/24` - *src* - Quelle
    * man kann noch Time Ranges, AS Nummern, Protocole festlegen
    * *http_access* finden
    * `http_access allow localnet` - erlaubt den Clients aus lokalem NW Zugang zu http/https über Proxy
    * squid neustarten
* am dem Procy mit Username und Password anmelden
    * man dann dafür Apache benutzen
    * `sudo htpasswd -c /etc/squid/passwd scott`
    * `sudo htpasswd /etc/squid/passwd john` - weiteren User hinzufügen
    * */etc/squid/squid.conf* öffnen
    * *safe_port* suchen
    * `auth_param basic program /usr/lib/squid/basic_nsca_auth /etc/squid/passwd` - Basic-Auth-Parameter, Programm, das benutzt wird als Parameter für das Programm ist Passwd-Liste
    * `acl auth_users proxy auth REQUIRED` - ACL mit Namen auth_users erstellen
    * `http_access allow auth_users` - Access zu dieser ACL erlauben
    * Squid restarten
    * man kann Access für bestimmte Zeiten oder bestimmte Browser setzen
#### 3 - Configure an HTTP client to automaticaly use a proxy server
* wenn man möchte, dass Clients automatisch Proxy benutzen, dann PAC-File konfigureiren (Proxy-auto-config). ist JS, das auf dem Server gehostet wird. Clients holen die Datei ab und der Proxy wird eingerichtet.
* Skript erstellen:
* */var/www/html/proxy.pac* erstellen
* 
```javascript
function FindProxyForURL(url, host){
    return "PROXY 10.0.2.10:3128";
}
```
* im Browser bei Proxy -> Automatic proxy config URL *http://10.0.2.10/proxy.pac* eintragen
### 3 - Domian Name System
#### 1 - Configure an authoritative name server
* Linux benutzt Tool DNS mask um wie lokaler DNS-Server zu wirken. braucht *hosts files* und *dnsmasq*
* Linux DNS-Server = Bind (Berkeley Internet Name Domain). 
* DNS:
    * Root-Server haben Info über *de,net,com, usw*
    * Jede Seite hat DNS-Server, dass für sie einen Zone File bereitstellt
    * Zone repräsentiert meistens eine Domain
    * benutzt Port 53
    * Wenn DNS-Server liefert die Adresse 127.0.53.53, d.h man benutzt DomainNamen, der im Internet schon reserviert ist. Bzw. die reale Domain wird dann unerreichbar.
    * man solle Domains ab besten so nennen, mydomain.istreal, mydoamin.local usw. da jezt auch .dev,.home usw. im Internet verwednet werden. 
* Vorgehen:
    * `apt install bind9`
    * */etc/bind/* 
    * */etc/bind/named.conf* - Main Config, meistens include weitere Dateien
    * */etc/bind/named.conf.options* - Optionen für DNS-Server setzen
    * */etc/bind/named.conf.local* - Änderungen der Zone
    * */etc/bind/named.conf.default-zone* - Info über Default-Zones
        * */etc/bind/db.root* - Info über Dot-Zone = Top-Level in DNS-Hiearchy, hat Info über Root-Servers + Info über forward und reverse Zones
    * in *den db.xxx* - Files werden Zonen definiert
    * *db.empty* - File als Vorlage
    * Forward = nimmt z.B *example.de* und liefert dazu IP
    * Reverse = nimmt IP und gibt Domain zurück
* Bsp:
    * */etc/bind/named.conf.local* öffnen:
        * 
        ```
        zone "example.com" {# neue Zone einfügen
            type master;
            file "/etc/bind/db.example.db"; # Datei, wo Zone steht
        }
        zone "2.0.10.in-addr.arpa" { # Reverse Zone einfügen
            type master;
            file "/etc/bind/db.2.0.10";
        }
        ```
        * Zone Datein erstellen:
            * `cp /etc/bind/db.empty /etc/bind/db.example`
            * *db.example* anpassen
            * 
            ```
            $TTL 86400 # Time To Live, wie lange Eintrag valid ist, bevor der Server ihn nochmal nachfragt
            example.com. IN SOA  myserver.example.com. dnsadmin.example.com ( # . am Ende = Highest Level Domain, IN = Internet, SOA = Start of Authority, myserver... = Primary Name Server for this domain, dnsadmin - mail des Admin (. = @) 
                            1   ; Serial # Seriannummer, dass aktualiesert wird, wenn Eintrag sich verändert hat
                            604800  ;Refresh # Refresch in Sek.
                            86400   ;Retry #
                            24199200    ;Expire # wie lange dieser Eintrag valid ist
                            86400)   ;Negative Cache TTL
            
            ; - ; ist Kommentar
            @   IN  NS  myserver.example.com. #  wo die Name Server für diese Domain angegeben werden; @=Origin, in diesem Fall als example.com; NS=Name server. Hier werden eventuell Slave-Server hinzugefügt

            # jezt kommen die A-Einträge:
            @   IN  A   10.0.2.10 # wenn es nach example.com gefragt wird, wird es mit dieser IP geantwortet (normalerweise sollte man hier IP des WebServer eintragen)
            myserver    IN  A 10.0.2.10 # normaler eintrag
            www IN CNAME    myserver # CNAME-Eintrag ~ alias. 
            ```
            * man kann anstelle von A noch: Text Records, MX, Service Records und CName-Records machen. 
        * Reverse Zone:
            * `cp /etc/bind/db.empty /etc/bind/db.2.0.10`
            * *db.example* anpassen
            * 
            ```
            $TTL 86400 # Time To Live, wie lange Eintrag valid ist, bevor der Server ihn nochmal nachfragt
            2.0.10.in-addr.arpa IN SOA  myserver.example.com. dnsadmin.example.com ( # . am Ende = Highest Level Domain, IN = Internet, SOA = Start of Authority, myserver.exmample.com= Primary Name Server for this domain, dnsadmin - mail des Admin (. = @); 2.0.10 = ersten 3 Oktaven der IP rückwärts- hier kann man aber b
                            1   ; Serial # Seriannummer, dass aktualiesert wird, wenn Eintrag sich verändert hat
                            604800  ;Refresh # Refresch in Sek.
                            86400   ;Retry #
                            24199200    ;Expire # wie lange dieser Eintrag valid ist
                            86400)   ;Negative Cache TTL
            
            ; - ; ist Kommentar
            @   IN  NS  myserver.example.com. #  wo die Name Server für diese Domain angegeben werden; @=Origin, in diesem Fall als example.com; NS=Name server. Hier werden eventuell Slave-Server hinzugefügt

            10  IN  PTR myserver.example.com  # 10 - letzte Oktäte der IP, PTR-Pointer Record - IP zu Host
            ```
            * bind restarten `systemctl restart bind9`
* www.example.com - *com ist Root, dann example, dann www. www ist most specific - bestimmter PC
* 10.0.2.10 - 10.0.2 - ist Root, .10 ist most specific - bestimmter PC
* mit Dig testen: `dig @10.0.2.10 myserver.example.com`; `dig @10.0.2.10 example.com`
* eventuell in DHCP eintrag für DNS-Server machen:
    * /etc/dhcp/dhcpd.conf* öffnen
    * passendes *subnet* finden
    * `option domain-name-servers 10.0.2.10`
    * dhcp restarten
    * networking auf Client restarten
#### 2 - Configure caching an forwarding name servers
* Drei DNS-Typ-Server:
    1. Authoritative - antwortet auf Anfragen zu der eigenen domain
    2. Caching - hat info über andre Seiten, cached queries, performance recursion = leitet anfragen zu anderen DNS-Servers
    3. Forwarding - hat info über andre Seiten, cached queries,
* Bsp:
    * */etc/bind/named.conf.options* öffnen
    * bei `options{` 
        * `recursion yes`
        * `allow-query{allowed;}`
    * über `options{}`
        * `acl allowed {10.0.2.0/24; localhost; localnets;};` # welche Clients, den Server benutzen können
    * bind9 restarten
    * wenn man nur an bestimmte DNS-Server anfragen weiterleiten möchte, dann `forwarders{}`die Servers eintraen
    ```
    forwarders {
        8.8.8.8;
        8.8.4.4;
    };
### 4 - Mail Services 
#### 1 - Configure an SMTP server
* Mail:
    1. MTA - mail transport agent
    2. MDA - mail delivery agent
    3. MX Record - mail exchanger 
* Tools:
    1. MTA - Postfix `apt install postfix`
        * */etc/postfix/main.cf* öffnen
        * `myhostname = myserver.example.com`
        * `home_mailbox = Mail/` - Mails werden in /home/username/Mail/ abgelegt
        * Testen `apt installe mutt` - Mail Client installieren
            * `mkdir -p Mail/{cur,new,tmp}` - Order für Mails erstellen
            * `mutt -F Mail/` - Mail senden
                * *m* klicken
                * *y* abschicken
            * Aliases setzen z.B
                * */etc/aliases* öffnen
                * `admin: user1`
                * speichern
                * `newaliases`
    2. MDA - Dovecot ` `
* MX-Record in DNS:
    * */etc/bind/db.example.com*
    * `@ IN MX 10 myserver` einfügen: MX =MailExchange 10 = Priorität (lower = mehr Preosiert)
    * bind restarten

#### 2 - Configure an IMAP server
* - MDA - Devcot `apt install dovecot-common dovecot-imapd`
* nach */etc/dovecot/conf.d* navigieren
    * *10-mail.conf* öffnen
    * `mail_location = maildir:~/Mail`
    * *10-ssl.conf* öffen
    * *ssl_cert* korriegieren
    * *ssl_key* ändern
    * `ssl = required`
* Thunderbird installieren
    * lokale Mal hinzufügen
    * eventuell SSL-Exception akzeptieren

### Additional
#### 1 - Auditing network services
* `ss -aptu` - zeigt an, welche Prozesse welche Ports benutzen
* `ss -aptun` - zeig an, welche Prozesse, welche Ports bentutzen + ss rät keine Anwendung, falls nicht kennt
* `sudo ufw status` 
* `sudo ufw enable`
* `nmap -sU -sT 10.0.2.10` - scannen, welche Ports auf System offen sind. -sU = UDP, -sU = TCP