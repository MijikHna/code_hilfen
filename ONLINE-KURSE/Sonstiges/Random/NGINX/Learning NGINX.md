### 0 - Introduction
#### 1 - What is NGINX
#### 2 - Linux, NGINX, Web technologies
#### 3 - Comparing NGINX to Apache
Apache | NGINX
---| ---
free + open source|
community driven |
compilierte Bibs |
Erweiterbar durch Landen der Module |
können als Proxy Servers konfiguriert |
Event-based Connections |
Config-Fromat XML| Conig-Format C
.htaccess files| nur zentralisierte Files (Block) 
per Haus hat Module| muss man zusätzlich installiert werden
|schneller bei statischen Dateien

* nginx ist einfacher zu konfigurieren + effizienter 
#### 4 - Set up a Sandbox with VB und Vagrant
* Lab - ubuntu-server in vagrant
* `VBoxManage --version`
* `vagrant --version`
#### 5 - Create a VM with Vagrant
* in ExFiles ist schon fertiges Vagrantfile
```ruby
Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-18.04"
    config.vm.network "private_network", ip: guest_ip
end
```
* `vagrant up`
* `vagrant ssh`
### 1 - Install and Configure NGINX
#### 1 - Install NGINX on Ubuntu
* `sudo su -`
* `apt update && apt dist-upgrade`
* `apt install nginx`
* `nginx -v`
* `systemctl status nginx` oder im Browser zu vagrant-IP navigieren
#### 2 - NGINX files and directories
* **/etc/nginx** - Konfigs für ganzes NGINX
    * nginx.conf - Main-Config Datei
    * conf.d - Order
    * sites-available - Order
        * default - Order, wo Begrüßungs-Seite von NGINX liegt
    * sites-enabled - Order
* **/var/log/nginx** - Logs von nginx
    * error.log
    * access.log
