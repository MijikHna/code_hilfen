* Wildfly ist Image für Java-Server
* https://github.com/arun-gupta/docker-for-java


<details>  

### 1 - Introduction to Docker
#### 1 - Introduction to Docker
* Docker = package sw, deploy sw, run sw
* Docker Image = SW "verpacken", dass man dann mit anderen teilen kann
* Docker Container = SW laufen (run). man kann ja mehrere Container gleichzeitig laufen
#### 2 - Java and Docker
* WORA - Write Once, Run Anywhere (Java)
* PODA - Package Once, Deploy Anywhere (Docker)
#### 3 - Docker workflow
* Docker = Client + DockerHost (Docker Engine) + Registery (Images)
* Client <-> DockerHost reden über RestAPI. DockerHost hört auf bestimmten Port
#### 4 - Get started with Docker
* Docker Toolbox = Docker Engine, Docker Machine - CLI, die einen Hyperviser z.B VirtualBox benutz, Dockerr Container
    * `docker-machine -create --driver=virtualbox myhost` - Docker Machine wird VM in Virtualbox einrichten und dort Docker installieren.
    * auf Windows und Mac sollte es als erstes ausgeführt werden, damit Docker Engine installiert wird
    * Als folge hat man dann Client auf dem Rechner und DockerHost in VM
        * Vorteil von Docker-Machine ist, dass man DockerHost auch in AWS, Azure usw installieren kann
    * `docker-machine env myhost`
    * `eval $(docker-machine env myhost)` - die PATH-Variablen für Docker-Client werden gesetzt.
#### 5 - Docker Toolbox for Windows demo
* = Docker Engine, Compose, Machine, Kitematic
* Hyperwise (auch in der VirtualBox) sollte aktiviert sein, sonst wird Docker Engine nicht funktionieren
* während der Installation wird Hyperwiser installiert (z.B VirtualBox)
</details>


<details>

### 2 - Run Containers and Build Images
#### 1 - Docker CLI
* `docker --version`
* `docker info`
* `docker version`
* `docker --help`, `docker subcommand1 [subcommand2] --help`
#### 2 - Run your first Docker container
* `docker container run -it jboss/wildfly` - Container starten (falls image noch nicht heruntergeladen, wird er heruntergeladen); `-it` - in Interaktive-Mode, diese tty dem Container zuweisen
* `docker container run -d jbos/wildfly` - in Detachted-Mode (im Background starten).
    * `docker container ls` 
    * `docker container stop container-name/container-id`
    * `docker container rm container-name/container-id`
* `docker container run -d --name my_web jboss/wildfly`
* `docker container rm -f container-web` - Container stopen und löschen
* `docker container run -d --name myweb jboss/wildfly bash` - z.B per Default startet wildfly-Container wildfly, jetzt aber überschreibt man den default-Befehl *wildfly* mit *bash*
    * Container können nur einen Befehl starten, also hier `bash`
    `docker container run -it --name myweb jboss/wildfly bash`
#### 3 - Run container (ports and volumes)
* `docker container run -d --name myweb -P jboss/wildfly` - *-P*= Ports publizieren, d.h. alles laufenden Ports des Container publizieren (z.B Per Defatult läuft Wildfly auf 8080)
    * `docker container ls` - es wird sowas wie *0.0.0.0:32689->8080/tcp* stehen, d.h. Port 32689 leite an den DockerContainer-Port 8080 weiter. Eventuell direkt die IP des Containers benutzen
    * `docker container logs container-name/container--id` - Logs des Containers ausgeben
* `docker container run -d --name myweb -p 8081:8080 jboss/wildfly` - Mappe Port 8081 des Hosts zu Port 8080 des Containers
* Chapter 2 webapp.war benutzen (ist Java-Application)
    * `docker container run -d --name myweb -p 8081:8080 -v 'pwd'/webapp.war:/home/kirill/wildfly/standalone/deployment/webapp.war jboss/wildfly` - Volume-mapping
#### 4 - Create your first Docker image
* dafür benuzt man DockerFile -> Mögliche Eingaben:
    * `FROM` - welches Image vewendet weden soll
    * `RUN`
    * `CMD` - welche Befehle nach dem Start des Containers ausgeführt werden sollen
    * `LABEL`
    * `MAINTAINER`
    * `EXPOSE`
    * `ENV`
    * `ADD`
    * `COPY`
    * `ENTRYPOINT`
    * `VOLUME`
    * `USER`
    * `WORKDIR`
    * `ARG`
    * `ONBUILD`
    * `STOPSIGNAL`
    * `HEALTHCHECK`
    * `SHELL`
