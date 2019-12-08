### 1 - Tools for Network Management
#### 1 - Explore NetworkManager and iproute
1. NW-Einstellugne sind in ein paar Dateien gespeichert (unterschiedlich auf verschiedenen Distros)
    * mit den Tools hat besseren (einheitlicheren) Zugriff auf diese Dateien
        1. ifconfig (net-tools) oder ip/iproute (Red Hat)
        2. NetworkManager (hat mehrere Programme)
            * *nmcli*
            * *nmtui*
            * *nm-connection-editor* - GUI
        3. man kann auch alles manuell machen
#### 2 - Find device information with ip
* `ip addr` oder `ifconfig` - *LOWER UP* ~ *state UP* 
    * `ip -4 addr` - nur ip4 anzeigen
    * `ip link set intname up/down` - Interface an/aus machen
    * `ethtool intname` - Eth-Interface schauen (man 8 page)
#### 3 - Predictable network interface names
* *enp0s3* - 0 - kann immer Unterschiedlich sein, da davon abhängt, welches Gerät vom System zuerst entdeckt wird
    * *en* - Ethernet (*wl* - Wireless)
    * *p* - Bus hier PCI (*u* - USB)
    * *s* - Slot
* man kann System-BUSe mit *lspci* oder *lsusb* 
### 2 - Configure Networking with NetworkManager
#### 1 - Manage the connection
* `systemctl status NetworkManager` 
* `apt-get install Network-Manager`
* CentOS:
    * `nmcli device` - schauen, welche Devices gemanagt werden
    * `cd /etc/sysconfig/network-scripts` - Konfigs für NW-Devices
    * `nano ifcfg-enp0s3`
        * `NM_CONTROLLED=no` - Device nicht von NetworkManager managen
        * `systemctl restart network`
* Ubuntu:
    * `nmcli device`
    * `nano /etc/NetworkManager/NetworkManager.conf`
        * `managed=true` 
        * `systemctl restart NetworkManager`
#### 2 - Using the NetworkManager tools
* `nm-connection-editor` - GUI für NW-Connections öffnen
* `nmcli` - NetworkManagement-CLI
* `nmcli` - Help anzeigen
* `nmcli d` - d = Device
    * Device = HW
    * Connection = Settings die man für Device setzen kann
    * man kann Device- und Connection-Profiles erstellen
* `nmcli connection show enp0s3` - Settings für eine Connection anzeigen. Am Anfang ist Connection-Profile so wie Device benannt.
    * `nmcli connection edit enp0s3` -> Connection-CLI wird geöffnet:
        * `print connection` - Infor zu Connection anzeigen
        * `describe connection.id` - Infor zu bestimmten Settings anzeigen 
        * `set connection.id myEthernet` - Connection-Profil-Namen ändern
        * `set connection.autoconnect yes` - so zu sagen default machen
        * `save`
#### 3 - Configure a dynamic address using DHCP
* per GUI machen
* `nmcli connection down Connection-Name` - Verbindung deaktivieren
* `nmcli connection up Connection-Name` - Verbindung aktivieren
* `nmcli con edit Connection-Name`
    * `print ipv4`
    * `set ipv4 auto` 
* `nmcli con add con-name OtherConnectionProfile ifname enp0s4 type ethernet` - Neuen VerbindungsProfil hinzufügen
    * `nmcli con up OtherConnectionProfile`
#### 4 - Configure a static client
* per GUI
    * Manual -> alles eingeben
* per Terminal
    * `nmcli con edit MyEthernet`
        * `remove ipv4.addresses`
        * `set ipv4.address 10.0.0.8/24`
        * `set ipv4.gateway 10.0.0.1`
        * `set ipv4.dns 10.0.0.1`
        * `save`
        * `quit`
    * `nmcli con up MyEthernet`
* per Terminal 2:
    * `nmcli con mod MyEthernet ipv4.address 10.0.0.8 ipv4.gateway 10.0.0.1 ipv4.dns 10.0.0.1`
    * `nmcli con up MyEthernet`
#### 5 - Configure WiFi
* per GUI
    * ADD -> WiFi -> Device auswählen -> SSID -> usw
