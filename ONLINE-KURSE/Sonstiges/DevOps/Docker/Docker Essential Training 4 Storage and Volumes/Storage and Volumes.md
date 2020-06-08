### 0 - Intoduction
#### 1 - Settin up your environment
* Drei VMs mit Docker installieren
* 
### 1 - Understanding Docker Storage
#### 1 - Docker storage overview
* in einem Container sollte nur eine App laufen
* App-Daten sollten nicht im Container bleiben, da wenn Container gelöscht => geht alles verloren => Optionen:
    1. Volumes (Docker Volumes) in */var/lib/docker/volumes* (es gibt bestimmten Bereich auf dem Host für Volumes/Daten) 
    2. Bind Mounts (hat Zugriff auf bestimmte Daten auf dem Host) 
    3. tmpfs mounts (nur Linux) (speichert Daten in Memory)
* beste Option ist Volumes
#### 2 - Compare object storage solutions
* Storages:
    1. Block - in Datenblocken gespeichert (Standard in OS)
    2. Object - Daten haben Metadaten + eine ID, Scalability ist limmetless, Daten kann man per REST erreichen
#### 3 - Analyze Docker's layered storage
* Docker benutzt StorageDrivers um Inahlt von Images zu verwalten. Jede Driver managet die Daten etwas anders. 
* `docker history image-name` -> Zeile mit `<missing>` => der Befehl wurde nicht auf diesem Rechner ausgeführt
### 2 - Configuring Docker Storage
#### 1 - Storage driver options and use cases
* man sollte nicht Container Writer Layer schreiben => lieber in Docker Volume.
* damit man in den Container Writer Layer schreiben kann, braucht man Storage Driver
* Docker empfielt `overlay2` oder `overlay` - Driver zu benutzen (Docker storage drivers - Doku). Weiterer Driver `devicemapper`. In der Doku steht Empfehlung für unterschiedliche OSes + Filesystem.
* Wenn man Storage Driver ändern => hat man keinen Zugriff für laufende Container
#### 2 - Change storage driver
* `docker info | more` -> bei Storage Driver schauen
* in der Docker-Doku -> Storage -> zum richtigen Storage Driver gehen
    * steht auch wie man den Driver ändert
* Bps:
    * `sudo systemctl stop docker`
    * `sudo cp -au /var/lib/docker $HOME/lala` - Backup
    * `nano /etc/docker/daemon.json` - per Default, man kann keinen Storage-Driver
        * Json mit `"storage-driver":"overlay"` einfügen
    * `sudo systemctl start docker`
#### 3 - Device mapper
* ist Alternative zum *overlay storage driver*
* in der Doku nach Device Mapper schauen
* arbeitet auf dem Block-Level - er kann dann z.B angeschlossene HW managen => bessere Performance 
#### 4 - Configure device mapper
* Bsp: Ubuntu (eigentlich wird nicht von Ubuntu nicht unterstützt)
    * `systemctl stop docker`
    * `nano /etc/docker/daemon.json`
        * einfügen `"storage-driver": "devicemapper"`
    * `systemclt start docker`
* dabei verliert man Zugriff zu den bereits existierenden Images
* `docker info | grep Storage`
* man muss dann aber noch z.B `direct-lvm`-Mode konfigurieren
#### 5 - Docker volumes
* Docker-Doku -> Volumes
    1. create
    2. ls
    3. inspect
    4. rm 
    5. run (--volume, -v)
    6. service mit Volumes
    7. 
#### 6 - Configure Docker volumes
* `docker volume ls`
* `docker volume` - help
* `docker volume inspect volume-name | more`
    * `Mountpoint` = wo es gespeichert ist
* `docker container run --mount source=newvolumename, target=/app image-name`
* `docker container run -d --mount source=newvolumename, target=/app image-name` -d für als Deamon
* `docker container run -d --mount source=newvolumename, target=/app image-name2`
#### 7 - Docker bind mounts
* Mounten genau os wie normale Volume
+ ist nicht so mächtig wie `volumes`
* sollte wirklich auf dem Host existieren
#### 8 - Configure Docker bind mounts
`docker container run -d --mount type=bind, source=pfad/zum/ordern, target=/app image-name`
#### 9 - Configure Docker cluster storage
* man kann die volumes auch ohne Docker Volume driver zwischen den Containern verteilen
* Docker - Volume-Plugins - Optionen in der Doku
* Volumes zwischen verschiedenen Docker-Hosts und Docker-Nodes vertielen -> meisten mit Docker-Plugins
#### 10 - Clean up unused Docker Images
+ um z.B Speicher zu leeren
* docker xxx prune.
    * image
        * image --filter...
    * volume
        * volume --fitler...
    * system -> ??
* <- Doku dafür checken
* `docker image prune`
* `docker system prune`

