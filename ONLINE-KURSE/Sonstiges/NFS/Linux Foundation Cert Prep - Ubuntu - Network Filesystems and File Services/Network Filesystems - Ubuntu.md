### 1 - Samba (SMB/CIFS)
#### 1 - What is SMB?
* SMB - Server Message Block
    * benutzt lokale Benutzer, braucht aber smb-Password
* CIFS - Common Internat File System (alte SMB)
#### 2 - Configuration an SMB Server
* `apt install samba`
* `mkdir /srv/smbhshare`
* `touch /srv/smbshare/file{1..10}`
* `nano /etc/samba/smb.conf`
    * 
    ```
    [files]
    comment = "Shared File to the team"
    browseable = yes
    path = /srv/smbshare
    ``` 
* `testparm` - Config Testen
* `systemctl restart smbd`
* `smbpasswd -a user1` - user1 sollte auf dem Rechner installiert sein
#### 3 - Configuration an SMB client
+ `apt install cifs-utils`
* `mkdir /mnt/sharedfiles`
* `mount //10.0.1.10/files /mnt/sharedfiles -o username=user1,password=passwd`
* in /etc/fstab
    * `//10.0.1.10/files /mnt/sharedfiles cifs username=user1,password=pass(,etc.) 0 0`
#### 4 - SMB server settings
* in smb.cnf
    * [global] - gelten für alle Shares
    * [homes] - Platzhalter für User home Shares
    * [printers] 
    * [myshare] - eigene Shares
    * path=/srv/files
    * read only = yes
    * guest ok = yes
    * create mask = 0770
    * directory mask = 0700 - ??
    * force user=username -??
    * hosts allow=10.0.2.0/255.255.255.0
* Client
    * mit `-o`
    * `man mount.cifs`
    * `smbclient -L` - Shares untersuchen 

### 2 - Network File System (NFS)
#### 1 - What is NFS?
* NFS werden für Host bereitgestellt. Alles andere übernimmt Filesystem, d.h. user-uid und Rechte usw. müssen stimmen. Man kann uid auch ignorieren
#### 2 - Configuring an NFS server
* `apt isntall nfs-kernel-server`
* `mkdir /srv/shared`
* `touch /srv/shared/file{1..10}`
* `nano /etc/exports`
    * `/srv/shared  10.0.2.0/24(rw,root_squash)` - zwischen /24 und () darf kein _ sein.
* root_squash:
    * heißt: Client UID = Server UID
    * root_squash = wenn root-UID den Share mounten wird er als *nobody* behandelt
    * all_squash - alle wie nobody
    * no_root_squash - ist default
* `epxortfs`
* `systemctl status nfs-server`
#### 3 - Configuring an NFS client
* `apt isntall nfs-common`
* `mkdir /mnt/shared`
* `mount 10.1.1.10:/srv/shared /mnt/shared`
* `ls -l /mnt/shared`
* `nfsstat -mounts` - Info zu NFS-Mounts
* `/etc/fstab`
    * `10.1.1.10:/srv/shared /mnt/shared nfs4 defaults 0 0`
#### 4 - NFS server settings
* NFS Defaults
* /etc/exports:
    * (rw)
    * (sync/async) - gechached/ungecached
    * (all_squash) - alle wie nobody
    * (anonoud=uid/anongid=gid) - ?
* NFS Client - Optoins
    * Timeouts
    * performance Options
    * <- man-Seite checken