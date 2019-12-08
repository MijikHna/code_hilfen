### 10 - NFS Services
#### 1 - NFS services Intorduction
#### 2 - Install NFS and configure NFS Services
* `sudo yum install -y nfs-utils`
* `rpm -ql nfs-utils` - was ist in dem Packet
* `nfs` und `nfs4` sind für NFS-Exports
* `exportfs` `mountstats` und `nfsstat` - Info zu Mounts
* `sudo yum install -y nfs4-acl-tools` 
+ `rmp -ql nfs4-acl-tools`
* `nfs4_edit...`, `nfs4_get...` und `nfs4_set...` - Tools zum Editieren von NFS4
* 
#### 3 - Manage SELinux for NFS services
* `sudo systemctl start nfs-server`
* `sudo systemctl enable nfs-server`
* `ps -eZ | egrap 'nfs|rpc'` -
* `ls -lZ /etc/exports` - 
* `getsebool -a | grep nfs`
* ` - booleand in NFS-Policies anschauen
    * `nfs_export_all_ro/rw` - sollten an sein
#### 4 - Provide network shares to specific clients
* `sudo mkdir /home/usershare`
* `ls -lZ /home` - zeigt Rechte + NFS-Rechte für die Ordner in /home
* `sudo setsebool -P nfs_export_all_ro on`
`sudo setsebool -P nfs_export_all_rw on`
* `getsebool -a | grep nfs_export`
* `sudo firewall-cmd --permanent --add-service nfs` - NFS zu Firewall hinzufügen
* `sudo firewall-cmd reload` - Firewall neustarten
* `sudo systemctl start nfs-server`
* WEnn man NFS3 benutzt muss man auch RPC-Bind starten
* `sudo vi /etc/exports`
    * `/home/usershare rhhost2(rw)`
* `sudo exprots -avr` - Exports freigeben
* `cat /var/lib/nfs/etab` - Export ansehen
* `grep annoid /etc/passwd`
* `sudo chown user1:user /home/usershare` - damit der User auch schreiben kann
#### 5 - Moint a simple NFS share
* `sudo mkdir /home/usermount`
* `sudo mount -t nfs rhhost1:/home/usershare /home/usermount`
* `mount`
* Troubleshouting:
    * Name Resolution (/etc/hosts auf beiden checken)
    * checken, ob nfs-server läuft
    * `showmount -e rhhost1` - checkn, ob Export für den User1 sichtbar ist
    * Firewall checken
        * `sudo systemctl stop firewalld`
#### 6 - Create an NFS share for group collaboration
* `sudo mkdir /home/groupshare`
* `sudo useradd user2`
* `cat /etc/psswd`
* `groupadd -g 6000 groupcolab`
* `sudo usermod -aG groupcollab user1`
`sudo usermod -aG groupcollab user2`
* `sudo chown nfsnobody:groupcolab /home/groupshare`
* `sudo chmod 2770 /home/groupshare` - SGID-Bit setzen
    * `ls -ld /home/groupshare`
* `sudo setsebool -P nfs_export_all_ro on`
`sudo setsebool -P nfs_export_all_rw on`
* `sudo firewall-cmd --permanent --add-service nfs`
* `sudo firewall-cmd --reload`
* `sudo systemctl start nfs-server`
* `sudo systemctl enable nfs-server`
* `sudo vi /etc/exports`
    * `/home/groupshare rhhost2(rw,no_root_squash)`
* `sudo exportfs -avr`
#### 7 - Mount an NFS share for group collaboration
* `sudo mkdir /home/groupmount`
* `sudo useradd user2`
* `cat /etc/psswd` - checken, dass die uid wie auf host2 ist
* `sudo passwd user2`
* `sudo groupadd -g 6000 groupcolab`
* `sudo usermod -aG groupcolab user1/user2`
* `cat /etc/groups`
* `sudo mound -t nfs rhhost1:/home/groupshare /home/groupmount`
* Test - mit den Usern Dateien auf dem Mount erstellen
#### 8 - Challenge: NFS share for group collaboration
* Augabe:
    1. rhhost1 hat shared Dir /var/nfsshare
    2. rhhost2 mountet diese automatisch on boot als /home/nfscollab
    3. andere hosts können nicht mounten
    4. andere hosts andere shares von rrhost1 mounten
    5. drei user haben read+write, keine andere User haben zugriff
* Lösung:
    * rhhost1:
        1. `sudo mkdir /var/nfshare`
        2. `sudo useradd bob`
        3. `sudo useradd ted`
        4. `sudo useradd sally`
        5. `sudo passwd bob/tes/sally`
        6. `cat /etc/passwd` - uid aufschreiben
        7. `sudo groupadd -g 6000 nfsgroup`
        8. `sudo usermod -aG nfsgroup bob/ted/sally`
        9. `sudo chown nfsnobody:nfsgroup /var/nfsshare`
        10. `sudo chmod 2770 /var/nfsshare`
        11. `sudo setsebool -P nfs_export_all_ro on`
        12. `sudo setsebool -P nfs_export_all_rw on`
        13. `sudo firewall-cmd --permanent --add-service nfs`
        14. `sudo firewall-cmd --reload`
        15. `sudo systemctl start nfs-server`
        16. `sudo systemctl enable nfs-server`
        17. `vi /etc/exports`
            1. `/var/nfsshare rhhost2(rw,no_root_squash)`
        18. `sudo exportfs -avr`
    * rhhost2:
        1. `sudo mkdir /home/nfscollab`
        2. `sudo useradd -u 1002 bob`
        3. `sudo useradd -u 1003 ted`
        4. `sudo useradd -u 1004 sally`
        5. `sudo passwd bob/ted/sally`
        6. `sudo groupadd -g 600 nfsgroup`
        7. `sudo groupadd -aG nfsgroup bob/ted/sally
        8. `sudo vi /etc/fstab`
            1. `rhhost1:/var/nfsshare   /homenfscollab  nfs4    defaults    0 0`
        9. `sudo mount -a`
        10. Testen - sich mit usern anmelden und Dateien erstellen

