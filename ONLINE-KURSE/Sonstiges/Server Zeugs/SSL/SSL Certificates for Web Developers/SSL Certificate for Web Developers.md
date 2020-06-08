### 0 - Introduction
#### 1 - Why SSL are essential for every website
* man braucht eine Domain (IP ist nicht genug)
#### 2 - What you need
* man braucht eine Domain (IP ist nicht genug)

### 1 - SSL and HTTPS
#### 1 - What are SSL certificates
* Certificate zertifiziert den Public Key der Seite - sagt diese Organisation/URL besitzt diesen Public Key
    * hat Endung .crt, .cer
#### 2 - Handshakes and cryptography
* 
#### 3 - The urgent need for HTTPS

### 2 - Choose a Certificate
#### 1 - Certificate authorities (CAs)
* CAs:
    1. stelle die Zertifikate aus
    2. zertifizieren den Besitz des Public Keys
        + man geht zu CA, gibt ihr Info über die URI, die Organisation, den Public Key
        * CA erstellt dann Zerifikat, dass besagt, dass wir den Public Key wirklich besitzen
        * CA = Trusted third Party, Browser hat eine Liste von diesen CAs (von OS)
            + es gibt verschieden CA-Levels:
                * Root Certificate Authorities - ganz wenige
                * Intermediate Certificate Authorities - Root CA deligieren die Arbeit und das Vertrauen an sie
                    * Browser der Root CA vertrauet, vertraut automatisch deren Intermediate CA - also Thrust Chain
#### 2 - Free certificates with Let's Encrypt
* ist Free CA
* Unterschiede zu normalen CAs:
    * man kann nicht den gleichen Cert bekommen
    * nur 90 gültig + fast auto-renewable
#### 3 - Self-signed certificates
* werden nicht von CA, sondern von sich selber.
#### 4 - Certificate types
* Zertifikat Typ:
    * Single domain Scope (nur für www.coolsite.com)
    * Wildcard (für *.coolsite.com)
    * Multi-Doman (für coolsite.com, greatsite.org)
    * UCS-Zert. (Microsoft-Communications)
* Validation Level:
    * Domain Validation (DV) - Public Key für domain
    * Organisation Validation (OV) - Public Key für domain + checkt Business DB für das Unternehmen
    * Extended Validation (EV) 

### 3 - Install a Certificate with Let's Encrypt
#### 1 - Certbot
* Certbot ist ein Projekt von let's Encrypt, ist Python client für ACME (Automatic Certificate Management Environment) protocol
    * Let's Encrypt stellt Cert aus
    * EFF verwaltet die Certificats
    * Cetbot benutzt ACME Protocol
* Standard-Cert:
    * Generate a public-private key pair
    * mit public-Key Certificate Signing Request (CSR) erstllen
    * Seite der CA besuchen und CSR abschicken
    * Zertificate bekommen
    * auf dem eignene Web Server installieren
* ACME (lets Enrypt):
    + auf dem Server anmelden
    * ACME client installieren
    * ACME cleint starten
    * Client hilft bei bekommen und einrichten
#### 2 - Install using Certbot
* auf lets Encrypt auf Get started 
* au Certbot klicken
* richtiges System auswählen
* es werden Install-Vorgehen angezeigt.
    * `sudo certbot --nginx` - Cleint starten
        * Lets Encrypt erstellt eine Datei auf der Seite, damit es für Let's Encrypt sichtbar ist. Wenn es sichtbar ist, löscht es wieder die Datei und stellt Zertifikat und Private Key
#### 3 - Install using  a hosting provider
* den Hoster kontaktieren, da er Zugang zum Server hat.

### 4 - Install a Pruchased Certificate
#### 1 - Certificate signing request (CSR)
* keine Online CSR-Generatoren benututzen:
    * da 1. Schritt sit public-private-key pair erstellen
* Tools:
    * openssl
        * key pair erstellen 
        * csr erstellen - `openssl req -new -key domain.key -out domain.csr`
        * Org-Info eingeben
        * Schritte:
            * privte Key erstellen - `openssl genrsa -out domain.key 2048`
            * csr erstellen - `openssl req -new -key domain.key -out domain.csr`. Passwort benutzt keiner. Dabei wird zu dem private key passendes public key erstellt
            * private Key + csr - `openssl req -newkey rsa:2048 -keyout domain.key -out doamin.csr` 
        * `open -req -text -in domain.crt -noout` - zeigt den Text des Requests
