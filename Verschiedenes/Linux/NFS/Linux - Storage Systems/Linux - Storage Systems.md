### 3 - Network File Systems
#### 1 - Network File System (NFS)
* FS Issues
    * Security (Verschlüsselung)
    * Performance
    * Locking (Schreiben/lesen gleichzeitig)
* NFS - Unix NW-Filesystems
    * z.B Home-Directory mounten
    * man muss auf UID aufpassen
    * Rechner-Permissions
CIFS - Linux braucht vifs-utils
    * `mount -t cifs`
    * um Windows-Server zu mounten 
    * hat User-Permissions
* Samba für Linux
* Bsp NFS:
    * `cat /etc/exports` -> Ausgabe `/tmp/shared *(rw, no_root_squash)
    * `watch -n1 cat /tmp/shared/file.txt` - `-n1` - jede Sekunde Datei caten
    * `mount | ls grep Netzwerk-Ordner` -> Ausgabe:
        `/tmp/shared on /tmp/sdr1 type nfs4 (rw,relatime,vers=4.0,rsize=1048576, wsize=1048576,namlen=255, hard,proto=tcp6,port=0,time0=600,retrans=2,sec=sys,clientaddr=::1,local_lock=none,addr=::1) 
#### 2 - Distributed file systems
* auf mehreren Servers, aber errschient auf dem Client als ein einzelnes FS
* => Redundancy, bessere Performance
* Bsp:
    * OpenAFS
    * GlusterFS -> man8 glusterfs
        * `rpm -qa | grep gluster | more` - schauen, welche Gluster-Pakate installiert sind
        * `yum list 2 > /dev/null | grep gluster|wc -l` - sagt, wieviele Packete den Namne gluser enthalten
        * `rpm -qf 'which gluster'` - sagt wie der gluster-Packet heißt
        * `which gluster`
        * `rpm -qf 'which mount.glusterfs'` - ist Fuse-Based FileSystem
        * `rpm -qf 'locate gluster.service'`  sagt, welches Packet Gluster-Daemon hat
#### 3 - Cluster file systems
* Bsp:
    * GFS2 - kommt mit Linux - gfs2(5) (man 5 für gfs2); unterstützt fsck, mounting, etc
    * OCFS - Oracle Cluster File System, braucht Oracle-Linux 
    * CLVM - Cluster Logical Volume Manager (kommt mit lvm2-cluster RPM). clm-Deamon läuft auf allen Nodes, die Deamons unterhalten sich untereinadner
* Packete:
    * gfs2:
        * `locate gfs.ko` - Kernelmodule mit gfs auflisten
        * `rpm -qf 'locate gfs2.ko'` - welches Packet hat gfs2.ko
        * `rpm -qf 'which mkfs.gfs2'` - Packet das ;make-Utilities für gfs2 hat
        * `rpm -ql gfs2-utils` - welche Utilities gfs2 hat
    * clvm:
        * `rmp -qf 'which clmvd'`
        * `rpm -ql lvm2-cluster | more'` - aus welchen Programmen besteht lvm-cluster

#### 4 - SSHFS file system
* ist Fuse-based
* not priviliged
* Communikation ist über SSH
* man kann UUID mappen `man sshfs`
    * `sshfs [user@host:[serverdir] mountpoint [options]]`
    * Verbindung ist kann aber abbrechen, wenn man lange nichts macht
    * Bsp:
        * `sshfs guest@server1: bhome`
        * Password eingeben
        * `fusermount -u bhome` - unmounten
#### 5 + 6 - Challenge: NFS bahavior and SSHFS
* NFS Sync machen:
    * /tmp/shared *(rw,no_root_squash,sync)
    * NFS restarten
SSHFS:
    * `time csp guest@server1:lala.iso /tmp` - über csp kopieren, damit wird die Zeit angezeigt
    * `sshfc guest@server1: bhome`
    * `cd bhome`
    * `time cp lala.iso /tmp`