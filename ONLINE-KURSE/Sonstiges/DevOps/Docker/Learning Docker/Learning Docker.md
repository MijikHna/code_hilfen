### 0 - Introduction
#### 1 - What is Docker

### 1 - Installing Docker
#### 1 - Setting up Docker
#### 2 - Docker Toolbox
#### 3 - Install Docker on Mac
#### 4 - Install Docker on Windows
#### 5 - Install Docker on Linux

### 2 - Using Docker
#### 1 - The Docker flow: Images to containers
* TAG ist ~ Versionsnummer
* `export FORMAT="\nID\t{{.ID}}\nIMAGE\t{{.Image}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.RunningFor}}\nSTATUS\t{{.Status}}\nPORTS\t{{.Ports}}\nNAMES\t{{.Names}}\n"` - eine VARIABLE $FORMAT anlegen, die die Ausgabe in vertikaller Form ausgibt
* `docker ps --format $FORMAT`
#### 2 - The Docker flow: Containers to images
* `docker ps -l` - letzten exited Container anzeigen
* Workflow:
    1. `docker run`
    2. `docker stop` - Container noch da aber gestoppt
    3. `docker commit` - aktuellen Stand zu Image machen
        * `docker commit container-id`
        * `docker tag image-id-aus-obigem-befehl my-image1` - Image einen Namen geben
        oder 
        * `docker commit container-name my-image2`
#### 3 - Run process in containers
* Beispiele:
    * `docker run --rm -ti image-name sleep 5` - --rm = Container wird nach exit gelöscht
    * `docker run --rm -ti image-name sleep 5`
    * `docker run -ti image-name bash -c "sleep 3; echo all done"` - mit *-c* sagt man dass bash mehrere Sachen starten soll, hier *sleep* dann *echo*
    * `docker run -d -ti image-name bash` - in detached Mode starten, d.h wird nicht direkt exited
    * `docker attach container-name` - in den Container springen. (exit *STRG+P+Q)
    * `docker exec` - weiteren Prozess im Container starten z.B weiteren Service starten
        * `docker exec -ti container-bash bash` - weitere Bash im Container ausführen
#### 4 - Manage containers
* `docker logs` bzw. `docker logs container-name`  - Output des Containers, solange Container noch existiert
* Container Resources einstellen:
    * `--memory max-allowed-memory`
    * `--cpu-shares`
    * `--cpu-qoute`
* Resourecen-einstellung ist bei Multiple-Containers wichtig
#### 5 - Network between containers
* man kann private NW erstellen
* Port-Weiterleitungn + Linking
* `-p host-port:container-port/protocol(udp/tcp)` - auch Inside:Outside-Port
    * `-p 1200:12000/udp`
* `-p container-port` - Docker entscheidet selber, welcher Port des Hosts genommen wird
* `docker port container-name` - anzeigen die Port-Mapping
* `nc -lp port` - mit NetCat am Port *port* horchen
    * `nc -lp 8080`
* `nc ip port`
    * `nc 10.35.35.35. 8080`
#### 6 - Link containers
* Container unter einander verbinden
* wird überwiegent in Orchestrations (nur in eine Richtung also vom Client zum Server)
* `docker run .. --link container-name-zu-dem-verbunden-wird ..`
    * dann ist es möglich den server-Container über seinen Namen zu erreichen also:
        * `nc container-name`
    * dabei wird der Container-name in */etc/hosts* eingetragen
    * wenn aber die IP des Server-Containers geändert wird, bricht der Link zusammen 
#### 7 - Dynamic and legacy linking
* private NW erstelen
* `docker network create nw-test` - NW erstellen
* `docker run .. --net=nw-test ..` - den Container in privates NW aufnehmen
* `docker run -p 127.0.0.1:1234:1234/tcp` - sagen, Localhost:1234 des Host auf 1234 des Docker-Containers mappen, sonst nichts mappen
#### 8 - Images
* `docker commit` - tagt die Images automatisch als *latest*
* man sollte den Image folgendermaßen tagen: *Besitzer/image-name:version* oder *Organisation/image-name:version*
* `docker pull ...` - Image holen
* `docker push ...` - Image hochladen
* `docker rmi image-name/id`
#### 9 - Volumes
* Dateien zwischen Container und Containers bzw. Container und Host teilen
* Dafür werden Virtuelle Disk benutzt -> zwei Varianten
    * Persistent - auf dem Host
    * Ephemeral - wenn Container Daten nicht benutzt, wird dieses gelöscht
* Host und Container:
    * `docker run ... -v /home/ich/lala:/contaiiner-folder/folder ...`
* Container zu Container (solange da bis die Container da sind, die es benutzen)
    * `docker run ... -v /container-folder/folder .. --name container1`
    * `docker run ... --volumes-from container1 ...`
    * `docker run ... --volume-from container1/container2 ...` - also solange ein Container diesen Volumen benutzt, ist es zugänglich
