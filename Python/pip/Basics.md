+ `pip3 install package`
+ `pip3 install`
+ `pip3 show --files package` - Infos zum Package anzeigen
+ `pip3 list` - zeigt alle installierten Packages
+ `pip3 list --outdated`
+ `pip3 install --upgrade package`
+ `pip3 uninstall package`

### pip installieren:
#### pip über apt installieren - 1
+ `sudo apt-get install python3-pip`
+ `pip3 install -U pip` - pip upgraden
#### pip über apt installieren - 2
+ `sudo apt-get install python3-venv python3-pip`
#### mit python installieren
+ `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`- pip herunterladen
+ `python3 get-pip.py`

### Virtaulenv
#### Installation:
* `pip3 install virtualenv`
* man kann auch über github virtualenv installieren
#### Benutzung
* `virtualenv myEnv1` - Virt Env erstellen
* `virtualenv --system-site-packages myEnv1` - auch die Python-Bibs aus */usr/lib/pythonX.X/site-packages* einbinden
* `virtualenv --extra-search-dir=/my/dir myEnv1` - eigenen Pfad für Bibs usw. angeben
* `source ~/myEnv1/bin/activate` - Env Aktivierene, dabei wird */bin* des *myEnv1* in Path als erster Eintrag eingetragen
* ! man muss im Kopf behalten, wann Python-Bibs aus */usr/...* ausgeführt werden sollen
* `deactivate` - Env ausmachen 
* `rm -r ~/myEnv1` - Env löschen

### VirtualEnvWrapper - Alle Virt Env managen
#### 1 - Installation
* `pip install virtualenvwrapper` - es wird Dab