### 1 - Serve Web Content with Apache
#### 1 - How a web server works
* static vs. dynamic
* WebServer SW: Apache, nginx, Microsoft IIS, (Tomcat,,Node,js, Sinata)
* Ports: (80/TCP, 443/TCP)
#### 2 - Ensure network connectivity
* Server sollte statische IP bzw. immer DNS ändern bzw. dynDNS verwenden
* Port 80 + 443 öffnen
* oft werden Server in den Zone DMZ aufgesetzt und Access nur über Port 80/443 erlaubt. Verwaltung über SSH kann nur aus internem NW gemacht werden  
#### 3 - Install Apache
* Appache ist open source
* Appache - Software foundation um Open Source SW zu machen
    * Web SW ist dann https (Hypertext Transfer Protocol daemon)
* Appache kann erst nur HTML-Sertien servieren, damit er auch php usw. kann, muss man zusätzliche Module installieren
* Installation:
    * `sudo yum install httpd` bzw. `sudo apt install appache2`
    * `sudo systemctl status httpd` bwz. `sudo systemctl status appache2` bzw. `service appache2 status`
#### 4 - Explore the configuration file
* Haupt-config-Datei ist `/etc/httpd/conf/httpd.conf` bzw. `/etc/appache2/conf/appache2.conf` und noch ein paar Dateien (in Debian ist es aufgeteilt)
* ServerRoot - wo die Server-config-s liegen
* Listen - IP und Port setzen z.B wenn Server hat mehrere IPs. Wenn IP nicht gesetz ist => wird auf allen möglichen IPs gehört
* Dynamic Shared Objects (DSO) Support - zusätzliche Module über Shared Objects z.B Support für php
* User und Group - User und Gruppe unter denen Server läuft
* Main Server config - 
* ServerAdmin - Adresse des Admins
* Servername - Domainname
* `<..>...</...>` - Definition-Block - z.B `<Directory /> ... </Directory>` - Parameter für Direktory /
 setzen
   * `AllowOverride none` - diese Regel kann nicht von nichts aus `/` überschrieben werden.
   * `Require all denied` - lehnt Access für alle, die versuchen diesen Ordner zu lesen
   * `Require all granted` - erlauben dem Server den Inhalt aus diesem Ordner anzuzeigen
*`Document Root` - sagt, wo die HTMLs liegen sollten
* Directory Index - sagt, was angezeit werden soll, wenn keine bestimmte Datei requested wurde d.h wenn z.B nicht www.google.de/index.html sondern www.google.de aufgerufen wird
* `<IfModule dir_module>DirectoryIndex index.html</IfModule>` - Modul dir_module muss vorhanden sein, sonst ist dieser Code nicht gültig
*`<Files ".ht*">` - Rechte für bestimmte Datein
* `ErrorLog "logs/error_log"` - wohin Errors geschrieben werden
* `LogLevel warn` - Errorlevel
* `<IfModule alias_module>` - Aliase für Dateien setzen 
* `<IfModule mime_module>` - Welche Typen akzeptiert/erkannt und wie sie interpretiert werden
* ...
* `IncludeOptional conf.d/*.conf` - lädt alle conf-Dateien in conf.d-Ordner
* Debian httpd.conf:
    * /etc/appache2/conf-available
    * /etc/appache2/conf-enabled - Symlinks config
    * /etc/appache2/
#### 5 - Start up and shut down the web
* `systemstcl status firewalld`
* `sudo firewall-cmd --zone=public --add-service=http --permanent`
* `sudo firewall-cmd --reload` 
* `sudo systemctl enable httpd` - wenn enable => Dienst startet beim Boot
#### 6 - Deploy a site
* 3 Schritte:
    1. dem Server einen Namen geben
    2. Dateien kopieren
    3. Seite prüfen
* Vorgehensweise: 
    1. Domain registrieren
    2. DNS A eintragen (domain <-> IP)
    3. CNAME-Record (www -> domain)
    4. internal DNS-Eintrag
    5. Hostnamen setzen `hostnamectl set-hostname example.com`
    6. Domain zu Hosts eingragen: in /etc/hosts -> `12.343.234.52 example.com`
    7. in httpd.conf `ServerName example.com:80`
#### 7 - Configure logging:
* sehen, wei Leute Info erreichen + welche Errors
* Appache hat zwei Logs:
    1. Access Log - zeigt Instanzen, wo User den Web Server erreichen (html, css - Datei usw.) */var/log/httpd/access_log*
    2. Error Log - */var/log/httpd/error_log* - Falsche Configs und andere Probleme
    * beide in /etc/httpd/logs - `sudo ls -lh /etc/httpd/logs` - oft SymLink zu */var/log/httpd