* **var/www/** - hier HTML-Seiten ablegen, die NGINX servieren soll
* Config-s sind ähnlich VirtualHost von Appache
#### 3 - The NGINX files and directories
* als *sudo* ausführen
* Status
    * `systemctl status nginx`
    * `systemctl statux nginx --no-pager`
* Start/Stop/Reload
    * über systemctl
    * `systemctl is-active nginx` - chechen, ob gestartet
#### 4 - The NGINX CLI
* ODER nginx-Commands benutzen
    * `nginx -h` - Help
    * `nginx -t` - Config auf Syntax-Fehler testen
    * `nginx -T` - Config testen + ausgeben
    * da Config von NGINX in mehreren Dateien sein kann => `-T` zeigt alles an einer Stelle
#### 5 - Inside nginx.conf
* eigentlich wird nginx.conf nicht so oft verwendet
* Syntyx: `directive { unterdirective };`
* `user www-data;` - User den nginx benutzt
* `http { accedd_log /var/..; include /etc/nginx/conf.d/*.conf}`
    * besser die Config über erweitern
        1. /etc/nginx/conf.d/*.conf 
        2. /etc/nginx/sites-available/*; und diese dann per SymLink nach /etc/nginx/sites-enabled/* linken
*  /etc/nginx/conf.d/*.conf ist besser
#### 6 - Configure a VirtHost: Part 1
1. default-Link in */etc/nginx/site-enabled* löschen `unlink default`
2. erstellen */etc/nginx/conf.d/seitenName.local.conf*
```c
server {
    listen 80;
    root /var/www/seitenName.local;
}
```
* `nginx -t` 
* `systemctl restart nginx`
#### 7 - Configure a VirtHost: Part 2
* Fortsetzung von #6
```c++
server {
    listen 80 default_server; //Standardseite setzen, wenn nichts weitere zutrifft
    server_name seitenName.local www.seitenName.local; //alle möglichen Webnamen
    index index.html index.htm index.php;
    root /var/www/seitenName.local;
}
```
#### 8 - Add files to the root directory
* `apt install unzip`
* `unzip -o lala.zip -d /var/www/seitenName.local` -o = override
* `find /var/www/seitenName.local/ -type -f -exec chmod 644 {}\;` - für alle Dateien in *seitenName.local rw-r--r-- setzen
* `find /var/www/seitenName.local/ -type -d -exec chmod 755 {}\;` - für alle Ordner in *seitenName.local rwxr-xr-x setzen
#### 9 - Configure locations
* = Config erweitern, basierend auf URI
* Syntax:
```nginx
server {
    location [modifier] location_definiont{
        ....
        location [modifier] location_definiont{
        
        }   
    }
}
```
* sind Blocks in **server**-Block
* können genestet sein
* man kann Einstellen, wie bestimmte URI behandelt werden, ohne kompletten neuen **Server**-Block zu erstellen
* Bsp:
    * `nano /etc/nginx/conf.d/widompets.local.conf
    * 
    ```nginx
    server {
        root /var/www/widsompetmed.local

        server_name widompetmed.local www.widompetmed.local

        index index.html index.htm index.php;

        location / {
            try_files $uri $uri/ =404
        }

        //images-Directory

        location /images {
            autoindex on
        }

        error_page 404 /404.html;
        location = /404.html {
            internal;
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            internal;
        }

        location = /500 {
            fastcgi_pass unix:/this/will/fail;
        }
    }
    ```
    * <= `try_files` sind relativ zu root und wenn eine Übereinstimmung wird getroffen, wird diese Datei angezeigt. Wenn kein Match, wird letzte Seite in `try_files` genommen (= Error-Code-Seite)
    * sucht in der `$uri`-Variable nach Matches, sonst `404` augegeben
    * ` autoindex on` - erlaubt Anzeige der `/image`-Order-Inhalt im Browser
    * dann Locations für Error vorgeben => Custom-Error-Pages statt Default-Seiten angezeigt
    * letzte Location zum Testen
    * `nginx -t` - Config testen
    * `systemctl restart nginx`
#### 10 - Configure logs
* Hier reinschauen, wenn Probleme auftretten
* Pfade zu Logs stehen in */etc/nginx/nginx.conf*
    * unter *access_log* und *error_log*
        * access_log - speichert die Daten zu Requests
* wenn mehrere Seiten globale Log-Configs benutzen => werden Logs dieser Seiten in globalen Log-File geschrieben
* man kann aber Logs in *server*- und *location*-Logs einstellen
```nginx
server {
    //...
    access_log /var/log/nginx/widompetmed.local.access.log;
    error_log /var/log/nginx/widompetmed.local.error.log;

    location /images {
        //...
        access_log /var/log/nginx/widompetmed.images.local.access.log;
        error_log /var/log/nginx/widompetmed.images.local.error.log;
    }
}
```
* Logs für Images werden hier auch getrennt
* mit Curl Verbindungen testen:
    * `for i in {1..10}; do curl localhost > /dev/null; done`
    `for i in {1..10}; do curl localhost/images/ > /dev/null; done`
#### 11 - Troubleshoot NGINX
* `nginx -t` - Config chechen => gibt Syntax-Error
* `systemctl status nginx`; `systemctl reload nginx`
* `sudo lsof -P -n -i :80 -i :443 | grep LISTEN` - chechen, ob die HTTP(S)-Porst offen sind
    * `lsof` - list open files
* `sudo netstas -plan | grep nginx` - ID die auf die Ports hört
* `tail -f /var/logs/nginx/*.log`

### 2 - The Linux, NGINX, MySQL and PHP Stack
#### 1 - The LEMP stack
* Web Stack aus 4 Teilen:
    1. OS (Linux)
    2. Web Server (Apache => LAMP-Stack); (Nginx => LEMP-Stack)
    3. DB (MySQL)
    4. Scripting Language (PHP, Perl, Python )
#### 2 - Install PHP on NGINX
* `apt update`
* `apt install php-fpm php-mysql` - FAST CGI Magager + MySQL-Verbinder
* `php --version`
* `systemctl status php-7.2-fpm` - Fast CGI Manager chechen
* `nano /etc/nginx/conf.d/widompetmed.local.conf`
```nginx
server {
    //...
    location ~ \.php$ {
        include snippets/fastcgi-php.conf; //hat Direktiven für Sicheheit
        fastcgi_pass unix:/var/run/php/php7.2-fpm.sock; //wie nginx und php intern kommunizieren soll
        fastcgi_intercept_errors on //
    } 
}
```
* location hinzufügen für Dateien, die auf *.php* enden
* mit `include` Dateien bekannt machen, die Direktiven/Schlüsselwörter enthält, die außerhalb von nginx sind => dann kann man z.B `fastcgi_pass` im Nginx-Konfig schreiben. 
* `systemctl reload nginx`
* php-Datei in */var/www/wisdompetmed.local/info.php* erstellen. `<?php phpinfo(); phpinfo(INFO_MODULES); ?>`
#### 3 - Install MariaDB on NGINX
* `apt install mariadb-server mariadb-client`
* `systemctl status mysqld.service`
* `mysql --version` - Client checken
* MariaDB Settings für bessere Security ändern:
    1. root Password setzen
    2. Remote für root-Account disableln
    3. Annonyme Accoutns löschen
    * `mysql_secure_installation`
    * ENTER
    * Y
    * Password für root setzen
    * Y für anonymous User
    * Y für Disallow root login remotely
    * Y to remove Test-DB