#### 2 - Sign up for an SSL certificate
* 
#### 3 - Install on Apache
* Configs sind in */etc/httpd/* oder */etc/apache2*
    * oft wird für einzelne VirtHost eigener Cert installiert
    * 
    ```
    <VirtualHost 192.0.0.1:443>
        ServerName mydomain.com
        DocumentRoot /var/www/html/
        #SSL
        SSLEngine on
        SSLCertificateFile /path/to/domain.crt
        SSLCertificateKeyFile /path/to/domain.key
        SSLCertificateChainFile /path/to/chain.crt
    </VirtualHost>
    ```
    * `apachectl configtest` - Config auf Richtigkeit testen
    * `apachectl restart` oder `apchectl graceful`
#### 4 - Install on NGINX
* Config zuerst BackUp-en
* Configs in */etc/nginx* oder */opt/nginx*
    * */etc/nginx/sites-available*. */etc/nginx/sites-enable* enthalten Links zu *sites-available*
    * 
    ```
    server {
        ;listen 80 default_server;
        server_name mydomain.com;
        root /var/www/html;
        index index.html;

        ;SSL
        listen 443 ssl;
        ssl_certificate /path/to/domian.crt;
        ssl_certificate_key /path/to/domian.key;
    }
    ```
    * `sudo /etc/init.d/ningx -t` - Config auf Fehler testen
    + `sudo /etc/init.d/nginx restart` oder `sudo /etc/init.d/nginx -s reload`
#### 5 - Install on hosted web servers
* Host Provider kontaktieren oder Host Company Guides schauen.

### 5 - Configure a Web Server to Require to HTTPS
#### 1 - Redirect requests to HTTPS
* Certboot von Let's Encrypt macht das automatisch
* Apache: Browser landet bei 80 und macht dann direkt Request an 443
```
 <VirtualHost 192.0.0.1:80>
        ServerName mydomain.com
        DocumentRoot /var/www/html/
        
        Redirect permanent / https://mydomian.com
</VirtualHost>
```
* nginx:
```
server {
    listen 80 default_server;
    server_name mydomain.com;

    return 404;
    if ($host = mydomian.com){
        return 301 https://$host$request_uri;
    }
}
```

#### 2 - HTTP Strict Transport Security (HSTS)
* Browser redet mit Seite, wenn sie https unterstützt. Browser macht den 443 request
* man muss Directicve to HTTP header hinzufügen "Strict-Transport-Security"
    * "max-age=300; includeSubdomains;"
    * Restart Server
* Apache:
```
 <VirtualHost 192.0.0.1:443>
        ServerName mydomain.com
        DocumentRoot /var/www/html/
        
        Header always set Strict-Transport-Security
        "max-age=300; includeSubdomains;"
</VirtualHost>
```
* nginx:
```
server {
    listen 80 default_server;
    server_name mydomain.com;

    add_header Strict-Transport-Security "max-age=300; includeSubdomains;";
}
```
* man sollte mit kleinerer Zeit beginnen, dann größer machen, wenn alles funktioniert. Ziel ist 63072000 Sek = 2 Jahre. Bei 2 Jahre kann man HSTS preloading benutzen
#### 3 - HSTS preloading
* Browser hält HTTPS-only Seiten List.
* HSTS muss mindestens 1 Jahr sein + subdomain + preload:
    * `"max-age=300; includeSubdomains; preload"`
* https://hstspreload.org gehen und die Seite da registrieren. Browser bekommen dann beim Update die Liste mit den Seiten Browser wird immer zu HTTPS umleiten. 
* 
### 6 - Manager Certificates
#### 1 - Expiriation dates
* da Standards ändern, werden nach Expiration neue Standars implementiert beim neuen Certs.
* new CSR, reapply bei Third Party
* Certboot boe Let's Encrypt
#### 2 - Renew Let's Encrypt certificates
* bie Linux kann man cronjob benutzen:
* `sudo certboot renew --dry-run` - zeigt was es machen würde
* `sudo certboot renew` - wird renu
* `sudo certboot -q renew` - bei Cronjob, *-q* - keine Ausgabe
* `m   h  d m dayweek`
* `0 */12 * * * cerboot -q renew`
* `/etc/cron.d/certbot` - checken ob Certboot Cronjob schon erstellt hat.
* `crontab -e` - läuft es als current User
* in */etc/cron.d* - läuft automatisch als sudo