### 0 - Introduction
#### 3 - OS installation
#### 4 - Lab setup
#### 5 - Configure VM settings
#### 6 - Install Guest Additions

### 1 - Introduction to Network File System
#### 1 - Introduction to NFS
* ist Filesystem Protocol - erlaubt Remote Access
* benutzt UDP
#### 2 - NFS versions
* ab Version 3.2 kann auch TCP
* unterstütz ACL
#### 3 - NFS security
#### 4 - Install NFS packages
* `sudo yum install -y nfs-utils`  
* `rpm -ql nfs-utils` - schauen, was ist in derm Paket
    * `/sbin/mount.nfs` und `/sbin/mount.nfs4` - sind nfs-Export-Commands
    * `/usr/sbin/nfstat`, `/usr/sinb/exportsfs` und `/usr/sbin/mountstats` - Info über nfs-Exports/-Mounts
* `sudo yum install -y nfs4-acl-tools` - für NFS-ACLs
### 2 - NFS Server Configuration
#### 1 - NFS commands
* `exportfs`- Filesystem für Export bereitstellen
    * `exportfs server:/data` - bestimmtes Filesystem exportieren
    * `exportfs -a` - alles exportieren, was in /etc/exports und /etc/exports.d steht
* `mount` - NFS-Filesystem am Client mounten
    * Optionen:
        * nfsvers - NFS-Version festlegen
        * noacl - keine ACLs
        * noexec - 
        * nusuid
        * port
        * rsize und wsize
        * sec=mode - Kerberos Modus
        * tcp/udp - TCP besser
* `nfsiostat` - Stats zu NFS-Mounts
* `nfstat` - NFS und RPC Stats
* `mountstats` - Per Mount Stats
#### 2 - NFS files
+ in */etc/exports* stehen Share-Definitions
* /etc/export.d/*exports - Directory of Share-Definitions
* */var/lib/nfs/etab* - Liste der verfügbaren Shares
* */etc/nfsmount.conf* - Client-Config-Datei für Mounts
* */etc/fstab* - Liste aller Typen der Mounts
* */etc/mtab* - Tabele mit gemounteten Drives
* */etc/sysconfig/nfs* - Server und Client Startup Config File
#### 3 - About the exportfs file
* zu */etc/exports*
    * ein Export pro Zeile
    * Exportierten Hosts Identifizierer mit Leerzeichen trennen
    * Format für den Export:
        * `export host1(options) host2(options) host3(options)`
        * Bsp:
            * `/ rhhost1(rw) rhhost2(rw)` - ganzen Rechner exportieren
            * `/project rhhost*.localnet.com(rw)` - Wildcard-Bsp
            * `/usr *.localhost.com(ro) @trusted(rw)` - alle Rechenr in lcoalhost.com und alle in trusted
            * `/home/user1 hrhost1(rw,all_squash,anonuid=150)` - für User mit UID=150
            * `pub *(ro,insecure,all_squash)` - für alle Hosts in der Welt
            * `/var/www -sync,rw server @trusted @exteranl(ro)` - exportier für den Rechener *server* + trusted-NetGruppe + external-NetGruppe
            * `/data 2001::/64(rw) 192.0.1.0/24(rw)` 
            * `/build buildhost[0-9].localnet.com(rw)` - Wildcard-Bsp
#### 4 - NFS and SELinux
* `sudo systemctl start nfs-server`
* `ps -eZ | egrep 'nfs|rpc'`
* `ls -lZ /etc/exports`
* `getsebool -a | grep nfs` - SELinxu-Boolen für NFS anschauen
#### 5 - Create a simple NFS share
* `sudo mkdir /home/usershare`
* `ls -lZ /home` - Besitz + Rechte checken
* `sudo setsebool -P nfs_export_all_ro on` und `sudo setsebool -P nfs_export_all_rw on`- SELinux-Boolens seten
    * `getsebool -a | grep nfs_export` - die gesetzten SELinux-Bools checken