* Beispele für DockerFiles: https://docs.docker.com/engine/reference/builder/
* Vorgehensweise:
    * neuen Order erstellen `mkdir neuesContainer`
    * Dockerfile erstellen `touch Dockerfile`
    * `FROM ubuntu` - *FROM* sollte als erster Eintrag stehen
    * `CMD echo "hello world"` 
    * Image Builden: `docker image build -t imageName .` - *-t imageTag* - dem Image einen Namen geben, *.* - verwende diesen Ordner (sagt eigentlich benutze Dockerfile aus diesem Ordner, falls man noch .dockeringore hat, wird es auch benutzt usw.)
    * `docker history imagename` - Anzeigen, wie der Image gebildet wurde
    * Fertig: Image starten: `docker container run imageName` 
#### 5 - Create your forst Java Docker image
1. einen Ordner erstellen
2. OpenJDK-Image von https://hub.docker.com herutnerladen (nach openjdk suchen, eventuell in Tags schauen (z.B nach kleineren Images schauen)). Images auf Docker-Hub sind gepresst
3. Dockerfile erstellen
4. 
```
FROM openjdk
CMD java -version
```
ODER (jdk-alpine-Tag ist kleienr als Defualt openjdk-Image)
```
FROM openjdk:jdk-alpine
CMD java -version
```
5. `docker image build -t javaContainer .`
6. `docker container run hellojava`
7. Größe ist wichtig, da Images eventuell über NW versendet werden
#### 6 - Copy files in the Docker image
* `COPY` - Dateien/Ordner auf Host in Container kopieren
* `ADD` - wie `COPY` + packt automatisch .tar-Dateien aus (z.B `ADD app.tar.gz /opt/var/myapp`) + man kann Dateien aus URL benutzen (besser aber mit *curl* oder *unstead*, da .tar-Dateien aus URL nicht automatisch gelöscht werden)
* Vorgehensweise:
1. Ordner erstellen
2. in diesen Ornder eigene App kopieren z.B *myapp.war*
3. Dockerfile erstellen
```
FROM jboss/wildfly
COPY myapp.war /opt/kirill/wildfly/standalone/deployments/myapp.war
```
* die eigene `CMD` in Dockerfile überschreibt die default-Command (welche ist die default-Command, kann man auf hub.docker des Images anschauen). Also letze `CMD` überschreibt die vorherige
* `docker image build -t myJavaApp`
* `docker image history myJavaApp`
* `docker container run -p 8081:8080 -d myJavaApp` - Wenn Port benutzt wird => mit `docker container ls` schauen, welcher Docker-Container den Port schon benutzt.
#### 7 - Run JAR files from the Docker image
* Vorgehensweise:
1. Ordner erstellen
2. in diesen Ornder eigene .jar Dateien kopieren, die man z.B mit Netbeans gebildet hat
3. Dockerfile erstellen
```
FROM openjdk:jdk-alpine
COPY myapp/target/myapp-1.0-SNAPSHOT.jar /deployments/
CMD java -jar /deployments/myapp-1.0-SNAPSHOT.jar
```
4. .jar-Dateien erstellen (hier mit Maven): 
    1. `mvn -f myapp/pom.xml clean package` - wird dann *myapp/target/myapp-1.0-SNAPSHOT.jar* erstellt
5. `docker build -t myJavaApp:3`
6. `docker image history myJavaApp:3`
7. `docker container run -p 8081:8080 -d myJavaApp:3` - Wenn Port benutzt wird => mit `docker container ls` schauen, welcher Docker-Container den Port schon benutzt.
* Wenn man nun Code geändert hat und es Image nochmal bilden sollte:
1. `mvn -f myapp/pom.xml clean package`
2. `docker build -t myJavaApp:4`
#### 8 - Other Dockerfile instructions
* `RUN` - software-Packages installieren, Script laufen, z.B `RUN apt-get update && apt-get install -y git` oder `RUN /opt/jbos/wildfly/bon/add-user.sh admin Admin#007 -silent`
* `CMD` - default um Container zu starten z.B `CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]`
    * `docker run mycontainer bash` - überschreibt dann die default-CMD
