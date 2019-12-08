### 1 - PKI Overview
#### 1 - Cryptography overview
#### 2 - Symmetric and assymetric encryption
* Symmetric Algorithmen:
    1. AES - 256 Bit
    2. RC4 - 2048 Bit
    3. 3DES - 168 Bit
    4. Blowfish - 448 Bit
* Assymetrische Encryption:
    * RSA - 4096 Bit
    * Deffie-Hellman -
    * EiGAmal - 2048 Bit
    * ECC - 256 Bit
#### 3 - PKI hierarchy
* PKI - Public Key Infrastructure
* PKI-Hierarchy - Collections of Certificates
    * Zertifikate haben immer public key
    * Zertifikate können private key haben
    * PKI - Hierarchie:
        * CA - stellt Zertifikate aus
        * RA - Registration Authority (läuft unter CA)
        * CRL - Certificate Revocation List, OCSP - Online Certificate Status Protocol - verifiziert die Zertifikate mit Hilfe von Serialer Nummer
        * Certificate Template - Blueprint used when issuing certificates
        * Certifikate - Subject Name (URI, usw), Signature of CA, expiry Datum public Key
    * Single-Tier PKI Hierarchy = Certificate Authority, die direkt Zertifikate verteilt
    * Multi-Tier PKI Hierarchie = eine CA unter der mehrere RA laufen und Certs ausstellen. CA kann man dan offline stellen, bis sie wirklich benötigt wird.
#### 4 - Certificate Authorities
* CA/CA-Cerst haben längere Validität als Certificates, die sie ausstellen
* Zertikate haben die digitale Signatur von CA. Dig Signatre, die mit Private Key erstellt wurden, können nicht so leicht vorgegaukelt werden
* man muss CA-Root-Certs von self-signed Zertifikaten importieren
#### 5 - Certificates 
* Zertifikate haben:
    1. Version number
    2. Serail number - um Revocations zu checken
    3. Digital Signatur
    4. Valid Time
    5. Usage Detail
    6. Subject (URL, email des Users)
    7. Public Key (eventuell Private Key)
* Certificate Revocation List (CRL) - wird von CA published = Liste von revoked certificate serial numbers. also Clients sollte diese Liste bekommen
* OCSP - Online Certificate Status Protocol - die Validität wird Online abgefragt
* OCSP Stapling - Besitzer des Certs fragt CA periodisch, ob der benutzte Cert valid ist. Clients die sich mit der Seite verbinden, erhalten diese Status und checken so die Validität
#### 6 - Certificate lifecycle management
* Cert Lifestyle:
    * Cert Request = CA bieten den Cert zu unterzeichnen
* Simple Certificate Enrollment Protocol
    * per MDM Zertificate für Geräte ausstellen
### 2 - PKI CA Implementation
#### 1 - Install a Microsoft AD CS certificate
#### 2 - Configure Microsoft AD CS certificate templates
#### 3 - Configure a Linux OpenSSL PKI environment
* `apt install openssl`
* davor eventuell *\cert* ersellen
* `openssl genrsa -aes256 --out CAprivate.key 2048` - private key für CA erstellen
* `openssl req -new -x509 -key CAprivate.key -sha256 -days 365 -out FakedDomain2CA.pem` - Cert für CA erstellen 
* jetzt muss man diesen Cert. auf die Clients bringen.
#### 4 - Configure an AWS Certificate Manager subordinate CA

### 3 - PKI Certificate Acquisition
#### 1 - SSL vs. TLS
* Gleich:
    * benutzen PKI Certs
* Unterschiede:
    * SSL durch TLS ersetzt -> SSL sollte auf Client und Server disabled sein
    * TLS ist besser bei Man in the Middle Attack (versuch die mögliche Verschlüsselung downzugraden). man sollte >TLS 1.1 benutzen
#### 2 - Acquire a web server certificate using Microsoft AD CS
#### 3 - Acquire a client certificate using Microsoft AD CS
#### 4 - Acquire a web server certificate using OpenSSL
* `openssl genrsa -aes256 -out www.fakesitelocal.key 2048` - private Key generieren, den man z.B für WebServer benutzt
* `openssl req -new -key www.fakesitelocal.key -out www.fakesite.local.csr` - CSR generieren
* Datei erstellen die Info für den Certifikat hat z.B *otherinfo.ext*:
    * 
    ```
    authorityKeyIdentifier=keyid,issuer
    basicConstraintss=CA:FALSE
    keyUsage=digitalSignature, nonRepudiation, keyEnchipherment, dataEncipherment
    subjectAltName = @alt_names

    [alt_names]
    DNS.1 = www.fakesite.local # Client brauchen diesen Namen um dem Certifikat zu vertrauen
    ```
    * `openssl x509 -req -in www.fakesite.local.csr -CA FakeDomain2CA.pem -CAkey CAprivate.key -CAcreateserial -extfile otherinfo.ext -out www.fakesite.local.crt -day 365 -sh256`
    * `a2enmod` - SSL-Modul installieren
    * `cat /etc/apache2/sites-enabled/000-default.conf`
    * bei VirtHost *:443 einfügen.
    * `SSLEngine on`
    * `SSLCertificateFile /cert/www.fakesite.local.crt`
    * `SSLCertificateKeyFile /cert/www.fakesite.local.key`
    * `SSLCACertificateFile /cert/FakeDomain2CA.pem` - diese Datei muss man dann auf dem Client importieren, damit es dem Server vertauet
    * Apache restarten
#### 5 - Acquire a web server certificate using AWS Certificate Manager
#### 6 - Acquire a code-signin certificate

### 4 - PKI Certificate Usage
#### 1 - Hashing and digital signatures
#### 2 - Configure a website with a certificate
#### 3 - Configure a web browser with a certificate
#### 4 - Configure a code-signing certificate with Microsoft PowerShell
#### 4 - Encrypting file system and certificates
#### 5 - Encryption file system and certificates
#### 6 - Configure a TLS VPN
#### 