#### 10 - Docker registeries
* `docker search image-name` - nach bestimmten Images suchen
ODER
* auf https://hub.docker.com suchen, hier noch Info wie man das Image benutzen kann (also Doku zu dem Image)
* `docker login`
* `docker tag image meine-docker-repo/image-name:version`
* `docker push meine-docker-repo/image-name:version`
### 3 - Building Docker Images
* kleine Programme, in denen steht, wie ein Image gebildet werden soll, dabei wird jede ausgeführte Zeile des Dockerfiles gecacht.
* `docker build -t mein-image-name:version .` - -t = dem Image einen Namen geben, . = Dockerfile ist in diesem Ordner
* Bsp1 :
* *Dockerfile* erstellen
```
FROM busybox
RUN echo "building simple docker Image" # diese Zeile wird beim Bilden ausgeführt 
CMD echo "hello container"
```
* `docker build -t test-hello` - wenn jetzt der Image ausgeführt wird, wird CMD-Zeile gestartet
* Bsp2:
* *Dockerfile* erstellen
```
FROM debian:sid
RUN apt-get -y update
RUN apt-get install nano
CMD ["/bin/nano", "/tmp/notes"]
```
* `docker build -t test/nano` - wenn jetzt der Image ausgeführt wird, wird CMD-Zeile gestartet
* Wenn man die Ausgaben verfolt, dann werden nach jeder Zeile Images erstellt, die dann gelöscht werden.
* Bsp3:
* *Dockerfile* erstellen
```
FROM test/nano
ADD test.txt /notes.txt
CMD ["/bin/nano", "/notes.txt"]
```
* `docker build -t test/nano` - wenn jetzt der Image ausgeführt wird, wird CMD-Zeile gestartet
#### 1 - What are Dockerfiles
* Dockefile - ein Program, das sagt, wie man Docker-Images bildet
* mehrere RUNs produzieren größere Images, da jede Zeile gecacht wird.
* ENV - Environmnent Variablen werden in/für die nächste Zeile gesetzt
#### 2 - Building Dockerfiles
* CMD:
    1. `CMD echo printe das`
    2. `CMD ["echo", "printe", "das"]`
#### 3 - Dockerfile syntax
* `FROM` - was ist der Ausgangsimage. wenn man mehrere `FROM`s benutzt werden mehrere Images erstellt
* `MAINTAINER Vorname Name email@email.de`  - Author des Images. Für Dokumentation, an wenn man sich wenden soll
* `RUN` - Shell-Befehl im Container laufen
* `ADD host container` - Archive werden dabei ausgepackt, anstelle von Host kann auch URL stehen
* `ENV` - setzt Environement Variablen auch für den Dockerfile und für Ausgangsimage
* `ENTRYPOINT ls` - setzen den Anfang des Befehls 
* `CMD` - ganzer Befehl
    * man kann beide zusammen benutzen
    * `ENTRYPOINT` - lässt den Container mehr wie normales Programm aussehen
* `RUN`, `CMD` und `ENTRYPOINT` zwei Varianten:
    1. Shell-Form: `nano text.txt` - hier wird shell gestartet
    2. Exec-Form: `[ "/bin/nano", "text.txt" ]`
* `EXPOSE 8080` - Ports mapen
* `VOLUME` - shared oder ephemeral Volumes definieren
    1. `VOLUME [ "/host/path", "/container/path" ]` - ephemeral (man sollte dies vermeiden, da dieses Volumen nur auf diesem Rechner funktionieren wird)
    2. `VOLUME [ "/shared-data" ]` - shared.
* `WORKDIR` - setzt Arbeitsordner für den Container (auch zwischenContainer)
* `USER name/uid` - Befehl als dieser User ausführen (nutzlich bei NW-Laufwerken, wo Rechte für bestimmte User gesetzt sind)
* Doku zu Dockefile: https://docs.docker.com/engine/reference/builder/
#### 4 - Multi-project Docker files
* Multi-Stage-Build, um z.B einen Completen-Dev-Container und Kleinen-für-Alle-Container machen
* Bsp:
```dockerfile
FROM ubuntu:16.04 as builder
RUN apt-get update
RUN apt-get -y install curl
RUN curl https://google.com | wc -c > google-size

FROM alpine
COPY --from=builder /google-size /google-size
ENTRYPOINT echo googleis this big; cat google-size
```
* man gibt dem ersten Image/Container einen Namen, mit `COPY` kopiert man aus dem ersten Image in den zweiten. Dabei wird der erste Image verworfen
#### 5 - Avoid golden images

### 4 - Under the Hood
#### 1 - Docker the program
* Kernel macht:
    * bekommt Nachrichten von HW
    * scheduled Programms
    * Speicher organisieren
    * sendet Mitteilungen zwischen den Programmen
    * Alloziert Resources: RAM,CPU, NW usw.
