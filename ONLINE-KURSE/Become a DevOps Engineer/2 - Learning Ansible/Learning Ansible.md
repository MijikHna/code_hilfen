### 0 - Introduction
* IT automattion Engine
* OS: Fedora 25 oder Red Hat 7 oder CentOS 7

### 1 - What is Ansible?
#### 1 - An introduction to Ansible
* ist Task execution engine 
    * Action auf einem/mehreren Rechnern ausführen
    * Remote-Management
* Standard ist Lineare Ausführung = Task auführen, warten bis alle Maschinen dieses Task aufgeführt haben -> nächstes Task zum Ausführen senden
* Rolling Deployment: (serielle Ausführung)
    * Spezielle Batches in bestimmte Reihenfolge
    * minimaler Impakt auf speziele Services
* Ausführen so schnell man kann (freie Ausführung)
    * jede Maschine führt Task so schnell sie kann und bekommt dann weitere Tasks
    * reduziert Interuptions
* ist in Python geschrieben, ist in Github
* Tasks werden in .yml geschrieben
#### 2 - Low-cost fleet management
* eine Maschine hat Ansible Daemon (Server), alle anderen sind Fleets(?) (Clients), muss kein Agent installiert werden
* Kommunikatin mit Clients ist per SSH
* ist Stateless 
* braucht 
    * *Inventory Source mit potentiellen Ziel-Maschinen*
    * *State Directiven* 
    * Zugangsdaten für Clients (zur Kommunikation)
#### 3 - Get started with Ansible
* man kann über *apt* installieren auf dem Server
* man kann auch über *pip* installieren => mit Environements => mehrere Ansible-Server  
    * um dann Pythone-Lib zu bilden, muss man *gcc* und *openssl-tools (development headers)* installieren
    * man kann nach ansible-Bib mit `pip search` suchen oder direkt auf *https://pypi.org*-Seite
* `which ansible`
* `ansible --version`

### 2 - What are the parts of Ansible?
#### 1 - Work with hosts and variables
* Inventory enthält:
    * potenzielle Targets
    * Aktions für diese Targets
    * Beispiele:
        * liste von hosts/ips
        * Hosts sortiert in Gruppen
        * Host in Gruppen und Subgruppen
* Patterns 
* mehrere Inventories möglich
* Inventories haben Variablen: Key-Schlüssel-Paare (Daten für den Host)
    * Variablen in Tasks 
    ```
    pip:
        name: {{ foo }}
    ```
    * Variablen in Templates für Configurationen
    ```
    [database]
    conn = {{ db }}
    ```
    * Ansible Verhalten z.B wie Ansible Verbindung aufbauen soll
    ```
    ansible_user=fred
    ```
    * können direkt in Inventory stehen ODER
    * in separater Datei als Teil des GroupFiles:
    ```
    inventory/group_vars/web.yaml
    foo: different_value
    inventory/group_vars/all.yaml
    foo: default_value
    ```
* es gibt:
    * static Sources => einfach aber müssen manuell updatet werden
    * dynamic Sources => um z.B Daten aus Cloud, Container zu ziehen 
#### 2 - Provided code to accomplish work
* Tasks:
    * Data => Argument für ein Befehl z.B `mkdir DATA`
    * Controls => Task Kontrolle z.B Task loopen, sudo/root
+ Ansible wiederholt die Task nict jedes Mal => Wenn Retur war OK, hört aud diesen Task auszuführen
* Task Return Data:
    * *skipped*
    * *changed*
    * *path*
    * *mode* z.B 755
* Module Code + Common Code (Task Argument) => führt die Tasks aus. Wird dann *Return Data* zurückgegen
    * Module gibts auf Ansible-Seite
    * man kann aber eigene Module erstellen 
#### 3 - Playbooks: Collections of tasks
* sind .yml Files, die *Plays* enthalten
* Play - Task(s), das einem Host zugewiesen sind
    * `ansible-playbook --help` - Playbook strarten
