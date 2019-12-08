### 0 - Introdution 
* Kurs mit CentOS
+ *STRG+T* bei laufender VM - Snapshot 
#### 1 - Lab setup
+ nach Einstellung des NW Snapshot machen
+ Klone -> linked Klone - weniger Speicherplatz
#### 2 - Install guest additions
* `sudo yum -y update`
* `sudo kill -9 PID`
* `sudo reboot`
* `sudo yum group install -y --setopt=group_command=objects "Development Tools"` - Dev Tools für CentOS installieren
* `sudo yum install -y kernel kernel-devel` - Kernel-Headers
* Guest Addition reinlegen + installieren
* Restart
### 1 - Performance Monitoring tools
#### 1 - Introduction to performance testing
* Bevor Update System backupen
* Testen der Updates zuerst auf Kopie
#### 2 - Monitoring processes using ps
* `ps` - zeigt Processes des Users
* ps hat 3 Syntax-Varianten: Unix, BSD-keine Dashes, GNU
* `ps -e` - alle Prozesse
* `ps -eH` - Kind-Eltern Prozesse anzeigen
* `ps -ef` - Alle anzeigen
* `ps -eF` - noch Memory + CPU anzeigen
* `ps -eFl` - alles mögliche anzeigen
* `ps -e --format uid,pid,ppid,%cpu,cmd` - Ausgabe anpassen
* `ps -e --format uid,pid,ppid,%cpu,cmd --sort %cpu` - Ausgabe noch sortieren
* `ps -e --format uid,pid,ppid,%cpu,cmd --sort -%cpu` - absteigend sortieren
* `ps -U root` - Prozesse von User *-u* - User ID, *-G* - Gruppe, *-g* - GUID
* `ps -C firefox` - gleiche Prozesse eines Programm anzeigen
Bsp:
* `ps -e --format uid,pid,tty,rss,cmd --sort rss`
* `ps -U kirill --format %mem | awk '{memory +=$1};END {print memory}'` - Memory für User berechnen
#### 3 - Monitoring precess in real time
* `top`
    + `l` - toggle display load average
    * `1` - CPU für einzelne CPUS
    + `t` - toogle how tasks are displayed
    * `1 t` 
    + `m` - toggle how memory usage is displayed
    * `f` - field management
    * `SPACE` 
    * `s` - designate sort field
    * `<-` und `->` Zeilen nach oben/unten
    *  `q` 
    * `c` - toogle between Command name/Command line
    * `Shift + u` + Kirill - Processe von User anzeigen
    * `Shift + u` + Enter - Alle Prozesse anzeigen
    * `k` + PID - Signal killen
    * `r` + PID - renice a task
    * `shift + m` - nach Memory Usage sortieren
    * `shift + P` - nach CPU % sortieren
    * `shift + t` - nach CPU zeit sortieren
    * `shift + n` - nach Process ID sortieren
* `man top`
#### 4 - Monitoring processs using GNOME System Monitor
#### 5 - Use Performance Co-pilot (PCP) to gather statistics
* PCP - Performance monitoring suite of tools, services and libs
* kann archivierte Logs abspielen und analysieren
* ist für Windows, Linux und Mac
* kann locale oder remote Hosts analysieren
* hat Daemon laufen, der Daten von agents samelt
* `sudo yum install -y pcp pcp-gui pcp-doc pcp-system-tools`
* `sudo systemctl start pmcd`
* `pcp` - Testen ob PCP läuft
* `pmstat` - Stats der Systems (5 sec Takt)
* `pmatop` - ~ top
* `pmcollectl` - Stats für CPU, Festplatte und NW-Platten
* `pmchart` - GUI, -> eigene Monitorings zusammenstellen
* `pmval`
* `pminfo` 
* PCP-Doku anschauen
#### 6 - Use turbostat to gather CPU statistics
* turbostat - wie lange CPU in verschiedenen Zuständen bleibt
* `sudo yum install -y kernel-tools` 
* `sudo tubostat` - 5 sec Takt
    * `C-States` - idle Power states
    * `C0-states` - null idle power states
    * `P-States` - executing states
    * `PC-states` - Package C-States: idle states for all cores
    * Mehr Info: http://software.intel.com/en-us/articles/power-management-states-p-states-c-states-and-package-c-states
