# Ansible Essential Training

```inventory
[all]
web1 ansible_ssh_host=web1.kumulus.co
web2 ansible_ssh_host=web2.kumulus.co
db1 ansible_ssh_host=db1.kumulus.co
db2 ansible_ssh_host=db2.kumulus.co
[web]
web1
web2
[db]
db1
db2
[backup]
db2
```

## 1 - Ansible Overview and Setup

### 1 - Environment setup

* Targets
  1. Hosts: Ubuntu (hier 4 Hosts (2xweb; 2xdb))
      * Python installiert
      * Upstream Internet Access
      * IP Adressen kennen
  2. Network Devices (Routers)
      * KVM 32GB, 8-threaded, 4-core-processor
      * VyOS (Virtual Routers)
  3. Ansible Hosts (Master)
      * Ansible (mit PIP)
      * PIP: *netaddr* - IP-Address manipulieren
      * *packaet-python* und *packet_net.py* für dynmische Inventory (eventuell manuell installieren)

## 2 - Task Execution Management

### 1 - Defining task execution with host groups

```bash nventory
[all] #per default sind alle in [all] 
# aber hier noch Variablen bei [all] an die Hosts vergeben
web1 ansible_ssh_host=web1.kumulus.co
web2 ansible_ssh_host=web2.kumulus.co
db1 ansible_ssh_host=db1.kumulus.co
db2 ansible_ssh_host=db2.kumulus.co
[web]
web1
web2
[db]
db1
db2
[backup]
db2
```

* mit `watch -t ls /tmp` die Änderungen im Verzeichnis /tmp tracken

```yml
---
- hosts: all
  tasks:
  - name: create a file on a remote machine
    file: #modul = Task
      dest: /tmp/file #param 1 des moduls => zeil
      state: '{{file_state}}' #parm 2 //Status des Files setzen (löschen(absent), erstellen(touch), usw = wie File erstellet werden muss)

- hosts: web
  tasks:
  - name: create file on web machines
    file:
      dest: /tmp/web-file
      state: '{{file_state}}'

- hosts: all:!db # all + db auschließen
  tasks:
  - name: create file on web machines
    file:
      dest: /tmp/web-not-db-file
      state: '{{file_state}}'

- hosts: all:&backup:!web # all vereining mit backup + db excluded
  tasks:
  - name: create file on web machines
    file:
      dest: /tmp/backup-file
      state: '{{file_state}}'
```

* `aniblle-playbook -i ../inventory lala-tasks.yml -e file_state=touch`
  * `-e` ENV-Var hier `file-state` für file-Modul
* `aniblle-playbook -i ../inventory lala-tasks.yml -e file_state=absent`

### 2 - Using tags to limit play execution

* mit Tag in Plays Task tagen und nur diese Tags (nicht) ausführen

```yml
---
- hosts: all
  tasks:
  - name: create a file
    file:
      dest: /tmp/file
      state: touch
    tags:
      - create-file

- hosts: all:!db2
  tags:
    - delete-file
  tasks:
  - name: delete a file
    file:
      dest: /tmp/file
      state: absent

- hosts: db2

  tasks:
  - name: delete a file
    file:
      dest: /tmp/file
      state: absent
    tags:
      - delete-file
```

* `aniblle-playbook -i ../inventory lala-tasks.yml --tags create-file`

* `aniblle-playbook -i ../inventory lala-tasks.yml --skip-tags create-file`

### 3 - Execution tasks on localhost

* mit Ansible Task auf Ansible-Host ausüfhren z.B SSH-Keys erstellen, die dann in Clients verteilt werden

```yml
---
# localhost ist auch ohne inventroy bekannt
- hosts: localhost # hier wird SSH-Session erstellt
  tasks:
  - name: create a file via ssh connection
    file:
      dest: /tmp/ssh-created
      state: touch


- hosts: localhost
  connection: local # ohne SSH-Session => ist schneller

  tasks:
  - name: create a file via direct local connection
    file:
      dest: /tmp/direct-created
      state: touch
```

### 4 - Limiting plays from the command line

* wenn man z.B Tasks vom Playbook skippen will z.B wenn ein Task zu lange geht

```yml
---
- hosts: all
  tasks:
  - name: the first task
    file:
      dest: /tmp/first-task
      state: '{{file_state}}'
  - name: the second task
    file:
      dest: /tmp/second-task
      state: '{{file_state}}'
  - name: the last task
    file:
      dest: /tmp/last-task
      state: '{{file_state}}'
```