* `ENTRYPOINT` - default-Entrypoint ist */bin/sh -c*. mit diesem Befehl überschreibt man dann den default-Entypoint. z.B `ENTRYPOINT ["/entrypoint.sh"]
    * `docker container mycontainer --entrypoint`
* `EXPOSE` - an welchem Port der Container horchen soll z.B `EXPOSE 9990`
* `VOLUME` - mount-Punkt 
* `USER` - Usernamen bzw. UID für den Container setzen, wenn man Container startet.
* `HEALTHCHECK` - checkt, ob Application im Container noch richtig läuft. z.B `HEALTHCHECK --interval=5s --timeout=3s CMD curl --fail http://localhost:9081/pools || exit 1` - checke jede 5 sec, wenn keine Antwort nach 3 sek, dann wird CMD ausgeführt (localhost anpingen, wenn nicht pingable, dann exit)
#### 9 - Docker an Maven
* man kann Maven als Plugin in Netbeans einfügen (Maven sowas wie make)
* `mvn clean package exec:java` - Java-App packen, und ausführen
* In Maven-Datei (pom.xml). Docker-Maven-Plugin hinzufügen (z.B io.fabric8). In diesem Docker-Teil alles konfigurieren:
    * `mvn package -Pdocker` - Docker-Image wird gebildet
    * `mvn install -Pdocker` - Docker-Image bilden und ausführen
* Docker-Maven-Plugins muss man von github herunterladen + die Doku auf github checken
#### 10 - Docker and Gradle
* Gradle ist alternative zu Maven
* die Datei *build.gradle* bearbeiten. 
* Gradle-Workflow:
    * zum Projekt-Ordner gheen `./gradelew build run`
    Oder mit Docker
    * `./gradelew dockerBuildImage`
    * `./gradelew startContainer`
* Docker-Graven-Plugins muss man von github herunterladen + die Doku auf github checken
#### 11 - Tag and share Docker images
* `docker image ls -aq` - gibt nur Image-IDs aus als Liste
* `docker image rm -f $(docker image ls -aq)` - alle Docker-Images löschen
* `docker container  ls -aq` - alle Container-ID ausgeben
* `docker container rm -f $(docker container ls -aq)`
+ 
+ `docker image build .` - es wird Docker-Image gebuildet (aber ohne Repo und ohne Tag, da man es nicht angegeben hat) => Image nur über Image-ID ansprechbar
* `docker image build -t myContainer1 .` - so wird dem Image die Repo zugewiesen + als Tag = latest
* `docker image build -t myContainer1:1 .` - so auch der Tag = 1 gesetzt
* `docker image tag myContainer:1 myContainer:latest` - den Image auch den Tag *latest* geben.
* also *latest* ist einfach nur ein Tag, der bei `docker container run myContainer` ausgewählt wird
* `docker image push myContainer:latest` - es wird ein Fehler kommen, da man vor dem richtigen Image-Namen noch den Repo-Namen angeben sollte:
    * `docker image tag myContainer:1 kirill/myContainer:latest` - auf hub.docker sollte Repo *kirill* existieren 
* `docker run -d -p 5000:5000 --restart always --name registery registery:2.6.0` - private Regisery/Repo local starten
    * damit die Images jetzt zur privaten Resistery geschoben werden, muss man die Images entsprechen umbennen/tagen: `docker image tag myContainer:latest localhost:5000/kirill/myContainer:latest`
    * `docker image push localhost:5000/kirill/myContainer:latest` 
</details>


<details>

### 3 - Multicontainer application with Docker Compose
#### 1 - Introduction to Docker Compose
* Docker Compose erlaubt mehrere Container zu laufen. *docker-compose.yml* ist defautl-Name, man kann es aber anders nennen. Es gibt noch *docker-compose.override.yml*, wo man einige Sachen von *docker-compose.yml* überschreiben darf.
* bsp:
    * `docker-compose -v` - Docker Compose Version checken
    * `docker-compose --help` 
    * `docker-compose up` - Contaienr starten
    * `docker-compose down` - Container stopen
#### 2 - Docker Compose file
* Bsp:
    * Ordner erstellen
    * in diesem Ordner *docker-compose.yml* ertellen
    * 
    ```
    version: '3'
    services: # welche Services gestartet werden sollen
        web: # Name des 1. Services
            image: jboss/wildfly
            volumes: 
                - ~/deployments:/opt/jboss/wildfly/standalone/deployments # falls ~/deployments nicht existiert, wird es erstellt
            ports:
                - 8080:8080
    ```
    * `docker-compose up -d` - docker-compose.yml in detached-Mode starten
    * `docker-compose ps` - alle Services anzeigen
    * `docker-compose log -f`
    + Hier im Beispiel wurde .war in deployments eingefügt und es war über den Browser erreichbar. Also googlen nach *Java .war*
