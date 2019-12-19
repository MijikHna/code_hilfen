### 0 - Introduction
#### 1 - What is NGINX
#### 2 - Linux, NGINX, Web technologies
#### 3 - Comparing NGINX to Apache
Apache | NGINX
---| ---
free + open source|
community driven |
compilierte Bibs |
Erweiterbar durch Landen der Module |
können als Proxy Servers konfiguriert |
Event-based Connections |
Config-Fromat XML| Conig-Format C
.htaccess files| nur zentralisierte Files (Block) 
per Haus hat Module| muss man zusätzlich installiert werden
|schneller bei statischen Dateien

* nginx ist einfacher zu konfigurieren + effizienter 
#### 4 - Set up a Sandbox with VB und Vagrant
* Lab - ubuntu-server in vagrant
* `VBoxManage --version`
* `vagrant --version`
#### 5 - Create a VM with Vagrant
* in ExFiles ist schon fertiges Vagrantfile
```ruby
Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-18.04"
    config.vm.network "private_network", ip: guest_ip
end
```
* `vagrant up`
* `vagrant ssh`
### 1 - Install and Configure NGINX
#### 1 - Install NGINX on Ubuntu
* `sudo su -`
* `apt update && apt dist-upgrade`
* `apt install nginx`
* `nginx -v`
* `systemctl status nginx` oder im Browser zu vagrant-IP navigieren
#### 2 - NGINX files and directories
* **/etc/nginx** - Konfigs für ganzes NGINX
    * nginx.conf - Main-Config Datei
    * conf.d - Order
    * sites-available - Order
        * default - Order, wo Begrüßungs-Seite von NGINX liegt
    * sites-enabled - Order
* **/var/log/nginx** - Logs von nginx
    * error.log
    * access.log
* **var/www/** - hier HTML-Seiten ablegen, die NGINX servieren soll
* Config-s sind ähnlich VirtualHost von Appache
#### 3 - The NGINX files and directories
* als *sudo* ausführen
* Status
    * `systemctl status nginx`
    * `systemctl statux nginx --no-pager`
* Start/Stop/Reload
    * über systemctl
    * `systemctl is-active nginx` - chechen, ob gestartet
#### 4 - The NGINX CLI
* ODER nginx-Commands benutzen
    * `nginx -h` - Help
    * `nginx -t` - Config auf Syntax-Fehler testen
    * `nginx -T` - Config testen + ausgeben
    * da Config von NGINX in mehreren Dateien sein kann => `-T` zeigt alles an einer Stelle
#### 5 - Inside nginx.conf
* eigentlich wird nginx.conf nicht so oft verwendet
* Syntyx: `directive { unterdirective };`
* `user www-data;` - User den nginx benutzt
* `http { accedd_log /var/..; include /etc/nginx/conf.d/*.conf}`
    * besser die Config über erweitern
        1. /etc/nginx/conf.d/*.conf 
        2. /etc/nginx/sites-available/*; und diese dann per SymLink nach /etc/nginx/sites-enabled/* linken
*  /etc/nginx/conf.d/*.conf ist besser
#### 6 - Configure a VirtHost: Part 1
1. default-Link in */etc/nginx/site-enabled* löschen `unlink default`
2. erstellen */etc/nginx/conf.d/seitenName.local.conf*
```c
server {
    listen 80;
    root /var/www/seitenName.local;
}
```
* `nginx -t` 
* `systemctl restart nginx`
#### 7 - Configure a VirtHost: Part 2
* Fortsetzung von #6
```c++
server {
    listen 80 default_server; //Standardseite setzen, wenn nichts weitere zutrifft
    server_name seitenName.local www.seitenName.local; //alle möglichen Webnamen
    index index.html index.htm index.php;
    root /var/www/seitenName.local;
}
```
#### 8 - Add files to the root directory
* `apt install unzip`
* `unzip -o lala.zip -d /var/www/seitenName.local` -o = override
* `find /var/www/seitenName.local/ -type -f -exec chmod 644 {}\;` - für alle Dateien in *seitenName.local rw-r--r-- setzen
* `find /var/www/seitenName.local/ -type -d -exec chmod 755 {}\;` - für alle Ordner in *seitenName.local rwxr-xr-x setzen
#### 9 - Configure locations
* 
#### 10 - Configure logs
#### 11 - Troubleshoot NGINX

### 2 - The Linux, NGINX, MySQL and PHP Stack
#### 1 - The LEMP stack
#### 2 - Install PHP on NGINX
#### 3 - Install MariaDB on NGINX
#### 4 - LEMP stack demostration

### 3 - NGINX Security
#### 1 - Secure sites with NGINX
#### 2 - Configure allow and deny directory
#### 3 - Create a 403 page
#### 4 - Configure password authentication
#### 5 - Configure HTTPS
#### 6 - Create an SSL certificate
#### 7 - Install an SSL certificate on NGINX

### 4 - Reverse Proxies and Load Balancers
#### 1 - Reverse proxies and load balancer
#### 2 - Configure NGINX as a reverse proxy
#### 3 - Configure NGINX as load balancer