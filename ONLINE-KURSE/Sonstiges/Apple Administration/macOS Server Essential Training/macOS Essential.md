## 1 - Planning and Requirements
#### 1 - Documentation of needs
Jeder Server sollte eigene Dokumentation, damit man wieß, was und wozu der Server da ist.
* Rollen: Admin, Clients usw.

#### 2 - User and IT balance
* IT Needs:
    * Security
    * HW Einkaufszyklen
    * Ablaufpläne
    * Limits
* Beim Aufsetzen des Servers:
    * Wozu dieser Server
        * Wozu FileServer: Welche Dateien?, wozu ist das nötig? <- Alternativen überlegen
    * Bestehen dann Security Gefahren
#### 3 - Network readiness
* Tools:
    * AirPort Extreme - Admin Tool für macOS und iOS.

#### 4 - Apple ID management
* Apple ID - wenigstens eine
* eine Apple-ID für APNS (push notification)
* VPP - Volume Purchase Program <- Apple-ID mit zwei-Weg-Authentizierung
* DEP - Device Enrollment Program <- Apple-ID mit zwei-Weg-Authentizierung
* unter appleid.apple.com Einstellungen für die Apple-ID machen z.B Apple-ID mit zwei-Weg-Authentizierung

## 2 - Setting Foundation
#### 1 - Static IP addressing
* OS X Server installieren
* System Einstellungen -> Netzwerk -> Ethernet 1 (sonstigen ausmachen) -> IPv4 zu Manuell -> IP und Maske setzen -> Erweitert -> DNS-Server hinzufügen -> Anwenden. 

#### 2 - Hostname configuration
* Go -> Utilities -> Terminal
* `sudo -s` -> Password eingeben
* `scutil --set HostName osxserver.test.net` - Domainname des PC
* `scutil --set LocalHostName osxserver` - Localer Name des PC 
* `scutil --set osxserver` - Computername des PC
*Tests:
    * `hostname`
    * `changeip -checkhostname` - 

#### 3 - Running OS X Server for the first time
* OS X Server starten

## 3 - Network Services
#### 1 - OS X Server DNS setup
* gibt es eigentlich nicht mehr

* Lookup checken
* Forwarding -> z.B google-DNS-Server eingeben.
* Bei Hostnamen auf + klicken -> eigenen Hosnamen eintragen z.B osxserver.testdomain.com + eigene IP eintragen + Alias `www` eintragen.
* auf Rädchen klicken -> Zeige alle - zeigt Details zu den erstellten Hostnamen.
* An-Button anklicken.
Tests:
1. Netzwerk Utilities -> Loolup -> eigenen Servernamen eingeben - sollte die IP anzeigen
2. changeip -checkhostname - sollte success
3. hostname

#### 2 - DHCP explained
* DHCP -> Einstellungen checken, eventuell korrigieren.
* da DHCP schon auf dem Router läuft, dann muss man sich für DHCP auf OS X Server oder Router entscheiden.
* Tipp: lieber Router-DHCP benutzen.

#### 3 - VPN service configuration
* Configure VPN for 
    1. L2TP auswählen (sicherer)
* VPN Host Name:
    1. osxserver.testdomain.net
    ODER
    2. WAN-Port-IP-Adresse des Routers eingeben
* User müssen sich mit eigenem Usernamen und Password authentifizieren + mit Schared Secret - Password
* Client Addresses -> Edit Adresses = Adress-Range + max. Anzahl gleichzeitiger Verbindungen erstellen. Adress-Range sollte über den Adressen von DHCP-Server liegen, da sonst kann es zu Konflikten kommen.
* Routes = statische Routen setzen, damit die Tunnelung verschlüsselt wird.
    * z.B IP des Server eingeben und `private`
* Config Profile -> Save Profile... - Profil für VPN speichern und den Benutzern geben <- auf Benutzernrechnern wird VPN damit eingerichtet.
* mit AirPort (Utility) kann man die Port-Forwarding anschauen:
    * AirPort (Utility) -> Router -> Edit -> Netzwerk -> Port Settings -> ...VPN -> Edit 
#### 4 - Firewalls explained
* Firewall sollte auf jedem Rechner installiert sein und angeschaltet sein.
* Nachteil: Traffik kann langsam sein, da jeder Paket analysiert sein wird.
* 

## 4 - Users Sharing Files
#### 1 - Users and groups
* Wenn man in einer Organisation arbeitet, die AD betreibt:
    1. den OS X Server in AD aufnehmen:
        1. System Eisntellungen -> User und Groups -> "Schloss" aufmachen -> unten bei Netzwerk Account Server auf **Join** klicken -> Prmären AD-Server eintragen -> sich mit Benutzer anmelden, der Rechte hat Rechner in AD aufnehmen.
>
> Hier im Beispiel werden USER und GRUPPEN direkt auf dem Server erstellt.

USER
* nachdem man USER erstellt hat, auf den User "doppelklicken" und schauen, dass "User erlauben" "log in" checked ist. Unchecked = Account deaktiviert.
* User auswälen -> Rädchen unten klicken - weitere Einstellngen für den User

GRUPPEN
* Gruppe erstellen
* Gruppe auswählen + doppelklicken

#### 2 - Sharing setup
1. Finder oder `CMD+SHIFT*C`
2. neuen Ordner erstellen
3. in OS X Server auf Storage-Reiter klicken
4. Ordner auswählen -> Rädchen anklicken -> Edit Permissions -> + klicken -> Gruppen hinzufüfen.

#### 3 - Sharing access configuration
>Gibt es nicht mehr 

