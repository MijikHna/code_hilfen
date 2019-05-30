### Resource 1
|**Docker Hilfe anzeigen**|
|----|
| <ul><li>`docker`</li> <li>`docker [docker-subcommand --help`</li></ul> |
| **Docker Basics** |
| <ul><li>`docker run -p 8000:8000`  - `-p port:port` = Port angeben </li></ul>
|<ul><li>`dockerd -D -H tcp://192.168.1.3:2376 --tls=false` - `-D` =Debug-Modus freischalten, `-H` = zur Konfiguration des tcp-Hosts danach also tcp….; `-tls=true/false` = tls aktivieren/deaktivieren</li></ul>
| </ul><li>`docker pull nginx` - Imgae herunterladen </li><li>`docker run -d --name demo_nginx -p 80:80 nginx` - nginx-Image unter Namen demo_nginx starten => localhost:80 kann man nginx erreichen</li><li>`docker exec -it demo_nginx /bin/bash` - Bash von demo_nginx aufrufen</li></ul>|
|`docker ps` = Dockerprozesse anzeigen|
|`docker commit demo_nginx my/nginx` - Änderungen im Container demo_nginx als my/nginx speichern|
|**Docker File**|
|<ul style="list-style-type:none">`FROM ubuntu:15.04` - Basis-Image spezifizieren</li><li>`RUN apt-get update RUN apt-get install -y php5 RUN echo „<?php echo ‚Hello Welt!‘;“ > /var/index.php` = was auf der Basis-Image weitergemacht wird</li><li>`WORKDIR /var`</li><li>`CMD [„php“, „-S“ „0.0.0.0:9090“, „-t“, „.“]`</li> </ul>|
|<ul><li>`docker build -t php-example .` - aus einem DockerFile ein Image erstellen, `-t xxx` = Name des Images</li><li>`docker run -it -p 9090:9090 php-example` - php-example starten|
|<ul><li>`ADD ./directory/to/add/ /path/into/the/container` - also wenn `index.php` im gleichen Ordner wie Docker-Image liegt kann man folgendes eingeben stat RUN-Zeile im Docker-File:<ul><li>`ADD ./index.php /var/index/php`</li></ul><li>`docker build -t mein_name/php-example .`</li><li>docker run -it -p 9090:9090 mein_name/php_example</li></ul>|
|**Repository**|
|<ul><li>`docker login` - sich in einer Registery anzumelden (z.B hub.docker.com)</li><li>`docker push kirillsafin/php-example` - image in die Registery hochladen</li><li>`docker rmi -f kirillsafin/php-example` - rmi löscht Image vom Laptop</li><li>`docker run -i -t -p 8000:8000 -v /home/gianarb/.ssh/id/rsa:/root/.ssh/id_rsa -v $PWD:/opt --network front-tier --memory 10M --name site gianarb/micro`</li><ul><li>`-i` - hält stdion offen</li><li>`-t` - weist eine tty zu</li><li>`-p` - teilt Port aus dem Container mit dem Host → hier Port 8000 bis 8000, man kann mehrere `-p`-es haben</li><li>`-v` - teilt Dateien und Verzeichnisse aus dem Host mit Container</li><`--network` - fügt dem Container dem Front-Tier-Netzwerk hinzu</li> <li>`--memory` - beschränkt verwendbaren RAM<li><li>`gianarb/micro` = Name des Images</li></ul></ul>|
|**Docker Basics 2**|
|<ul><li>`docker ps` - zeigt laufende Container an</li><li>`docker ps -a` - auch Liste der gestoppten Container</li><li>`docker exec container_name ls -lsa` - Befehl `ls -lsa` in dem Container container_name ausgeführt</li><li>`docker logs container_name` - Logs des Container container_name anzeigen</li><ul>|
|**Repository 2**|
|<ul><li>`docker pull gianarb/micro:1.0.0`</li><li>`docker push gianarb/micro`</li><li>`docker tag 5wgs46h gianarb/micro:1.0.1` - Image mit ID 5wgs46h mit tag 1.0.1 tagen</li><li>`docker tag 5wgs46h registry.gianarb.it:gianarb/micro:1.0.1` - tagen und in Registery schieben
|**Docker Basics 3**|
|<ul><li>`docker inspect 5wgs46j` - Inof über Images und Container</li><li>`docker inspect 5wgs46j format` - CLI-Output in JSON konvertieren</li></ul>|
|<li>`docker start/stop/restart/kill 464gts4` - Container starten</li>|
|<ul><li>`docker run -it -v /tmp ubuntu /bin/bash` - `-v` = neues Volumen erstellen und dem Container hinzufügen</li><li>`docker run -it -v /tmp -v /opt ubuntu /bin/bash` = mehrere Volumes verbinden</li></ul>|
|**Repository 3**|
|<ul><li>`docker save gianarb/micro > micro.tar.gz` - Image Verpacken</li><li>`cat micro.tar.gz | docker import – my/micro:new` - docker import http://example.exampleapp.com/micro.tar.gz</li></ul>|
|**Volumes**|
|<ul><li>`VOLUME /tmp` - Volume in Docker-File anhängen</li><li>`-v /tmp:/tempory` - Verzeichnis aus dem Host /tmp dem Container als Volume :temporary einhängen</li><li>`docker run -it -v /tmp ubuntu /bin/bash -v /tmp` - Volume /tmp anlegen</li><li>`docker run -it -v /tmp -v /opt ubuntu /bin/bash` - 2 Volumes erstellen</li><li>`docker volume ls`</li><li>`docker volume create`</li><li>`docker volume rm`</li> <li><- Volumes anzeigen/schaffen/loeschen</li><li>`docker run --rm --volumes-from img_avatar -v $PWD: /backup ubuntu tar cvf /backup/backup.tar /var/www/front/public/avatar` - mit `--volume …` = Volume aus anderem Container anhängen</li></ul>|
| |
|`docker run --name mysql-service -e MYSQL_ROOT_PASSWORD` - `root -d mysql` = Container mysql-service mit root-Passwort „root“|
|`docker run --name my-wordpress -e WORDPRESS_DB_PASSWORD=root -e WORDPRESS_DB_HOST=mysql.my-wordpress --link mysql-service:mysql.my-wordpress -d wordpress` - `--link …:…` = |
|**Netzwerk**|
|<ul><li>docker erstellt automatisch docker0 NW</li><ul><li>`docker network create nw-test` - NW erstellen</li><li>`docker run --name mysql-service -e MYSQL_ROOT_PASSWORD=root --network nw-test -d mysql`</li><li>`docker run --name my-wordpress -e WORDPRESS_DB_PASSWORD=root --network np-test -d wordpress`</li></ul><li>Docker hat eigenen DNS-Server, wenn man eigene NW erstellt</li></ul>|