* eventuell kann man Scripts schreiben, um bestimmte Errors und Adressen zu chekcen
* es gibt auch Monitoring SW z.B *Splunk*
#### 8 - Add modules to extend Apache
* um z.B PHP enableln - Module in Apache hinzufügen, sind Trunks of Code oder Bibs
* einige Module, auf die Appache sich bezieht, sind in SW kompiliert. `httpd -l` - kompilierte Module anschauen.
* dynamische Module anschauen `httpd -M`. Oben sind statische Module, unten sind dann shared Module
* in *httpd.conf* gibt es Teil, der Module aus *conf.modules.d* lädt. Wenn man PHP-Modul insalliert, es wird conf-Datei darein nehmen und noch einen conf-Datei in *conf.d* um PHP-Handler für PHP-Dateien einzurichten + PHP-Binary wird installiert.
    * `sudo yum install php` - PHP-Binary installieren. 
    * `ls -l /etc/httpd/conf.modules.d` - checken die PHP-Config Dateien
    * `cat /etc/httpd/conf.modules.d/10-php.conf - Hier ist dan der Call für PHP.so oder shared Object Modul
    * in */etc/httpd/conf.d* liegt der Handler 
    * */etc/httpd/conf.d/php.conf* - added Support für PHP Dateitypen und deault Index (wenn man PHP-App mit index.php erstellt, braucht man nicht diesen Dateinamn nicht zu URL hinzufügen (root-File))
    * `sudo systemctl restart httpd` - Apache neustarten
#### 9 - Use virtual hosts to serve many sites
* man kann Subdomains erstellen für die Maindomain erstellen z.B *api.example.com* aus */var/www/api und *docs.example.com* aus */var/www/docs* oder können komplett getrennte Domains sein. Oder man kann Server so einstellen, dass er Daten von verschriedenen Ordnern serviert, abhängig von Port des Requests. <- Dafür Virtual Hosts benutzen
* Virtual Host - Entry in der Config, dass dem Server sagt, wenn Reqeust bestimmten Muster, dann soll er Inhalt von bestimmter Location servieren
    * per Default wird alles aus */var/www/html* über den Port 80 serviert.
    * z.B Subdomain members.example.com erstellen für innternen Zugriff -> Schritte:
        1. DNS-Entry für die Subdomain. 
        2. Dateien in den Ordner für Virtual Host reinstellen.
            * `cd /var/www`
            * `sudo cp -Rv ~/members members` - Ordner mit Dateien nach /var/www/members kopieren
        3. Server Conf, um Virtual Host zu nutzen, einstellen.
            * `cd /etc/httpd/conf.d`
            * ` ls -lh`
            * `sudo touch members-site.conf`
            * `sudo nano members-site.conf`
            * `<VirtualHost *:80>`
            * ` ServerName members.mysite.com`
            * ` DocumentRoot "/var/www/members"`
            * `</VitualHost>`
            * Speichern
            * Apache reloaden
        * Das ganze würde die die Main Seite überschreiben. Fix:
            * `sudo vi default-site.conf`
            * `<VirtualHost *:80>`
            * ` ServerName mysite.com`
            * `ServerAlias *.mysite.com` 
            * ` DocumentRoot "/var/www/members"`
            * `</VitualHost>`
        * ABER die conf-s in */etc/httpd/conf.d* werden in alphabetischer Reihenfolge abgearbeitet. Da defautl-site.conf zuerst kommt und da `*.mysite.com` steht => wird members.mysite.com nicht mehr erreicht. Fix - Datien Umbennen:
            * `sudo mv default-site.conf welcome-site.conf`
            * Apache restarten
        4. Apache restarten
#### 10 - Common troubleshooting topics
* `systemctl status httpd`- Checken, ob Apache an ist
* `ss -an` - in Output schauen, ob Port 80 hört
* `curl localhost` oder `curl 10.0.2.8` - Checken, ob Server antwortet. Wenn nur zu localhost antwortet, dann in Listen-address in httpd.conf checken. Oder die Firewall falsch eingestellt `firewall-cmd --list-all` - HTTP sollte aufgelistet sein. Eventuell DNS falsch
* Wenn man Dateien ändert, werden die Rechte machmal verändert. Bsp:
    * `sudo chcon -t user1 style.css`
    * `ls -lhZ`
    * `sudo restorecon style.css`
    * `ls -lhZ`
    * Dateien sollte root root als Besitzer haben und 644 als Rechte haben
    * Bei PHP ob PHP module installiert: `httpd -M` - PHP Sollte dabei sein
    * `tail /var/log/httpd/error_log` - alles Weitere
### 2 - Secure the Site and Control Access
#### 1 - Secure access with SSL
* Verschlüsselung zwischen Server und Client
    * Client und Server bestimmen Shared Secret
    * Server hat dafür einen Crypto-Certificate
    * Client weiß, dass man dem Server vertrauen, da er von CA die vertraunswürdigen Cetificate kennt
* man kann Self-Signed Certificate erstellen, aber nicht von CA => nicht vertraunswürdig
#### 2 - Create a self-signed certificate
* Vorgehensweise:
    1. mit openssl private Key ersellen
    2. mit openssl Certificate Signing Request (CSR) erstellen
    3. aus diesen Beiden Certificate erstellen
* Bsp:
    * `openssl genrsa -out ca.key 2048`
    * `openssl req -new -key ca.key -out ca.usr` 
    * `openssl x509 -req -days 90 -in ca.csr -signkey ca.key -out ca.crt` 
#### 3 - Use a certificate from a Certificate Authority(CA)
#### 4 - Add an SSL certificate to your site
* Appache für SSL eisntellen - SSL-Modul aus Repo installieren
    * `sudo yum install mod_ssl` - added Modul in Appache-conf und erstellt Datei ssl.conf in conf.d
* Cert-Datein in richtige Ornder kopieren:
    * `sudo cp ca.crt /etc/pki/tls/certs`, `sudo cp ca.key /etc/pki/tls/private`
    * Server braucht Zugang zu diesen Dateien:
        * `sudo nano /etc/httpd/conf.d/ssl.conf`
            * `SSLCertificateFile /etc/pki/tls/certs/ca.crt`
            * `SSLCertificateKeyFile /etc/pki/tls/private/ca.key`
        * Speichern
        * Apache neustarten
    * Port 443 freigeben:
        * `sudo firewall-cmd -zone=public --add-service=https --permanent`
        * Apache restarten
* man kann noch VirtualHost einstellen, dass er zu https weiterleitet:
    * `sudo vi default-site.conf`
    * `<VirtualHost *:80>`
    * ` ServerName mysite.com`
    * `ServerAlias *.mysite.com` 
    * ` DocumentRoot "/var/www/members"`
    * `Redirect / https://mysite.com`
    * `</VitualHost>`
    * Apache restarten