#### 7 - Use SS to gather network statistics
* netstat - NW-Stats anschauen
* `netstat -s` - alle Packet-Counters
* `nstat -asz` - alle Packete-Counters
* `nestat -a` oder `ss -a` - alle Ports anzeigen
* `netstat -l` oder `ss -l` - Ports zu Services -> eventuell mit grep nach Service oder Port suchen
* `ss -lp` oder `netstat -lp` - Ports zu Service
* `netstat -t -a` oder `ss -t -a` - alle TCP-Verb
* `netstat -u -a` - UDP
* `netstat -w -a` - Row-Sockets
* `netstat -i` oder `ip -s link` - Interface Stats
* `netstat -r` oder `ip route` - Routing STats
#### 8 - Other CLI parformance monitoring tools
* iostat - Input/Output-Stats
    * `sudo yum install -y sysstat` 
* irqbalance - Iterupt-Balance
    * `sudo yum install -y irqpackage`
    * `man irqbalance`
* vmstat - CPU, Memory, DeviceIO
    * `vmstat`
    + `vmstat -s` - Event-Counters + CPU-Stats
    + `vmstat -d` - IO-Devices Stats
+ x86_energy_perf_policy - Energie verwalten
* sar - Aktivitäten auf STDIN/OUT
* numastat/numad - Systeme mit non-uniform-Arch beobachten
* systemtap 
* oprofile 
### 2 - Tune the Kernel with tuned
#### 1 - Introducing to tuned
* tuned - Service um Devices zu monitoren + System Settings tunen. Hat Profile für *Low latency*, *High throughput*, *power saving*. Profile kann man kopieren, speichern, und zwischen ihnen wechseln
* normalerweise läuft als Service, kann man auch als *one time only* starten
* kann statische und dynamische Settings verändern
* hat zwei Plugin-arten
    1. Monitoring - disk, net, load
    2. Tuning - cpu, net, sysctl, usb, vm, audio, disk, mounts, sysfs, video
* `sudo yum install -y tuned`
* `sudo systemctl start tuned`
* `sudo systemclt enable tuned`
* `sudo tuned-adm list` - Profile anzeigen
* `sudo tuned-adm active` - aktives Profile anzeigen
* `sudo tuned-adm profile desktop` - Profile auf *desktop* wechseln
+ Wenn mehrere Profile angegeben werden, werden Settings aus den Profile gesetzt, letzte Profile überschreibte gleiche Settings des vorherigen
* `sudo tuned-adm recommend`
#### 2 - Install additional tuned profiles
* `tuned-profile-compat`
* `tuned-pfofile-atomic` - Atomic Host und Guest Profiles
* `tuned-profiles-realtime` 
* `tuned-profiles-nfv`
#### 3 - Create custom tuned profiles
* man kann eigne Profile erstellen oder existierende erstetzen. Custom Profiles werden in */usr/lib/tuned* gespeichert.
* `cd /etc/lib/tuned/ && ls` - vorhandenen Profile ansehen
* `cd destop && ls`
* `less tuned.conf`
* wenn man eigne Profile erstellen will, kann man vorhandenes Kopieren und verändern. 
    * `cp -Rf desktop /etc/tuned/customprofile`
    * `cd /etc/tuned/customprofile`
    * `nano tuned.conf`
    * Profile haben Main-Section weitere Sections sind Plugins (Name der Section ist Plugin) `include=...` - welcher Profile includiert wird
    * `summary=Hinweise zum Profile`
    * `[disk] # Diskmodul verändern (Disk-Plugin)`
    * `devices=sda` oder `device=sd*`=sda/sdb/usw oder `device=!sda`=nicht sda
    * `disabla_barriers=false`
    * man kann mehrere Profile includieren, bei gleichen Settings, werde die vom letzen vorherige überschreiben
        * `replace=1` - Ersetzung erzwingen
        * `enabled=0/1` - Plugin aktivieren/deaktiveren, sinnvoll wenn man Plugins auf includieren Profilen deaktivieren möchte
    * `tuned-adm list`
    * `tuned-adm profile customprofile`
    * `tuned-adm active`