* Bei Services -> File Sharing ein paar Ordner hinzufügen
* alles einstellen -> On-Button

## 5 - Making OS X Server a Time Machine Destination for Clients
#### 1 - Time Machine service
> Gibt es nicht mehr

1. Finder -> Ordner für Backup erstellen
2. OS X Server -> Time Machine -> bei Backup Dest + klicken -> den Ordner auswählen -> Create
Tipp: man sollte nicht das Boot-Laufwerk lieber NW-Laufwerk.
* Man kann mehrere Destinations auswählen.
3. bei Permissons auswählen, welche User backupen dürfen

#### 2 - Client Time Machine management
* System Einstellungen -> Time Machine -> Volume auswählen -> eventuell den Ordner System und alle System-Ordner ausschließen.
* oben in der Leiste sollte Backup-Symbol auftauchen, der Info zu Backups liefert.

#### 3 - Time Machine destinations
* Time Machine -> Backups
* Alert -> Delivery -> Email eintragen -> bei Delivery Settins entsprechende Häckchen setzen.
* Time Machine arbeitet nur mit `afp`.

## 6 - Caching iCloud Data, and Apple Updates
#### 1 - OS X Server caching server
> gibt es nicht mehr

* Services -> Caching
* Cache Size einstellen.
* Performance steigern

#### 2 - Using a caching server on complex networks
* Services -> Caching
* Edit permissions -> Only some networks mit + Subnetze erstellen
* Bei Server clients with public address -> die Public IP einstellen. -> unte Client Configuration -> DNS-Typ auswählen 
* Cache für personale Daten ausmachen:
    * `sudo -s`
    * `serveradmin settings caching: AllowPersonalCaching = no`
    * `serveradmin settings caching` - Caching-Einstellungen anzeigen
#### 3 - 5.2 Sierra update
* Edit peering Permissions - wenn mehrere OS X Server den Cache verwenden sollen (synchronisieren)

#### 4 - Reports in Sierra
* schauen, ob schon Caching-Server im NW installiert sind.
* im Terminal
    * `AssetCacheLocatorUtil`

## 7 - Learning to Be a Mail Server Admin with OS X Server
#### 1 - Mail server administration
> gibt es nicht mehr
* Domain -> + -> testdomain.net eintragen
* Mitglieder -> + -> Mitglieder eintragen
* Aliases erstellen: Mitglieder -> + Mitglied zweites Mal aufnehmen -> Email zu Email-Alias korrigieren.
* Gruppen kann man auch hinzufügen. -> Create
#### 2 - Mail server authentication types explained 
* Zertifikate -> Custom -> Mail (IMAP und POP) (am besten richtiges Zertifikat besorgen) auswählen
* Mail -> Authentikation -> Edit Athentikation -> Custom -> Häkchen bei Digest und Digest-MD5 (anderen sind nicht so sicher) ->  
#### 3 - SpamAssasin, Spamhaus und SMTP relay
* Virus and Junk Filtering -> (Tipp lieber Drittanbieter dafür benutzen) -> Häkchen setzen -> 
* Mail Relay -> beim Email-Anbieter nach smtp fragen und hier eintragen.
* 

## 8 Using the Profile Manager
#### 1 - Profile Manager mobile device management (MDM) setup
* Profile Manger ist Apple-MDM-Lösung.
* Device Management -> Configure -> Direktory Administrator erstellen -> Firmennamen und Firmenemail eintragen -> Adresse und Telefon eintragen -> Zertifikat auswählen -> apple-ID für Push Notifications eintragen (sollte Organisations-Apple-ID). 
#### 2 - DEP und VPP integration with Profile Manager
* DEP - Geräte, die man hier eintragen sind müssen vom speziellen Apple-Retailer oder direkt von Apple stammen:
---
* in Browser-Profile-Manager kann man eigene DEPs erstellen:
    * unten auf + klicken -> Namen geben (Test MDM) -> Downloaden. Jedes Gerät, dass dieses Profil herunterlädt, wird in MDM eingetragen
    * oben rechts klicken -> Download Trust Profile und installieren. 
* offizielles Apple-DEP - sich bei deploy.apple.com registrieren.

* VPP: 
    * VPP anhaken -> sich in Bussines Apple anmelden und Token holen -> 

#### 3 - Zero-touch configuration for IT

#### 4 - Creating configuration profiles

#### 5 - Managed distribution of apps

#### 6 - Zero-touch configuration and managed distribution results

#### 7 - Managed distribution of books still requires Apple IDs

#### 8 - 5.2 Sierra updates

#### 9 - Certificate payloads in 5.2 Sierra

#### 10 - Firewall payloads in 5.2 Sierra

#### 11 - Mac payload restrictions in 5.2 Sierra

#### 12 - iOS payloads restrictions in 5.2 Sierra

#### 13 - iOS Wi-Fi payloads changes in 5.2 Sierra

#### 14 - Configure iPad sharing in 5.2 Sierra

#### 15 - Classroom app configuration in 5.2 Sierra

## 9 - Collaboration and Communication 
#### 1 - CalDAV and CardDAV service configuration

#### 2 - Website server setup and testing

#### 3 - Wiki server: OS X Servers' hidden gem

#### 4 - Jabber server with XMPP configuration for messages service

#### 5 - El Capitan and iOS 9 configuraion for services 

#### 6 - iOS collaboration setup

#### 7 - El Capitan collaboration setup and comparison

## 10 - Review and Lockdown 

#### 1 - OS X Server security

#### 2 - OS X Server SSL explained

#### 3 - Performance mode enabled on OS X Server for El Capitan

#### 4 - Backup OS X Server for El Capitan