#### 3 - Milticontainer application with Docker Compose
* Hier der Bsp: besteht aus: Java-Server (Wildfly) und DB (Couchbase). Kommunikation mit DB funktioniert mit *CRUD using N1QL*
* *docker-compose.yml* erstellen
```
version "3"
services:
    web:
        image: arungupta/couchbase-javaee:traval
        environment:
            - COUCHBASE_URI=db #ist der Name des DB-Containers
        ports:
            - 8080:8080
            - 9990:9990
        depends_on:
            - db
    db:
        image: arungupta/couchbase:travel
        ports:
            - 8091:8091
            - 8092:8092
            - 8093:8093
            - 11210:11210
```
* Code zu Java: https://github.com/arun-gupta/couchbase-javaee-application
* für Rest-API: https://github.com/arun-gupta/docker-images/tree/master/couchbase-server
* `docker-compose up -d` - Containers in detached-Mode starten
* `docker-compose logs -`
* `docker-machine ip container-name`
* `docker-compose down` - Services + NW ausmachen
#### 4 - Docker Compose options (project and override)
* `-p name` - erstellt einzelne Evironments on Host (random), wo die Services laufen. man kann dann Service erneut starten, ohne vorherige herunterzufahren.
    * `docker-compose up -d -p myenv1`
    * `docker-compose -p myenv1` - zeigt Info zu den Services
    * `docker-compose -p myenv1 down`
* *docker-compose.override.yml* - überschreibt/erweitert *docker-compose.yml*
    * Single-Values (image) werden überschrieben
    * Multi-Values (ports) werden ergänzt 
#### 5 - Docker Compose options (multiple files)
* man hat z.B noch *docker-compose.db.yml*
* `-f` - wird auch override-File benutzt
    * `docker-compose -f docker-compose.yml -f docker-compose.db.yml up -d` - erste .yml ist Nr1, Nr2 usw. überschreiben/erweitern vorherige
    * `docker-compose docker-compose.yml -f docker-compose.db.yml` - Services checken
    * `docker-compose -f docker-compose.yml -f docker-compose.db.yml down`
* `extends` - Service aus einem .yml erweitern
    * noch *configuration.yml*
    ```
    verison: "3"
    services:
        config:
            environment:
                AWS_ACCESS_KEY: xxx
                AWS_SECRET_KEY: xxx
    ```
    * docker-compose.yml
    ```
    services:
    web:
        extends: # etwas einfügen
            file: configuration.yml # sagen, welche Datei hier eingehägt werden soll
            service: config #was genau übernommen werden soll
        image: arungupta/couchbase-javaee:traval
        environment:
            - COUCHBASE_URI=db #ist der Name des DB-Containers
        ports:
            - 8080:8080
            - 9990:9990
        depends_on:
            - db
    db:
        image: arungupta/couchbase:travel
        ports:
            - 8091:8091
            - 8092:8092
            - 8093:8093
            - 11210:11210
    ```
    * `docker-compose --verbose up -d`
    * 
</details>


<details>

### 4 - Docker Clustering
#### 1 - Introduction to swarm mode
* managt Cluster von Docker-Engines (braucht Docker-Mashine)
    * `base=https://github.com/docker/machine/releases/download/v0.16.0 &&`
    * `curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&`
    * `sudo install /tmp/docker-machine /usr/local/bin/docker-machine`
* mit Docker CLI (Client) erstellen/managen Swarm
    * es gibt darin Service Discovery (in Swarm werden bestimmte Services automatisch gefunden), Load Balacing, Scaling
    * Rolling updates
* man sollte ungerade Anzahl von Swarm-Managers haben
    * Swarm-Manager haben alle gleichen State
* Sicherheit:
    * Manager erstell CA und Zertifikate, wenn ein neuer Worker gestartet wird, bekommt er den RootCA-Zert + Worker-Cert => Kommunikation Node <-> Manager ist verschlüsselt
    * werden alle 90 erneuert (kann man aber selbst konfigurieren)
    * man kann auch external CA einrichten