#### 4 - Use PowerTOP suggestions in tuned
* Power Usage und Wake UP CPU-Komponente monitoren
* `yum install -y powertop`
* `yum install -y tuned-utils`
* `powertop2tuned powetune` - scant das System und erstellt tuned-Profile
* `cd /etc/tuned/powertune/` - *powertune* wurde mit vorherigem Command erstellt. alle Parameter sind erstmall kommentiert, man muss sie manuell aktivieren (aus Sicherheitsgründen)
* `tuned-adm profile powertune` - Powerttune-Profile aktivieren
#### 5 - Boot-time kernel parameters
* mit tuned-Plugin Boot-Parameter ändern
* `nano /etc/tuned/customprofile/tuned.conf`
* Boot-Seckton hinzugüfen:
    * `[bootloader]`
    * `cmdline=quite`
* `tuned-adm profile customprofile`
### 3 - Manually Tune the Kernel
#### 1 - Understanding Linux kernel verstions
* `yum -q list installed kernel-*` - Kernelversion anzeigen
#### 2 - Tune live kernel parameters manually using sysctl
* Kernel-Parameter mit tuned-Profilen managen
* Um Configs zur Testezwecken ändern -> sysctl benutzen (nicht systemctl), bevor dann diese als tuned-Profile implementieren. Parameter sind Dateien in */proc/sys*, die dann mit *sysctl* veränder werden können. 
* `sysctl -a` - Parameter, die mit sysctl verändert werden können anzeigen
* `sudo echo 1 > /proc/sys/kernel/sysrq` - kommt Permissions denied, da Redirectiom mit normalen Rechten stattfindet
* `sudo sysctl -2 kernel.sysrq="1"`
#### 3 - Use Tuna to tune the kernel
* Tool um Pläne, Thread Priotitäten, IRQ Handlers und isolated CPUs und Sockets zu verbessern. HAT GUI.
* `yum install -y tuna`
* `tuna` - GUI starten
* Drei Tabs: Monitoring, Profile management, Profile editing
* Rechtsklick auf Prozesse, um Menü anzuzeigen
* man kann Prozesse auf CPUs ziehen = Prozess wird auf diese CPU ausgeführt -> in Set Process Attributes bei Affinity wird jetzt die entsprechende CPU-Nr angezeigt.
* `tuna --show_threads` - Threads und Prozesse anzeigen
* `tuna --threads=1` --show_threads - Zeigt den Thread-ID=1 an
### 4 - Kernel Module Tuning
#### 1 - Linux Kernel directory structure 
* `ls -l /boot` - Linux Kernels + Init RAM, Grub
* `ls -l /boot/grub2`
    * *grub.cfg* - Boot-Menu + fürht Kernel aus
* `ls /proc` - wird beim Start in RAM erstellt und beim Shutdown zerstört. Ordner mit Nummer = Process-ID. String-Ordner = Info über System
* Kernelmodule sind in */lib* oder */lib64*
* `ls -l /lib/modules/$(uname -r)/kernel` - Kernel-Module, Kernel-Drivers usw.
#### 2 - Manage kernel modules
* Es gibt Module die weitere Funktionen für den Kernel erweitern. In */lib/modules/* und */lib64/modules*
* `ls /lib/modules/$(uname -r)/kernel`
* `lsmod` - geladene Module ansehen
* `modinfo modulname` - genaue Info zum Modul anzeigen
* `sudo modprobe -v modulname` - Modul laden
* `sudo modprobe -v -r modulname` - Modul entfernen
* manche Module können Parameter annehmen
* `sudo depmod -v` - Welche Module von HW benötigt werden
* um Modul beim Boot zu starten => Datei in `/etc/modules-load.d` erstellen. Name dabei ist egal. Bps:
    * `sudo nano /etc/modules-load.d/dm-mirror.conf`.
        * `dm_mirror`