* `sudo firewall-cmd --permanent --add-service nfs` und `sudo firewall-cmd --reload` - Firewall-Regeln für NFS setzen
* `sudo systemctl start nfs-server`
* `sudo systemclt enable nfs-server`
* Wenn man NFS3 benutzt => muss man noch bind starten
* /etc/exports aufmachen
    * `/home/usershare rhhost2(rw)`
    * `sudo exportfs -avr` - sollte Ausgabe mit *exporting ..* kommen
    * `cat /var/lib/nfs/etab` - Exports checken -> es sollte bei anonuid=65534 und anongid=65534 stehen
    * `grep 65534 /etc/passwd` - zeigt wemm die uid 65534 gehört, sollte nfsnobody sein
    * `sudo chown user1:user1 /home/usershare` - Besitz an den Richtigen User übertragen
### 3 - NFS Client Usage
#### 1 - Mount a simple NFS share
* `sudo mkdir /home/usrmount`
* `sudo mount -t nfs rhhost1:/home/usershare /home/usrmoung` 
* `mount` - zeigt, ob wirklich gemountet wurde
* Falls nicht gemountet wurde, 
    + checken die /etc/hosts-Datei, dass die Hostnamen richtig aufgelöst sind
    * checken, ob nfs-server ist gestartet
    * `showmount -e rhhost1` um zu schauen, dass der Export sichtbar ist 
    * Firewall checken
    * 
#### 2 - NFS client options
* *hard/soft*
* *retrans*
* *rsize/wsize*
* *ac*
* *fg/bg*
* *Retry*
* *sec=mode*
* *async/sync*
* *_netdev*
* *nfsvers*
* *remount*
* *rw/ro*
* *suid/nosuid*
* *auto/noauto*
* *exec/noexec*
* *defaults*
#### 3 - Mount NFS exports
* `sudo mount -t nfs -o nfsvers=4.2 rhhost1:/home/usershare /home/usrmoung` - mit Client-Optionen
* `sudo mount -t nfs -o nfsvers=4.2 rhhost1:/home/usershare /home/usrmoung`
* über fstab:
    * `rhhost1:/home/usershare /home/usrmoung nfs nfsvers=4,nosuid,nouser,_netdev 0 0`
#### 4 - Delayed mounting with autofs
* `sudo yum install -y autofs`
* aus fstab den NFS-mount rausnehmen
* /etc/auto.master bearbeiten
    + hinzufügen: `/-   /etc/auto.direct` - sagt autofs in /etc/auto.direct nach den Mounts zu schauen
* /etc/auto.direct erstellen
    *  hinzufügen: `/home/usermount/rhost1:/home/usershare`
* `sudo systemctl restart autofs`
* Wenn man jetzt versucht in die Direktory zu navigieren, wird es gemountet. Nach 5 Minuten wieder unmounted

#### 5 - Troubleshoot NFS exports
#### 6 - Monitor NFS activity

### 4 - NFS Share Exercises
#### 1 - Create an NFS share with root access
#### 2 - Create an NFS share for group collaboration
#### 3 - Mount an NFS share for group collaboration

### 5 - Introduction to Samba
#### 1 - Introduction to Samba
#### 2 - Samba commands and services
#### 3 - Samba files
#### 4 - Install Samba packages
#### 5 - Preparing your lab for Samba

### 6 - Samba Server Configuration
#### 1 - Samba configuration file format
#### 2 - Samba global configuration options
#### 3 - Samba share configuration definitions
#### 4 - Configure SELinux for Samba
#### 5 - Create a simple public share

### 7 - Samba Client Tools
#### 1 - Use smblcient to test shares
#### 2 - CIFS mount options
#### 3 - Mount a simple public share

### 8 - Samba Sahre Exercises
#### 1 - Create a private Samba file share
#### 2 - Automation using a credentials file
#### 3 - Create a Samba share for group collaboration
#### 4 - Mount a share for group collaboration
#### 5 - Create a secure share using Kerberos