### Quickstart
* `pip install package`
* `pip install /pfad/package-x.x.whl` - heruntergeladenes Packet installieren
* `pip sho --files package` - zeigt welche Dateien vom Packat installiert werden
* `pip list --outdated` 
* `pip install --upgrade package`
* `pip uninstall package`

### Installation
* Pip ist schon bei Versionen ab 2.7.9 und 3.4 schon installiert
* Virtuelle Env die mit `virtualenv` und `pyvenv` erstellt wurden ist *pip* ist auch installiert 
#### mit get-pip.py installieren
* `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
* `python get-pip.py`
    * dabei muss man aufpassen, da *get-pip.py* nicht auf OS achtet
    * installiert:
        1. setuptools = um *source distributions* zu installieren
        2. wheel = um *wheel cache* zu bilden
    * Optionen:
        * `--no-setuptools` - setuptools nicht installieren
        * `--no-wheel` - wheel nicht installieren
        * `--user` - zu User installieren
        * `--proxy="http://[user:passwd@]proxy.server:port"` - hinter Proxy installieren
        * `python get-pip.py pip==9.0.2 wheel==0.30.0 setuptools==28.8.0` - bestimmte Versionen von *wheel* und *setuptools* installieren
#### mit Linux OS Package Manager installieren
* `sudo apt install python3-venv python3-pip` - z.B Debian
#### Upgrade pip
* `python -m pip install -U pip` ODER
* `pip install -U pip`

### User Guide
* `pip ...` - wenn pip nicht zugreifbar ist => `$PATH` checken
* `python -m pip ...` - pip über Python-Interpreter starten
* In Python Programmen kann man pip über `import pip` benutzen

#### Packete installieren (von PyPI installieren):
* `pip install package`
* `pip install package==x.x.x`
* `pip install package>=x.x.x` - minimum Version installieren

#### Proxy Server benutzen
* also Proxy für pip-Installationen einstellen
    1. `--proxy [user:passwd@]proxy.server:port`
    2. Proxy-Einstellungen aus Config-Datei benutzen
    3. Standard Env-Variable `http_proxy`, `https_proxy` und `no_proxy` setzen
    4. Env-Variable `PIP_USER_AGENT_USER_DATA` benutzen, um JSON-encoded String zu der User-Agent-Variablen hinzufügen

#### mit Requirements Files installieren
* enhalten Packag-Namen, die installiert werden sollen
* `pip install -r requirements.txt` 
* 4 Uses Cases für Requirements Files:
    1. Um `requirements.txt` zu erstellen, die man dann weiter geben kann.
        * `pip freeze > requirements.txt` 
        * `pip install -r requirements.txt` - auf dem zweiten Rechner
    2. Um dependencies zu lösen, da pip selbst es noch nicht kann.
        * Bsp: if pkg1 requires *pkg3>=1.0* and *pkg2* requires *pkg3>=1.0,<=2.0*, and if *pkg1* is resolved first, pip will only use *pkg3>=1.0*, and could easily end up installing a version of pkg3 that conflicts with the needs of *pkg2*. To solve this problem, you can place *pkg3>=1.0,<=2.0*
        * dann in `requirements.txt
        ``` 
        pkg1
        pkg2
        pkg3>=1.0,<=2.0
        ```
    3. Um alternative Versionen von Dependecies zu installieren:
        * Bsp: *ProjectA* in your requirements file requires *ProjectB*, but the latest version (v1.3) has a bug, you can force pip to accept earlier versions
        * dann in `requirements.txt
        ```
        ProjectA
        ProjectB<1.3
        ```
    4. um Dependencies mit lokalen Patces zu überschreiben, die in git leben. 
        * Bsp: *SomeDependency* from PyPI has a bug, and you can’t wait for an upstream fix. You could clone/copy the src, make the fix, and place it in VCS with the tag *sometag*.
         * dann in `requirements.txt
         ```
         git+https://myvcs.com/some_dependency@sometag#egg=SomeDependency
         ```
