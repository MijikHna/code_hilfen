### 1 - https://medium.com/google-cloud/kubernetes-101-pods-nodes-containers-and-clusters-c1509e409e16

#### 1 - Nodes
* = Hardware: 
    1. Rechner
    2. VM
* kleinste Unit der Hardware
* represäntiert einzelne Machine
* also Maschine = Node = Set von CPU, RAM usw.

#### 2 - Cluster
* mehrere Nodes formen Cluster => powerful Maschine
* wenn man Programme deployt, verteilt K8 diese auf Nodes. Wenn Nodes dazukommen oder entfernt werden, K8 verteilt die Programme entsprechend

#### 3 - Persistent Volumes
* da Nodes kommen und gehen, müssen die permanenten Daten irgendwo sicher gespeichert werden
* Volumes existeren per Cluster ~ Plug-In von Volume
* wird für Cluster gemountet

#### 4 - Container
+ mit Containern, wird CI/CD beschleunigt
* Idee: ein Programm = ein Container

#### 5 - Pods
* wrappt einen oder mehrere Container in einen Pod
+ diese Container können können dan gleiche Ressourcen verwenden und sind im gleichen Subnetz.
* Unit der Replication = man kann Pod replizieren
    * Good Practice: mehrere Replicas eines Pods laufen zu lassen => Load Balancing
* Obwohl Pods mehrere Container haben können, sollte man Pods trotzdem so klein wie möglich halten

#### 6 - Deployments
* Pods werden von Deployments (Layer der Abstraktion) verwaltet
* deklariren:
    1. wie viele Replicas der Pods
* Deployments werden für Cluster ertellt
* wird der State des Systems deklariert

* Also Vorgehen:
    1. Cluster aus Nodes ertellen
    2. Deployments von Pods auf dem Cluster laufen lassen

#### 7 - Ingress
* Pods können nur mit andren Pods kommunizieren. Nach Außen keine Kommunikation möglich
* Ingress = Kanal für die Kommunikation
* es gibt mehrere Wege Ingress für Cluster hinzufügen:
    1. Ingress Controller dem Cluster hinzufügen
    2. LoadBalancer dem Cluster hinzufügen

### weiter Tipps:
1. Tutorial: https://medium.com/google-cloud/kubernetes-110-your-first-deployment-bf123c1d3f8
2. Google Kubernetes Engine - Tutorials: https://cloud.google.com/kubernetes-engine/docs/tutorials/
3. Best Practises für Cotainer: https://12factor.net/
