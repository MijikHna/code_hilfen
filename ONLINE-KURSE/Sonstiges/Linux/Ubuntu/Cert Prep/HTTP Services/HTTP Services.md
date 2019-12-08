### 1 - Appache HTTP server
#### 1 - What a web server needs
+ Domain Namen + static IP
    * Domainnamen kaufen + global registrieren (A-Eintrag)
#### 2 - Installing and configuring the HTTP server
* Apache ist Foundation, die auch z.B Kafka, Hadoop,Tomcat usw. entwickelt
* `apt install apache2`
* Dateien:
    * in `/etc/apache2`
    * `/etc/apache2/apache2.conf` - Main datei - globale Conf + Server Conf.
    * `etc/apache2/sites-available`
        * `000-default.conf` - Normale Seiten
            * darin ist `<Virtual Host *:80>`
                * *ServerAdmin* - öffentlich
        * `default-ssl.conf` - 
#### 3 - Apache directives
* Apache Sections: https://httpd.apache.org/docs/2.4/sections.html
* Apache Directiven: https://httpd.apache.org/docs/2.4/mod/quickreference.html
* Directiven: (z.B VirtualHost, Directory, IfModule):
    * `<VirtualHost address:80> ... </VirtualHost>`
    * `<IfModule>`
    * `<FileMatch>` - wie bestimmte Dateien behandelt werden sollen z.B Handler für bestimmte Datein
    * `<Directory>`
    * innerhalb der Directories:
        * `Options` - Controls available features 
        * `AllowOverride` - Features that later configurations can override
        * `Require` - Controll access based on a condition
        * `Include` - Load another file
        * `DocumentRoot` - Directory to serve files from
#### 4 - Name-based virtual Hosts
* Subdomäne bei DNS registrieren
* in `/etc/apache2/sites-available` *010-subdomainName.conf* erstellen (eventuell alles aus *000-default-conf* kopieren)
```
<VirtualHost *:80> # eventuell hier domainNamen oder IP eitnragen
ServerName subdomainName.mystie.com
DocumentRoot /var/www/subdomainName
</VirtualHost>
```
* in `/var/www/subdomainName` die Dateien ablegen
* `a2ensite 010-subdomainName.conf`
* Apache restarten
### 2 - Adding Ecryption
#### 1 - Enabling HTTPS
* `/etc/apache2/sites-available/default-ssl.conf` aufmachen
    * `ServerName mysite.com`
    * `SSLEngine on`
    * `SSLCertificateFile ...`
    * `SSLCertificateKeyFile ...`
    * <- eventuell weitere Einstellungen
#### 2 - Creating a self-signed certificate
* Zertifikat erstellen
    1. Zertifikat erstellen
    2. Signing-Request erstellen
    3. Zertificat unterzeichnen
    * aber alles in einem Schritt:
        * `openssl req -x509 -newkey rsa:2048 -keyout mycert.key -out mycert.pem -nodes -days 365`
            * `req -x509` - Request erstellen
            * `-newkey rsa:2048 -keyout mycert.out ` - Key erstellen
            + `-out mycert.pem` - Signed-Cert erstellen
            + `nodes` - NO DES: no password
        * *mycert.key* nach */etc/ssl/private* verschieben
        * *mycert.pem* nach */etc/ssl/certs*
        * diese Pfade bzw. Dateien in */etc/apache2/sites-available/default-ssl.conf* eintragen
        * `a2enmod ssl` - SSL-Modul aktivieren
        * `a2enmod default-ssl.conf` - SSL-Seite aktivieren
        * Apache restarten