* `aniblle-playbook -i ../inventory lala-tasks.yml e- file-state=touch --start-at-task='the second task'`

### 5 - Specifying variables via inventory

```bash
[all]
web1 ansible_ssh_host=web1.kumulus.co
web2 ansible_ssh_host=web2.kumulus.co
db1 ansible_ssh_host=db1.kumulus.co
db2 ansible_ssh_host=db2.kumulus.co
[web]
web1
web2
[db]
db1
db2
[backup]
db2 backup_file=/tmp/backup_file #Variable für db2 nämlich back_file
# Variablen für ganze Gruppen
[all:vars] # Variablen für all
all_file=/tmp/all_file
[web:vars] # Variablen für web
web_file=/tmp/web_file
```

```yml
---
- hosts: web
  tasks:
  - name: create a web file
    file:
      dest: '{{web_file}}' # Hier wird Variable von inventory benutzt
      state: '{{file_state}}' # Hier wird Varible über anbsible-playbook -Command übergeben

- hosts: backup
  tasks:
  - file:
      dest: '{{backup_file}}'
      state: '{{file_state}}'

- hosts: db
  tasks:
  - file:
      dest: '{{db_file}}'
      state: '{{file_state}}'
    when: db_file is defined # Hier wird dieser Tasks nicht ausgeführt wenn db_file nicht definiert wird
- hosts: all
  tasks:
  - file:
      dest: '{{all_file}}'
      state: '{{file_state}}'
```

* `aniblle-playbook -i ../inventory lala-tasks.yml e- file-state=touch`

### 6 - Defining inventory dynamically

* z.B anhand von vorhandenen IP erstellen. Dafür wird Provide *packet.net* verwendet.

* `packet_net.py --list` - Liste der Devices anzeigen (IP + Host)

```yml
---
- hosts: tag_all
  tasks:
  - name: create a file
    file:
      dest: /tmp/file
      state: touch
    tags:
      - create-file

- hosts: tag_all:!tag_db2
  tags:
    - delete-file
  tasks:
  - name: delete a file
    file:
      dest: /tmp/file
      state: absent

- hosts: tag_db2
  tasks:
  - name: delete a file
    file:
      dest: /tmp/file
      state: absent
    tags:
      - delete-file
```

* hier sind die Gruppen nach den Ausgaben von *packet.net* gruppiert

* `aniblle-playbook -i ../packet_net.py lala-tasks.yml --tags create-file`

### 7 - Variables with dynamic playbooks

* Varaiblen für dynamische Inventories sind schwieriger zu maintainen
* Konzept der Gruppen und Host Variablen

* Konzept:
  1. Ornder z.B **group_vars** mit Dateien **all** und **web**, **host_vars** mit Dateien **xxx.xxx.xxx.xxx** oder **host_name** erstellen  erstellen wo man die Variablen einträgt z.B **

  ```yml
  ---
  all_file: /tmp/all-file
  ```
  
  2. Mapping der Inventory zu Var-Datei geschieht über Dateinamen

```yml
---
- hosts: web
  tasks:
  - name: create a web file
    file:
      dest: '{{web_file}}'
      state: '{{file_state}}'

- hosts: backup
  tasks:
  - name: create a backup file
    file:
      dest: '{{backup_file}}'
      state: '{{file_state}}'

- hosts: db
  tasks:
  - name: create a db file
    file:
      dest: '{{db_file}}'
      state: '{{file_state}}'
    when: db_file is defined

- hosts: all
  tasks:
  - name: all systems should have a file
    file:
      dest: '{{all_file}}'
      state: '{{file_state}}'
```

* weiter Datei die Ausgabe von *packet_net.py* zu Inventory mapped

```yml
[all:children]
tag_all # alle von Inventory zu tag_all von python_net.py mappen. childred ist nötig, da sonst all als einzelner hostname interpretiert wird, so als Gruppe interpretiert 
[web:children]
tag_web
[db:children]
tag_db
[backup:children]
tag_backup
```

* `ansible-playbook -i ../packet_net.py -i ../inventory -e file_state=touch`
* Also hier wurden zwei Inventory verwendet (dynamische un statische), wobei eine nur zum Mappen verwendet wurde

### 8 - Jinja and templates

* für Templates wird Jinja-Template-Langugae verwendet

