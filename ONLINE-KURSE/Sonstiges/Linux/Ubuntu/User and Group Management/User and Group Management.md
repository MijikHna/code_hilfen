### 0 - Introduction
#### 1 - Users and Groups
* UID - User-ID
* GID - Group-ID
* /etc/password - User
* /etc/group - Gruppen
* scott:x:1000:1000:scott,,,;/home/scott:/bin/bash - User:x=Password ist in /etc/shadow:UID:GID=Users primary group:Beschreibung des Users (GECOS):Home-Directory:Users default shell (kann false,nologin sein)
* scott:asfr0afüt:17025:0:9999:7:n:n:n - User:verschlüsseltesPassword:Datum letzter Passwordänderung(/etc/shadow):minPassworddauer:maxPassworddauer:WarningPeriode:InactivityPeriod:ExpirationDate:FutureUse
* gruppe:x:1000:scott,marry - Gruppenname:GruppenPassword:Mitglieder
* `groups`, `id` - Gruppen-, User-Tool
#### 2 - Environment setup
### 1 - Local Users and Groups
#### 1 - Create user accounts
* `useradd` - liest /etc/adduser.conf
    * `useradd alex` - Std-User erstellen
    * `useradd --system alex` - System-User erstellen
    * GECOS = Full Name, Room Number, Work Phone, Home Phone
    * Systemuser haben UID kleiner als 1000, Standarduser haben UID größer als 1000
    * `user add alex` - wird auch Gruppe alex erstellt, die die Primary group für alex wird
    * `useradd --system botuser` - haben keine Gruppe, sind für automatische Prozesse,
    * `id username` = Info zum User ansehen
#### 2 - Modify and delete use accounts
* `passwd` - Passwort ändern, fordert auf current Password einzugeben
* `sudo passwd` - als Sudo Passwort ändern, muss man nicht current Password eingeben
* `chsh` - Default-Shell ändern oder Login verbitetn - `/bin/false`
* `sudo chfn alex` - GECOS für User ändern
* `sudo usermod -l alexander alex` - Usernamen ändern
* `sudo usermod -d /home/alexander -m alexander` - Homefolder ändern. `-d` = Setzt Homefolder, `-m` = verschiebt Homefolder des Benutzers. Also muss man gemeinsam benutzen.
* `sudo deluser` - User löschen (eventuell mit `--help` Optionen ansehen)
#### 3 - Create and modify groups
* `addgroup` - man kann mit `--system` Systemgroupen erstellen
    * `sudo addgroup finance`
    * `sudo adduser alexander finance`
    ODER
    * `sudo usermod -aG alexander finance` - `-a` = append statt replace, `-G` = Liste der Gruppen ausgeben, aus denen dann eine passen muss
* `groupmod` - Gruppen ändern 
* `delgroup` - Gruppen löschen
#### 4 - Home folder templating and global environment configuration
* in /etc/adduser.conf
* in /etc/skel:
    * Bsp:
        * mkdir /etc/skel/Documents
        * nano /etc/skel/Documents/welcome.txt
        * Welcome Text
        * Speichern
    * <- der Inhalt von /etc/skel wird in /home von neuem User kopiert
* Environemnt für Users setzen:
    1. in /etc/profie:
        1. Bsp:
    2. in /etc/profile.d (Folder)
        * Bsp:
            1. nano myfile.sh
            2. alias l="ls -lh"
            2. Speichern
#### 5 - Configure and monitor user resources
* `yes > /dev/null &` - yes unendlich eingeben
* Monitoring:
    * `top -u username`
    * `ps -u username`
    * `kill -9 pid`
* in `/etc/security/limits.conf` kann man für User/Gruppen Grenzen für CPU,Memory, Menge der geöffneten Dateien setzen
    * soft - dem User wird nur Warnung angezeigt
    * hard - wird Unterbunden
    * Bsp:
        * `alexander hard fsize 100000` - User verbieten Dateien größer als 100MB zu erstellen
        * Test:
            * sich mit dem User anmelden
            * `fallocate -l 100M 100mfile.txt`
* Quota (?):
    * `apt-get install quota`
    * 

#### 6 - Configure permissions to allow group collaboration
* Ordner bestimmten Gruppen zuweisen, und darin erstellten Datien übernehmen die Besitzteigenschaft von dem Ordner
* Bsp:
    * `mkdir /shared`
    * `chgrp finance /shared` - dem Ordner shared der Gruppe finance zuweisen
    * `chmod g+w /shared`
    * `usermod -aG finance mike`
    * `chmod g+s /shared/` - Schaltet groupid an, sodass, was in diesem Ordner liegt, gehört der Gruppe.
    ODER
    * `chmod 2775 /shared/`