### Resource 2
|**Basics 1**|
|-----|
|<ul><li>`docker ps`</li><li>`docker ps -a`</li><li><- Container anzeigen<li><ul>|
|<ul><li>`docker run -it con_name sh` - `-it` = hängt tty dem Container + öffnent diese => man kan im Contaier weitere Befehle ausführen</li><li>`docker run --help`</li><li>`docker rm container-id1 container-id2` - mehrere Contaier direkt löschen</li><li>`docker rm $(docker ps -a -q -f status=exited)` - löschte alle Container, die exited sind</li><li>`docker container prune` - alle exited Container löschen<li>`docker rmi ImgaeName` - Löschen Images, die man nicht braucht</li><li>`docker run --rm Container` - führt Container aus, wenn exited, löscht ihn</li><li>`docker run -d -P –name lala Image` - `-P` = wählt Ports selber ausführe</li><ul><li>`docker port lala` - zeigt Ports, die gewählt wurden</li></ul></ul>|
|**Docker Images**|
|<ul><li>python ubuntu, busybox, hello-world</li><li>`user/imgae-name` - User Images</li><li>onbuild-Version des Images = hat bestimmte Vorinstallationen schon erledigt</li></ul>|
|*Docker-File*|
|<ul style="list-style-type:none"><li>`FROM lala` - welche Image gestartet werden soll</li><li>`EXPOSE 5000` - verwendete Port freigeben</li><li>`CMD [„python“, „./app.py“]` - innerhalb des Containers python .app.py starten</li><li></li><li>`docker build -t Verzeichnis/DockerFile .` - DockerFile starten=Image erstellen, `-t` = Lokation für den Images angeben</li></ul>|
|**Docker Hub (offentliche Registery)**| 
|<ul><li>`docker push image_Name` - image_Name in die Reg. Hochladen</li><li>`docker login`</li></ul>|
|**Bsp: DockFile**|
|<ul style="list-style-type:none"><li><code>FROM ubuntu:14.04 </br>MAINTAINER Kirill Safin</br>RUN apt-get -yqq update</br>RUN apt-get -yqq python-pip</br>RUN curl -sl https://deb/nodesource.com/setup8.x \| base</br>RUN apt-get install -yq nodej</br>ADD flask-app /opt/flask-app</br>WORKDIR /opt/flask-app</br>RUN npm install</br>RUN npm build</br>RUN pip install -r requirements.txt</br></br>EXPOSE 5000</br>CMD [„python“, „./app.py“]</br>.yqq #= Ausgabe ausblenden + YES zu allem</br>ADD Quelle_auf_Host Ziel_im_Container
</code></li></ul>|
|**Netzwerk**|
|<ul><li>`docker network ls` - zeigt NW, die Docker erstellt in bridge NW laufen die Containers per default</li><li>`docker network inspect bridge` - Details von NW bridge anzeigen</li><li>`docker network create nw-name` - eigenes NW erstellen</li><li>`docker run -d --name cont_name --net nw_name -p 9200:9200 -p 9300:9300 -e  „discovery.type=single-node“ docker.elastic.co/elasticsearch/elasticsearch:6.3.2` = mit `--net` den Container mit bestimmten NW laufen lassen</li><ul>||**Weitere Docker-Tools**|
|<ul><li>Docker Machine</li><li>Docker Compose</li><li>Docker Swarm</li><li>Kubernetes</li></ul>|
|**Dcoker-Compose**|
|<ul><li>mit *docker-compose.yml* erstellen, darin die Konfigurationen für zu laufende Container reinschreiben</li><ul><li>`docker-compose up` - führt die Datei docker-compose.yml aus</li><li>`docker-compose up -d` - im detached Mode laufen lassen</li><li>`docker-compse ps` - zu laufende Container anzeigen</li><li>`docker-compose down -v` - Container stoppen</li></ul><li>Vorteil: erstellt selber NW, da man ja mehrere Container gleichzeitig laufen will</li><li>docker-compose run web bash = im Container „web“ bash starten</li></ul>  

|**Resource 3**|
|---|
|<ul><li>`docker search ubuntu` - in Docker Registery nach Ubuntu images suchen</li><li>`docker pull ubuntu` - Image von Docker Registery herunterladen</li><li>`docker ps -l` - zeigt den letzten Container</li><li>`docker commit -m „Kommenatar“ -a „Author“ container-id neuerImgaeName1/lNeuerImageName`</li></ul>|