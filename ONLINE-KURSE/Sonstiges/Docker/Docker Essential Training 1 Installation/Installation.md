### Introduction
#### 4 - Setting up your environment
#### 5 - Set up a Linux virtual machine
* *openssh-server* isntallieren
* man sollte der VM eine statische IP geben, sonst kann es zu Problemen bei Docker Swarm führen
### 1 - Preparing to install Docker
#### 1 - Docker editions
* zwei Editionen:
    * EC - Community
    * EE - Enterprise (in drei Varianten)
#### 2 - Docker platforms
* EE kann in public Cloud laufen => zuerst lokal testen, dann in die Cloud (Production)
#### 3 - Sizing Docker
* UCP und DTR brauchen mehr Ressourcen - man sollte die Docker-Requirements-Seite checken
#### 4 - Review: Docker arch
* Docker-Engine: - Server-Client-Application
    1. dockerd = Docker-Server
    2. REST API - wird von allen Anwendungen benutzt um mit dockerd zu reden
    3. Docker CLI - Docker Client = Docker Befehle eingeben
* Dockerd wird auf dem Server installiert. Dort laufen dann Images und Containers
* Docker Client/CLI (kann auf dem gleichen Rechner oder Remote Rechner installiert sein). Damit kann man Images aus Registery ziehen auf im Dockerd installieren
#### 5 - Docker Universal Control Plane (UCP)
* Docker-Engine 
* Universal Control Plane (UCP) - Management für alle Container = Web-Application
* Docker Trusted Registry DTR - eingene Registery verwalten = Web-Application
#### 6 - Docker namespaces
* um zu isolieren, was im Docker-Container geschieht von OS.
* Typen für Namespaces:
    1. Process
    2. Mount
    3. IPC
    4. Network
    5. User
* durch Namespaces haben die Container eigene CPU-Resourcen, Network-Resourcen, File-System usw.
* man kann auch User von OS in Docker-Container integrieren
#### 7 - Docker control groups
* Cgroups = Controllgruppen umd CPU/RAM zu managen:
    * CPU Limits
    * CPU reservations
    * Memory limits
    * Memory reservations
* Cgroups-Commands.
    * `-c, --cpu-shares int`
    * `--cpus deicam`
    * `--cpuset-cpus string`
    * `--cpuset-mems string`
    * `-m, --memory bytes`
    * `--memory-reservation bytes`
    * `--memory-swap bytes`
    * `--memory-swappniss int`


### 2 - Installing Docker
#### 1 - Installing Docker on Linux
#### 2 - Installing Docker on Windows
* `docker container run -it ubuntu` - Ubuntu-Image ziehen, starten und sich im Container anmelden
* `docker run microsoft/dotnet-samples:dotnetapp-nanoserver` - Windows-Container (.NET Core) starten
#### 3 - Installing Docker on Amazon Web Services
#### 4 - Installing Docker on Windows Server
* `docker container run -it microsoft/windowsservercore powershell`
#### 5 - Installing Universal Control Panel (UCP)
* UCP ist Management Tool für EE
#### 6 - Upgrading Docker
* eventuell Docker davor backupen -> */var/lib/docker* 
* dann einfach der Installtion von Docker folgen
#### 7 - Playing with Docker
* dafür gibt es Docker-Seite: https://labs.play-with-docker.com - man braucht aber Docker-Account - auf 4 Stunden begrenzt
### 3 - Configuring Docker
#### 1 - Docker storage drivers
* man sollte Daten in Docker-Volumes speichern
* `docker info` 
    * *Storage Driver: ...*
* Docker hat plugable storage arch und unterstütz verschiedene Storage Drivers
* in der Docker-Doku Docker Storage Driver anschauen
#### 2 - Docker repositories and Docker Hub
* `docker login` - in Docker Hub einlogen (https://hub.docker.com)
* `docker pull alpin` - Alpin-Image von Docker Hub ziehen. (kleiner Linux Image)
* `docker images`
* `docker tag image-id dockerhubid/imagename:tag1`, `docker tag image-id dockerhubid/imagename:tag2` - Images tagen
* docker push docker-id/imagename
* `docker image rm image-id` - delete Image
* `docker image rm image-id -f` - Image deleten mit force
* `docker pull dockerhubid/imagename:tag1` - getagten Image aus Repo ziehen
#### 3 - Docker swarm: Joining nodes
* Swarm Cluster = mehrere Docker Worker Nodes sie laufen die containisierten Applications
* Swarm Manager Nodes ist für die Verwaltung von Worker Nodes
* Wenn ein Worker Swarm geht down, dann werdnen die Apps auf den anderen Workern gestartet
* *hier wurde Worker Node über UPS erstellt*
* Also Worker Nodes sind z.B Server. auf denen Docker installiert ist. Auf dem Worker Manager ist Docker-Engine und UPS installiert
    * Worker hinzufügen: `docker swarm join --token Token... 10.0.0.10:2377` - diesen Befehl über UPS oder über Worker Manager herausfinden
#### 4 - Creating and managing users and teams
* man braucht dafür UPS:
    * Organisation -> Team -> User erstellen
#### 5 - Configuring Docker to start on boot
* `sudo systemctl enable docker`
* `sudo systemctl disable docker` 
#### 6 - Backing up Docker
* 4 Teile backup:
    1. Docker Swarm -
    2. UCP
    3. DTR
    4. Container-Data
* Vorgehensweise: (ist aber alles auf der Docker Seite)
    * `systemctl stop docker`
    * `cp -R /var/lib/docker/swarm /tmp/swarm`
    * `docker container run --log-driver none --rm -i --name ucp -v /var/run/docker.sock:/var/run/docker.sock docker/ucp:2.2.5 backup --interactive`
    * DTR siehe Docker-Seite
#### 7 - Installing Docker Trusted Registery
* Braucht man wenn man Swarms betreibt.
* `docker run -it --rm docker/dtr:2.4.2 install --ucp-insecure-tls` - man muss das auf dem Worker Node ausführen, wo man eigene Docker-Registery betreiben möchte
* DTR wird bei UCP registriert
### 4 - Troubleshooting Docker Install and Config
#### 1 - Checking the status of Docker
* `docker version` - sagt welche Version auf dem Server und Client läuft
* `docker info` 
* `docker ps` - laufende Container
* `docker ps -a` - alle Container
* `docker node ls` - nur auf Docker-Manager möglich, zeigt alle Cluster und deren Status
#### 2 - Configuring Docker logging
* 2 Möglichkeiten wie man Logs konfiguriert
    1. allgemeiner Pfad bei */var*
    2. für einzelnen Container kann man json mit Log-Optionen erstellen
* `docker info | grep "Logging Driver"` - zeigt wie Log konfigureirt ist (Default ist json)
* in */etc/docker/* *daemon.json* anlegen und die Logs umkonfigurieren, sonst default benutzt, z.B den Logging Driver ändern (syslog, cloudlog, usw)
* `docker logs` oder `docker logs container-id`
* `docker run --log-driver=syslog --log-opt syslog-address=udp://1.1.1.1 alpine` - für Containter den Log-Driver ändern
#### 3 - Analyzing Docker errors
es gibt auf der Docker-seite empfehlungen für Docker Post-Installation, z.B Kompatibilität checken.
