### 1 - Grundlagen zu Kubernetes
#### 1 - Warum Kubernetes
* früher als Monalit = feste Beziehunen zwischen Kompomenten = All in One
    * Vorteil: einfach bereitzustellen
    * Nachteil: schlechte Wartbarkeit/Erweiterbarkeit
* dann Verticals: App in vertikal zerlegt = Apps entkoppelt
* jetzt Probleme:
    1. schnelle Deployments
    2. geringerer Time-to-Market
    3. bessere Reaktion/Skalierbarkeit
    4. mehr Automatisierung
    5. Rollbacks
    6. niedrige Kosten
* => CloudNative-Applikationen:
    1. Architektur
    2. Middleware
    3. Organisation
    4. Culture
* = Microservices:
    1. sehr klein + unabhängig
    2. spezifisch betrieben (hier Kubernetes)
    3. ein Mikroservice = ein Zweck
    4. kommunizieren über HTTP oder Message-Qeues
* Mikroservice = Container => einfach bereitzustellen, versionierbar, leichgewichtig (Ursprung in Linux-Kernel)
* Kuberntes (Steuerman) = Container betrieben; von Google angefangen ~ Betreibssystem für CloudNative-Applikationen
 
#### 2 - Geschichte und Einordnung
* basiert auf Borg (Google-internes System für Management)
* Omega - Weiterentwicklung von Borg
* Kubernets - basiert auf Borg und Omega -> aber Open-Source
    * Orchestrator-Aufgabe: Einzelkomponenten in Beziehung zu setzen
    * Back-End-System = stellt Applikationen bereit; stellt Laufzeitumgebung für Apps = abstrahiert Umgebung wo Apps laufen
#### 3 - Nodes
* = Kubernetes-Cluster zu betrieben ~ VM oder so
* Node-Arten:
    1. Master Nodes
        1. System-Services bereitstellen
        2. Steuerung des System
        3. meistens keine Workloads 
        4. ungerade Anzahl von Master-Nodes
        5. stellt Komponenten bereit:
            1. API-Server (REST), um an Kub Nachrichten zu senden = steuern
            2. Controller-Manager ~ als Task-Manager Task überprüfen und reagieren
            3. Scheduler - deployen, skalieren usw. - redet mit Worker-Nodes
            4. Control Panel(s) - GUI für API-Server
            5. etcd-DB - alle Kub-Einstellungen werden hier gespeichrt. Wenn die Master-DB nicht synchron sind => etwas ist schief gelaufen
        * über **kubectl** kann man mit API-Server reden
    2. Worker Nodes
        1. Workloads (Apps) ausführen
        2. reagieren auf API-Server
        3. geben Rückmeldungen an API-Server
        4. Komponenten:
            1. Kubelet ~ Agent
            2. Container Runtimes/CRI - Abstraktion für Container (z.B für Docker) -> kann unterschiedliche CRIs in einem Cluster geben + können nachinstalliert werden
            3. Kube Proxy - NW für interne Cluster
#### 4 - Pods und Deployment
* App besteht aus Microservices; Microservices weden in Container verpackt; Container werden dann in Kubernetes verpackt und ausgeführt <- sind aber nicht direkt in Kubernetes bereitstellbar => müssen in Pods verpackt werden
* Pod = Wrapper um Container; als YAML als Manifest-Datei -> beschreibt, was zu deployen gilt; = kleinste Deployment-Einheit
* Pod-Spezifikation (yaml-Datei) - gibt an welche Komponente man deployen möchten (hier Pod), namen der Komp, Label-namen, Spezifikaiton = wecher Container, welcher Image, welches start-Commando für Container:
```yaml
apiVersion: v1.0
kind: Pod
metadata:
    name: myapp-pod
    labels:
        app: myapp
    spec:
        containers:
            - name: myapp-container
                image: busybox
                command: ['sh', '-c' 'echo Hello Kub && sleep 3600' ] 
```
+ so macht man aber nicht => stattdessen **Deployments**
* Deployments definieren den Zustand:
    1. Anzahl der Replikas = wie viele Instanzen des Pods
    2. Gesundheitsstrategie
    3. Rolling Updates
    * Kubernetes stellt dann diesen Zustand auf den Nodes