* Swarw-Vorgehen:
* `docker swarm --help`
* `docker swarm init` - bei Windows muss man noch switch-Option + IP angeben oder `docker swar init --listen-addr <ip>` - erstellt Swarm + Rechner ist Manager
* `docker swarm join --token <worker_token> <manager>` - Workder hinzufügen
* `docker swarm join --manager --token <manager_tokem> --listen-addr <master2> <master1>` - weiteren Manager hinzufügen
* `docker info` - Info zu Container, Images + Swarms
* `docker swarm leave` oder `docker swarm leave -f` - ohne `-f` wird nicht funktionieren, falls es der letzte Node ist
#### 2 - Create a multinode swarm mode cluster using Docker Machine
* Bsp:
    * mit docker-machine 6 Server erstellen mit .sh-Skript (da auf dem Server Docker-Engine installiert sein soll)
        * `docker-machine create -d virtualbox worker$node/manager$node`
    *  `docker-machine ssh manager "docker swar init --listen-addr $(docker-machine ip manager1) --advertise-addr $(docker-machine ip manger1)` - den Server1 als manager1 im Swarm initialisieren
    * `docker-machine ssh manager1 "docker node ls"`
    * `docker-machine ssh manager1 "docker swarm join-token manager/worker -q"` - vom Manager1 nach Manager/Worker-Token verlangen
    * `docker-machine ssh manager2 "docker swarm join --token $(docker-machine ssh manager1 "docker swarm join-token manager/worker -q") --listen-addr $(docker-machine ip manager2/worker2) --addvertise-addr $(docker-machine ip manager2/worker2) $(docker-machine ip manager1` - den Server2 als Manager in swarm aufnehmen
    * usw. für alle Manager und Worker
    * `docker-machine ssh manager1 "docker info"`
Bsp: mit bash-script 3 Manger und 3 Worker erstellen
```bash
#!/bin/bash
managers=3
workers=3

for node in $(seq 1 $managers);
do
    docker-machine create - virtualbox manager$node;
done

for node in $(seq 1 $workers);
    docker-machine create -d virtualbox workder$node;
done

docker-machine ls
```
#### 3 - Deploy services to swarm mode
* Services deployen
    1. replicated Service: `docker service creat --replicas 3 --name web -p 8080:8080 jboss/wildfly`
        * Manager ist auch ein Worker, mann kann ihn aber nur als Manager konfigurieren
* Swarm-Mode hat Load Balancer (Routing Mesh):
    * es reroutet Traffic von beliebigem Host zum Container
    * es benutzt dann DNS-based Service Discovery => man braucht kein externes DNS
Ablauf:
1. `docker machine ssh manager1`
2. `docker service creat --replicas 3 --name web -p 8080:8080 jboss/wildfly`
3. `docker service ls`
4. `docker service inspect web`
5. `docker service ps web`
#### 4 - Container or node failure
#### 5 - Scaling and rolling update of service
* Scalen = neuer Anzahl an Services machen: `docker service scale web=6`
* Upgrade = `docker service update web --image wildfly:2 --update-parallelism 2 --update-delay 10s` - jeweils 2 Container in 10 Sek Abständen upgraden
* `docker-machine ssh manager "docker service ps -f \"desired-state=running\" web"` oder `docker-machine ssh manager "docker service ps -f "desired-state=running" web"` - -f = Filter
* `docker service ls` - ganzen Service löschen
#### 6 - Multicontainer application to swarm mode cluster
* mestens im realen Leben benutzt
* Vorgehen:  
    * sich auf dem Manager 1 einlogen. .yml-Datei erstellen.
    * `docker stack --help` - Stack deployen - Mehrere Container auf mehreren Hosts laufen
    * `docker stack deploy --compose-file=docker-compose.yml webapp`
    * `docker stack ls`
    * `docker service ls`
    * sich auslogen
    * `docker-machine ls` - IP von Manger 1 merken
    * `curl http://$(docker-machine ip manager1):8080/pfad/zur/seite` - man kann über die Machine auf der docker-compose.yml gestartet wurde auf den Service zugreifen
    * sich auf dem Manger 1 einlogen
    * `docker stack rm webapp` - Stack löschen

#### 7 - Node maintenance, label/constaints, and global service
* 
#### 8 - Create multinode swarm mode cluster on AWS/Azure
</details>


<details>

### 5 - Stateful Containers
#### 1 - Create a database cluster using Docker Service
#### 2 - Persistent containers overview
#### 3 - Persistent containers practice
#### 4 - Docker volume plugin overview
#### 5 - Docker volume plugin practice
</details>


<details>

### 6 - Monitor Docker Containers
#### 1 - Monitor Docker using CLI
#### 2 - Monitor Docker with Prometheus
#### 3 - Monitor Docker with cAdvisor
</details>