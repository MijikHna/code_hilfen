### 1 - Get Started with Vagrant:
#### 1 - What is Vagrant:
1. leichte vorkonfigurierte VM zu installieren, als
2. Drei Komponenten:
    1. CLI = Terminal
    2. Vagrantfile = definiert Vagrant-VMs ← in Ruby
    3. Vagrant Cloud
3. Features:
    1. Connect to Vagrant VM
    2. Ordnersynchronisierung
    3. Netzwerk
    4. Provider = Plugins für bestimmte Sachen
    5. Multi-machine Vagrantfiles 
### 2 - Run your first box:
1. Ordner für Vagrant-VMs anlegen (mkdir)
    1. in diesen Ordner navigieren
2. `vagrant init bento/ubuntu-16.04` = Vagrantfile herunterladen
    1. hier findet die Arbeit an der VM statt. Nur dieser Ordner ist davon betroffen
3. `vagrant up`:
    1. schauet, ob die Box bento/ubuntu-16.04 (bento = Organisation). Wenn Box schon einmal gelaufen wurde => wird in Cache(~/.vagrant.d) gespeichert => wird nicht mehr nochmal heruntergeladen
    2. Beim ersten vagrant up => wird Order in ~/.vagrant.d/boxes/Organisation/Builddatum/virtualbox erstellt. Dort werden box.ovf, .vmdk und Vagrantfile heruntergeladen + ein paar andere Dateien. Dann fügt den heruntergeladen und selbst erstellten Vagrantfile zusammen. Wobei eigene Vagrantfile ist übergeordneter = da kann man Default-Settings von Vagrantfile überschreiben. Vagrant enthält z.B Daten wie viele CPUs usw.
    3. nach vagrant up die VM läuft.
    4. => dann mit Hilfe von Vagrant-CLI mit der Box kommunizieren
    5. + kann aus der Ordner mit Vagrantfile ausgeführt werden (eigenem Ordner, nicht ~/.vagrant)
### 2 - Work with Boxes
#### 1 - Box status
1. `vagrant status` = zeigt laufende VMs an. Kann aber nur aus der VM-Ordner ausgeführt werden
2. cd .. → `vagrant global-status` = von überall ausführbar => zeigt alle laufenden VMs + deren ID
3. `vagrant halt id` = VM herunterladen
#### 2 - Connect to a box:
1. Vagrant startet VMs in headless mode = ohne GUI
2. => mit SSH verbinden
3. Vagrant hat schon SSH-Clienten
4. ALSO:
    1. `vagrant ssh` = vebindet sich mit VM mit SSH per Standard-User: vagrant → PW:vagrant
#### 3 - Halting and destroying boxes
1. `vagrant halt` = VM herunterfahren. ← aus dem Ordner mit VagrantFile ausführen
2. `vagrant destroy` = die VM löschen, ABER Vagrantfile wird nicht zerstört. = Box der des Ordners wird gelöscht. Die Base-Box bleibt aber in Cache
#### 4 - Vagrant Cloud
1. app.vagrantup.com = hier kann man nach den VMs suchen
### 3 - Configure Boxes with Vagrantfiles:
#### 1 - Get started with Vagrantfiles:	
1. Erweiterung für Vagrantfiles in vscode holen (Syntaxunterstützung für Ruby)
2. in vscode in Ordner navigieren, wo Vagrantfile oder wo Vagrantfile liegen sollte navigieren → code -r . = wird den Ordner in vscode öffnen
3. `vagrant init` = wird default-Vagrantfile erstellt. Wenn im Vagrantfile bei config.vm.box=“base“ ← steht dann base
    1. config.vm.box_check_update = false/true = ob beim Start der VM Vagrant nach Updates für VM checkt
4. `config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"` = NW-Einstellugnen für VM
5. `config.vm.synced_folder "../data", "/vagrant_data"` = Ordner auf dem HOST mit VM synchronisieren/eibinden
6. `config.vm.provider "virtualbox" do |vb|` = Providerspezifische Einstellungen
#### 2 - Vagrant synced folders
1. per Defualt ist es der Ordner mit Vagrantfile auf dem HOST + wird in VM als /vagrant eingebunden
2. `config.vm.synced_folder "../host_ordner", "/vm_order"`
3. `vagrant reload` = VM neustarten
#### 3 - Vagrant networking
1. Unterstützt folgende NW-Featues:
    1. Port forwarding
    2. Private NW
    3. Public NW
    4. ← per Default sind Vagrant-VMs unsicher d.h. ohne Password und Verschlüsselung usw.