* Um Modul blacklisten => Datei in `/etc/modprobe.d` :
    * `sudo nano /etc/modprobe.d/ctxfi.conf`
        * `blacklist snd-ctxfi`
#### 3 - Displaying information about kernel modules
* `ls /lib/modules/$(uname -r)/kernel/drivers/usb/storage` - Module für USB anzeigen
    * Ausgabe: Dateien mit `.ko.xz` - mit xz- kompremiert
* `modinfo usb-storage` - ein Modul aus vorheriger Ausgabe wählen (ohne Endung) 
* `moinfo usb-storage -p` - nur Parameter anzeigen
#### 4 - Installing kernel modules from disk
* Bsp: einen Driver installieren
* `sudo yum install kmod-oracleasm --downloadonly --downloaddir=/tmp/drivers`
* `cd /tmp/drivers`
* `sudo yum install kmod-oracle...rpm`
* `sudo depmod -a` - Module + Dependencies aktualisieren
* Initial RAM-Disk updaten, falls Modul beim Boot geladen werden soll: 
    * `sudo cp /boot/initramfs-$(uname -r).img /boot/initramfs-($uname -r).img.bak` - Backup 
    * `ls /boot`
    * `sudo dracut -f -v` - neuen RAM-Disk erstellen. Letzte Zeile zeigt die neuen RAM-Disk-Datei
    * `sudo lsinitrd neuenRAMName` 
    * reboot
### 5 - Logging Module Tuning
#### 1 - Understainding Enterprise 7 logging
* `journald` in `/var/run/ (ist in RAM)
* Da in RAM => nicht persistent, kann man aber persistent machen
* `sudo journalctl`
* `sudo journalctl -k`- Nur Kernel
* `sudo journalctl /sbin/crond`
* `sudo journalctl -u crond` - Systemd-Sachen anzeigen
* `sudo journalctl -f` - Journal tailen
* `sudo mkdir -p /var/log/journal`, `sudo systemclt restart systemd-journald` - Journald persistent machen
    * `sudo journalctl -b -1` - Boot 1 - Sachen anzeigen
    * `sudo journalctl --since "2015-01-10 17:15:00`
    * `sudo journalctl --since "2015-01.10" --until "2015-01-11 03:00"`
    * `sudo journalctl yesterday`
    * `sudo journalctl --since 09:00 --until "1 hour ago"`
#### 2 - rsyslog filters
* Facilities = Produzieren logs
* Rsyslog hat 7 Prioritäten
    * den Facilities Prioritäten zuordnen `mail.=crit` `mail.!crit`- Crititsch aussließen, `mail.*` - alle
* Filters z.B:
    * `:msg, contains,"openvpn"` - Messages die nur openvpn enthalten ausgeben 
    * `:hostname, isequal, "Server1"`
#### 3 - rsyslog actions
* Für jedes Filter gibt es einen Action 
    * `cron.* /var/log/cron.log` - Aktion ist in eine Datei zu schreiben (hier syncron)
    + `cron.* -/var/log/cron.log` - asynchron
    * man kann Templates benutzen => siehe man rsyslog.conf
#### 4 - Log to a remote rsyslog server
* `cron.* @192.168.1.100` per UDP
* `*.* @192.168.1.100` alles zur Remote
* `*.* @@192.168.1.100:6514` - TCP + Port statt UDP
* `*.* @@(z9)192.168.1.100` - Kopmremierung - 1-9
* Bsp:
    * Server
        * `sudo nano /etc/rsyslog.conf`
            * `ModLoad imtpc`
            * `sInputTCPServerRun 514`
        * Firewall: `sudo firewall-cmd --permanent --add-port=514/tcp`, `sudo firewall-cmd --reload`
        * `tail -f /var/log/messages`
    * Client
        * `sudo nano /etc/rsyslog.conf`
            * `*.*@@ip-sever:514`
    * `sudo systemclt restart rsyslog`
    * Zum Testen auf dem Client: `sudo logger "Test 1234"`