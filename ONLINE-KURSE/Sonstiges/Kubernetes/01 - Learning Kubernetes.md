### 1 - Containerization with Kubernetes
#### 1 - What is containerization
* Container - Menge an SW das von einem Namespace ausgeführt wird, das das gleiche System Kernel benutzt
* Vorteil von Containern:
    * Apps sind 
        1. portabler
        2. verpackt auf standardisierte Art und Weise
    * Deployment ist
        1. leichter
        2. einheitlicher
    * Testing, Packaging und Integrationen können automatisiert werden
    * unterstützen neue Microservices Technologie
    * Platformunabhängig
    * kein Unterschied mehr für DEV und PRODUCTION 
#### 2 - What is Kubernetes
* Container-Orchestragion
* Orchestration Features:
    1. Versorgung von Host
    2. Container auf dem Host instanzieren
    3. Restarten Container, wenn crashen
    4. verbinden die Container
    5. Container als Service nach Außenwelt presäntieren
    6. Cluster skalieren
* Kubernetes (K8s) - von Google
* man kann auch andere Container als Docker benutzen
#### 3 - Kubernetes features
* Kubernetes - automatisiert deploying, scaling und managing app in Gruppen, Clustern von mehreren Machinen.
* Features:
    1. Mulit-Host Container Scheduling
        * wird von kube-Scheduler gemacht
        * Teilt Pods(Container) zu Nodes(Hosts) zu Runtime
        * Check die Ressourcen und Services, Policies
    2. Scalability und Availability
        * K8s-master in verschiedenen Configs deployed werden
            * hat add-ons: NW Drivers, Service Discovery, Container Runtime, Visualisierung und Commands
            * Plug-and-Play Arch
        * Scaling wird mit 
            1. Registration gemacht = neue Nodes registrieren sich selbst beim master
            2. Sevice Discovery = neue Services und Endpoints per DNS oder envVar entdeckt
        * Persistent Storage
        * App Upgrade/Rollback
        * Logging and Monitoring
            * TCP, HTTP und Container Execution Check
            * Node Check
            * Kubernetes Status mit Heapstar oder cAdvisor checken
            * Logging Tools benutzen
        * Secrets Management
            * Daten <-> Namespace
* Kube-Slack: https://kubernetes.slack.com
#### 4 - Other implementations
* also Alternativen zu Kubernetes
    * Docker-Swarm
    * Rancher 
    * Mesos (C++, Java, Python) - oldest, more stable
    * Amazon EC2 Contaienr (Cloud)
    * Oracle Container (Cloud)
### 2 - Kubernetes: The Terminology
#### 1 - Architecture of a Kubernetes cluster
* Arch:
    1. Master-Node
        1. API-Server - Kommuikation (Frontend von Kube)
        2. Scheduler - Pods  den Nodes zuweisen
        3. Controller Manager - Task im Cluster laufen
        * Scheduler und Manager reden mit Pods über API-Server
    2. etcd - Key-Value-Store = DB für Cluster-Daten (Jobs, Pod-Details, States )
    3. kubectl - CLI um mit Master Node zu sprechen
        + hat kubeconfig-Datei = Server-Info z.B Authen-Info
    4. Worker-Nodes
        1. kubelet - redet mit Master 
        2. Docker
            * Docker-Container(-s) = Pod = Container-Gruppen, die Namespaces, Storage IP, Linux-Namespace teilen
        3. kube-proxy - Load-Balancer für Pods
#### 2 - Basic building blocks: Nodes and pods
* Cluster = 
    * Node
    * Master
    * Node Prozesse
* Node = Worker Machine, kann VM oder HW sein
    1. muss kubelet running sein
    2. muss Container Tool z.B. Docker installiert haben
    3. kube-proxy laufen haben
    4. supervisord laufen haben
    * man sollte mindestens 3 Node-Cluster haben
* Minikube - Tool um Cluster für Kubernetes zu simulieren
* Pod = Unit 
    + Docker App Container
    * Storage Ressourcen
    + Unique IP
    * Optionen wie Container(s) laufen sollen
    * Controller benutzen um Pod zu erstellen/managern usw.
    * States von Pod:
        1. Pending
        2. Running - wenn alle Container erstellt und wenigstens eins gestartet wurde
        3. Succeeded - alle Container haben exited mit Success
        4. Failed - alle Container exited und mindestens einer mit FAIL
        5. CrashLoopBackoff - wenn Kube versucht gecrachted Container immer wiedre neuzustarten