#### Constraints Files
* sind Requirement Files, die nur kontrollieren, welche Version ist installiert, aber nicht, ob instaliert oder nicht
* Syntax von `constraints.txt` ist fast identisch zu `requirements.txt`
* `pip install -c constraints.txt`
* man erstellt ein `constraints.txt` und benutzt ihn in der ganzen Firma, um zu checken, ob überall die richtigen Versionen der Packete installiert sind

#### Installing from Wheels
* ist built, archive Format. Beschleunigt das Bilden und Installieren aus source Archiven. (siehe Wheel docs)
* Pip wählt *wheels*-Installation vor einer andren
    * um dieses Verhalten auszuschalten => `pip install --no-binary ...`
* `pip install package-x.x.x.whl` - aus wheel Archive installieren
* da wo *wheels* nicht verfügbar ist, kann man mit `pip wheel` wheels für eigene *requirements* bilden. (braucht `wheel`-Packet `pip install wheel`)
    * `pip wheel --wheel-dir=/local/wheels -r requirements.txt` - bildet *wheels* für requirements in den lokalen Pfad `(--wheel-dir)`.
    * `pip install --no-index --find-links=/local/wheels -r requirements.txt` -dann Requirements mit lokalem *wheels* installieren

#### Uninstalling Packages
* `pip uninstall package`
    * beim Upgrade deinstalliert pip das alte Packet

#### Packete auflisten
* `pip list`
* `pip list --outdated`
* `pip show package`

#### Nach Packeten suchen
* `pip search "package"`

#### Konfiguration
##### Config File
* man kann alle pip-Optionen in `ini`-Style in einer Konfig Datei schreiben. Konfig datei kann sein:
    1. per-user
        * in Linux: `$HOME/.config/pip/pip.conf` oder `$HOME/.pip/pip.conf` 
        * MacOs: `$HOME/Library/Application Support/pip/pip.conf`
        * Windows: `%APPDATA%\pip\pip.ini` oder `%HOME%\pip\pip.ini`
        * man kann auch Konfig Datei irgendwo ablegen und den Pfad dann in `PIP_CONFIG_FILE`-Variable ablegen
    2. per-virtualevn
        * Unix/Linux`$VIRTUAL_ENV/pip.conf`
        * Windows: `%VIRTUAL_ENV%\pip.ini`
    3. site-wide
        * Unix/Linux in `/etc/pip.conf` oder in beliebigem Subpfad von `XDG_CONFIG_DIRS`-Variablen
        * MacOS `/Library/Application Support/pip/pip.conf`
        * Windows `C:\Documents and Settings\All Users\Application Data\pip\pip.ini`
* die Konfigs werden in obiger Reihenfolge gelesen und letzteres überschreibt gleiche Settings von der vorherigen.
* Bsp: `--index-url`, `--default-timeout`
```
[global]
timeout = 60
index-url = https://download.zope.org/ppix
```
* für einzelne Pip-Befehle kann man unterschiedliche Optinen setzen -> Bsp: *gobale* und für `pip freeze`
```
[global]
timeout = 60

[freeze]
timeout = 10
```
* Bsp für `pip install` und boolean-Optionen:
```
[install]
ignore-installed = true
no-dependencies = yes
```
* Appending options like --find-links can be written on multiple lines:
```
[global]
find-links =
    http://download.example.com

[install]
find-links =
    http://mirror1.example.com
    http://mirror2.example.com
```

#### Environment Variablen
* man kann pip- Optionen auch per Env-Variablen setzen. Syntax: `PIP_UPPER_LONG_NAME`
    * Bsp 1: `export PIP_DEFAULT_TIMEOUT=60` ist = `pip --default-timeout=60`
    * Bsp 2: `export PIP_FIND_LINKS="http://mirror1.example.com http://mirror2.example.com"` ist = `pip install --find-links=http://mirror1.example.com --find-links=http://mirror2.example.com`
    * Booleans => mit `no` oder `false` oder `0`