```yml
---
- hosts: all
  tasks:
  - name: deploy a simple template file
    template:
      src: templates/2-8-template.j2
      dest: /tmp/2-8-template.txt
    tags:
      - create
  - name: remove templated file
    file:
      dest: /tmp/2-8-template.txt
      state: absent
    tags:
      - destroy
```

* hier Wird Ansible-Modul: *template* benutzt um in Datei zu schreiben.

* `watch -t cat /tmp/lala.txt` - im Inhalt der Datei zu tracken

```j2
This file is a template on {{hostvars[inventory_hostname]['ansible_fqdn']}}
backup_file {% if backup_file is defined %} is defined {% else %} is not defined {% endif %}
```

* `hostvars['VARNAME]['VARNAME]` Host-Variablen des Devices injekten
* `if else endif` - Statements

* `ansible-playbook -i ../inventory lala-tasks.yml --tags create`

### 9 - Host facts for conditional execution

* Abhängig von Host-Facts/States Tasks ausführen

* `ansible -n debug -i ../inventory -a "var=hostvars['web2'] web1`  - Asible in/mit Debug(-Modul) ausführen und `hostvars['web2']` vom **web1** anzeigen. Daten sind, was Ansible über diese Machine weiß

```yml
---
- hosts: web
  tasks:
  - name: create
    file:
      dest: /tmp/web2-on-web1
      state: '{{file_state}}'
    when: hostvars[inventory_hostname]['inventory_hostname'] == 'web1' # inventory_hostanme von Dict hostvars holen; mit web vergliechen = wird nur für web1 ausgeführt

  - name: create
    file:
      dest: /tmp/web1-on-web2
      state: '{{file_state}}'
    when: inventory_hostname == 'web2' # geht auch verkürzt
```

### 10 - Looping tasks with variable lists

```yml
---
- hosts: all
  vars:
    packages: [git,vim,ruby]
  tasks:
  - name: install packages for Debian style OSs
    apt:
      name: '{{item}}'
      state: '{{pkg_state}}'
    with_items: '{{packages}}' # Loop durch List package
    when: ansible_os_family == "Debian" # System Fact abfragen und vergleichen apt-Modul wenn Debian

  - name: install pacakges for Redhat style OSs
    yum:
      name: '{{item}}'
      state: '{{pkg_state}}'
    with_items: '{{packages}}'
    when: ansible_os_family == "RedHat" # yum-Modul wenn RedHat

  - name: create files based on package names
    file:
      dest: /tmp/{{item}}
      state: '{{file_state}}'
    with_items: '{{packages}}'
    when: ansible_os_family == "Debian"
```

* `ansible-plabook -i ../inventory lala-tasks.yml -e file_state=touch -e pkg_state=latest` - pkg_state=latest für letzte Version des apt/yum-Packages
* `ansible-plabook -i ../inventory lala-tasks.yml -e file_state=absent -e pkg_state=absent` - hier auch apt/yum-Packages deinstallieren

### 11 - Looping tasks with dictionaries

* wenn man z.B Json-Obj/Dict hat

```yml
---
- hosts: all
  vars: # hier ist Dict bzw. JSON-Obj.
    animals:
      cats:
        tabby:
          color: grey
          persnickityness: high
        calico:
          color: orange
          persnickityness: medium
      dogs:
        doberman:
          color: black
          persnickityness: extreme
        retriever:
          color: golden
          persnickityness: low
  tasks:
  - name: iterate over animal array
    file:
      name: '/tmp/{{item.key}}-{{item.value.color}}' # Also hier: tabby/calicio/-grey/orange/black
      state: '{{file_state}}'
    with_dict: '{{animals.cats}}'

  - name: iterate over animals array
    file:
      name: '/tmp/{{item.key}}-{{item.value.color}}'
      state: '{{file_state}}'
    with_dict: '{{animals.dogs}}' # with_dict erstellt item => weiter wird item.XXX benutzt. Item hat key und value
    when: 'item.value.persnickityness == "low"'
```

* `ansible-playbook -i ../inventory lala-tasks.yml -e file_state=touch`

### 12 - Looping in templates with variable lists

```yml
---
- hosts: all
  vars: #Variablen für diese Hosts/Tasks
    packages: [git,vim,ruby] #Variable packages
  tasks:
  - name: deploy a template file with a loop
    template:
      src: templates/2-12-template.j2
      dest: /tmp/2-12-template.txt
    tags:
      - create
  - name: remove the templated file
    file:
      dest: /tmp/2-12-template.txt
      state: absent
    tags:
      - destroy
```

