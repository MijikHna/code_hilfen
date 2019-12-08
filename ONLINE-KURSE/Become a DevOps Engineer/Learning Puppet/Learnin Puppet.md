* Infrastructure as Code
* Cross-Platform
---
* Evn: Sandbox, die auf Github zeigt
* VM: CentOS <- vagrant

### 1 - Pupper Overview
#### 1 - What is Puppet?
* Sprache + Tools um Zustand der Infrastruktur zu beschreiben
* = Configuration Management Tool (=Chef, Ansible, Salt)
* benutzt Abstraktion: 
    * Dateien, Users = Resourcen
    * Resourcen können gruppiert werden und zu Modulen gemacht
    * man bündelt Speziele Konfiguratinen zu Abstrakten Layer = Profile und Rolen
        * Profile = Klassen, die zusammen gehören z.B für DB-Server, für Web-Server
        * Jede Machine bekommt eine Role
* Reporting = Logging - 
* hält System auf vorgesehen Zustand. <- Abgleich jede 30 Minuten
* Puppet Begriffe:
    * Node - Server oder Device, das von Puppet gemanaged wird
    * Resources - Einheiten zum Konfiguration (Dateien, Users)
    * Class - Puppet-Code, gruppiert Ressourcen
    + Manifest - Text Datei, die Puppet-Code enthält (.pp)
    * Profile - Klasse, die Set of Config definiert. Sollte sollte man in Scopes limitieren, was die Klasse konfigurieren kann. 
    * Role - definiert Role des Nodes. Aus mehreren Profile-Klassen. Jeder Node sollte nur eine Rolle haben
### 2 - Setting Up a Dev Environemnt
* vagrant-Datei:
#### 1 - Create a sandbox
```ruby
CPUS="1"
MEMORY="1024"
Vagrant.configure("2") do |config|
    config.vm.box = "centos/7"
    config.vm.hostname = "master.puppet.vm"

    config.vm.provider "virtualbox" do |v|
        v.name = "master.puppet.vm"
        v.memory = MEMORY
        v.cpus = CPUS
    end
end
```
#### 2 - Install your Puppet master
* `rpm -Uvh https://yum.puppet.com/puppet6-release-el-7.noarch.rpm` - Puppet-Paket herunterladen
* `yum install -y puppetserver vim git`
* `nano /etc/sysconfig/puppetserver`
    * `JAVA_ARGS="-Xms512 -Xmx512m -...` - für JAVA-Puppet 512mb zuordnen
* `systemctl start puppetserver` + eventuell PuppetServer enablen
* `nano /etc/puppetlabs/puppet/puppet.conf` - Sagen, dass dieser Rechner als Agent auf sich selber zeigen soll
    * dazu schreiben:
    * `[agent]` 
    * `server = master.puppet.vm`
* Ruby-Gem installieren bzw. Ruby in Path aufnehmen, das mit Puppet installiert wurde
    * `nano .bash_profie`
        * `PATH="PATH:/opt/puppetlabs/puppet/bin`
* `gem install r10k` - r10k - Tool um Puppet-Code von github auf dem Server zu deployen
* `puppet agent -t` - Testen - eigentlich Code auf dem Agent ausführen, aber da kein Code => wird "leer" ausfühen
#### 3 - Version Contmrol
* master wird zu production umbennant, da Puppet-Master master heisst
* r10k zeigt auf Git-Repo. r10k wird dann Code zu master pushen
#### 4 - Set up a control repo
* Repo auf Github erstellen
* Puppet-master wird nicht mit Branchnamen master funktionieren:
    * neuen Brachn ertellen: production
    * in Settings -> Brunches -> production zum Default-Branch machen. master löschen
* r10k vorbereiten:
    * `mkdir /etc/puppetlabs/r10k`
    * `nano /etc/puppetlabs/r10k/r10k.yml` - r10k einstellen. ist in YAML-Format => yml.org chekcen für die YAML-Syntax
    * 
    ```yaml
    ---
    :cachedir: "var/cache/r10k" # Dir wo r10k checkt die Module von Fork hier, bevor zu diese in Code-Dir kopiert 

    :sources:
        :my-org: 
            remote: "https://github.com/.../..-repo.git"
            basedir: "/etc/puppetlabs/code/environments"
    ```
    * `r10k deploy environment -p` - Code aus Github wird zu `basedir` gepusht. <- Kann man auch alles manuel machen

### 3 - First Steps with Puppet
#### 1 - Built-in resource types
#### 2 - Manage a file in site.pp
#### 3 - Classes
#### 4 - Introduction to the Forge
#### 5 - The NGINX module
#### 6 - Editing the Puppetfile
#### 7 - Roles and profiles
#### 8 - Roles and profiles demo

### 4 - Managing More Nodes
#### 1 - Manage more modes
#### 2 - Expand site.pp
#### 3 - Connect agent nodes to the master
#### 4 - Orchestration in Puppet
#### 5 - Understand the Puppet run
#### 6 - Facter
#### Challenge/Solution: Installing SSH and adding hosts

### 5 - Modules
#### 1 - What is a module?
#### 2 - Write modules: Write manually
#### 3 - Write modules: Write the code
#### 4 - Write modules: Test your module
#### 5 - Get the order right 
#### 6 - Use parameters
#### 7 - Templates