#### 5 - Protect a site with a .htaccess file
* Seiten Config auch per .htaccess einstellen, pro Website-Directory eine .htaccess
* Damit Änderungen über .htaccess akzeptiert werden, muss man das in den Apache-conf einstellen
    * `sudo nano /etc/httpd/conf/httpd.conf`
    * `<Directory "/var/www/html">`
    * `AllowOverride All
    * `</Directory>`
    * Restart
* `cd /var/www/html`
* `sudo touch .htaccess`
* `sudo nano .htaccess`
    * ```
    Require all denied # alle Request werden abgelehnt
    Require all granted # alle Request werden erlaubt
    Require all denied # alle Request werden abgelehnt
    ```
* Es gibt drei Require Groups:
    1. Require all
    ```
    <RequireAll>
    Require host
    Require ip
    Require not ip
    </RequireAll>
    ```
    2. Requier any
    ```
    <RequireAny>
    Require all denied/granted
    #Require host
    Require ip 216.0.0.0/8
    #Require not ip
    </RequireAny>
    ```
    3. Require none
    ```
    <RequireNone>
    Require host
    Require ip
    Require not ip # Negation
    </RequireNone>
    ```
* mehr Info zu Require - auf http://httpd.apache.org/docs/
#### 6 - Rewrite a URL with a .htaccess file
* es gibt ein Module *mod_rewrite* um einzustellen, wie URL Requests funktionieren. Benutz um z.B Tiefe (schwerk einprägbare Directorys umzuleigen) - Rewrite-Rules erstellen
    * `sudo touch .htaccess`
        * `RewriteEngine On`
        * `RewriteRule "^my$" "archive/talks/2005/25/07/widgets/lala/lala/my.html`
    * Wenn man jetzt im Broser eingibt: *mysite.de/my* man wird dann weitergeleitet
### Additional
#### 1 - Other web servers
+ Apache - Web-Server
+ nginx - Event-Driven, kann auch Module haben, Module müssen einkompiliert in nginx sein. Oft werden mit Appache zusammenbenutzt
+ App-Server: z.B für .js (Node), .py (), .java (Tomcat). 
###