```j2
We are on host {{inventory_hostname}}
We installed:
{% for package in packages %}
  {{package}}
  {% if not loop.last %}, {% endif %}
{% endfor %}
```

* `,` -> wenn kein letztes loop/Element
* Variablen in j2 können Inventory`inventory_hostname`/Host/Ansible-Playbook-Variablen`packages` sein
* `loop` ist Jinja Loop-Obj

### 13 - Looping int with dictionaries

* Bps: Dict-Variable in playbook die in j2-Datei verwendet wird

```yml
---
- hosts: all
  vars:
    animals:
      cats:
        tabby:
          color: grey
          persnickityness: high
        calico:
          color: orange
          persnickityness: medium
      dogs:
        doberman:
          color: black
          persnickityness: extreme
        retriever:
          color: golden
          persnickityness: low
  tasks:
  - name: deploy a dictionary looping template file
    template:
      src: templates/2-13-template.j2
      dest: /tmp/2-13-template.txt
    tags:
      - create
  - name: remove the templated file
    file:
      dest: /tmp/2-13-template.txt
      state: absent
    tags:
      - destroy
```

```j2
We are in groups:
{% for group in hostvars  [inventory_hostname]['group_names'] %}
  {{group}}
  {% if not loop.last %}, {% endif %}
{% endfor %}

We like both 
{% for key,value in animals.iteritems() %}
  {{key}}
  {% if not loop.last %} and {% endif %}
{% endfor %}

We like
{% for key,value in animals.iteritems() %}
  {% for animal,name in animals[key].iteritems() %} 
    {{name.color}} {{animal}}s
    {% if not loop.last %} and{% endif %}
  {% endfor %}
  {% if not loop.last %} and w{% endif %}
{% endfor %}
```

* ein durch hostvars-Dict interieren
* duch Animals iterrieren mit key und values, da Nested Dicts sind

### 14 - Testing plays with check mode

* check-Modul verwenden

* `anbible-playbook -i ../inventory lala-tasks.yml --tags create --check` - mit `--check` prüft ob alles funktionieren wird gibt. Also sowas wie `--dry-run`. Kann aber nicht alles check, z.B spezielle Dateien auf Remote-Hosts

## 3 - Roles

### 1 - Managing complex playbooks with roles

* Tasks gruppieren und dann diese Tasks in sowas wie Master-Task einfügen

```yml create_play.yml Master-Tasks
---
- hosts: all
  vars:
    user_name: robert
    user_state: present/absent
    ssh_key: ~/.ssh/cloud_key.pub
  tasks:
     - include_tasks: tasks/create_user.yml # hier Einfüge Role-Task/Gruppe von Tasks
```

* `ansible-playbook -it ../inventory create_play.yml`

* um Tasks, Playbooks, Variablen sharen => Rolen erstellen
* Dafür wird oft ansible-galaxy verwendet sowas wie hub
  * `ansible-galaxy init create_user` Role **create_user** erstellen dabei wird Ordner mit Dateien (BoilerPlaste Files) erstelt
  * in den erstellt Orndern: `templates, vars task kann man Tasks, Variable usw. erstellen, die später geteilt werden
  * im **meta** steht, wofür diese Role ist usw. `more meta/main.yml`. Die `galaxy_tags` beschreiben eigentlich die Role
  * jeder Ornder hat `main.yml`

```yml create_role.yml
---
- hosts: all
  tasks:
     - include_role: # hier jetzt stats playbook zu include die Role includen
         name: create_user # Name der Role hier angeben
       vars:
         user_name: robert
         ssh_key: ~/.ssh/cloud_key.pub
         user_state: present
```

* `cp create_user.yml create_user/task/main.yml` eventuell in main.yml einfügen
* `cp templates/lala.js create_role/templates` - auch Templates zu Role *create_role* kopieren
* ``ansible-playbook -it ../inventory create_play.yml`

```yml create_user.yml
---
# tasks file for user_create
- name: Create user on remote host
  user:
    name: '{{user_name}}'
    state: '{{user_state}}'
    remove: yes
    shell: /bin/bash
    groups: sudo
    append: yes

- name: Publish local ssh public key for remote login
  authorized_key:
    user: '{{user_name}}'
    state: '{{user_state}}'
    key: "{{ lookup('file', '{{ssh_key}}') }}"

- name: Add bashrc to include host and user
  template:
    dest: '~{{user_name}}/.bashrc'
    src: templates/bashrc.j2    
```