* per Terminal
    * `nmcli d`
    * `nmcli d wifi list` - sichtbare WiFi anzeigen
    * `nmcli con add con-name myWiFi ifname wlp0s6u1 type wifi ssid "My WiFi-Name"`
    * `nmcli con mod MyWiFi wifi-sec.key-mgmt wpa-psk wifi-sec.psk "SectretKey!"`
    * `nmcli c`
    * `nmcli con up MyWiFi`
### 3 - Configure Network Manualliy on Ubuntu and Debian
#### 1 - Locate network adapter settings
* `cat /etc/network/interfaces` - Devices Manuell managen über diese Datei
* `nano /etc/NetworkManager/NetworkManager.conf` - das Management von NetwrokManager rausnehmen
    * `managed=false` 
#### 2 - Configure a dynamic address using DHCP
* `nano /etc/network/interface`
    * `auto enp0s3` - Device hochfahren, wenn System bootet
    * `allow-hotplug enp0s3` - ähnlich wie auto
    * `iface enp0s3 inet dhcp` - DHCP benutzen
* `ifup enp0s3` - Device hochfahren
#### 3 - Confiugre a static Wi-Fi
* `nano /etc/network/interface`
    * `auto enp0s3` - Device hochfahren, wenn System bootet
    * `allow-hotplug enp0s3` - ähnlich wie auto
    * `iface enp0s3 inet static` - DHCP benutzen
    * `address 10.0.0.8`
    * `netmask 255.255.255.0`
    * `gateway 10.0.0.1`
    * `dns-nameserver 10.0.0.1`
* `ifup enp0s3`
#### 4 - Configure Wi-Fi
* `ip a` - DeviceNamen schauen
* `nano /etc/network/interface`
    * `allow-hotplug wlx..`
    * `iface wlx.. inet dhcp`
    * `wpa-ssid My Network`
    * `wpa-psk "SecretKey!"` - man kann auch Hexzahl daraus machen
* `ifup wlx...`

### 4 - Configure Networking Manually on Red Hat and CentOs
#### 1 - Locate network adapter settings
+ `cd /etc/sysconfig/network-scripts`
    * `cat ifcfg-enp0s3` - ist Connection-Profil
#### 2 - Configure a dynamic address using DHCP
* `systemclt stop NetworkManager` + `systemctl disable NetworkManager` + restart - NetworkManager ausmachen, damit man alles manuell verwalten kann
* `cd /etc/sysconfig/network-scripts`
    * `nano ifcfg-enp0s3` - ist Connection-Profil
        * `BOOTPROTO=dhcp` - eventuell alle IP-Addressen löschen, sonst ist dhcp + static konfiguriert
* `systemclt restart network`
#### 3 - Configure a static client
* `cd /etc/sysconfig/network-scripts`
    * `nano ifcfg-enp0s3` - ist Connection-Profil
        * `BOOTPROTO=none`
        * `IPADDR=10.0.0.8`
        * `PREFIX=24` oder Maske
        * `GATEWAY=10.0.0.1`
        * `DNS1=10.0.0.1`
* `systemclt restart network`
### 5 - Hostname and Firewall
#### 1 - Set the system hostname
1. mit NetworkManager (nmlci)
    * `nmcli general hostname server1`
    * `nmcli general hostname` - Hostnamen lesen
2. mit hostnamecll
    * `hostnamecll` - Hostnamen lesen
    * `hostnamectl server1`
#### 2 - Firewall configuration with iptables
* Iptable-Regeln => Chains
    * Input
    * Output
    * Forward = wenn Machine Router sein sollte
* CentOS:
    * `sudo iptables -L`
    * `sudo iptables -save > rules-backup` - Backupen
    * `sudo iptables -F` - alle Regeln löschen
    * `nc -l 4545` - in anderem Terminal wechseln. Auf der Machine `nc ip-des-hosts 4545` -> etwas eingeben
    * Regel appenden:
        * `sudo iptables -A INPUT -p tcp --dport 4545 -j DROP/REJECT/ACCEPT` 
    * `sudo iptables-save` 

    * `sudo iptables -F`
    * `sudo iptables restore rules-backup`
* Tips
    * Practical Cybersecurity
    * Protect Your Network with Open-Source Software
