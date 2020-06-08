### 1 - Backup and Restore
#### 1 - Back up with Time Machine
* man kann jetzt auch auf `smb` backupen
* man kann zwei Festplatten zum Backupen verwenden.
* Options - Sachen vom Backup ausnehmen, z.B google Drive usw. Wenn man Systemsachen ausschließen will, dann einfach Macintosh HD\System ausschließen. 

#### 2 - Back up with Blackblaze
> \- Online Backup
* von backblaze-Seite die SW herunterladen, Account erstellen und installieren.
* in Systemeinstellungen wird Backblaze auftauchen
* Backup einrichten (Settings)
#### 3 - Time Machine file restore
* Rechstsklick oder CTRL halten auf Laufwerk bei Timemachine - kann man auswählen, ob jetzt gebackupt werden soll, die Backups verifizieren.
* in der oberen Leiste auf Time Machine (rechts)klicken, wird ein Menü angezeigt. Wenn man während dessen OPT klickt, werden weitere Optionen angezeigt.
WIEDERHERSTELLUNG:
* Time Machine öffnen (nicht über Systemeinstellungen)
* kommische Fenster sind Sicherungen, man kann darin scrollen
* Die Dateien wählen, die man wiederherstellen möchte

> Qickview - Datei auswählen -> SPACE klicken.

#### 4 - Backblaze file resore
* über Systemsteuerung Backblaze aufmachen
* auf den Link unten klicken -> sich anmelden
* View/Restore Files -> nötige auswählen
* per Mail wird Downloadlink kommen


### 2 - iCloud Administration
#### 1 - iCloud Drive destop and documents
* Systemeinstellungen -> iCloud -> sich anmelden
* auf dem anderem Rechner das gleiche machen
* Wenn man sich mit dem gleichen Account auf zwei Rechnern anmeldet und der erste Rechner wurde noch nicht synchronisiert, dann wird ander Vorgang initiiert, es wird gefragt, ob man iCloud Drive nutzen möchte
* beim Hauptrechner iCloud Drive auswählen und anhacken **Desktop und Dokument**, so wird Desktop und Dokumente in iCloud gespeichert.
* auf dem zweiten Rechner iCloud Drive auswählen und wieder **Desktop und Dokuemte** anhacken
* als Ergebnis wird auf jeweiligem Desktop ein neuer Ordner mit Namen **Dekstop von XXX Computer** angelegt, da keine vollständige Synchronisierung stattgefunden hat.
* Prozess **bird** wird dann viel CPU verbrauchen, da viel hin- und her geschoben werden soll. 

* Fazit: zuerst einen Rechner komplett synchronisieren, dann den anderen aufräumen und synchronisieren.
#### 2 - iCloud deletion recovery
* Option **Optimiesiere Mac Storage** - lädt Datein aus iCloud nicht vollständig.
* über diesen Mac -> Storage -> Manage... -> 
* wenn iCloud -> Desktop und Dokumente an sind, dann werden sie nicht mehr lokal auf dem Rechner gespeichert, Zugriff nur über iCloud möglich
* über iCloud (Safari) kann man dann gelöschte lokal gelöschte Dateien wiederherstellen (lokal gelöschte Dateien, werden noch 30 Tage in iCloud gehalten)
#### 3 - Getting out of iCloud
* wenn man iCloud Drive ausmacht. Es wird alles gelöscht auf lokalem Rechner, aber diese Dateien sind noch in iCloud
#### 4 - Disable iCloud with MDM restrictions
* in OS X Server auf Profilmanager gehen -> Rechner auswählen -> Bearbeiten -> in macOS Section zu Restriction gehen -> Tab Functionality -> bestimmte iCloud Sachen unchecken = verbieten

### 3 - Working with Storage
#### 1 - Storage tools in macOS
#### 2 - Disk image tricks
#### 4 - RAID with Disk Utility reborn
#### 5 - Defragmenting the user space

### 4 - Apple File System
#### 1 - Introduction to APFS
#### 2 - Convert HFS to APFS
#### 3 - Create an APFS disk image
#### 4 - Create an APFS container and volume
#### 5 - Running a file system check

### 5 - New Console
#### 1 - The unified logging system
#### 2 - Reading logs and activities
#### 3 - Message labels and organization
#### 4 - Console actions
#### 5 - Searching through logs
#### 6 - Viewing connected device logs

### 6 - New Log Command
#### 1 - Overview of the log command
#### 2 - Using predicates to search logs
#### 3 - Log stream levels and debug logging
#### 4 - Using log show
#### 5 - Collection logs with log collect

### 7 - Security
#### 1 - Install a self-signed certificate
#### 2 - Sierra's update Gatekeeper
#### 3 - Troubleshooting Keychain password errors
#### 4 - Get an enterprise FileVault recovery key
#### 5 - Enterprise FileVault setup
#### 6 - Enterprise FileVault implementaion
#### 7 - MDM-based FileVault 2 deployment

### 8 - Security
#### 1 - Why MDM
#### 2 - Why not image
#### 3 - Enroll without DEP
#### 4 - Configure Time Machine via MDM
#### 5 - Configure Wi-Fi settings with profiles
#### 6 - VPN options available via MDM
#### 7 - Installing applications on Macs via MDM
#### 8 - Configure a MacOS firewall via MDM
#### 9 - Configure enterprise printing with MDM