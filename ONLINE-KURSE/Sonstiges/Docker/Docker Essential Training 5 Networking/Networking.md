### 0 Introduction
* Lab Environment
    * 3 VMs im gleichen Netz in jeder ist Docker installiert + in einer VM Docker UCP
### 1 - Understanding Docker Networking
#### 1 - Docker networking overview
* was wird gelernt
    * Typen des NW
    * Published Ports
    * DNS
    * Load balancer
    * Traffic flow
    * NW logging
* Docker Reference Architecure: Designing Scalable, Portable Docker Container Networks-> Doku dazu
* Docker Netwrok (ist auch eine Sandbox):
    * Docker Network <-> Endpoint zum Container
    * man muss 
        1. Network Driver
        2. IPAM Driver  (ip address management address)
            * es gibt Docker IPAM Drivers oder Third Party IPAM Drivers
        * konfigurieren
* 2 NW - Modele
#### 2 - Types of container networks
* Use Cases:
    1. Native Network Driver (Bridge) - Default
    2. Host Network Driver - nur ein Container möglich, ist direkt mit Host-NW verbunden
    3. Overlay - nur bei Swarm (Multi-Docker-Host NW)
    4. Macvlan - klont host Interface um virtuelles Inteface zu erstellen, unterstützt VLAN - ist sehr kompliziert
    5. None - kein NW
    6. Third-Party Network Plugins (aus dem Docker Store)
        1. infobox IPAM plugin
        2. Weave net
        3. Contiv Network plugin
* Hilfe -> auf Docker Blog -> *Understanding docker networking drivers and their user cases*
### 2 - Configuring Docker Networking
#### 1 - Creating a bridge network
* bei Enterprise kann man auch `overlay`-NW erstellen
* `bridge` ist immer dabei <- ist Default-NW
* `docker network inspect nw-name`
* Bsp: eigenes *bridge*-NW erstellen
    * `docker network create --driver birdge nw-name`
    * `docker run -dit --name container-name --network nw-name alpine ash` - *ash* ist alpine-Shell
* `docker container attach container-name` - sich im Container anmelden also ~ `docker exec -it container-name
* `STRG+P+Q` - den Container verlassen
* `docker network rm nw-name`
#### 2 - Creating an overlay network
* *overlay* wird automatisch erstellt, wenn man auf einem Node swarm erstellt.
* Bsp: *overlay*
    * `docker network create --help`
    * `docker network create --driver overlay nw-name-overlay`
    * `docker service`
    * `docker service --help`
    * `docker service create --network=nw-name-overlay --name=swarm-service-name --replicas=6 nginx`
    * `docker service ls`
    * `docker ps | grep swarm-service-name`
    * `docker service inspect swarm-service-name` -> z.B Netwrok-Config checken
    * `docker container inspect container-id-von-swar-service-name` - z.B die IP checken
* mit overlay kann man auch verschlüsselte Kommunikation zwischen Nodes einstellen
#### 3 - Publishing ports
* * Container werden mit *Bridge NW* verbunden, *Bridge NW* ist mit physikalischen NW-Karte verbunden
    + d.h Container können etwas senden aber nicht empfangen
    * => port Mapping: *Public:Private*
* es gibt verschiedene Optionen, um Ports zu mappen (siehe Doku)
    * `-p host:container`
    * `-P` - alle exposed Ports werden gemacht (werden in Dockerfile festgelegt)
* `docker container run -dit -p 8080:80 nginx`
* `docker cotainer run -dit -P nginx`
#### 4 - Comparing host and Ingress port publishing
* Host Port Publishing:
    * wenn man global mode service benutzt = ein Container auf einem Host
        * ein Port vom Host dem Container zuweisen
        * `mode=host`

* Ingress Port Publisching
    * beim replicated swarm service benutzt
    * ein Port von allen Hosts einem Pool von Containern zuweisen
    * checken Doku -> Swarm -> Use Swarm mode routing mesh
#### 5 - Configuring DNS
* per default erben DNS-Settings von Host
* Wege um bestimmte DNS einstellen:
    1. `docker container run  -it --dns 192.168.1.200 image-name /bin/bash`
    2. man kann auch DNS per *docker network* einstellen
    3. Um DNS für gesamten Docker-Host zu ändern:
        * `nano /etc/docker/daemon.json`
        ```json
        {
            "dns:" ["192.168.1.200"]
        }
        ```
        * hier kann man auch mehrere DNS-s eintragen
        * `systemctl restart docker`
        * `docker container run -it image-name /bin/bash
        * <- wird dann dieser DNS-Server im Container in */etc/resolv.conf* eingetragen 
#### 6 - Configuring load balancing
* Docker benutzen um HTTP und HTTPS zu bestimmter APP zu load balancen (Layer 7 Load Balancing)
* für *Docker Swarm* wichtig bzw. kommt mit Enterprise
* Doku checken: Docker Refernce Architecutre: Universal Control Plane 3.0 Service Discovery and Load Balancing  (New. Swarm Layer 7 Routing )
    * vor allem *Interlock Proxy* 
* Load Balancing:
    * Docker Swarm stellt Load Balancer von Workloads wenn Workloads instantiert werden
    * Scalieren von neuen Workloads ist einfach (wurde in Docker Swarm demonstriert)
    * Swarms haben keine traditionelle *scalled up* und *scalled down* containers per Anfrage (ist neues Feature von Docker Swarm)
#### 7 - Configuring host networking
* Host Network - also Container hat die gleiche IP wie HOST (also direkt mit NW-Karte verbunden). Es muss keine Mapping, keine IP-Translation stattfinden.
    * `docker run -d --network host --name contName imageName` - ist über `localhost` und über normalen APP-Port erreichbar (`-d` - deamon-Container)

### 3 - Troubleshooting Docker Networking
#### 1 - Understanding Docker EE traffic flow
* Traffic zwischen Docker Engine + Docker Truste Reg und UCP Controllers
* Aufbau von Docker Universal Control Plane

| Docker Aufbau |
|---|
|Docker Trusted Registery UND Containers/Applications|
|Universal Control Plane (UCP)|
|Cloud Server (Azure) ODER Physical Servers ODER Virtual Servers|

* Bsp: Docker Swarm Cluster
    1. Docker Swarm Manager 1 hat:
        1. Docker EE
        2. UCP Agent
        3. UCP Magager
        4. Magager 
        5. [Containers]
    2. Docker Swarm Manager 2 hat:
        1. Docker EE
        2. UCP Agent
        3. UCP Magager
        4. Manager 
        5. [Containers]
    3. Docker Swarm Worker 1/2 hat:
        1. Docker EE
        2. UCP Agent
        3. UCP Worker
        4. Worker 
        5. [Containers] 
* Traffic Flow:
    * Docker API benutzt TCP/IP.
    * in Docker Doku nach UCP-Components suchen -> UCP-Komponenten (sind eigentlich eigenständige Containers die auf Manger und Workers laufen)
    * nach Docker EE Architecture suchen
#### 2 - Identifying external network ports
* `docker container port contName` - zeigt Ports des Containers (Host ist 0.0.0.0:port)
* `docker container inspect contName` 
#### 3 - Using logs to analyze networking
* `docker container logs contName`
* `docker container logs --help`