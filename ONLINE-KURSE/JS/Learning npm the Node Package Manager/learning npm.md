### 1 - Introductin and Installation
<details>

#### 1 - What are packages and npm
* Node.js-Packages/Dependencies installieren
* Node.js-Projecte haben Project-Datei, wo steht, welche Packages gebraucht werden.
* npmjs.com - Packages durchsuchen
* node.js und npm gehören zusammen
#### 2 - Installing Node/npm on Mac
#### 3 - Installing Node/npm on Windows
#### 4 - Installing Node/npm on Linux
* zu https://github.com/nodesource/distributions gehen, unten schauen, wie man auf bestimmten Distros installiert
* `curl -sL https://deb.nodesource.com/setup_10.x | bash -`
* `sudo apt-get install -y nodejs`

</details>


### 2 - Getting Started with npm

<details>

#### 1 - Initializing a package.json file
* bei jedem Node.js-Project einen Package-File erstellen
    * `npm-test`
    * den Namen für Packages usw. geben
    * es wird *.json* erstellt.
* Wenn man jetzt Packages installiert, werden sie hier erscheinen
#### 2 - Addin node packages
* man kann Packages global oder lokal installieren
* Local = in Projekt-Ordner
* Glboal = für alle Projekte
* Neuen Package holen
    * `npm install express` - es wird package.json erweitert
    * `npm install babel-cli babel-preset-stage-0 babel-preset-es2015 --save-dev` - Packet nur für Entwicklung installierrn. in *package.json* wird *dev-Dependencies*-Abteilung erstellt, die in Production-Build nicht eingefügt werden
* googeln wofür *.babelrc*
#### 3 - Managing global directory
* Linux: */usr/local/lib/node_xxx; Windows: *%AppData%\npm\node_modules* werden die globalen Dependencies installiert
* `npm install -g pacakge`
    * `npm install -g react` - man muss aber *sudo* benutzen; also `-g` bedeutet global
* https://docs\npmjs.com\ - Doku bei Problemen
#### 4 - Updating a package
* `npm install -g eslint@5.2.0` - mit *@x.x* bestimmte Version installieren
* `npm outdated` - nach Package-Updates schauen für lokale Packages
* `npm outdated -g` - nach Package-Updates schauen für globale Packages
* `npm update package` oder bei Fehlern `npm install -g package`
#### 5 - Removing a package
* `npm uninstall package`
#### 6 - Sematic versioning
+ Versionen:
    * MajorRelease.MinorReleas.PatchNr
    * *^* -> ^1.X.X - wird letzte Version für 1. installieren
    * *~1.5.X* - letze Version von 1.5
    * *1.5.6* - bestimmte Version installieren
#### 7 - Introduction to package-lock.json
* ist der Output npm-Installationen. Er merkt wechle Version momentan installiert wurde und so werden die Dependencies beachtet

</details>

### 3 - Advanced Subjects

<details>

#### 1 - Working with a npm cache
* Falls etwas nicht funktioniert, dann npm-Cache leeren
* `npm cache verify` - Zeigt die Info zu Cache
* `npm cache clean --force` - Cache leeren, falls die vorherige Ausgabe Fehler ausgibt
#### 2 - Run an npm audit
* `sudo npm install npm@latest -g` - letzte npm-Version global installieren
* `npm audit` - zeigt Warnings zu NPM + kleine Beschreibung dazu
* Wenn SEMVEER-Warning - dieser Patch könnte das Package kaputtmachen
* `npm audit fix` - automatisch fixen oder die vorgeschlagenen Packages selbst installieren
#### 3 - Scripting in package.json
* auf npm-Seite schauen, welche Scritps es gibt.
* Sckripts sind in  Teil in package.json:
```
"scripts":{
    "name": "befehl optionen"
}
```
* man kann aber im Terminal die Scripts laufen lassen, den Teil *befehl optionen* in Terminal eingeben.
* um z.B Node.js server zu starten
* wenn man weitere Scripts laufen will, einfach weitere zeile in *scripts* einfügen
* Skript aufrufen:
    * `npm run script-name` 
#### 4 - Introduction to npx
* `npx -p @angular/cli ng new myapp` - wird Angular/CLI temporär installiert ü `ng new myapp` ausgeführt, ohne dass dabei dass Packet wirklich installiert wird
* `npx mocha` - um z.B Mocha-Test ausführen
* `npx cowsay hello!`
* man kann npx-Sckripte auch als *scripts* ausführen
#### 5 - Other alternatives to npm
* *yarn* - von Facebook www.yarnpkg.com
    * man kann yarn mit npx ausprobieren: `npx yarn` 
* *ni* - GitRepo
    * `npx -p better-npm-install ni` 

### Next Steps:
* npm-Packages publizieren
</details>