#### 7 - Granting users and groups sudo access
* /etc/sudoers bearbeiten
* Bsp:
    * `visudo` - öffnet direkt /etc/sudoers
    * `ALL=(ALL:ALL) ALL` - Hosts von denen der User sich verbinden kann = (Alle User emulieren:Alle Gruppen emulieren) : Commandos, die Ausgeführt werden sollen
### 2 - Authentication Tools
#### 1 - Explore pluggable authentication modules (PAM)
* in /etc/pam.d Ordner sind Dateien, die PAM benutzen.
* die Dateien anschauen, um zu verstehen, was passiert wenn dieses Tool/Befehl aufgerufen wird
* nicht so ganz verstanden, wie das ganze funktioniert
#### 2 - Use LDAP for user authentication
* LDAP = Lightweight Directory Access Protocol
* man muss PAM einstellen, um LDAP zu erlauben, geeignete Methode zur Authentitierung zu sein
* LDAP Server installieren:
    * ldap-utils = um mit LDAP zu komminizieren
    * slapd = LDAP Server
    * `apt-get install slapd ldap-utils`
    * `dpkg-reconfigure slapd` - LDAP neu konfigurieren
    * ldapmodify - Tool = mit LDAP managen
    * `sudo apt-get install phpldapadmin`
    * in LDAP sollte kein User die UID 1000 haben => z.B 10001
    * man sollte überlegen, welche USER man nach LDAP umzieht und welche auf dem Rechner local lässt (sonst Probleme mit UIDs)
* LDAP Client installieren
    * `apt-get install nscd ldap-auth-cliesudo nt`
    * URL zum LDAP eintragen
    * `dc=test,dc=de` eintragen
    * LDAP Version 3 auswählen
    * password utility -> YES
    * LDAP admin eitnragen: `cd=admin,dc=test,dc=de`
    * <- dabei werden einige Sachen in PAM-config eingetragen
    * `dpkg-reconfigure ldap-auth-conf` - LDAP-Client nochmal konfigurieren 
    * Man muss noch /etc/nsswitch.conf eintragen, wo es nach Passwörtern schauen soll:
        * `nano /etc/nsswitch.conf`
        * `passwd: compat ldap`
        * `passwd: compat ldap`
        * `passwd: compat ldap`
        * <- `ldap` sollte als letztes stehen, sonst wird zuerst in ldap geschauet
    * Einstellungen für LDAP checken
    * `grep ldap /etc/pam.d`
    * `pam-auth-update` - zeigt, ob LDAP-Authentication an ist, evenutell, ob beim login home-Ordner erstellt wird
    * `nano /etc/pam.d/common-session`
    * `session setion pam_mkhomedir.so skel=/etc/skel` einfügen/ergänzen
    * systemctl restart nscd
#### 3 - Authenticate clients with Kerberos
* Kerberos-Server (KDC=Key Destribution Center)
* Kerberso-Server:
    * `nano /etc/hosts`
    * `127.0.0.1 kdc.example.com`
    * `apt install krb5-kdc krb5-admin-server`
    * realm = `EXAMPLE.COM` - muss großgeschrieben werden
    * `kdc.example.com` eintragen
    * `kdc.example.com` eintragen
    * `krb5_newrealm` - um neuen realm zu ertellen
    * Master-Password ausdenken
    * `kadmin.local` - kdm-Konsole aufmachen
    * `addprinc alexander` - ein Eintrag in ein principal
    * Passwort für alexander setzen
    * man kann die Kerberos-Einträge nach LDAP übertragen
    * `exit`
* Kerberos-Client:
    * `apt get install krb5-user krb5-config`
    * `dpkg-reconfigure krb5-config`
    * `EXAMPLE.COM` - realm eingeben -> es wird /etc/krb5.conf erstellt
    * <- man kann diesese Datei auf alle Clients schieben
    * `kinit -p alexander@EXAMPLE.COM` - Kerberos-Session initialisieren
    * `klist` - Tickets des Users auflisten
    * `adduser pat` - User erstellen, der sich mit Kerberos (eventuell in LDAP diesen Benutzer erstellen) unterhalten wird
    * `apt install libpam-krb5` - Support für PAM für pat user.
        * trägt Kerberos in `/etc/pam.d`
    * libpam-secret-Package - für gecached Accounts falls Kerberos-Server nicht erreichbar ist
### Additional
* `who` - wer ist gerade am Rechner eingelogt
* `last` - wer sich wann eingeloggt hat. Inhalt kommt aus binary-Logs
* `lastlog` - zeigt alle User an, die dem System bekannt sind, und wann sie sich zum letzten Mal eingeloggt haben.
