### 0 - Introduction
#### 0 - Additions
* `docker image prune -a` - alle Images löschen

### 1 - Understanding Docker Images
#### 1 - What is a Docker Image?
#### 2 - Understanding layering with Docker Images
* Images habe mehrere read-Only Layers
* Wenn man einen Image startet => wird Top writble Layer erstellt.
* Storage Drivers verwaltet diese Layer:
* Docker Image:
    1. Manifest - beschreibt, was ist im Container
    2. 1. Container Layer -> OS z.B Ubuntu
    3. 2. Container Layer -> Configs Veränderung
    4. 3. Container Layer -> Application 
    5. usw. 
    6. Image Starten -> Container => Writable Layer wird erstellt.
#### 3 - What is a Dockerfile?
* hat alles um `docker build` auszuführen
* `docker build` sendet Dockerfile zum Docker-Server/Daemon, der Image dann erstellt.
* `man dockerfile` - Manual zum Dockerfile
* `man docker build` 
#### 4 - Analyzing a Dockerfile
* `ADD` - Datei in Image kopieren + *tar* + *url*
* `COPY` - Datei in Image kopieren
* `VOLUME` - Mount-Point beim *run* erstellen
* `ENTRYPOINT` - was ausgeführt wird, wenn *run* ausgeführt wird. Default ist `/bin/sh -c`
    * bei `docker run` => `ENTRYPOINT CMD` ausgeführt
* `EXPOSE` - Ports freigeben
* `CMD` - Argumente für `ENTRYPOINT` 
* `ENV` - Env-Variablen definieren
* `FROM` - welcher Base-Image
* `MAINTAINER` - deprecated - Autor von Dockerfile
* `ONBUILD` - wird nur dann benutzt/ausgeführt, wenn von diesem Dockerfile/Image weitere Dockerfile/Images erstellt/gebinldet werden
* `RUN` - führt Befehl im neuen Layer aus
* `WORKDIR` - 
* `LABEL` ist einfach nur Kommentar
* `docker build .` 
* `docker image inspect image-id` 
    * *Cmd* = Befehle die ausgeführt wurden
    * *Labels*
    * *Layers* - zeigt alle Layer des Images
* `docker image history image-id` - zeigt welche Befehle ausgeführt wurden + Layers-größen 
#### 5 - Managing Images with the CLI
* `docker image` - zeigt alle Befehle an für `docker image`
* `docker image rm image-id/name` - Image löschen
* `docker image ls` oder `docker images`
* `docker rmi image-id` - auch Image löschen
* `docker image prune` - nicht benötigte Images löschen (ungetaggte Images)
* `docker image prune -a` - alle Images, die nicht in einem Container benutzt werden

### 2 - Managing Docker Images
#### 1 - Inspecting Images
* in docker-Doku unter *docker inspect* und *docker image inspect*
* `docker image inspect image-id` - Ausgabe ist JSON
+ `docker image inspect image-id | grep xxx` 
* `docker image inspect image-id > datei.txt`
* Docker inspekt filtern lassen
    * `docker image inspect --help`
    * `docker image inspect image-id --format='{{.Id}}'` - die Image-Id ausgeben. `{{.}}` ist Pflicht sonst variable
    * `docker image inspect image-id --format='{{.ContainterConfig}}'` - den Inhalt von *ContainerConfig* unformatiert ausgeben.
    * `docker image inspect image-id --format='{{json.ContainterConfig}}'` - den Inhalt im Json-Format ausgeben
    * `docker image inspect image-id --format='{{.ContainterConfig.Hostanme}}'`
* man kann auch Ranges ausgeben
* alles hier gesagte gilt auch für `docker container/network inspect`
#### 2 - Using Image tagging
* Tag = Version des Images
* `docker iamge tag image-id name:tag name:tag` - Image dopplt taggen
* `docker image tag name:tag docker-hub-repo/name:tag` - für Decker Repos
#### 3 -Creating an Image from a file
* `docker build` hat viel Optionn -> *docker build*-Doku
* `docker build -f ./dd-docker .` - `.` ist Build-Context. `-f ./dd-docker` - fals *Dockerfile* *dd-docker* heißt
* `docker build --no-chache=true -f ./dd-docker .`
* Best Practices - Doku *best practices docker build`
    * *.dockerignore*
    * Sort Multi-line Arguments:
        * 
        ```dockerfile
        RUN apt-get update && apt-get install -y \
        bzr \
        cvs \
        git
        ```
    * hier `RUN apt-get update && apt-get install -y`, da sonst `apt-get update` gecachet wird
#### 4 - Modifying Image layers
* `docker image history image-name` - Layers ansehen
* Image bzw. Layer reduzieren => zu einem Layer machen
    1. Squash-Feature benutzen
        * `docker version` -> Experimental sollte enabled sein
        * `docker build --squash -t image-name .` 
    2. 
        * `docker container run -d image-name`
        * `docker container export container-name > image-tar.tar`
        * `docker image import image-tar.tar` 
        * `docker tag image-id image-name` dem importierten Image einen Namen geben
#### 3 - Understanding the Docker Registry
#### 1 - What is the Docker Registry?
* Docker Registry ist eine Application
    1. kann Local + Private sein
    2. kann public + Public/Private sein z.B.:
        * Docker Trusted Registry
        * Docker Hub
 
#### 2 - Deploying a registry
* auf der Docker-Doku-Seite steht wie man eigen Registry als Docker-Container startet
    * `docker run -d -p 5000:5000 --restart=always --name registry registry:2`
    * `docker tag image-name localhost:5000/image-name:version`
    * `docker push localhost:5000/image-name:version` 
* DTR - hat Web-Interface + weitere Features
    * man kann Organistaionen, User erstellen
#### 3 - Configuring a registry
* Docker-Doku checken
* ist per YAML gemacht
#### 4 - Logging into a registry
* `docker login` - sich in Registry einlogen (Default ist Docker-Hub) -> Username + Password eingeben
* `docker logout`
* `docker login localhost:5000` 
* `docker login ip`
#### 5 - Pushing, Pulling, and signing
* nach dem Einloggen werden auch mit `docker image ls` Registery Images angezeigt
* `docker tag image-name registery-name/image-name:version` - damit man Image Pushen kann
* Beim Push wird automatisch Repository erstellt
* `docker image repository-name/image-name` - Lokalen Image löschen
* Docker Content Trust - Image mit dem Private Key zeichnen = feststellen, dass es wirklich Image von demjenigen ist. (nur Enterprise)
* Docker Notary - Eigene Images zeichnen
#### 5 - Searching Docker registries
* `docker search image-name`
* `man docker search` 
* `docker search --filter "stars=3" fedora` - nach Fedora mit min 3 Stars Images suchen
* `docker search --limit=100 image-name` - Per Default werden nur 25 Treffer angezeigt.
* `docker search --filter "is-official=true" image-name`
* `docker search --filter "stars=3" --fitler "is-official=true" fedora` - mehrere Filters
#### 6 - Tagging Docker Images
* `docker tag` - Help anzeigen
* Tags für Images für Private Registry kann auch die *IP/image-name* sein 
#### 7 - Deleting Images from a registry
* `docker image rm --force id/name-image` - z.B auch bei laufendem Container deleten
* Registory-Images löschen => am besten per GUI, es gibt auch auch Scripts dafür