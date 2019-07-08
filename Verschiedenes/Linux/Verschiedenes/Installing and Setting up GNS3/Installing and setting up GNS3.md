### 1 - GNS3 GUI Install
# um Response Time Viewer zu isntallieren muss man email eingeben (SW ist kostenlos)

### 2 - Your first GNS3 Network
#### 1 - Basic GNS3 network
* Consolen in Windows laufen in Putty
* VPCS - einfachaes PC
    * `ip 10.1.1.1 255.255.255.0`
    * `save` - config von VPCS speichern
* GNS3 speichert nur Topologie, nicht die Configs der Devices
#### 2 - Where do i get Cisco IOS images
#### 3 - Cisco IOS network using Dynamics
* Edit -> Preferences -> Dynamips -> IOS Routers -> New -> IOS Image auswählen -> dem Router einen Namen geben -> ...

### 3 - GNS3 VM
#### 1 - GNS3 VM, VIRL, and switching
* Cisco Virtuelle Images importieren
* also GNS3 VM benutzen um VIRL Images zu laufen
* man kann also mit Dynamips (reele Cisco-OS) oder VIRL benutzen
* beste Wahl aber Qemu-Images benutzen
* über gms3.com/Marketplace kann man weitere Images benutzen
+ um GNS3 VM benutzen -> VMware benutzen (Workstation Pro oder Workstation Player) (VB nicht empfehlenswert, da VB keine Nested NW erlaubt)
#### 2 - GNS3 VM and VMware isssues
* GNS3 VM in GNS GUI integrieren:
    * WMWare herunterladen (es gabt Probleme mit VMWare 14 - Integration (12 war OK) )
#### 3 - Cisco VIRL IOSv import into GNS3
* VMWare installieren
    * GNS3 VM für VMWare herunterladen
    * GNS3 VM anklicken - Import in VMWare
        * eventuell Pfad zu VM ändern
        * Import
    * GNS3 starten
        * Prfernces -> GNS3 VM -> Engine auf VMWare setzen -> VM name die importierte VM eintragen
* GNS3 starten 
    * Router z.B Cisco ISOv - Image des Routers wird in GNS3 VM laufen -> eventuell ...config.img herunteralden, eventuell Cisco Image für IOSv herunterladen. 
    * Qemy installieren -> mit Default weitergehen
#### 4 - Cisco VIRL and Dynamimps network
* Prefernces -> Danymips -> IOS routers -> Run this IOS router on the GNS3 VM
    * eventuell -> IOS Image uploaden
    * Name ändern
    * RAM ändern
    * NW Adapter + WIC Module einstellen
* nun unter installed Appliances kann man den installierten Router sehen