* DaemonSets definieren - Pod auf allen Nodes laufen lassen:
    1. Pods auf jedem Node im Cluster
    2. für Infrastrukturaufgaben z.B Logs sammeln, Zustandsüberwachung des Systems
    3. DaemonSets werden auf neuen Pods dann automatisch ausgeführt
* Deployments und DaemonsSets sind Statelos => StatefulSets einsetzen = zustandsbehaftete Komponenten einführen:
    1. Reihenfolge beim Start/Update definieren
    2. bestimmte IDs festlegen (per Default Random-IDs)
    3. gleichen Speicher-Block zuweisen
* CronJob definieren, wenn Pods/Jobs nach Zeitplan laufen sollen 
* FAZIT: Schema:
```xml
<deployment/daemonset/statefulset/cronjob>
    <pod>
        <container>
            app
        </container>
    </pod>
</deployment/daemonset/statefulset/cronjob>
```
#### 5 - Labels und Annotation
* = Deployments und Pods "kategorisieren"
* Labels = Schlüssel-Wert-Paare, Schlüssel müssen auf jedem Objekt eindeutig sein
    * werden zur Fitlerung verwendet
* Annotationen = Schlüssel-Werte-Paare; Meta-Informationen
* in JSON/YAML-Format
```json
//Labels:
"metadata": {
    "labels": {
        "key1": "value1",
        "key2": "value2"
    }
}

"metadata": {
    "annotations": {
        "key1": "value1",
        "key2": "value2"
    }
}
```
+ Label-Selektoren, um zu Filtern
    1. wertbasierende => auf Gleichheit/Ungleichheit verglichen
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
        name: ...
    spec:
        ...
        nodeSelector:
            accelerator: nvidia-tesla-p100
    ```
    2. set-basierende - Auswahl anhand von Existenz einer Werteliste; mögliche Operationen:
        1. `In` im Label
        2. `NotIn` nicht im Label
        3. `<Key>` = KeyName existeirt
        ```yaml
        # ..
        matchExpressions:
            - {key: tier, operator: In, values: [cache]} # tier = cache
            - {key: environment, operator: NotIn, values: [dev]} # environemnt != dev
        ```
#### 6 - Services
* Service vs. Pod
    * Services sind für Pods zuständing
    * Pod = Unit-Of-Work; werden skaliert, terminiert; im Fehlerfall neu gestartet; neue IP bei Neustart; sind volatil
    * Service = verbirgt ein Set von Pods, hat eindeutige/unveränderliche IP; hat Load-Balancer-Funktionalität für interne Pods; ist stabil
    * Schema:
    ```xml
    <depoloymentA>
        <pod name="prod"></pod>
        <pod name="test"></pod>
    </depoloyment>

    <depoloymentB>
        <pod name="prod"></pod>
        <pod name="stage"></pod>
        <pod name="prod"></pod>
    </depoloyment>

    <service>
        <label name="prod"></mode>
    </service>
    ```
    * Service erkennt für welche Pods er zuständig ist anhand von Labels
    * Service-Definition ist YAML
    ```yaml
    kind: Service
    apiVersion: v1
    metadata:
        name: prod-service
    spec:
        selector:
            mode: prod
        ports:
            -protocol: TCP
                port: 80
                targetPort: 9376
    ```
    * also Service representiert Pods nach außern. Über Services werden Pods gemanagt
#### 7 - Ingress
* bei bestimmten "States" besimmte Services ausführen => über Ingress-Controller
* spezielel Form von Service (verbirgt Komponente nach außen)
* erlaubt Zugriff per HTTP/S
* arbeitet regelbasiert = Services nach bestimmten Regeln anschmeißen
* bis Ingress wird per SSL geredet, dann bis zu den Pods per HTTP
```xml
<ingress>
    <service1>
        <deployment1></deployment1>
        <deployment2></deployment2>
    </service1>
    <service2>
        <deployment3></deployment3>
        <deployment4></deployment4>
        <deployment5></deployment5>
    </service2>
</ingress>
```
* Anfragen landen im Ingress landen und Ingress schmeißt dann entsprechenden Service an
* Ingress als YAML definiert
```yaml
# ...
spec:
    rules:
    - host: foo.bar.com
        http:
            paths:
            - path: /foo
                backend:
                    serviceName: service1
                    servicePort: 4200
            -path: /bar # wenn Ingress Nachricht /bar bekommt => wird service2:8080 angeschmießen
                backend:
                    serviceName: service2
                    servicePort: 8080
