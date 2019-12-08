### 0 - Introductin
#### 1 - Setting up Environment
* Drei Ubuntu-Server als Virtuelle Machinen
### 1 - Getting Started with Docker Swarm
#### 1 - Introducing Docker Swarm
* ist Cluster Manager und Orchestration in Docker Engine eingebaut.
* Servers die in Swarm Mode laufen und "Service" aufrufen
    * man kann z.B. Web Server Service (können mehrere Web Server sein) haben und denen bestimmten State geben
    * z.B Port 80 für alle Web Servers aufmachen, Speicher für alle Servers definieren
* Fazit:
    * Server laufen als Swarm. Man lässt auf diesen Servers verschiedene Dienste laufen. Wein ein Node ausfällt, werdein diese Servives/Applications auf andere Nodes migriert
* Swarm Cluster wird vom Manager verwaltet und die Services/Apps laufen auf den Worker Nodes
* Vorteile:
    1. High availability
    2. Load Balancing
    3. Resiliency
    4. Placement
    5. Declarative service mode = Welcher Service auf welchem Server läuft
* Nodes-Kommunikation ist verschlüsselt
#### 2 - Set up a Docker Swarm cluster
* siehe Dokumentation
* `docker swarm init` - swarm Mode anmachen. Server auf dem dieses Befehl ausgeführt wird ist Manager. Dabei werden die Befehle für redundanten Manager und Workers angezeigt. Diese dan kopieren und auf dem passenden Server/Worker ausführen
* `docker node ls` - Cluster Status anzeigen
* `docker swarm join-token worker/manager` - Befehle zum Joinen als Worker/Manager anzeigen
#### 3 - Nodes, services, containers, and tasks
* Node = Physikal Host, der Docker-Engine installiert hat
* `docker service create --name webapp1 --replicas=6 nginx` - einen Service starten. `--replicas=6` - sollte 6 Tasks im Cluster laufen haben. Image/Container auf dem das ganze läuft ist `nginx`. (auf dem Manager ausführen) Also:
    1. Node = Phy Hosts z.B 3
    2. Task = WebApp1 (6 Mal)
    3. Container/Image = NGINX
* `docker service ls` - alle Services anzeigen
* `docker ps` - zeigt welche Container nach derm *docker service* erstellt wurden und laufen
#### 4 - Locking a Swarm cluster
* = Sicherheit (siehe Docker Doku)
* `docker swarm init --autolock` - beim Cluster erstellen
*  `docker swarm update --autolock=true` - laufenden Cluster locken
    * den angegebenen Key im Paswort-Manager speicher oder so
* `systemctl restart docker`
* `docker swarm unlock` -> Key einfügen
* `docker swarm unlock-key` = Key anzeigen, Nur möglich wenn Cluster unlock ist
* `docker swarm unlock-key --rotate` - Key Rotieren => mehr Sicherheit = wird neuer Key erstellt
#### 5 - Why Qourum is important
* Qourum ist Majority of Managers = wie Entschiedungen bie mehreren Managern getroffen werden -> man sollte Docker-Doku lesen. 
### 2 - Managing Docker Swarm 
#### 1 - Visualizing Swarm services
* `docker node ls` - alle Nodes im Cluster + deren Rollen anzeigen
* `docker info | more` - Infos zu Cluster + Nodes
* von github.com/dockersamples/docker-swarm-visualizer -> Docker-Swarm-Visualizer herunterladen - zeigt per GUI was auf einzelnen Nodes läuft.
    * `docker run -it -d -p 8080:8080 -v /var/run/docker.sock dockersamples/visualizer` - Visualizer downloaden + starten - ist auch ein Container
    * `docker service ls` - Services anzeigen
    * IP des Host herausfinden
    * im Browser dann ip:8080 aufrufen