2. 1-Port Forwarding:
    1. Host→ 8080; VM → 80
    2. `sudo apt-get install -y nginx + curl localhost` = NGINX isntallieren
    3. `config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"` = Portweiterleitung von HOST:8080 nach VM:80 wenn localhost bzw. 127.0.0.1
3. 2-Private NW:
    1. `config.vm.network "private_network", type: "dhcp"` =  wird DHCP-Server einbaut in VirtulBox benutzen, um der VM eine private IP zuzuweisen
#### 4 - Vagrant providers:
1. erlaubt Vagrant die Box für bestimmten Hypervisor zu definieren
2. hat schon eingebaute Providers für VirtualBox und Hyper-V
3. + hat eingebauten Support zum Bilden von Docker-Containers
4. in Providers Teil von VagrantFile spezifische Provider-Configs einstellen z.B CPU usw.
5. Memory + CPUs ändern:
    1. `vmstat -s` = in VM ausführen => schauen, wie viel VM von HOST benutzt
    2. `lscpu` = in VM anzeigen wie viel CPU VM benutzt
    3. 
    ```
    config.vm.provider "virtualbox" do |vb|
    #   # Display the VirtualBox GUI when booting the machine
    #   vb.gui = true   
    #
    #   # Customize the amount of memory on the VM:
    vb.memory = "2048"
    vb.cpus = 2
    end
    ```
6. GUI bzw. extra Fenster beim Start von VM anzeigen:
7. `lspci -v -s 00:02.0` = anzeigen wie viel Grafikspeicher benutzter wird.
8. `vb.gui = true`
9. `vb.customize ["modifyvm", :id, "--vram", "16"]`
10. ← wenn man anderen Provider als VirtualBox benutzt muss man Option --provider benutzen
#### 5 - Vagrant provisioners:
1. = Scripts, die in VagrantFile definiert werden können (oft BASH-Scripts zum ausführen bestimmter Sachen beim Start)
2. `config.vm.provision "shell", inline:` <←SHELL
3. ← man kann Inline- oder Path-Skripte definieren
4. Es gibt noch FILE-Provisioners, Docker-Privisioners und viele mehr
5. Provisioners werden nur beim vagrant up ausgeführt ↔ nicht beim vagrant up. ← Man kann vagrant mit Optionen starten, die den Script immer ausführen:
    1. -run „always“
### 4 - Vagrant Use Cases
#### 1 - Application developer environment overview
1. Web-Service mit Node.js-Entwicklungsumgebung erstellen:
https://github.com/dswersky/node_todolist.git = Todo-Application
2. Einrichtung:
    1. Sync-Order erstellen
    2. Port-Forwarding
    3. Provider = Memory
    4. Provisioner = benötige SW installieren + alles konfigurieren
#### 2 - Creating a developer environment
#### 3 - Vagrant multi-machine Vagrantfile
1. Node.js auf einem Server, MongoDB auf anderem Server + privates NW:
2. `vagrant ssh vm_name` = sich mit vagrant auf der vm_name-VM anmelden
### 5 - Vagrant Features and Services
#### 1 - Create a base box, part1:
1. Box eines Entwicklers besteht z.B aus:
    1. OS (Ubuntu)
    2. Node.js (Server)
    3. Referenz Programme
2. <= eigene Boxen erstellen (packen):
#### 2-  Create a base box, part2:
1. ← eventuell einen VagrantFile mit einpacken:
2. Reihenfolge in der VagrantFiles geladen werden:
    1. verpackte Vagrantfile
    2. Vagrantfile in ~/.vagrant.d (← wenn es einen gibt)
    3. Vagrantfile des Environments
3. `vagrant package --vagrantfile vagrant_file/Vagrantfile --output node_dev_env.box` = Paket erstellen
4. `vagrant box list` = alle Boxen in Cache anzeigen
5. `vagrant box add node_dev_env node_dev_env.box` = Paket zum Cache hinzufüfen → `vagrant add name_der_box name_des_pakets.box`
6. `vagrant init name_der_box_im_cache`
#### 3 - Upload a box to Vagrant Cloud:
1. auf app.vagrantup.com = kann man eigene Boxen erstellen. ← kann man öffentliche Boxen erstellen.
    1. ← Version 0.0.1 = erster Release
#### 4 - Vagrant tips and tricks:
1. `vagrant snapshot save nave_des_snapshots`
2. `vagrant up --provision` = Box starten + Provisioner starten mit Gewalt
3. `vagrant snapshot list`
4. `vagrant snapshot restore name_des_snapshots --no-provisioners` = Box starten + ….provisioners-Zeilen in Vagrantfile auslasen
5. Man kann Plugins für Vagrant herunterladen: z.B github.com/hashicorp/vagrant/wiki/Available-Vagrant-Plugins
6. `vagrant suspend` = Box schnell stopen