* Bsp: 
    1. Inventory *hosts*:
    ```
    [groupA]
    host1
    host2
    [groupB]
    host4
    host3
    [all:vars] #Variable, die sagt dass Ansible sich mit den Hosts lokal verbinden soll
    ansible_connection = local
    ``` 
    2. Playbook demoplays.yaml
    ```yaml
    --- # yaml-Datei markieren
    -   name: "Do a demo" # Play-Name
        hosts: groupA # für welche Hosts

        tasks: # Task erstellen, Task => Yaml-Liste
            -   name: demo task 1 # Name des Tasks
            -   debug: # Modul des Tasks
                    msg: "this is task 1" #Argument des Task

            -   name: demo task 2
            -   debug:
                    msg: "this is task 2"
    # ------------------
    -   name: "Do another demo"
        hosts: groupB

        tasks:
            -   name: demo task 3
                debug:
                    msg: "this is task 3"

            -   name: demo task 4
            -   debug:
                    msg: "this is task 4"
    ```
    * Plays + Tasks werden von oben nach unten ausgeführt:
    * `ansible-playbook -i hosts demoplays.yaml` - `-i` = welche Inventory

#### 4 - Control task and play behavior
* Playbook führ alle Plays aus
* Wenn ein Play Error meldet => werden weitere Plays abgebrochen
+ Wenn auf einem Host ein Error passiert, ist löscht Asible dieses Host aus Targets
```yaml
--- # yaml-Datei markieren
-   name: "Do a demo" # Play-Name
    hosts: groupA # für welche Hosts

    tasks: # Task erstellen, Task => Yaml-Liste
        - name: demo task 1 # Name des Tasks
        - debug: # Modul des Tasks
            msg: "this is task 1" #Argument des Task

        - name: demo task 2
          fail: # Modul fail, um Error auf dem Host zu simulieren
            msg: "this is task 2"
    # ------------------
    -   name: "Do another demo"
        hosts: groupB

    tasks:
        - name: demo task 3
        - debug:
            msg: "this is task 3"

        - name: demo task 4
        - debug:
            msg: "this is task 4"
```
* es gibt conditional Tasks
    * führt Task auf dem Host wenn Condition ist true
    ```yaml
    --- # yaml-Datei markieren
    -   name: "Do a demo" # Play-Name
        hosts: groupA # für welche Hosts

        tasks: # Task erstellen, Task => Yaml-Liste
            - name: demo task 1 # Name des Tasks
            - debug: # Modul des Tasks
                msg: "this is task 1" #Argument des Task

            - name: demo task 2
              fail: # Modul fail, um Error auf dem Host zu simulieren
                msg: "this is task 2"
                when: inventory_hostanme == "host2" # Condition -> Führt diesen Task nur auf Host 2 aus
    # ------------------    
    -   name: "Do another demo"
        hosts: groupB

        tasks:
            - name: demo task 3
            - debug:
                msg: "this is task 3"

            - name: demo task 4
            - debug:
                msg: "this is task 4"
    ```
* Play Controls:
    1. Strategie:
        1. Seriel
        2. Free
    2. Max Fail:
        1. in Prozent
        2. in Anzahl
    3. Privileges
        * root/sudo
* Bsp Serial:
```yaml
--- # yaml-Datei markieren
-   name: "Do a demo" # Play-Name
    hosts: groupA # für welche Hosts

    tasks: # Task erstellen, Task => Yaml-Liste
        - name: demo task 1 # Name des Tasks
        - debug: # Modul des Tasks
            msg: "this is task 1" #Argument des Task

        - name: demo task 2
            fail: # Modul fail, um Error auf dem Host zu simulieren
            msg: "this is task 2"
            when: inventory_hostanme == "host2" # Condition -> Führt diesen Task nur auf Host 2 aus
    # ------------------
    -   name: "Do another demo"
        hosts: groupB
        serial: 1 # Seriale Execution Strategie benutzen mit Batch = 1 

    tasks:
        - name: demo task 3
        - debug:
            msg: "this is task 3"

        - name: demo task 4
        - debug:
            msg: "this is task 4"
```

#### 5 - Challenge + Solution: Write a playbook
* dazu muss man Modul `pip` in der Ansible-Doku checken
myplaybookchallenge.yaml
```yaml
---
- name: Challenge Me ##Play-name
  hosts: host1 # Host Target
  
  tasks: 
    - name: ansible pip # Task Name
      pip:
            name: ansible
            virtualenv: ~/challenge1
```
* `ansible-playbook -i hosts myplaybookchallenge.yaml`
### 3 - What is Ansible goot for?
#### 1 - Code-driven deployment and operations
* Configuration Automation -> um Manuelles Configuration zu verringern
    * Ansible gibt leichte Sprache für Konfiguration, die von Developers und Operators verstanden wird
* On-Demand Infrastructure um Infrastructure Provisioning zu verbessern also (Infrastructure as Code)
    * Ansible hat Module um Infrastructure zu erstellen und zu Konfigurieren
