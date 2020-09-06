* Seite: https://nuancesprog.ru/p/6482/
+ Gute Daten Basen für Vulnabilities:
    1. CVE: https://cve.mitre.org/
    2. NVD: https://nvd.nist.gov/
    3. VULD: https://vuldb.com/
* Idee: aus diesen DB die Vulnabilities lesen und die Schichten in Dockerfiles auf diese testen => Dockerfile muss gestartet werden
* Bsp: Anchore Engine: (Es gibt noch: Clair, Dadga, Nexus Repository Pro, Black Duck, Qualys, Harbor, Twistlock):
    1. Anchore installieren: `curl https://raw.githubusercontent.com/anchore/anchore-engine/master/docker-compose.yaml | docker-compose -p anchore -f - up`; Anchore besteht selbst aus Dcoker-Containers (5 Container, die dann die DB mit Vulnabilities auslesen und Dockerfiles prüfen)
    2. Anchore-Client starten = Anchore-CLI starten: `docker run --rm -e ANCHORE_CLI_URL=http://anchore_engine-api_1:8228/v1/ --network anchore_default -it anchore/engine-cli`; `anchore-cli --version`
    3. Docker-Image prüfen (Bsp: WordPress-Image prüfen): `anchore-cli image add wordpress:4.6.0 && anchore-cli image wait wordpress:4.6.0`
    4. Vulnability-Bericht prüfen: `anchore-cli image vuln wordpress:4.6.0 all`
* Das ganze sollte man in CI/CD integrieren