### SMB Services:
#### 1 - SMB services Introduction
#### 2 - Install and configure Samba services
* `sudo yum -y install samba samba-client` - Server + Cleint installieren
* `rpm -aq | egrep 'smb|samba|cifs'`
    * beide auf allen Rehnern
* eventuell nfs-Share in /etc/exportfs auskommentieren
#### 3 - Manage SELinux for SMB services
* rhhost1:
    * `sudo vi /etc/smb/smb.conf.example`
        * `setsebool -P samba_enable_home_dirs on` auskommentieren
        * `setsebool -P samba_domain_controller on` 
        * `chcon -t samba_share_t /path/to/directory`
        * um Scripts bei Events laufen zu lassen, mus man sie in /var/lib/samba/scripts kopieren
    * `getsebool -a | egrep 'smb|samba|cifs'`
    * `samba_share_nfs --> on` - Samba und NFS könen den gleichen Ordner freigeben
#### 4 - Samba global configration options
* globale Optionen:
    1. workgroup
    2. server name
    3. netbios name
    4. interfaces (falls man mehrere hat)
    5. hosts allow/deny
    6. log file
        * `log file = %m.log` - Log per Host
        * `log file = %S.log` -Log per Share
    7. max log size
    8. log level
* Security-Modes:
    * `security = ads` - Kerberos benutzen
    * `security = domain` - Authent gegen NT4, PDC oder BDC
    * `security = user` - Authentikatio zu lokalen user-DB -> drei DBs:
        1. smbpasswd - /var/lib/samba/private/smbpasswd
        2. tdbsam - locale DB in /var/lib/samba - Default
        3. ldapsam - remote LDAP-Accounts
#### 5 - Samba share configuration definitions
* Config Options:
    * `comment` - Beschreibung des Shares
    * `browsable` - Share Visible to Cleint
    * `writable` - Beschreibbarer Share
    * `valid user` - User die Zugrif haben
    * `write user` - User die Schreiben dürfen
    * `path` 
    * `public` - User hat Zugriff ohne Password
    * `guest only` 
    * `force group` - ??
    * `create mask` - ???
* man-page für smb.conf checken
#### 6 - Provide network shares to specific clients
* rhhost1:
    * `sudo mkdir /home/smbprivate`
    * `sudo chown user1:user1 /home/smbprivate`
    * `sudo chmod 775 /home/sambaprivate`
    * `sudo semanage fcontext -at public_content_rw "/home/sambaprivate(/.*)?"` - SELinux 
    * `sudo restorecon /home/sambaprivate`
    * `sudo vi /etc/samba/smb.conf`
        * [sambaprivate]
            * comment = Private Samba available to user1
            * path = /home/sambaprivate
            * valid users = user1
            * write list = user1
            * public = yes
    * `testparm` - Configuraton testen
    * `sudo smbpasswd -a user1` - Password für smb für user1 setzen
    * `sudo pdbedit` - Einstellungen für User1 checken
    * `sudo systemctl restart smb`
    * `smbclient -NL //localhost` - zeigt Info über Samba-Server
* rhhost2:
    * `smbclient //rhhost1/sambaprivate` -> Password eingeben. Wenn es möglich war sich einzulogen, dann funktioniert Samba
    * `sudo mkdir /home/sambaprivate`
    * `sudo mount -t cifs -o usrname=user1 //rhhost1/sambaprivate /home/sambaprivate`
    * `df`
#### 7 - Automount using a credentials file
* rhhost2:
    * `sudo vi /root/sambaprivate.cred`
        * 
        ```
        username=user1
        password=user1
        ```
    * `sudo vi 7etc/fstab`
    * `//rhhost1/sambaprivate /home/sambaprivate cifs credentials=/root/sambaprivate.cred 0 0`
    * `sudo mount -a`
#### 8 - Provide network shares suitable for group collaboration
#### 9 - Mount a share for group collaboration
#### 10 - SMB:Share for group collaboration