
#### Hilfe anzeigen
* `docker`
* `docker container --help`
#### Info zu Docker:
* `docker --version`
* `docker version`
+ `docker info`
#### Container auflisten
+ `docker container ls`
+ `docker container ls --all`
+ `docker container ls -aq`
#### Curl
+ `curl http://localhost:4000` - curl redet mit http über Konsole => kann man http-Responses (=HTML-Seite) in Terminal anzeigen lassen
#### docker run
+ `docker run -p 4000:80 image-name` - Port 80 auf 4000 mappen
+ `docker run -d -p 4000:80 image_name` - `-d` Container im Hintergrund laufen lassen
#### Registory
* `docker login` - Davor Account z.B bei hub.docker.com anlegen
* `docker tag image_name username/repository:tag` = Image taggen
* `docker push username/repository:tag`  

* `docker pull username/repository:tag` - man kann das aber auslassen, wenn lokal Image nicht gefunden wird (siehe unten) 
+ `docker run -p 4000:80 username/repository:tag` - wird automatisch gepullt

>docker-compose (Services) = YAML-Datei definiert, wie Docker container sich verhalten sollten (docker-compose.yml) ← statt die ganzen Option - einzeln einzugeben, diese in .yml reinschreiben.
### Apps mit .yml-Einstellungen laufen lassen
* `docker swarm init` - sonst bekommt man Error, dass node is not a swarm manager
+ `docker stack deploy -c docker-compose.yml appName` - App starten, App bekommt den Namen appName
+ `docker service ls` - sollte appName anzeigen lassen
+ `docker service ps appName` - zeigt alle Tasks der appName
+ `docker container ls -q` - die Ausgabe ist die gleiche wie `docker service ps appName`
+ `docker stack rm appName` - App ausschalten
+ `docker swarm leave --force` - den Swarm ausschalten

#### Swarms = Docker an verschiedenen Maschinen laufen:
>Swarm = Gruppe von Maschinen, die Docker laufen und zum Cluster zusammengehören.
=> Docker Befehle werden im Swarm Manager ausgeführt. Einzelne Maschine ist Node
Es gibt mehre Strategien für Swarms:
>1. emptiest Node = Füllt utilisierte Maschine mit Containern,
>2. Global=jede Maschine bekommt einen Node ← Strategien werden im ComposeFile festgelegt. Swarm Manager-Maschine ist Master, anderen sind Worker.= Swarm mode anschalten.

####  Oracle VB ist in Docker Toolbox installiert
* `docker swarm init` - Swarm Modus anschmeißen
* `docker swarm join` - auf anderen Maschinen ausführen = dem Swarm beitreten
* `docker-machine create --driver virtualbox myvm1` - Virtuelle Maschine erstellen
* `docker-machine ls` - alle VMs auflisten + deren Ips
* `docker-machine ssh VM_Name „Docker-Command:“`
    * `docker swarm init / docker swarm join`
    * `docker swarm join --token <token> <myVM ip>:<port>` - immer mit Port:2377 oder 2376 laufen lassen → Befehle ohne Port = Default = 
* Bsp: `docker-machine ssh myVN „docker swarm init –advertise-addr <myvm1 ip>“`
* Bsp: `docker-machine ssh myVN „docker swarm join --token <token> <ip>:2377“`
* `docker-machine ssh myVM1 „docker node ls“` - alle Nodes anzeigen ← da myVM1 Master ist
* `docker swarm leave` - Swarm beenden ← von beliebigem Node
* `docker-machine evn VM_Name` - ebenfalls VM starten + Shell konfigurieren zu Docker daemon auf der VM
* docker-machine -Shell konfigureiren um mit Docker Daemon auf der VM zu reden: => dann kann man lokales docker-compose.yml auf VM laufen
    * `docker-machine env myVM1`
    * `epxort DOCKER_TLS_VERIFY=“1“`
    * `export DOCKER_HOST=“tcp://192.168.99.100:2376“`
    * `export DOCKER_CERT_PATH=“/Users/sam/ .docker/myVM1“`
    * `export DOCKER_MACHINE_NAME=“myVM1“`
    * `eval $(docker-machine env myvm1)`
* `docker stack deploy -c docker-compose.yml Swarm_Name` - docker-compose.yml auf VM ausführen
* `docker service ps <service_name>` - auf dem Swarm-Manager ausführen um zu schauen, dass alle Services bereit sind
*`docker stack ps Swarm_name`  
Also:
* `docker-machine env bzw. docker-machine ssh`
* `docker-machine scp <file> <machine>:~` - Dateien zwischen Maschinen austauschen  
Bei Problemen mit Verbindung zwischen den Machinen => Ports 7946 und 4789 öffnen 
* `docker stack rm Stack_name` - Swarm löschen
* `docker-machine ssh myVMx „docker swarm leave“`
* `docker-machine ssh myVMx „docker swarm leave --force“` = Swarm löschen
`eval $(docker-machine env -v)` - Löchen Shell-Variablen(-Konfiguration) = Trennt Shell von docker-machine
docker-machine start myVMx

#### Stack - Gruppe von interagierenden Apps
* Visualizer - Serivce, dass in jeder App laufen kann, dass im Stack ist. 