* `sudo systemctl stop docker` z.B auf einem Node ausführen
* Visualizer im Browser aktualisieren.
#### 2 - Analyzing services with Docker Inspect
* `docker inspect` - Low Level betrachtung (Images, Nodes, Tasks, usw.)
* `man docker inspect`
* `docker inspect webapp1 | more ` - Details über webapp-Service (in json-Format)
* `docker inspect webapp | grep Replicas` 
* `docker inspect container-name/id` - Container betrachten
* `docker inspect container-id | grep IPAddress` 
#### 3 - Understanding stacks and stack files
* = Milti-tieried, Scalable Applications im Swarm Cluster implementieren
* Stack = z.B Web Service + DB Service + RPT Service
* Stack = Serveice1 (=Container1.1 Container1.2) + Service2 (=Container2.1 Container 2.2) + usw.
* man braucht dafür StackFile -> in YAML-Format = yaml definiet Stack
* z.B docker-stack.yml erstellen:
    * Bsp:
    ```
    version: "3"
    services:
        web:
            image: username/repo:tag
            deploy:
                replicas: 5
                resources:
                    limits:
                        cpus: "0.1"
                        memory: 50M
                restart_policy:
                    condition: on-failure
            ports:
                - "80:80"
            networks:
                -webnet
    networks:
        webnet:
    ```
    * siehe Docker-Doku
    * `docker stack deploy --compose-file docker-stack.yml mystack1` - mystack1 = Name des Stacks
    * `docker stack ls` - Stacks anzeigen
    * `docker stack ps mystack1` - Container im Stack anzeigen
    * `docker stack services mystack1` - Infos zum Stack anzeigen
#### 4 - Manipulate a running stack of services
* man kann alles im Stack verändern: CPU, Memory, Network, Storage
* `docker service ls` - Services anzeigen, vorallem Namen des Services herausfinden
* `docker service update --replicas=20 servicename` - Replicas des Services updaten
* besser yml-Datei verändern und `docker stack --compose-file docker-stack.yml mystack1`
#### 5 - Modifying network ports
* man sollte die Befehle in Docker-Doku checken
* `docker service update --publish-add published=8080,target=8080 servicename`
* `docker service inspect servicename | grep 8080` - checken ob alles geklappt hat
#### 6 - Mointing volumes
* `docker service ls` - ServiceName herausfidnen
* `docker service update --mount-add type=volume,source=web-vol, target=/web-vol-dir servicename` - dabei web-vol = Volume, dass neu erstellt wird
* `docker service inspect serviename | grep vol` - Volume im Service checken
* `docker volume ls` - checken, welche erstellt Volumes es im Docker gibt 
ODER
* in yaml Datei verändern mit 
```
volumes:
    - /etc/mysql
    - /sys:/sys
    - /etc:/etc:ro
```
#### 7 - Replicated vs. global seriveces
* es gibt in Swarm zwei Arten:
    * replicated Service - alle Services haben den gleichen Content (z.B Web-Services)
    * global Service - einen Task auf einem Node laufen
        * `docker create --mode global --name global-service nginx`
        * `docker service ls` 
            * auf jedem Node wird einmal ein *nginx* laufen 

### 3 - Troubleshooting Docker Swarm
#### 1 - Troubleshooting a service
* `docker service logs --optionen`
* `docker service logs service-name`
* Bsp:
    * `docker service create --name webserver2 -p8080:80 httpd`
    * `docker service ls`
    * `docker service logs webserver2`
    * `docker service logs webserver2 -f` - zeigt Logs in Real-Time
#### 2 - Using labels
* Node-Labels hinzufügen
+ `docker node update --label-add labelname node-name`
    * `docker node update --label-add prio1 DC2-N1`
    * `docker node inspect DC2-N1 | more`
* Labels sind gut für Contrains - mit der Option `--constraint 'node.labels.type == queue'` - festlegen, welcher Service auf welchem Node laufen kann/darf.
#### 3 - Understanding container communications
* Docker NW-Konzepte:
    * per Default sind Container bridget zu Host-NW d.h. laufen unter der gleichen IP wie der Host
    * man kann auch einge NW-s für Container anlegen z.B nur einen Container zum NW verbinden.
    * Overlay-NW = erlaubt den Container im privaten NW zu kommunizieren.
* nach Docker-Reference-Architecture googeln.
#### 4 - Using templates with Docker services
* Services über Templates erstellen.
* Host-Info wird in den Container eingebettet
* mögliche Optionen: `hostname`, `mount`, `env`
    * Syntax: Go Text Template Format
    * `docker service create --hostname="{{Node.Hostname}}" httpd` - Hostname von Host einbinden