#### 3 - Firewall Configuration with firewalld (CentOS)
* `nc -l 5454` - -l= listen
* Firewall einstellen für 5454
    * `sudo firewall-cmd --zone=public --addport=5454/tcp --permanent` - mit TAB kann man Optionen anzeigen
    * `sudo firewall-cmd --reload`
    * `sudo firewall-cmd --zone=public --remove-port=5454/tcp --permanent`
#### 4 - Monitor network port activity
* `man ss` - mit ss Sockets checken
* `ss -t` - Established
* `ss -tl` - Listen-Ports
* `ss -tln` - keine Services für Port raten
* `ss 

### 6 - Route Traffic between Networks
#### 1 - Routing lab overview
* Lab:
    * VM als Router - routet beide NW-e
        * `nmcli c`
        * eventuell unnötiges löschen `nmcli con del conProfile`
        * `nmcli con mod myEth connection.id 10-net ipv4.method manual ipv4-address 10.0.2.6/24 ipv4.dns 10.0.2.1 ipv4.gateway 10.0.2.1`
        * `nmcli con mod Wired\ connection\ 1 connection.id 192-net ipv4.method manual ipv4-address 192.168.0.6/24 ipv4.dns 192.168.0.1 ipv4.gateway 192.168.0.1`
        * `sudo hostnamectl set-hostname router` 
    * 2 VMS als Client
        1. = in 192.168.0.0/24
            * `nmcli con mod MyEthernet ipv4.method manual ipv4-address 192.168.0.7/24 ipv4.dns 192.168.0.1 ipv4.gateway 192.168.0.1`
            * `sudo hostnamectl set-hostname 192-client` 
        2. = in 10.0.2.0/24
            * `nmcli con mod MyEthernet ipv4.method manual ipv4-address 10.0.2.7/24 ipv4.dns 10.0.2.1 ipv4.gateway 10.0.2.1`
            `sudo hostnamectl set-hostname 10-client` 
    * Routen:
        1. alle IP sind static
        2. Static Route von 10.0.2.7 nach 192.168.0.0/24
        3. static route von 192.168.0.7 nach 10.0.2.0/24
        4. Configure firewall on the Router für Forwaring (NAT)
#### 2 - Confiugre a static route
* 3 Möglichkeiten
    1. NetwrokManager
        * `nmcli con mod MyEthernet ipv4.routes "192.168.0.0/24 10.0.2.6`
    2. Manuel
        * CentOS: in */etc/sysconfig/network-scripts/routes-enps0s3*
            * `192.168.0.0/24 via 10.0.2.6`
        * in Ubuntu in */etc/networks/interfaces
            * `up route add -net 192.168.0.0/24 gw 10.0.2.6`
    3. Temporarily z.B für Tests 
        * `sudo ip route add 192.168.0.0/24 via 10.0.2.6 dev enp0s3`
* `ip route show` 
    * auf dem Router-Rechner IP-Forwarding enabeln:
        + `nano /etc/sysctl.conf`
            * `net.ipv4.ip_forward=1`
        * `sudo sysclt -p` 
#### 3 - Route traffic between networks with NAT
* Firewall konfigurieren => Rules:
    + Masquerade enabeln: = eigentlich NAT
    * alle ausgehende Packete aus internal Interface akzeptieren.
    * alle ankommenden Packete aus outside Interface akzeptieren aber wenn schon mit ausgehendem Traffic korrespondiert
    * `sudo firewall-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o enps0s8 -j MASQUERADE` - direct = direkt zu iptables einfügen, 0 = als oberste Regel machen
    * `sudo firewall-cmd --permanent --zone=public --add-masquerade`
    * `sudo firewall-cmd --direct -add-rule ipv4 filter FORWARD 0 -i enps03 -o enps0s8 -j ACCEPT`
    `sudo firewall-cmd --direct -add-rule ipv4 filter FORWARD 0 -i enps08 -o enps0s3 -m state --state RELATED, ESTABLISHED -j ACCEPT`
    * `sudo firewall-cmd --reload` 
#### 4 - Allow internet access through the router
* `mtr google.com` - Traceroute
* `nmcli con mod MyEthernet ipv4.gateway 10.0.2.6`
* `ip route show` - Metic checken
* `nmcli con edit 192-net`
    * `set ipv4.route-metirc 50` 