#### Konfig Priorität
* Terminal pip-Eingaben haben die oberste Priorität => überschreiben alle vorherigen Konfig-Einstellungen.

#### Pip-Completion
* kann man für verschieden Shells setzen:
    * Bash: `pip completion --bash >> ~/.profile`
    * Zsh: `pip completion --zsh >> ~/.zprofil`
    * Fish: `pip completion --fish > ~/.config/fish/completions/pip.fish`

#### aus lokalen Paketen installieren
* = wenn PIP-Paket schon heruntergeladen:
* `pip download --destination-directory /prad/zu/ordner -r requirements.txt` - das PIP-Paket herunterladen
* `pip wheel --wheel-dir /pfad/zu/order -r requirements.txt` - wheels fpr diese Pakets erstellen.
* `pip install --no-index --find-links=/pfad/zu/ordner/ -r requirements.txt` - die heruntergeladenen PIP-Pakete herunterladen

#### Only if needed Recursive Upgrade
* es gibt zwei `--upgrade-stratege`:
    * `eager` - alle dependencies upgraden, egal was in requirements steht
    * `only-if-needed` - upgarded Dependency nur, wenn es Parent Requirements nicht erfüllt -> ist Default
* `pip install --upgrae --no-deps PacketName`

#### User Installs
* die Option `--user` - Pakete in User-Ordner installieren
* User-Schema kann eingestellt werden über die ENV-Variable `PYTHONUSERBASE` -> `site.USER_BASE` wird dann upgedatet
* `export PYTHONUSERBASE=/myOrdner`
* `pip install --user PipPacket`
    * wenn das Paket schon global gibt => wird nicht installiert
    * wenn man in VirtEnv unterwegs ist, wird auch nicht installiert.
    * mit `ignore-installed` - kann man die Installation erzwingen
### Ensuring Repeatability
#### gepinnte Versionen
* = requirements.txt + `pip freeeze` benutzen
* Installationen mit `--no-deps` machen
#### Hash-checking Mode
* Hilfe bei Versionen + Sicherheit
* in requirements.txt z.B.:
    * `FooProject == 1.2 --hash=sha256:2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b982` 
* git für automatischen Server Deployment
#### Bundle Installationen
* mit `pip wheel` kann man Project Dependencies bündeln zu einem Archiv.:
    * Verpacken:
    ```bash
    tempdir=$(mktemp -d /tmp/wheelhouse-XXXXX)
    pip wheel -r requirements.txt --wheel-dir=$tempdir
    cwd=`pwd`
    (cd "$tempdir"; tar -cjvf "$cwd/bundled.tar.bz2" *)
    ```
    * Entpacken:
    ```bash
    tempdir=$(mktemp -d /tmp/wheelhouse-XXXXX)
    (cd $tempdir; tar -xvf /path/to/bundled.tar.bz2)
    pip install --force-reinstall --ignore-installed --upgrade --no-index --no-deps $tempdir/*
    ```
* aber diese Packete sind dann OS/Architekture-Abhängig
### PIP in Programm benutzen
* pip ist ein Programm in Python geschrieben
* kann man mit `import pip` benutzen. Aber sollte man eigentlich vermeiden: 
    1. pip ist nich Thread sicher
    2. User-Code kann überschrieben werden
    3. bei Doppeltem Ablaufen kann Code überschreiben
+ wenn man Packete installiert, während das Pyhton-Programm läuft, kann auch zu Problemen führen bzw. sich nicht wie erwartet verhalten.
* man sollte PIP in Subprocess laufen:
    * `subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])` 
    * `reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])` - pip-Ausgabe abspeichern bzw. den Subprozess ausgibt.
* dazu gibt es nocht Alternativen:
    * `packaging`
    * `setuptools`
    * `distlib`

### Reference Guide:
    * https://pip.pypa.io/en/stable/reference/