```
#### 8 - Storage
+ es gibt zwei Ansätze
    1. Volumes
        + auf Pod-Ebene definiert => Lebenszyklus = dem von Pod
        * => für temporäre Daten
        ```yaml
        #...
        volumes:
            - name: test-volume
                hostPath.
                    path: /data
        ```
    2. PersistentVolumes
        + unabhängig von Pods definiert => unabhängiges Lebenszyklus 
        + => persistente Daten
        * drei Klassen:
            1. PersistentVolume (optional) = dauerverfügbares Volume, ist aber nicht direkt an Pod bindbar
            ```yaml
                #...
            spec:
                storageClassName: standard # abhängig von der OS
                capacity: 
                    storage: 10Gi
                accessModes:
                    - ReadWriteOnce # Once = nur ein Node lesen+schreiben; 
            ```
            2. StorageClass (optional)
            ```yaml
            #...

            provisioner: kubernetes.io/aws-ebs #Plug-In für Erzeugung von Volumen (OS-abhängig)
                #...
            reclaimPolicy: Retain/Delete # wie mit Storage umgehen, wenn nicht mehr benötigt
            mountOptions:
                - debug
            volumeBindingMode: Immediate/WaitForFirstCustomer # wie mit Storage-Class umgegangen wird
            ```
            3. PersistentVolumeClaim - Volume für Pod anfordern = PersistentStorage und VolumeClasses zusammenführen; Volumes werden per Volume-Params identifiziert.
            ```yaml
               #...
            metadata:
                name: persistent-standard-claim
            spec:
                storageClassName: standard # abhängig von der OS
                accessModes:
                    - requests:
                        storage: 3Gi
            ```
        * Use-Cases: für DBs
* auf dem Pod Volume mounten.
```yaml
kind: Pod
apiVersion: v1
metadata: 
    name: mypod
spec:
    containers:
        # ...
    volumes:
        - name: persistentVolume
            persistentVolumeClaim:
                claimName: persistent-standard-claim #Name des VolumeClaims
```
### 2 - Kubernetes aufsetzen
#### 1 - Wo betreibt man Kubernetes
1. public Cloud -> als PaaS - Platform as a Service (wird von Cloud-Anbieter bereitgestellt z.B Azure (AKS - Azure Kubernetes Service), AWS (EKS - Amazon Elastic Container Service for Kubernetes), Google (GKE - Google Kubernetes Engine))
2. selbst aufgesezte => muss man selbst alles einstellen (= mehr Freiheit); Wartung selbst;

* Lokales Kubernetes = gut für Testumgebung
    1. Kubernetes in Docker (Docker + Kubernetes)
    2. Minikube - komplexeres Setup
    3. Play with Kubernetes - komplett Online (Testsetup)
#### 2 - kubeadm und kubectl
* = Kubernetes verwaleten.
1. kubeadm - AdminTool für Kub
    * Aufgaben:
        1. Cluster aufsetzen
        2. Cluster updaten
        3. Worker-Nodes updaten
    * über kubernetes.io installieren -> nur auf Linux möglich
2. kubectl - Management-Tool
    * Wrapper um REST-API
        1. erlaubt Scripting und Versionierung
        2. Typische Tasks:
            1. Deployments und Upgrade von Workloads
            2. Anlegen von Kubernetes-Obj
            3. Zugriff auf Informationen und Status
            4. Konfig und Installation von Komponenten
            5. Löschen von Komponenten
            6. scaling
    * von kubernetes.io installieren
#### 3 - Tests mit Play wit Kubernets durchführen
* auf labs.play-with-k8s.com kann man mit Docker- oder Github-Account anmelden
* `kubeadm init` - Cluster anlegen
* Ablauf:
    1. Add new instance => Master
    2. Add new instance => Worker
    3. Master auswählen:
        1. `kubeadm init --apiserver-advertise-address ${hostname -i}` - Cluster initialisieren = VM für Kub vorberetien
        2. `kubectl get nodes` - Nodes auflisten
        3. NW auf dem Cluster anlegen + aktivieren (es gibt verschiedene NW-Anbieter (hier wird Weave verwendet)): `kubectl apply -n kube-system -f "https://cloud.weave/works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"`
        4. `kubectl get nodes` - eventuell braucht ein paar Sekunden warten
        5. Workder-Node anlegen: auf dem Workder `kubeadm join PARAM` -> eventuell den Befehl vom Master bekommen (PARAM = ip + token + ..)
        6. auf Master: `kubectl get nodes`
        7. Nginx deployen: <-  wird direkt auf Master vorgeschlagen 
        8. `kubectl get deployments` - Deployments/Pods anschauen
        9. `kubectl get pods` - Pods checken
        10. `kubectl get services` - Services = laufende Apps schecken => eventuell über Browser zu der API navigieren
    4. 
#### 4 - Kubernetes lokal ausführen
* Windows: 
    1. HW-Virtualisierung aktivieren
    2. Windows 10 Pro
    3. Hyper-V
    4. Docker for Windows
* `kubectl get cluster`  - Cluster-Nodes werden angezeigt. Es wird `docker-for-dekstop` angezeigt -> da ein VM mit Docker aufgesetzt wird
* `kubectl get namespaces` - NS ansehen
    * NS trennt Resourcen
* Dashboard installieren:
    * `kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboars/master/src/deploy/alternative/kubernetes-dashboard.yaml`
    * `kubectl get deployments -n kube-system` -> kubernetes-dashboard wird auch angezeigt
    * auf Dashboard zugreifen -> nicht über IP möglich (wegen Sicherheit) ABER:
        + `kubectl proxy` benutzen => Aufrufe im Browser werden direkt an Kub weitergeleitet und als interner Aufruf betrachet
        + http://localhost:8001/api/v1/namespaces/kube-system/services/http:kubernetes-dashboard:/proxy/  -> eventuell als Lesezeichen speichern
* Aufräumen: 
    1. Dashboard deinstallieren: `kubectl delete -f http://localhost:8001/api/v1/namespaces/kube-system/services/http:kubernetes-dashboard:/proxy/`
    2. in Settings von Docker+Kubernetes-GUI komplett reseten