#### 2 - Coordinate complicated sets of actions
* um Orchestration zu realisieren
* Bsp: drei Hosts, die davor zwei Load Balancers haben. Den Node, der upgedatet werden soll, soll man vom Traffic herausnehmen
* webapp-File - Inventory-Datei
```
[web] //Gruppe web
host1
host2
host3

[lb] //Gruppe lb (Load Balancers)
lb1
lb2
lb3

[all:vars] //Variable all
ansible_connection=local
```
* Playbook: web-deploy.yaml - Playbook
```yaml
---
name: Deploy
hosts: web
serial: 1 #jeder Node soll Playbook durchlaufen, dann wird anderes Node dieses Paybook durchlaufen

tasks: 
 - name: disable node
   debug: # Modul
    msg: "disable {{ inventory_hostname }}" #Message mi Variable, Variable = Hostname
    delegate_to: "{{ groups['lb'][0] }}" #Redirected die Connection + hält Kontext von wirklichem Ziel

 - name: upgrade web
   debug: 
    msg: "upgrade software"

 - name: enable node
   debug: 
    msg: "enable {{ inventory_hostname }}"
   delegate_to: "{{ groups['lb'][0] }}" 
```
* `ansible-playbook -i webapp web-deploy.yaml`
#### 3 - Manage system configurations
* Config Management:
    1. Initial application install
    2. weitere Changes in der APP Config
* Bsp:
* webapp-File - Inventory-Datei
```
[web] //Gruppe web
host1
host2
host3

[lb] //Gruppe lb (Load Balancers)
lb1
lb2
lb3

[all:vars] //Variable all
ansible_connection=local
```
* playbook: web-app.yml (es wird `debug`-Modul verwednet, anstelle von richtigen Modulen um Aktion zu simulieren)
```yaml
---
- name: configure web app # Einzelnes Play
  hosts: web
  vars: # Variablen, die in den Tasks verwendet werden
   repo: myrepo.com/repo.git
   version: 8

  task:
   - name: install nginx #nginx installieren
     debug: 
      msg: "dnf install nginx" # dnf ist Package-Manger (sowas wie apt)
      
   - name: ensure web directory # Direktory erstellen
     debug:
      msg: "mkdir /webapp"
      
   - name: get content #App-Code reinkopieren
     debug: 
      msg: "git clone --branch {{ version }} {{ repo }} /webapp"

   - name: nginx config #Nginx-Config erstellen (man würde hier template-Modul benutzen )
     debug: 
      msg: "put nginx config in place"

   - name: ensure nginx running # checken, ob nginx wirklich läuft
     debug: 
      msg: "service nginx start"
```
* `ansible-playbook -i webapp web-deploy.yaml`
#### 4 - React to configuration changes
* Reaktionen auf Änderungen programmieren
* Bsp. z.B wenn nginx-Config verändert wird, muss man nginx neustarten
```yaml
---
- name: configure web app # Einzelnes Play
  hosts: web
  vars: # Variablen, die in den Tasks verwendet werden
   repo: myrepo.com/repo.git
   version: 8

  task:
   - name: install nginx #nginx installieren
     debug: 
      msg: "dnf install nginx" # dnf ist Package-Manger (sowas wie apt)
      
   - name: ensure web directory # Direktory erstellen
     debug:
      msg: "mkdir /webapp"
      
   - name: get content #App-Code reinkopieren
     debug: 
      msg: "git clone --branch {{ version }} {{ repo }} /webapp"

   - name: nginx config #Nginx-Config erstellen (man würde hier template-Modul benutzen )
     debug: 
      msg: "put nginx config in place"
     notify: restart nginx #notify Direktrive, die (hier den Hanlder "resatrt nginx" aktiviert)
     changed_when: True # Change simulieren, da debug: keine Änderung macht

   - name: ensure nginx running # checken, ob nginx wirklich läuft
     debug: 
      msg: "service nginx start"

handlers:
 - name: restart nginx
   debug: 
    msg: "service nginx restart"
```
* Handlers in Ansible :
    * sind speizielle Tasks, die nur bei bestimmter *notify* starten
    + reagiert auf Task-Änderungen per Notiz (*notify*)
    * erlaubt einzel Reaktion zu mehreren geänderten Tasks
* im Playbook für benötigten Task `notify: ...` einfügen +
 für diesen *notify* einen `handler` erstellen