#### 3 - Deployments, jobs services
* Controller:
    * Application reliability
    * Scaling
    * Load Balancing
* Arten der Controller:
    * ReplicaSets - besimmte Anzahl an Pod sollen immer laufen
    * Deployments - updates für Pods und ReplicaSets (haben auch Rollback-Mechanismus)
        * hat Status - Deployment Status
    * DaemonSets - alle Nodes haben eine Kopie von speziellen Pod
    * Jobs - Supervisor Prozess für Pods um Batch Jobs zu verteilen. Individuelle Prozesse einmal laufen lassen (typischerweise als CRON-jobs)
    * Services - NW-Verbindung zu Clustern (Pods)
        * Internal Service (IPs innerhalb von Cluster)
        * External Service (NodeIP + Port)
        * Load Balancer - App zu Internet freigeben
#### 4 - Labels, selectors and namespaces
* Label = Key-Value-Paare, die Objekten z.B Pods, Services und Deployments vergeben werden. Sowas wie Kommentare -> Bsp:
    * `"releae" : "stabel"`, `"release : "canary"`
    * `"environment" : "dev"`, `"environment" : "qa"`
    * `"tier" : "frontend"`, `"tier" : "backend"` 
* Label mit Selectors => mächtiger -> Set von Objects identifizieren
* Selectors (eigentlich Label-Selectors)
    1. equality-based Selectors - = - gelich; != - nciht gleich
    2. set-based Selectors - IN-Operator - Wert sollte im Set sein; NOTIN - Wert sollte nicht im Set sein;
    EXISTS - checkt, ob Label existiert oder nicht
    * werden mit `kubectl` benutz zum Suchen/Sortieren
* Namespaces:
    * Virtuelle Cluster auf gleicher HW
    * = Scopes
    * es gibt per Default ein `default`-NS
    * neuer Applications werden in andere NS installiert
#### 5 - Kubelet and kube proxy
* Kubelet - Node-Agent
    * redet mit API
    * führt Pod-Containers aus (ruft Container-Engine auf)
    * Mounten Volumes 
    * führt Health-Checks aus
    * Kubelet wird per Podspec konfiguriert (YAML-Datei,das den Pod beschreibt)
* Kubeproxy - NW-Forwarding (Port-Forwarding) (läuft auf allen Nodes)
    * Drei Modem:
        1. User space mode
        2. Iptables mode
        3. Ipvs mode (alpha feature)

### Kubernetes 101: Hello World
#### 1 - Getting up and running: Mac install
1. Docker installieren
2. VirtualBox (Virtualization) installieren
3. K8s installieren
    1. kubectl installieren (hier mit curl)
        * `kubectl version`
    2. Minicube installieren (hier mit curl)
* Alles starten:
    * `minikube start`
#### 2 - Getting up and running: Windows install
1. Docker installieren
2. Virtualizatin installieren (ab Windows 10 direkt eingebaut)
    1. Hyper-V-Manager öffnen
    2. Virtual-Switch-Manager öffnen
    3. einen Internal-Switch erstellen (MiniCube nennen)
    4. NW-Einstellungen anpassen
3. K8s installieren
    1. kubectl installieren (eigentich installieren und im Ordner ablegen)
    2. MiniCube installieren (eigentich installieren und im Ordner ablegen + eventuell umbennen)
    3. in PATH diese Order einfügen
        * `minicube verison`
        * `kubectl version`
* Alles starten:
    * `minikube start --kubernetes-verison="v1.8.0" --vm-driver-hyperv" --hyperv-virtual-switch="Minikube"` <- Einstellungen aus Hyper-V-Manager nehmen
    * `minikube stop`
#### 3 - Running a first Hello World application
#### 4 - Breaking down the Hello World application
#### 5 - Scaling the Hello World app

### 4 - Making it Production Ready
#### 1 - Add, change, delete labels
#### 2 - Working with labels
#### 3 - Application health checks
#### 4 - Handling app upgrades
#### 5 - Basic troubleshooting techniques

### 5 - Kubernetes 201 
#### 1 - Running a more complicated example
#### 2 - The Kubernetes dashboard
#### 3 - Dealing with configuration data
#### 4 - Dealing with app secrets
#### 5 - Running jobs in Kubernetes
#### 6 - Running stateful set app

### 6 - Advanced Topics
#### 1 - Production Kubernetes deployments
#### 2 - Detailed look at namespaces
#### 3 - Monitoring and logging
#### 4 - Authentication and authorization