* `kube get deployments -n kube-system` - Deployments des NS kube-system ansehen
* `kube get services -n kube-system` - Services von NS kube-system
#### 5 - Kubernetes und Azure
* AKS-Cluster in Azure anlegen:
* Requirements:
    1. auf lokalen Maschine sollte **Azure CLI** installiert sein
    2. Azure Subscription
    3. Verknüpfen Subscription mit CLI `az login`
* Schritte:
    1. `az group create --name RESSOURESEGRUPPE --location STANDORT` - RESSOURCEGRUPPE = Name des Clusters/Nodes in Azure; STANDORT = wo Speicher liegen sollte `az group create --name kirill-res --location westeurope`
    2. `az aks create --ressource-group  RESSOURCEGRUPPE --name CLUSTERNAME --node-count ANZAHL_NODES --enable-addons monitoring --generate-ssh-keys --node-vm-size Standard_A1_v2` - `--node-vm-size` - sollte man bei Azure nachschauen. Es wird Info als JSON returnt
    3. kubectl installieren + konfigureiren
        1. `az aks install-cli` oder Doku von K8 schauen
        2. `az aks get-credintials --resource-group RESSOURESEGRUPPE --name CLUSTERNAME`
    4. Dashboard aufrufen:
        1. `az aks browse --resource-group RESSOURESEGRUPPE --name CLUSTERNAME` - eventuell muss an NS manuel eingeben, damit sie ordentlich angezigt werden
    5. aus lokalem K8 mit Azure reden: `kubectl get geployments -n kube-system`
    6. `az aks scale --resource-group RESSOURESEGRUPPE --name CLUSTERNAME --node-count ANZAHL` - Nodes-Anzahl ändern
    7. `az delete --resource-group RESSOURESEGRUPPE --name CLUSTERNAME` - Cluster löschen
#### 6 - Kubernetes und AWS 
* EKS - Kubernetes von AWS
* Requiremtens:
    1. AWS CLI
    2. AWS Subscription
    3. EC2-Key-Pair anlegen ~ ssh für AWS
