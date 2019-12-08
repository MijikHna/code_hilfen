### 0 - Lab
* 3 Virtuele Mashine, die Docker Enterprise installiert haben
    * Docker von Docker Store herunterladen 
* Play with Docker Environement 
### 1 - Undertanding Docker Security
#### 1 - Describe default Docker Engine Security
1. Kernel Namespaces - wenn Container gestartet wird, läuft er im eigenen Namaspace. Jeser Container hat eigenen NW-Stack
2. Contol Groups (C-Groups). Eigene ControllGruppe wird für jeden Container wird erstellt.
3. Docker Daemon Attack Surface
4. Linux Kernel Capabilities.
* in Docker Doku unter Docker Security
#### 2 - Securing Docker Swarm
* Mutually Authenticated TLS (MTLS)
    * Manulles umstellen der Zertifikates ist schwer
        * MTLS is in Docker Swarm eingebaut und löst es
    * Docker Swarm ist PUblic Key Infrastructure
        * Nodes benutzen MTLS um verschlüsselte Kommunikation zu gewährleisten
        * der erste Manager hat CA
        * dieser Root-Cert wird benutzt für die Node-Kommunikation
        * wenn neues Node erstellt wird wird für diesen Node und Manager ein Schlüssel-Paar erstellt.
* `docker swarm ca --rotate` - neues CA Cert und Key erstellen, fall man den Verdacht hat, dass Swarm Node kompromentiert wurde
#### 3 - Secure Docker to registry Communication
* Docker Dock - DTR (Docker Trusted Registery) Security
    * wie man self-signed Certs für eigene Registery erstellt. 
#### 4 - Understanding Docker content trust
+ 

### 2 - Configuring Docker Security
#### 1 - Identifying roles in Unversal Control Plane (UCP)
#### 2 - Configuring role-based access control (RBAC) in UCP
#### 3 - Using external certs with UCP and Docker Trusted Registery (DTR)
#### 4 - Creating UCP client bundles
#### 5 - Using LDAP/AD with UCP
#### 6 - How to ensure images pass security scans