#### 5 - Configure the router to forward DNS
* *bind* + *named*
* Bsp:
    * `sudo yum install bind bind-utils`
    * `sudo nano /etc/named/named.conf`
        * `listen-on port 53 {any;};`
        * `listen-on-v6 port 53 {any;}`
        * Access-Controll-List setzen, damit nur bestimmte Hosts den Zugriff auf den DNS-Server haben
        ```
        acl allowed {
            192.168.0.0/24;
            10.0.2.0/24;
        };
        allow-query {allowed;};
        forwarders {
            192.168.0.1;
        };
        forward only; # immer forwarden
        dnssec-enable no;
        dnssec-validation no;
        ```
        * `systemctl enable named`
        * `systemctl start named`
        * `sudo firewall-cmd --permanent --zone=public --add-service=dns` - Firewall für DNS öffnen
        * `sudo firewall-cmd --reload`
        * dann mit nslookup testen `nslookup google.de 10.0.2.6` - Dns-Request an 10.0.2.6 senden
        * `nmcli con mod MyEthernet ipv4.dns 10.0.2.6` - auf den Clients die IP von DNS-Server aktualisieren
#### 6 - Sync system time with a network peer
* NTP -> NTP Pool
* Um Log-Events zu vergleichen
* Bsp: NTP-Server konfigurieren
    1. Chrony auf dem Router konfigurieren
    2. NTP in der Firewall erlauben
    3. Crony auf dem Client einstellen
* Router:
    * `chronyc` - checken, ob chrony installiert
    * `sudo nano /etc/chrony.conf`
        * `allow 192.168.0.0/24`
        * `allow 10.0.2.0/24`
    * `sudo systemctl status ntpd`, wenn ja ausmachen
    * `sudo systemclt restart choronyd`
    * `sudo firewall-cmd --permanent --zone=public --add-service=ntp`
    * `sudo firewall-cmd --reload`
* Client:
    * `sudo nano /etc/chrony.conf`
        + `server 10.0.2.6 prefer`
    * `chronyc sources` - chrony Client SW
* Statum 0 => Atom-Uhr
    * `chrony tracking`
    * `timedatectl` - Zeit einstellen
        * `timedatectl set-time 00:00`
        * `timedatectl set-ntp 1` - NTP enableln
#### 7 - Tunnels
* alternative zu NAT
* Typen
    * IP-IP = IP over IP
        + IP-Packete senden
    * GRE
        + auch andere Packete
* Bsp: braucht 2 Router
    * Router 1:
        * `sudo nano /etc/sysconfig/network-scripts/ifcfg-tun0`
            * `DEVICE=tun0`
            * `TYPE=GRE`
            * `BOOTPROTO=none`
            * `ONBOOT=no`
            * `PEER_OUTER_IPADDR=192.168.0.10`  - IP des Routers der an das NW angeschlossen ist zu dem Tunnel gehen soll
            * `PEER_INNER_IPADDR=192.168.2.0`  - IP des Tunnel-Ziel-NW
            * `MY_INNER_IPADDR=10.0.2.6` - IP des eigenen Routers
        * `sudo ifup tun0`
        * Router 2:
        * `sudo nano /etc/sysconfig/network-scripts/ifcfg-tun0`
            * `DEVICE=tun0`
            * `TYPE=GRE`
            * `BOOTPROTO=none`
            * `ONBOOT=no`
            * `PEER_OUTER_IPADDR=192.168.0.6`  - IP des Routers der an das NW angeschlossen ist zu dem Tunnel gehen soll
            * `PEER_INNER_IPADDR=10.0.2.6`  - IP des Tunnel-Ziel-NW
            * `MY_INNER_IPADDR=192.168.2.10` - IP des eigenen Routers
        * `sudo ifup tun0`
    * noch Firewall einstellen
    * GRE ist nicht verschlüsselt
#### 8 - Troubleshooting
* doppelte IPs -> testen `sudo arping -I enps03 10.0.2.6`
* Richtige NW-Range
* DNS (wenn man z.B nur public Domain anpingen kann)
* Firewall rules (zum testen Firewall ausmachen)
* 