* Schritte:
    1. EKS-Service-Rolle in AWS-Konsole erstellen (über Browser https://console.aws.amazon.com/iam)  + ARN-Rolle notieren (Role -> EKS -> Role ertellen)
    2. Cluster-VPC (Virtual NW) erstellen; Subnet-IDs und Security-Group-IDs notieren
        * CloudFormation -> Standaro auswählen (Ireland) -> Template + Template von EKS reinkopieren -> Namen für Stack geben -> Alles überprüfen -> Create klicken
        * Outputs kopieren
    3. kubectl installieren

    4. aws-iam-authenticator for Amazon EKS installieren (eine Ausführungsdatei) = herunterladnen und ins AWSCLI-Ordner reinkipieren
        * `aws-iam-authenticator help`
    5. Cluster anlegen: `aws eks create-cluster --name NAME --role-arn ROLLEN-ARN --resources-vpc-config subnetIds=>IDs, securityGroupsIds=SEC-IDs` - Return ist JSON mit Angaben
        * `aws eks desciibe-cluster --name NAME --query cluster.statsu` - Status des Cluster fragen
    6. mit Cluster verbidnen:
        1. sich mit Cluster verbinden: `aws eks update-kubeconfig --name NAME`
        2. dan kann man kubectl verwenden: `kubectl get svc`, `kube get nodes`, `kube pods -n NS`
    7. Nodes anlegen:
        1. im Browser in AWS CloudFormation-Template verwenden Create Stack -> EKS-Template für Nodes verwenden (Doku schauen)-> Cluster-Name Group, Node-ID EC2-KayPair nageben -> Return NodeInstanceRole notieren + Outputs notieren
        2. ConfigMap-Datei hinzufügen -> in der Datei ist ein Platzhalter, da mit NodeInstanceRole-Wert einstezen
        3. `kubectl apply -f aws-auth-cm.yml` - die Datei zurück an den Cluster senden
#### 7 - Kubernetes und AWS: Dashboard
* `kubectl apply -f https.//raw.git...yml` - Dashboard installieren
* `kubectl proxy` - Proxy starten, das Dachboard nur für localhost geöffnet ist => Verbindung muss durch Proxy gehen => kubectl bekommt die Adresse von Proxy gesagt
* Token-Anmeldung:
    1. Serivce-Account anlegen -> yaml-Datei
    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
        name: eks-admin
        namespace: kube-system
    ```
    2. `kubectl apply -f eks-create-account.yaml`
    3. Account mit cluster-admin-Rolle verknüpfen -> wieder mit yaml
    ```yaml
    apiVersion: v1
    kind: ClusterRoleBinding
    metadata:
        name: eks-admin
    roleRef:
        apiGroup: rbac.authorization.k8s.io
        kind: ClusterRole
        name: cluster-admin
    sujects:
        kind: ServiceAccount
        name: eks-admin
        namespace: kube-system
    ```
    4. `kubectl apply -f eks-bind-account.yaml`
    5. Token abrufen:
        1. `kubectl get secret -n kube-system` alle User-Obejkte anzeigen -> ID/Name des Token kopieren
        2. `kubectl describe secret TOKEN-ID/NAME -n kube-system` -> wird Token angezeigt kopieren ODER alles als einer Befehl auf Linux: `kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk {'print $1'})`
    7. Dashboard jetzt aufrufen -> also Proxy starten und dann Token eingeben
#### 7 - Kubernetes und AWS: Aufräumen
1. bei alle Workloads öffentlihen IPs auf AWS löschen
2. in AWS -> CloudFormatin -> Stack mit Nodes -> Action = delete
3. in der EKS-WebGui -> Cluster löschen
4. in CloudFormation -> EKS-Stack löschen
#### 8 - Kubernetes ung Google Cloud
* Requirements:
    1. Google Cloud SDK local installieren
    2. Google-Cloud-Account
    3. mit `gcloud init` Cloud-Account verbinde mit SDK
    4. Compute Engine API aktiveren über Web-GUI
* Schritte:
    1. Projekt in Cloud SDK anlegen: `gcloud config set project PROJ-ID` - wird nur lokal auswirkt
    2. Computer-Zone festelgen = Standardort: `gcloud config set compute/zone ZONE` - nur lokal auswirkt
    3. Cluster anlegen: `gcloud container clusters clreate CLUSTERNAME`
    4. mit Cluste verbinden: 
        1. K8s installieren: `gcloud components install kubectl` oder über Web-Gui herutnerladen
        2. kubectl konfigurieren: `glcoud container cluster get-credentials CLUSTERNAME`
        3. Auth durchführen: `gcloud auth application-default login` -> im Browser weitermachen = kubectl kann mit Cluster reden
    5. Dashboard aufrufen: 
        1. `kubectl cofnig view` - Token für Dashboard anzeigen
        2. `access-token` kopieren
        3. `kubectl proxy`
        4. URI (Adresse bookmarken) und öffnen
        5. Token einfügen
    6. als alternative zu Dashboard kann man Google-Console verwenden
    7. `gcloud container clusters resize CLUSTERNAME --size 2` - Node aus 2 setzen
    8. Cluster entfernen: `gloud container cluster delete CLUSTERNAME`

### 3 - Kubernetes konfigurieren
#### 1 - Namensräume verwenden
* wenn merhrere Projekte in einem Cluster laufen z.B Prod und Dev => über NS geregelt
* Abgrenzung von Applikationen und Zuständigkeiten
* bilden virtuelle Cluster
* K8 hat ein paar vordefinierte NS:
    1. kube-public - für alle lesbar
    2. kube-system - nur von K8 lesbar
    3. default - alles andere, hier werden User, Apps
* eigene NS definieren:
    1. NS in yaml anlegen.
    2. diese yaml dann an Cluster übertragen `kubectl create -f NAME.yaml`
    ```yml
    apiVersion: v1
    kind: Namespace # welcher Objekt-Typ angelegt werden soll
    metadata:
        name: development #Namespace=development
        labels: #optional
            "name": "dev"
    ```
    3. man kann auch NS direkt mit kubectl erstellen: `kubectl create namespace NAME`
* `kubectl pods -n development` - Pods von NS development erstellen
* `kubectl pods -n kube-system`

* kubectl mit NS verknüpfen um nich immer `-n NS` eingeben
    1. `kubectl config view` - aktuelle Kubectl-Config der Views (Cluster - Benutzer) anzeigen
    2. `kubectl config set-context NAME --namespace-NS --cluster-CLUSTER --user-USER-ID` - `kubectl config set-context NAME --namespace-development --cluster-docker-for-desktop-cluster --user-docker-for-desktop` = Context dev erstellen für cluster, user und NS erstellen
    3. `kubectl config use-context NAME` - diesen Context aktivieren

* `kubectl get namespaces --show-labels` oder `kubectl get namespaces` - NS anzeigen
* `kubectl delete namespace NAME` - 
#### 2 - Sicherheit: Rollen
* Rollen + Rollen-bassierte-Athentifizierung
* RBAC - Role Based Access Control - eine von mehreren K8-Tools zur Absicherung der K8-Ressourcen; an REST angelehnt
* Verwendung:
    1. User-Accounts mit Rechnten versehen = nicht jeder K8-Bunutzer kann alles mit K8-Cluster alles machen = User-Zugriff auf K8-API
        + Default: über K8-API nur Info abrufen nicht ändern
* Ressoursen = URIs
    * sind in API-Groups gegliedert
        1. core
        2. app
        3. batch
        4. extensions
        5. autoscaling
    * es gibt Verben = Operationen auf Ressourcen
        1. create
        2. get
        3. delete
        4. deletecollection
        5. list
        6. update
        7. watch
        8. patch
        9. exec
        10. impersonate
* Rollen = Ressource + API-Group + Verb
* 2 Arten der Rollen
    1. Role = auf Ebene von NS gültig
    2. ClusterRole = auf Clusterebene gültig
        * Standard-Clusterrollen:
            1. cluster-admin = kann alles
            2. admin
            3. edit
            4. view
        * `kubectl describe clusterrole NAME` - Rolle anzeigen oder: `kubectl ger clusterrole NAME -o yaml > Datei.yaml` - Ausgabe als yaml speichern
            * z.B: `kubectl describe clusterrole edit`
* Rollen anlegen + ändern:
    1. prüfen, ob aktuelle User es darf
    2. per kubectl
    3. über yaml-Datei = Dokumentation + Wiederholbarkeit + Versionierung
    ```yaml
    kind: Rolle
    apiVersion: alala/v1beta
    metadata:
        namespace: k8s-lala
        name: k8s-lala-role
    rules:
        - apiGroups: ["", "extensions", "apps"] # ""=core
            resources: ["", ""replicasets", "pods"]
            verbs: ["get", "list", "watch", "create", "update"]
    ```
    * `kubectl create -f alal.yaml -n k8s-lala` - yaml an K8 schicken
#### 3 - Sicherheit: Accounts = Subject und Bindings
* Sicherheit => Accounts + Bindings
* Accounts:
    1. User-Accounts = menschliche Benutzer => werden meist über externe Systeme authentifiziert (z.B. Tokens)
    2. Service-Accounts => Token für Authentifizierung. Token wird bei erstellung des Services erzeugt.
        1. über kubeclt erstellen
        2. über yaml-Datei
        ```yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
            name: k8s-service-account
        ```
        * `kubectl create -f lala.yaml -n NS_NAME` - an Cluster übertragen
        * `kubecelt describe serviceaccount -n NS_NAME`
* Rolle mit Subject verknüpfen = Satz mit Berechtigungen für Ressourcen => mit:
    1. RoleBindings = Rolle im NS mit Subject
    2. ClusteRoleBindings = Rolle im Cluster mit Subject verknüpfe
    * mit yaml oder kubectl
    ```yaml
    kind: RoleBinding # welces Binding
    apiVersion: v1
    metadata:
        name: role-binding # Name für diesen RoleBding
        namespace: myNS # soweit zutreffen
    subjects: # hier die Verknüfung mit Service oder User-Account herstellen
        kind: ServiceAccount
        name: k8s-service-account
        apiGroup: ""
    roleRef:
        kind: Role
        name: my-role
        apiGroup: ""
    ```
    * `kubectl create -f lala.yaml -n NS_NAME`
    * `kubectl rolebindings -n NS_NAME` 
* Rolle, Accounts, Bindings ändern
    1. yaml, die für Erstellung verwendet wurde, modifizieren. und mit `kubectl apply -f lala.yaml n NS_NAME` an Cluster übertragen
    2. `kubectl edit ART NAME -n NS_NAME` - mit kubectl => lädt yaml herutner und öffnet sie zum verändern. Wenn man Editor wieder schließt => wird an Cluster veränderte yaml übertragen
* Rollen, Accounts, Bindings lsöchen
    1. `kubectl delete ROLE NAME -n NS_NAME`
        * `kubectl delete role my-role -n NS_NAME`
        * `kubectl delete rolebinding my-binding -n NS_NAME`
        * `kubectl delete serviceaccount my-service-account -n NS_NAME`
### 4 - Applicationen deployen
#### 1 - Applikation bereitstellen
* Deployment = eine Application = ein oder mehrere Pods; Pods in der Regel ein Container
* Deployment ist zustandslos. Wenn Deployment heruntergefahren wird (Pod = Container heruntergefahren) => geht alles verloren
* Deployment als ymal oder kubectl definieren
* Schritte:
    1. Docker-Image für Pod
        1. Dockerfile erstellen
        2. docker builden und pushen zu Docker-Registery
    2. Deployment-Datei
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
            name: my-deployment
        spec:
            selector:
                matchLabels:
                    app: my-deployment
            replicas: 2
        template: 
            metadata:
                labels:
                    app: my-deployment
            spec:
                containers:
                - name: my-pod
                    image: hub-account/my-container:latest
                    ports:
                    - containerPort: 8080
         # ...
        ```
        * yaml and Cluster senden: `kubectl create -f lala.yaml -n NS_NAME`
        * `kubectl get deployments -n NS_NAME`
        * `kubectl get pods -n NS_NAME` - pods anzeigen -> z.B einen kopieren und
        * `kubectl describe pods kopierter_name -n NS_NAME` z.B IP im Cluster
        + `kubeclt exec -n NS_NAME -it kopierter_pod_name -- /bin/bash` - sich im Container des Pods anmelden
        + `kubectl delete -f lala.yaml -n NS_Name` oder `kubectl delete deployment DEP_NAME -n NS_NAME` - Deployment löschen
#### 2 - Applikation bereitstellen: MySQL
* Bsp: MYSQL deployen
    * Problem: mySql benötigt persistenten Speicher
        * => für mySql Speicher mit PersistentVolume verwenden
        * diesen Volume dann in Deployment angeben
    * Passwörter für Db mit `Secret` erzeugen
        * `kubectl create secret generic NAME --from-literal=password=PWD` 
* Schritte:
    1. PersistentVolumeClaim definieren:
        1. yaml-Datei
        ```yaml
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
            name: mysql-py-claim
            labels:
                app: mysql
        spec:
            accessModes:
                - ReadWriteOnce
            resources:
                requests:
                    storage: 2Gi
        ```
        2. `kubctl create -f lala.yaml`
    2. Deployment von mySQL
        1. yaml-Datei (ist im Cluster per defualt nicht erreichbar )
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata: 
            name: mysql
            labels:
                app: mysql
        spec:
            selector:
                matchLabels:
                    app: mysql
                    tier: backend
            strategy: 
                type: Recreate # Bereitstellungsstrategie
            template:
                metadata:
                    labels:
                        app: mysql
                        tier: backend
                spec:
                    containers:
                    - image: mysql:latest
                        name: mysql
                    env:
                    -name: MYSQL_ROOT_PASSWORD
                        valueFrom:
                            secretKeyRef:
                                name: mysql-pass
                                key: password
                    ports:
                    - containerPort: 3306
                        name: mysql
                    volumeMounts:
                    - name: mysql-persistent-storage
                        mountPath: /var/lib/mysql
                    volumes:
                    - name: mysql-persistent-storage
                        persistentVolumeClaim:
                            claimName: mysql-pv-claim
        ```
        * `kubectl create -f lala.yaml`
    3. Service bereitstellen, der DB den anderen Komponenten im Cluster zur Verfüng stellt
        1. yaml-Datei
        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
            name: mysql
            labels:
                app: mysql
        spec:
            ports:
                - port: 3306
            selector:
                app: mysql
                tier: backend
            clusterIP: None # außerhalb des Cluster nicht erreichbar
        ```
        2. `kubectl create -f lala.yaml`
        3. `kubeclt get deployments`
        4. `kubectl get services`
* Fazit:
    1. persistent Speicher 
    2. PersistentVolumeClaims = persistenten Speicher dem Cluster bereitstellen
    3. mit Service den Deployment nach außen aufmachen
    4. mit Secret Passwörter verschlüsseln und an Pods verteilen
#### 3 - Applikation bereitstellen: WordPress
* braucht persistenten Speicher, muss komplett nach außen bereitgestellt werden, `secret` für Wordpress anlegen
* Schritte:
    1. PersistenVolumeClaim:
        1. yaml
        ```yaml
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
            name: wordpress-pv-claim
            labels:
                apps: wordpress
        spec:
            accessModes:
                - ReadWriteOnce
            resources:
                requestes:
                    storage: 2Gi
        ```
        2. `kubectl create -f lala.yaml`
    2. Deployment anlegen
        1. yaml
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata: 
            name: wordpress
            labels:
                app: wordpress
        spec:
            selector:
                matchLabels:
                    app: wordpress
                    tier: frontend
            strategy: 
                type: Recreate # Bereitstellungsstrategie
            template:
                metadata:
                    labels:
                        app: wordpress
                        tier: worpress
                spec:
                    containers:
                    - image: wordpress:latest
                        name: wordpress
                        env:
                        - name: WORDPRESS_DB_HOST
                            value: mysql
                        -name: MYSQL_ROOT_PASSWORD
                            valueFrom:
                                secretKeyRef:
                                    name: mysql-pass
                                    key: password
                        ports:
                        - containerPort: 3306
                            name: mysql
                        volumeMounts:
                        - name: mysql-persistent-storage
                            mountPath: /var/lib/mysql
                        volumes:
                        - name: mysql-persistent-storage
                            persistentVolumeClaim:
                                claimName: mysql-pv-claim
        ```
        2. `kubectl create -f lala.yaml`
    3. Service bereitstellen
        1. yaml
        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
            name: wordpress
            labels:
                app: wordpress
        spec:
            ports:
                - port: 80 # Anfragen die hier ankommen, werden an POds des Services weitergeleitet
            selector: # über Selector wird gesagt, welche Pods der service verwaltet (sind Labels d.h Pod muss Label haben app: worpress und tier: frontend)
                app: wordpress
                tier: frontend
            type: NodePort # Typ des Services => NodePort nicht nur aus Cluster sondern auch von außen erreichbar
        ```
        2. `kubectl create -f lala.yaml`
        3. `kubectl get deployments`
        4. `kubectl get services`
* Tipp:
    * man kann alles in einer yaml-Datei bereitstellen und die Blöcke mit `---` trennen. Reihenfolge ist egal.
#### 4 - Applikation bereitstellen: Ingress
#### 5 - Applikation bereitstellen: HELM und Tiller aufsetzen

### 5 - Applikationen betreiben
#### 1 - Deployment updaten
#### 2 - Deployment skalieren
#### 3 - Gesundheit von Pod prüfen