* `ansible-playbook -it ../inventory create_play.yml`

* man kann die Role jetze durch Kopieren des Orders oder durch ansible-galaxy weitergeben

### 2 - Vairables in roles and variables precedence

* für Variablen zwei Ordern: defaults = für Vars die oft vorkommen aber nicht oft überschrieben werden, vars = Vars, die oft verändert werden

* `vi create_role/create_role.yml` -> Variable `user_state` in default bewegen

```yml
---
- hosts: all
  tasks:
     - include_role: # hier jetzt stats playbook zu include die Role includen
         name: create_user # Name der Role hier angeben
       vars:
         user_name: robert
         ssh_key: ~/.ssh/cloud_key.pub
```

* `vi defaults/main.yml`

```yml
user_state: present
```

* man kann diese Var `user_state` in vars oder über `-e`-Tag bei ansible-play überschreiben

* `ansible-playbook -i ../inventory create_role.yml`

* `ansible-playbook -i ../inventory create_role.yml -e user_state=absent` - die Var aus defaults wird überschreiben

### 3 - Role-based templates

* `more create_user/templates/bashrc.j2`

```j2
export PS1='{{inventory_hostname}}:{{user_name}} $ '
```

* `inventory_hostname` - wird automatisch erstellt von System abgefragt
* `user_name` - wird von der Rolle oder als ansible-play param übergeben

* `vim create_role/defaults/main.yml`

```yml
user_state: present
user_name: default
```

* README.md ergänzen

```md
create_user <!-- anstelle von Role User-->

Role Variables
--------------
# Define the user you would like to create
user_name: default
# Define the user state present or absent
user_state: present
```

* `ansible-playbook -i ../inventory create_role.yml -e user_name=jackson`

* `ansible-playbook -i ../inventory create_role.yml -e user_state=absent` - wird failen, da kein user_name angegeben wurde

### 4 - Documenting your role for reuse

* zwei Doku-Datei:
  1. README.md - die Variablen sollten mit Defaults belegt werden. Für andere Entwickler
  
  ```
  Name der Rolle
  ==============
  Descrption der Rolle: create user and upload ssh key to remote authentation

  Requirements
  ------------
  No specific required Ansible
  Need default ssh pub key or speiciifc key call in variable

  Role Variables
  -------------
  user_name: default
  user_state: present
  ssh_key: ~/.ssh/rsa.pbu

  Dependency
  ----------

  Example Playbook
  ---------------
  ...

  Liciense
  -------
  MIT
  ```

  2. meta/main.yml für die Ansible Galaxy

  ```yml
  galaxy_info:
    author: lala
    descriptoin: lalal

    license: MIT

    min_ansible_version: ...

    galaxy_tags: [user, admin] #Tags für die Suche in der Ansible Galaxy
    dependencies: []
    ```

### 5 - Pushing a role to Galaxy

* Ansible Galaxy - Repo für Ansbile Rolen
* Ablauf:
  1. Bundle als Git-Repo
  2. von Github zu Ansible-Galaxy pushen

* `git init`
* `git add + commit`
* `git push origin master`

* `ansible-galaxy login` Github-Cred eingeben
* `ansible-galaxy import maintainer repo` - anhand von meta/main.yml wird als ansible Role erkannt

* auf www.galaxy.ansible.com kann man dann die Ansible Role finden

### 6 - Finding roles via Ansible Galaxy

* `ansible-galaxy search create_user`
* `ansible-galaxy install lalal.lala -p /Pfad` - ohne -p werden in globalen ansible-galaxy gespeichert (wenn mehrere User am PC arbeiten ist besser)

### 7 - Centralizing roles with `roles_path`

## 4 - Working with Secrets

### 1 - Creating a secrets vault

### 2 - Using secrets in plays

## 5 - Network Management with Ansible

### 1 - Creating a secrets vaults

### 2 - Increment address with `netaddr`

### 3 - Network interface config with `hosts`

### 4 - Network device interface config

## 6 - Indempotence with Ansible Plays

### 1 - Indempotent "prototype" model

### 2 - Registering discovered state

### 3 - Creating and indempotent play

## 7 - System Infrastructure with AWX/Tower

### 1 - Managing systems of systems 

### 2 - Job scheduling

### 3 - Graphing job results

### 4 - Singelton task management

### 5 - Security/vault integration

### 6 - Role-based access/job management