#### 3 - Using a certificate from a certificate authority
* One Cert per Domain/Subdomain
* SAN Cert - list fo domain names
* Wild Card cert - (z.B *.mysite.com)
* Bei Intermediate Certificaten on */etc/apache2/sites-available/default-ssl.conf* noch `SSLCertificateChainFile /etc/ssl/certs/lala_intermeidiate.crt` eintragen
#### 4 - Making access easier
* z.B https://mysite.com, http://mysite.com, https://www.mysite.com und http://www.mysite.com - sind 4 verschiedene Seiten -> man muss Redirections einstellen un DNS support für WWW mit CNAME www für Subdomain eitragen
    * *www* zu Base-Domain hinzufügen
        * */etc/apache2/sites-available/default-ssl.conf* öffnen
        * `ServerAlias www.mysite.com`
    * http -> https: (ist ja eigener VirtHost)
        * */etc/apache2/sites-available/000-default.conf* öffnen
        * `ServerName mysite.com`
        * `ServerAlias www.mysite.com`
        * `Redirect permanent / https://www.mysite.com`
    * 
### 3 - Administering Apache Server
#### 1 - Apache logging
* Access Log  - */var/log/apache2/access.log*
* Error Log - */var/log/apache2/error.log*
* Format der Logs + LogLevel ändern in */etc/apache2/apache2.conf* oder bei VirtHost in deren conf-Datei
#### 2 - Working with Modules
+ `apache2ctl -M` - Module einzeigen (statische mit Apache +  shared, die man selbst installiert hat)
    + `apt search libapache2-mod*` - nach Apache Modulen suchen
    * Bps PHP isntallieren:
        * `apt install libapache2-mod-php`
        * `apache2ctl -M` 
            * PHP-Testen: */var/www/html/test.php* erstellen
            * <!php phpinfo(); >
            * in Browser: *mysite.com/test.php*
            * `a2dismod php7` - PHP-Modul deaktivieren
    * */etc/apache2/mods-available/ - hier sind Module die aktiviert/deaktiviert werden können (.load und .conf - Dateien)
#### 3 - User-based security
* Zugang zu Webpage beschränken = Apache Basic Authentication
    1. Config-Datei mit dem VirtHost bearbeiten, die über der Directory liegt 
        + */etc/apache2/sites-available/default-ssl.conf* öffnen
        + einfügen:
        ```
        <Direcotry /var/www/html/protected>
        AuthType Basic #Apache Basic Authen benutzen
        AuthName "please log in"
        AuthUserFile /usr/local/etc/apachepwds # wo User-Password gespeichert werden
        Require valid-user
        </Directory>
        ```
        * User anlegen:
            * `htpasswd -c /user/local/etc/apachepwds scott`
        * Apache neustarten
        * zur protected Seite navigieren
        * Authentication mit LDAP:
        ```
         <Direcotry /var/www/html/protected>
        AuthType Basic #Apache Basic Authen benutzen
        AuthName "please log in"
        #AuthUserFile /usr/local/etc/apachepwds # wo User-Password gespeichert werden
        AuthBasicProvider ldap
        AuthLDAPURL ldap://ldapserver..
        Require valid-user
        </Directory>
        ```
    2. .htaccess
#### 4 - Per-directory configuration changes with .htaccess
* Fragement der Config für bestibte Webpage
* arbeitet wie `<Directory>
* um es zu benutzen, muss man in Config `AllowOverride` enablen
* `AllowOverride`:
    * `AuthConfig`  - Change authorization parameters for a directory
    * `FileInfo` - Change document handling, enable rewrites
    * `Indexes` - Modify how directory idnexing works
    * `Options` - Allows or denies specific features
* Bsp:
    * */etc/apache2/sites-available/default-ssl.conf* öffnen
    * 
     ```
    <Direcotry /var/www/html/protected>
    AllowOverride Indexes
    </Directory>
    ```
    * Apache restarten
    * `.htaccess` anlegen in *protected* und öffnen
    * `HeaderName head.html`
    * *head.html* anlegen -> zeigt alle vorhandenen Dateien
    * Apache muss nicht neugestartet werden (Vorteil von .htaccess)
#### 5 - Troubleshouting HTTP services
* Checken mit *systemctl* ob apche läuft
* Schauen, ob seite enabled ist:
    * `ls /etc/apache2/sites-enabled`
    ODER
    * a2ensite mysite.conf
* Logs checken:
    * tail /var/log/apache2/error.log
    * tail /var/log/apache2/access.log
* Permission <- sollten von Apache-User mindestens lesbar sein
* Firewall 80,443
* DNS checken