* Docker managt Kernel-Features
    * benutzt cgroups - groupiert Prozesse
    * benutzt Namespaces (Feature von Linux)
    * Copy-on-Write
* Docker-Client <-> SOCKET <-> Docker-Server
    * */var/run/docker.sock*
        * `docker run -ti --rm -v /var/run/docker.sock:/var/run/docker.sock docker sh` - *docker*-Image starte und in ihm das Docker-Socket mounten => Client ist im Container zugänglich
#### 2 - Networking and namespaces
* Desktop macht virt NW mit Hilfe der Bridges ~ SW-Switches
* `docker run -it --net=host ubuntu:16.01 bash` - 
* `apt-get install brudge-utils` - Bridge-SW installieren
* `brctl show` - zeigt alle Bridges
* `docker netwrok create my-new-network`
    * `brctl show`
* `--net=host` - Sicherheit ausmachen
* Docker benutzt Hosts IP-Tables für Routing
    * `sudo iptables -n -L -t nat`
* `docker run -it --rm --net=host --privileged=true ubuntu bash` - dem Container die Kontrolle über Host-System geben
    * `iptables -n -L -t nat`
* Namespaces - erlaubt Prozesse to NW-Segmenten hinzufügen
* Private NW sind in Shared NW mit deren Containern gebridged
#### 3 - Processes and cgroups
* `docker inspect --format '{{.State.Pid}}` container-nam - den Prozess mit namen Pid finden
* `docker run -it --rm --net=host --privileged=true --pid=host ubuntu bash` - Priviligerten Container starten
    * `kill Pid` - killt den anderen Container 
#### 4 - Storage
* besteht aus drei Layern
    1. HW-Devices
    2. Logical Storage devices - Aufteilung/Zusammenfassung in logische Einheiten
    3. Filesystem - BS
    4. Programme die emmulieren Filesysem - FUSE-Filesystems (docker benutzt das)
* Volumes and Bind Mounting
    1. Linux VFS (Virtual File System)
    2. Mount Devices on the VFS
    3. Mount Directories on th VFS
* `docker run -it --rm --privileged=true ubuntu bash`
    * `mkdir test1`
    * `cd test1`
    * `mkdir test2`
    * `cd test2`
    * `touch a b c`
    * `cd ..`
    * `mkdir other-test2`
    * `cd other-test2`
    * `touch other-a other-b`
    * `cd ..`
    * `mount -o bind ohter-test2 test2` - other-test2 in test2 mounten = hat einfach den other-test2 zu test2 hinzugefügt (Filesystem), wobei die a,b,c durch diesen Mount überdeckt werden
    * `ls -R` 
    * `umount test2` 
* man kann nur Host-FS in Guest mounten

### 5 - Orchestratin: Building Systems with Docker
#### 1 - Registries in detail
* ist ein Programm/Service, das auf Port 5000 läuft
    * Docker Official Regiestery (hub)
    * Nexus
* man kann Registery auch in Docker laufen
    * `docker run -d -p 5000:5000 --restart=alway --name registery registery:2` - eigene Registery als Container laufen
    * `docker tag ubuntu14.04 localhost:5000/mycompany/my-ubuntu:99`
    * `docker push localhost:5000/mycompany/my-ubuntu:99`
        * man sollte Authentication + Sicherheit setzen
        * dazu https://docs.docker.com/registery lesen -> deployent instructions
* Images local speichern
    * `docker save` und `docker load`
        * `docker save -o my-images.tar.gz debian:sid busybox ubuntu:14.04` - drei Images local  speichern. `-o`=Output
        * `docker load -i my-images.tar.gz` - `-i`=Input
#### 2 - Intro to orchestration
* Orchestration - es gibt mehrere Möglichkeit für Orchestration (einfachste ist *docker-expose*):
    * Container starten und restarten, wenn sie ausgehen
    * Contaiener können sich untereinander finden
* Docker-Compose starten alle Container, Volumes, NW, etc mit einem Befehl
* für größere Deployments:
    * Kubernetes
        * Container laufen programme
        * Pods gruppieren Container zusammen
        * Labels zur Beschreibung
        * kann local oder in der Cloud
    * EC2 Container Service (von Amazon)
        * ähnlich wie Kubernets 
        * Task Definition - Container die zusammen laufen
        * Tasks - Container jetzt starten
        * Services and exposes it to NET - sichert, dass Task immer laufen
        * man kann es in AWS einfügen
#### 3 - Kubernets in AWS
* eventuell nochmal schauen
#### 4 - Google Kubernetes Engine
* eventuell nochmal schauen

### Fazit
1. Lernzielle:
    1. `docker run` üben
    2. Dockerfile lernen
    3. Produkt Service auf Laptop starten
    4. perönliches Development Image erstellen