#### 5 - Infrastructure management
* Infrastructue erstellen
* Bsp: 
    * Inventory:
    ```
    [web] //Gruppe web
    host1
    host2
    host3

    [lb] //Gruppe lb (Load Balancers)
    lb1
    lb2
    lb3

    [all:vars] //Variable all
    ansible_connection=local
    ```
    * playbook: docker.yaml -> hat zwei Plays
    ```yaml
    --- 
    - name: make dockers # Play 1 - erstellt Containers
      hosts: localhosts

      tasks:
        - name: make dockers #Task 1 Docker-Cont erstellen
          docker_container: # docker-container-Modul
           image: busybox #Docker image
           command: sleep 1d # Command für Docker
           name: "busy {{ item }}"
          with_sequence: count=3 # Loop für "item", da man 3 Container erstellen möchte
        - name: add hosts #Task 2 run-time- Inventory Additions erstellen
          add_hosts: #Modul 
           name: "busy {{ item }}" #Name, damit für die Connection (also Containernamen)
           groups: dockers # welche Gruppe
           ansible_connection: docker # Verbindungs Methode
          with_sequence: count=3 
    
    - name: hi from docker # Play 2 
      hosts: dockers
      gather_facts: False # keine Node-Fakts sammeln, da dafür Python auf den Hosts benötigt wird
          
      tasks:
       - name: ping 
         raw: echo $HOSTNAME # raw-Modul
    ```
    * `ansible-playbook -i webapp docker.yaml -v` - `-v` = Verbose-Mode
* Loops:
    * Task-Controlls, die weiderholt werden
    * Variablen Daten werden per Loop verändert, Variable Daten sind:
        1. Conditionals
        2. Module args
        3. Templates
    * Arten der Loops:
        1. Variable sets
        2. Sequences
        3. Retries on failure

#### 6 - Repeat a task across a fleet
* Ad Hoc Tasks = single Task auf bestimtmen Host ausführen => man braucht keinen Playbook. Dafür muss an *ansible-executable* verwenden
    * `ansible --help | less`
    * *ansible-Command` bekommt als Parameter die Inventroy, Hosts-Pattern, Module, dass ausgeführt werden soll -> Bsp:
        1. reboot: `ansible -i webapp web -m debug -a "msg='shutdown -r now'"` 
        2. Ansible-Version checken: `ansible -i webapp web -m comamnd -a "rpm -q ansible"`
        3. Kopieren zu einer Datei: 
            * `ansible-doc copy` - Doku zu `copy`-Modul
            * `ansible -i webapp web -m copy -a "src=myFile dest=/tmp/myFile"` (im Video gab es Error bei zwei Host, da sie das Modul *libselinux-python* nicht installiet hatten)
            * Fix *libselinux-python*-Modul: `ansible -i webapp web -m dnf -a "name=libselinux-python state=present" -f 1` -> `-f x` - Forks = Max Nummer gleichzeitiger Verbindungen
#### 7 - Challenge + Solution: Ad-hoc task
* Aufgaben:
    * Ad hock Task um Kernel-Release hearauszufinden:
        * Benötigt: Command-Modul, Kernel Release (`uanme -r`)
* Lösung:
    * `ansible --help`
    * `ansible-doc command` - Doku zu `command`-Modul
    * `asible -i inventoryName hostsInDerInventory -m command "uname -r"`
### 4 - Why choose Ansible
#### 1 - Asnible ease to use
* Leicht zu benutzen:
    * Inventory mit Zeilen
    * State to assert
    * credentials to log in
    * Open Source Code
+ Inventory:
    * in INI-Format
    * kann auch dynamisch erstellt werden 
        * aus existierendem fleet tracking system
* Tasks:
    * in YAML 
    * States:
        * als Module erstellt
* benutzt SSH zur Kommunikation
* Ansible + Module sind Open Source von Red Hat
#### 2 - Manage extensions in Ansible
* man kann Ansible erweitern
* drei Typen der Extensions
    * Module
        * werden in /usr/share/ansible
        * oder relative zu Playbook, die ausgeführt werden -> in ./library...py
        * oder relative zu Rolen, die ausgeführt werden -> ./role/xxx/library/...py
    * Plugins
        * Core erweitern
        * Logging/display callback
        * Communication
        * Template Filtering - Daten innerhalb der Templates manipulieren
    * Dynamic Inventories
        * returnt Inventory als JSON
#### 3 - Advantage to using Ansible
    * 