* `mysql -u root -p` 
    * `-u root` = als Root anmelden
    * `-p` = nach Passord fragen
    * `create database fi not exists appointments;`
    * `create user if not exists 'admin';`
    * `grant all on appointments.* to 'admin'@'localhost' identified by 'admin';` 
    * `exit`
* `mysql -u admin -p`
    * `show databases;`
    * `use appointments;`
    * `show tables;`
#### 4 - LEMP stack demostration
* PHP-Script der sich zu DB verbindet und dann in Browser den Result anzeigt => ist in Übung `index.php`
* `systemctl status nginx mysqld php7.2-fpm | grep -E "(Loaded|Active)"`
* `mkdir /var/www/wisdompetmed.local/appointments`
* `cp index.php /var/www/wisdompetme.local/appointments/index.php`
* `chmod +rx /var/www/wisdompetme.local/appointments/index.php`
* SQL import machen: `mysql -u admin -padmin appointments < /lala/appointments_data.sql`
    * `-padmin` = -pPASSWORD
    * `appointments` = DB-Name

### 3 - NGINX Security
#### 1 - Secure sites with NGINX
* alle up-to-date halten
* Access Restricten
* Passwords benutzen
* SSL benutzen
#### 2 - Configure allow and deny directory
* Nginx hat HTTP-Modul mit dem man Rechte für Directoris setzen kann
* Bsp: Seite protecten
    * `nano /etc/nginx/conf.d/wisdompetmed.local.conf`
    ```nginx
    server {
        //...
        location /appointments/ {
            deny all;
        }
    }
    ```
    * nginx reloaden
* Bsp: Nur Zugriff aus eigenem NW:
* `nano /etc/nginx/conf.d/wisdompetmed.local.conf`
    ```nginx
    server {
        //...
        location /appointments/ {
            allow 192.168.0.0/24
            allo 10.0.0.0/8;
            deny all;
        }
    }
    ```
#### 3 - Create a 403 page
* `nano /etc/nginx/conf.d/wisdompetmed.local.conf`
```nginx
server {
    //...
    location /deny/ {
        deny all;
    }

    error_page 403 /403.html;
    location /403.html/ {
        internal;
    }
}
```
* Nginx reloaden
* 403.html erstllen und nach /var/www/wisdompetmed.local/403.html kopieren
#### 4 - Configure password authentication
* http_auth_basic_modul dafür benutzen (ist eigentlich Appache Modul)
* d.h es wird nach Passwort und Username gefragt, wenn man die Seite sehen will
* `apt install apache2-utils`
* `htpassword -c /etc/nginx/password admin` - Password Datei als /etc/nginx/passwords ertellen und direkt den User admin darin ablegen. (man sollte diese Datei nicht in z.B /root ablegen, da nginx hat dann eventuell keinen Zugriff auf die Datei)
* `htpasswd /etc/nginx/password newuser` - weiteren User erstellen und diese Datei schreiben bzw. Password für den User ändern
* `htpasswd -D /etc/nginx/password/ UserName`-  User löschen
* <- Passwörter werden gehasht
* `chown www-data /etc/nginx/password`
* `chmod 600 /etc/nginx/password` - Rechte + Besitz auf nginx-User übertragen
* `nano /etc/nginx/conf.d/wisdompetmed.local.conf`
```nginx
server {
    location /appointments/ {
        auth_basic "Authentication is required" //zeigt Message im Browser;
        auth_basic_user_file /etc/nginx/passwords;
        location ~ \.php$ {
            include snippets/fastcgi-php.conf; //hat Direktiven für Sicheheit
            fastcgi_pass unix:/var/run/php/php7.2-fpm.sock; //wie nginx und php intern kommunizieren soll
            fastcgi_intercept_errors on //
        } //php-Config auch hier reinkopieren, da /appintments/ php serviert
        allow 192.168.0.0/24;
        deny all;
    }
}
```
#### 5 - Configure HTTPS
* Aufgabe:
    * Self-Signed Cert + http-ssl-modul benutzen
#### 6 - Create an SSL certificate
* 
#### 7 - Install an SSL certificate on NGINX

### 4 - Reverse Proxies and Load Balancers
#### 1 - Reverse proxies and load balancer
#### 2 - Configure NGINX as a reverse proxy
#### 3 - Configure NGINX as load balancer