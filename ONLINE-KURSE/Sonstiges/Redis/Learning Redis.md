### 0 - Introduction
* Redis ist In-Memory Data Structure Store
    * wird als DB, Cache und Message Broker benutzt. 
    * ist NoSQL 
    * Schlüssel-Wert-Speicher
#### 1 - Course prerequisites
* es wird Node.js-Server verwendet
#### 2 - Exercise Files
* `.babelrc`-Datei ist wichtig, damit man ES6-Server starten kann.
* Dateien: `redis.conf` und `redis2.conf` in Redis-Installations-Verzeichnis kopieren
### 1 - Settig Up
#### 1 - Install Redis
* www.redis.io eventuell von github herunterladen
* `wget http://download.redis.io/releases/redis-5.0.5.tar.gz` oder `curl -O http://download.redis.io/releases/redis-5.0.5.tar.gz`
* `tar xzf redis-5.0.5.tar.gz`
* `cd redis-5.0.5.tar.gz`
* `make`
* `src/redis-server` - Redis-Server starten, Default-Port: 6379
* Unter Apple muss man für make und wget Apple Developer Tools installieren
* im Terminal zu Redis-Installation-Verzeichnis gehen.
* `src/redis-cli` - CLI für Redis-Server
    * `set name manny`
    * `get name` 
#### 2 - Setting up Redis with ioredis
* Ordner `redis` erstellen zum Ordner naviggieren und ->
* `npm init`
    * dann einfach Enter überall 
    * es wird `package.json` erstellt
* `npm install --save-dev/dev babel-cli babel-preset-env babel-preset-stage-0` - Babel ~ Lint für JS
* `npm installl --save ioredis nodemon` - ioRedis installieren + nodemon = bei Änderung wird Redis-Server automatisch neugestartet
* in `package.json`
    * bei `redis` -> `scripts` -> bei `start` `"nodemon ./index.js --exec babel-node -e js` - was beim `npm start` passieren soll
* in `redis`-Odner Datei `.babelrc`-Datei erstellen. Diese Datei wird benötigt, um Babel-PreCompiler zu starten:
```json
{
    "presets":[
        //was man vorher mit npm installiert hat
        "env",
        "stage-0"
    ]
}
```
* in `redis`-Ordner Datei index.js erstellen
```js
import Redis from 'ioredis';  // Input-Output-Redis

const redis = new Redis(); // man muss eventuell hier die IP des Redis-Hosts einsetzen
redis.set("name", "Kirill");
redis.get("name", (err, result) => { //wenn result oder err zurückgeliefert und beide nicht Null dann führe disen Block aus
    console.log(result);
})
```
* `npm run start` oder `npm start`
* Fazit:
    * man hat Node.js-Server installiert, der eine Verbindung zum im vorherigem Kapitel installiertem Redis aufbauet. 
#### 3 - Overview of the client tools
* man kann auch andere Redis-Clients statt node.js benutzen
    * redis.io/clint -> auf die Sprache klicken -> es wird die IO-Lib angezeigt
### 2- Introduction to Redis Basics
#### 1 - Introduction to Redis
* is Open-Source in-Memory-Data-Structure-Store. Unterstütze Typen:
    * string, set, lists, sorted-set, bitmaps, hyperloglogs, geospatial indexes usw.
* ist in *C* geschrieben
#### 2 - Data types available
* Key - Eigenschaften-Name
    * Bsp: name -> Kirill (name = Key)
* Values:
    * Strings
    * Lists
    * Hashes 
    * Sets
    * Sorted Sets - Liste von sortierten Unique-Strings
#### 3 - Redis persistence explained
* Daten werden in Memory gespiechert für Fasten Access
* Zwei Optionen:
    1. Redis database file (RDB)
        * ~ snapshots, erstelt Point-In-Time Kopien der Daten
        * ist default
    2. Append-only file (AOF)
        * benutzt Logs um Datasets zu rebuilden
        * logt jede Operation in System-File, beim Restart, wird dieses Log rebildet. Kann sehr groß werden.

#### 4 - Setting up persistence
* Beste Strategie:
    * AOF wegen ihrer Geschwindigkeit benutzen
    * RDB wegen Disaster-Recovery.
    * beide benutzen => für alles gewaffnet
* Persistence einstellen
    * zu *redis...* gehen
    * *redis.conf* öffnen
    * nach snapshot-Section suchen - RDP vorkonfiguriert
        * `save 900 1` - bedeutet wenn nach/innerhalb 900 Sek ein Key geändert wurde => einen Snapshot machen
    * `appendonly yes` - AOF an
    * `src/redis-server /pfad/zu/redis.conf` - Redis-Server mit redis.conf starten
        * es wird *appendonly.aof* in *redis..*-Ornder für AOF angelegt 
#### 5 - Setting up replication
+ zweiten Server zur Rerplication einstellen
    + in *redis-...* gehen
    * redis.conf kopieren und *redis2.conf* nennen
    * nach *port* suchen
        *  sollte in der Section mit bind sein
    * einfügen: auf `port 6380` ändern
    * nach *slaveof* suchen
    * man sollte in Sektion *Replication* sein
    * `slaveof ip-address-des-main-servers main-server-port` auskommentieren und ergänzen
    * in *redis2.conf* `appendfilename "appendonly2.aof` umändern
    * `src/redis-server /pfad/zu/redis.conf` und `src/redis-server /pfad/zu/redis2.conf`

#### 6 - Redis further configuration
* im laufenden Server Configs ändern in CLI mit `config-set` ändern.
* Bsp in CLI:
    * `CONFIG GET SAVE "60 1"` - *save* einfügen
* in redis.conf
    * nach *requirepass* suchen
        * auskommentieren + `requirepass sicheresPassword`
* in redis2.conf
    * nach *requirepass* suchen
        * auskommentieren + `masterauth main-serverPassword`
* beide Server restarten
* `src/redis-cli -a sicheresPassword`
### 3 - Datasets in Depth
#### 1 - Exploratoin of strings
* in CLI
    * `set firstName Manny`
    * `get firstName` -> Manny
    * `set address 453`
        * `inc address` increment address
        * `incrby address 100` um 100 incrementieren.
        * `decr address`
        * `decrby address 100` 
#### 2 - Strings in action
#### 3 - The hash data stucture
#### 4 - Hashes in action
#### 5 - Exploration of Lists
#### 6 - Lists in action
#### 7/8 - Challenge + Solution: Implement ioredis
#### 9/10 - Challenge + Solution: Explore sorted sets

### 4 - Advanced Concepts
#### 1 - Security with Redis
#### 2 - Publish ans subscribe with Redis
#### 3 - Redis cluster and Sentinel