### 1 - Eine Entwicklungsumgebung für Angular-Proj. installieren + einrichten
#### 1 - node.js installieren
* ist JS-RunTime außerhalb des Browsers
* hat noch Package-Manager (npm)
* mit homebrew (MAC) `brew install node` oder direkt von nodejs.org
#### 2 - git installiren
#### 3 - Umgang mit den Übungsdateien

### 2 - Einführung in Angular CLI
#### 1 - Was ist Angular CLI
* CLI - Command Line Interface
* `ng new` - Project erstellen
* `ng generate component/module/..` - Teile erstellen
#### 2 - Angular-CLI-Alternativen
* Manueller-Setup:
    1. `npm init` - Node.js-Proj. initialisieren
    2. Abhängigkeiten installieren `npm install rxjs core-js @angular/core ... --save`
    3. `tsc init` - TS konfigurieren
    4. SystemJS oder Webpack konfigurieren
* weitere Alternative von https://github.com/angualar/angular2-seed als Start benutzen -> `npm install`
#### 3 - Angular-ClI installieren
* `node --version`
* `npm --version`
* `npm install -g @angular/cli`
* Tipps für Angular-CLI -> auf der Github-Seite: Wiki -> Stories
#### 4 - Projekt-Setup mit Angular CLI aufbauen
* `ng new PROJECT_NAME --directory ORDNDER_NAME --dry-run`
    + `--directory ORDNER_NAME` - Ordner angeben
    * `--dry-run` - zeigt nur an was gemacht wird, ohne es tatsächlich zu machen 
#### 5 - Häufig genutzte Parameter
* nutzliche Optionen:
    * `ng new PROJ --pefix XXX --style scss` 
        1. statt Prefix **app** **XXX** verwenden in Dateien.
        2. `--style scss` - statt css sass verwendent, entsprechende js-Module werden dafür installiert
        3. `--routing true` - so kann man Scenen-Page-Application bauen, verlangt Routing-Modul
#### 6 - Optionale Parameter
* `ng new PROJ ...`
    * `--inline-style` - .css werden ausgelasen, statt dessen direkt in .ts eingefügt
    * `--inline-template` - auch .html inline in .ts
    * `--skip-tests` - keine spec.ts erstellen
    * `--minimal` - vereinigt oberen drei
    * `--skip-install` - npm install auslassen
    * `--skip-git` - kein git-Versionierung erstellen, wenn man z.B andre Versionierung benutzen möchte
* als IDE WebStrom benutz
#### 7 - Angular CLI aktualisieren
* Doku dazu gibt es auch auf github.co/angualr/angular-cli -> update, wobei hier nur Update für CLI gezeigt wird
1. `npm uninstall -g @angular/cli --save-dev` mit `--save-dev` auch aus `package.json` löschen
2. `npm install @angular/cli`
3. eventuell, wenn von Angular verlangt wird `ng update @angular/cli`
4. `ng update @angular/core`
5. `ng update` - checken, ob alles up-to-date ist
6. `npm install -g rxjs-tslint` - Fix-Tool für rxjs-Inkompatibilitäten
    1. `rxjs-5-to-6-migrate -p /src/tsconfig.app.json` - Tool ausführen und rxjs-Inkopatibilitäten beheben
    2. `npm uninstall rxjs-compat --save`
* https://update.angular.io - Tipps was man beim Upgrade machen muss

### 3 - Vorstellung des Angular-CLI-Setups
#### 1 - Die Bedeutung der einzelnen Ordner
* e2e - End-to-End-Test mit Protraktor
* src
    * app - gesamtes Projekt lebt eigentlich hier
    * assets - Ressourcen für Project z.B Images aber keine JS-Skripte (besser mit Webpack Packages erstellen)
    * environments - Einstellungen für Releases z.B Prod vs. Dev: Debugger an/aus
#### 2 - Konfiguraionsdateien im Überblick
1. angular.json - Einstellungen ; meisten bei Erstellung eingetragen
2. editor.config - für IDEs, die dann entsprechende Einstellungen in der IDE machen => alle Entwickler haben gleichen Code-Stil; ~ Profil für IDe
3. package.json - Module, die für Projekt benötigt werden bzw. Tests (DevDepenencies) + Scripts (Commandos)
4. package-lock.json - Dependency-Einstellungen
5. tsconfig.json - Config für TS-Kompiler
    1. es gibt auch `tsconfig.app.json` - für Entwicklung
    2. es gibt auch tsconfig.spec.json - für Tests
    3. es gibt noch tsconfig.e2e.json
6. tsling.json - Linter wurde vor Compiler ausgeführt um Syntax zu checken
#### 3 - Grundlagen der Angular-CLI-Konfiguraion
* Details zu `tsconig.json` kann man auf Angualar-Github-Wiki schauen.
* angular.json
    1. `verion: 1` - Version des Projekts
    2. man kann mit `ng generate projectXXX` Unterprojekte anlegen
    3. `defaultProject`
    4. `projectName: { architect: extract-i18n}` = für internationalisierung - in `architect` werden Veröffentlichungs-Prozesse ~ Releases festgelegt
#### 4 - Deepdive: App-Einstellungen
* `index` - mit welcher HTML gestartet werden soll
* `main` - welche Datei ausgeführt wird, wenn index geaden wird
* `tsConfig` - welche tsconfig.json gilt
* `assets` - wo Images usw. liegen
* `styles` - css für index
* `scripts` - js für index
* `configurations` - Konfigs für Environments (Prod, Dev, usw)
* `server` - wie Code ausgeführt wird. Default: lokaler Server
#### 5 - Startdateien
* `index.html` - Root-HTML
* Scripte und Codes werden per Code eingefügt. Für index.html ist alles in `angular.json` -> Zusammensetzung macht **webpack**
* in `index.html` ist noch `<base href="/">` wichtig. Definiert wo auf dem richtigem Server, die Angualar-App wirklick liegt. Deafult ist `/`, da meistens ins Root-Verzeichnis des Servers kommt
#### 6 - Polyfills konfigurieren
* in angular.json gibt es Feld `"polyfills": "src/polyfills.ts"`
    * diese Datei importiert eigentlich nur ein Polyfill, viele sind aber auskommentiert z.B für ES9, ES10, ES11
#### 7 - Polyfills installieren und einbinden
* Angular kommt mit `core-js`-Polyfills
* => eventuell muss man entsprechende Polyfill-Module importieren
* Bsp: **web-animaitons.js** 
    1. in **polyfills.ts** `import web-animation-js` einstragen
    2. `npm install --save web-animations-js`
#### 8 - Einbindung der tsconfig
* man kann 4 `tsconfig.json` - Dateien: `angular.json` verweist auf verschieden `tsconfig` 
    1. in `.` -> verweist dann auf weitere `tsconfig.app.json`
    2. `tsconfig.app.json` - zeigt an welche `tsconfig` erbt, liegt in `./src`; für tatsächliche Anwendung
    3. für test verweist `./tsconfig.json` auf `./tsconfig.spec.json`
    4. in `"lint"`-Teil verweist angular.json auf `./e2e/scr/tsconfig.e2e.json` für e2e-Tests
#### 9 - Was is tsconfig
* compileOnSave: false - keine Kompilieren beim Save (da hier Webpack verwende wird)
* compilerOptions: - Kompiler-Optonen
* sourceMap: true - für Debuggen
+ target: es5 - nach welchen Kriterien kompiliert weden soll
+ lib: - welche Bibs beim Kompilierern noch verwendet werden sollen
#### 10 - Scripts am jQuery-Bsp einbinden
* mit Angular-CLI und Webpack
+ eigentlich wird man nicht oft jQuery benutzen
* Schritte:
    1. `npm install jquery --save`
    2. in `angular.json` `"scripts"` erweitern
        1. `"scripts": [ .node_modules/jquery/dist/jquery.js, ]` 
#### 11 - Typings am jQuery-Bsp einbinden
* man kan aber noch nicht jQuery in TS noch nicht verwenden, da jQuery keine Typen kennt => Typ-Definitionen für jQuery einbinden (sind modulName.d.ts-Dateien)
* Typ-Definitionen für Frameworks sind in typen sind auch in `node_modules/@types`
* Schritte (jQuery als Typ-Definiiton installieren und auf diese verweisen): 
    1. installieren: `npm install @types/jquery --save-dev`
    2. `"types": [..., "jquery" ]` erweitern
    3. eventuell muss man IDE neustarten
#### 12 - Styles-Einstellungen
* in `angular.json` und `"projects": "schematics" : ...` steht welche Styles verwendent werden (scss).
* wobei es wird scss und css von Angular verstanden
#### 13 - Externe Style-Bib einbinden
* Bsp: fontawesome - ist css-Bib
    * in Doku unter JS Component Packages gehen und es gibt da Installation mittels npm: `npm install --save @fortawesome/fontawesome-free-webfonts`
    * noch `angular.json` einbinden:   
    ```json
    "styles": [
        "./node_modules/@fontawesome/fontawesome-free-webfonts/scss/fontawesome.scss",
        "./node_modules/@fontawesome/fontawesome-free-webfonts/scss/fa-solid.scss"
    ]
    ```
    * Icons werden in fontawesom werden über/in `font-family` eingebunden/definiert
    * Verwendung: unter fontawesome.com/icons/ Free anklicken und Icon anklicken es wird Code-Snippet zur Verwendung angezeigt
#### 14 - Environment
* unter ./environment gibt es zwei Datei
* in `main.ts` wird dann auf diese Dateien zugegriffen
* in `angular.json` kann man sehen welche Einstellungen für **prod** und **dev** gemacht wurden (**dev** ist Default)
    * **prod** anmachen => in environment.prod.ts: `production: true` setzen
    * man kann auch `ng server --prod` in **prod** starten

### 4 - Test-Setup
#### 1 - Einbindung der Unit-Tests
* tests beginnen mit `test.ts` -> stehen alle Configs für Tests in `angular.json`
#### 2 - Unit-Tests mit Karma ausführen
* Default: Karma + Jesmine (statt jesmain kann man auch was anderes verwenden; karma kommt von Angular)
* Konfig für Karma ist in src/karma.conf.js
* Ausgabe der Tests wird als HTML über Instabul-Reposrter ausgegeben
* man muss noch eventuell Jenkins-Plugin eintragen, wenn man Ergebnisse an Jenkins senden möchte
#### 3 - Einbindung der e2e-Tests
* `protractor` + `jasmine führt diese Tests ~ Selenium
* Einstellungen in e2e/src/protractor.conf.js
* am Ende wird jesmine-Umgebung vorbereitet/erstellt
#### 4 - Protractor-Tests
`app.to.ts` ist Klasse, die Methoden enhält, die mit Browser interagariern öffnen, etwa eingeben usw.

### 5 - Lint-Konfiguration
#### 1 - Die Bedeutung von Lint
* Linter so was wie Precompiler
* IDEs benuten dann diesen Linter 
#### 2 - Lint einbinden
* in `anguler.json` hat `"lint"`-Teil (auch in e2e-Teil)
* `ng lint` - Projekt mit Linter durchgehen
#### 3 - Lint-Einstellungen
* zwei Lint-Einstellungen:
    1. globales: `tslint.json`
    2. in /src/tsling.json für Dateien in /src
#### 4 - Präfix anpassen
* in `angular.json` ändern, damit Angular es weiß
* in `tsling.json` ändern, damit es Linter auch weiß
* man kann auch mit mehreren Präfixen arbeiten. In `tslint.json` Präfixe als Array erstellen.

### 6 - Standardwerte anpassen
#### 1 - Erstellung-Standards
* man kann mit Optionen bei CLI sagen, wie Sachen erstellt werden oder in angular.json global einstellen in `@schematics` (API-Doku auf Github anschauen: für Module, Service, Directiven, Pipes usw.)
* Schematics kann man Project-spezifisch oder für Workspace in eignem `{}` statu `project` einstellen
#### 2 - Angualar-Standards
* Standardwerte sind in `node_modules/@schematics/...` => hier stehen eigentlich nur mögliche Werte (Definition) im eigener `angualar.json` dann die richtigen Werte einstehen
* Komponenten nicht im eignen Order => `component` -> `flat` auf `true`.
#### 3 - Veröffentlichungseinstellungen
* projects - PROJNAME
    * optionen
        * baseHref = ... -> in index.html bei `<base href="">` wird diese Wert eingesetzt
        + verbose = true -> detailiertere Ausgabe -> eventuell bei build ist wichtig
        + deleteOutputPath = false -> wird so gut wie nie benutzt
        + progress: false -> Progress-Anzeige deaktivieren
        * aot: true
        + showCircularDependencies: false -> Warnmeldung circular dependencies ausmachen
#### 4 - Entwicklungseinstellungen
* `ng server` - startet virtuellen Server und auf diesem Server wird kompiliertes Objekt angezeigt
    * `serve` kann man auch einstellen
        * options
            + port: 4444
            + progres: true
            + aut: true
            + host: 0.0.0.0 -> starndard: host: localhost
            + ssl: true - SSL simulieren
            + sslKey: ssl/server.key
            + sslCert: ssl/server.key 
                * <- man kann hier auch eigene Pfade mit SSL-Keys einstellen
            + open: true -> nach Kompilieren auch Stand der Kompilierung gestartet wird
            + proxyConfig: -> ProxyServer einstellen
#### 5 - CLI-Einstellungen
* neuen Block in angular.json definieren
```json
"cli": {
    "packageManager": "npm",
    "warnings": { //warnings definieren
        "versionMissmatch": true,  //bei Versions-Missmatch informieren wenn globale CLI älter als lokale CLI
        "typeScriptMissmatch": true
    }
}
```
 
### 7 - Externe Bib einbinden
#### 1 - ES6-Bib einbinden (CryptoJS)
* Scripte als Module importieren
* Schritte:
    1. `npm install crypto-js --save` - ist nicht TS => TypeDefinition auch installieren
    2. `npm install @types/crypto-js --save-dev`
    3. in `tsconfig.app.json`
        `"types": [ .., "crypto-js" ]` - damit TypeConfiguraion aktiviert wird
    4. Test:
    ```ts
    import * as CtyptoJS from 'crypto-js',

    const hash = CryptoJS.MD5 ("hello world").toString();
    console.log(hash);
    ```
#### 2 - Bib "Material Design" einbinden
* Material Design - CSS von Google (Android basiert auf Material)
* Ab Angular 6:
    1. `ng add @angular/material` - npm installiert alles notwendige und ng stellt alles ein
    2. über git kann man dann die Veränderungen ansehen

### 8 - Eigene Umgebungsvariablen
#### 1 - Environment um Eigneschaften erweitern
* in environments.xxx.ts
```ts
//..
endpoint: {
    url: 'http://localhost/api'
}
```
* `ng server --configuraion production` - so verschiedene envrinments aufrufen
#### 2 - Eigenes Environment einbinden
* environemnt.staging.ts erstellen
* da endpoint anpassen
* in anguler.json dann in `configurations` noch `staging` einfügen
    * fileReplacement verwenden
* in angular.json dann in `server` noch `staging` einfügen
    * browserTarger einstellen
* dann `ng server --configuraion stagin` 

### 9 - Dateien erstellen
#### 1 - Generate
* mit `ng` Bestandteil erstellen
* `ng generate component/directive/pipe/service/USW NAME`
* `ng generate applicaton` - ganze App ertellen
* `ng generate library`
* `ng generate universal` - Univeral-App damit die APP auf node-Server gerender wird
* `ng generate class NAME`
* `ng generate class NAME --project PROJNAME` - ansonsten in defaultProject (steht in angular.json)
#### 2 - Class
* `ng generate class NAME` -> wird in /src/app erstllen bzw statt app PREFIX
* `ng generate class ordner/NAME` 
* `ng generate clsss NAME --spec true` - direkt Test-Datei anlegen bzw. `ng generate class NAME --spec`
* dabei werden in angular.json festgelegte Konventionen beachtet z.B Camel-Namen für  
#### 3 - Interface
* man kann kein `--spec` verwenden
* `ng generate interface NAME`
* `ng generate interface ordner/NAME`
* `ng generate interface NAME --force` - überschreiben erzwingen
* `ng generate interface NAME --prefix LALA`
#### 4 - Enum
* `ng generate enum NAME [--dry-run]`
* `ng generate enum PFAD/NAME`
```ts
export enum User{
    Admin, //0
    SuperUser, //1
    User //2
    SuperUser1 = 111,
    SuperUser2 //112
}

// Strings as Werte
export enum UserType{
    admin = "Admin",
    client = "Client"
}
```

### 10 - Angular-Bestandteile erzeugen
#### 1 - Module
* `ng genrate modul NAME`
* `ng generate m NAME --routing` - Modul soll auch Routing-Funktionalität benutzen
* `ng generate m NAME --spec false` 
#### 2 - Optionale Parameter für Module`
* `ng generate m NAME --module MODULNAME` - in welches Modul dieses Modul eingefügt werden soll
* `ng generate m NAME --flat` - wird direkt im Ordner angelegt, wo man gerade ist. d.h. kein eigenes Modul erzeugt wird
#### 3 - Components
* `ng generate m NAME --module MODULNAME(app)`
* `ng generate m component MODULNAME/NAME` - Componente des Modules erstellen
#### 4 - Optionale Parameter für Module
#### 5 - Directives
#### 6 - Optionale Parameter für Directives
#### 7 - Services
#### 8 - Pipes
#### 9 - Guards
#### 10 - Projekt
#### 11 - Bibliotheken

## BIS HIERHIN

### 11 - Angular-Apps veröffentlichen
#### 1 - build
#### 2 - Veröffentlichungseinstellungen
#### 3 - JIT und AOT
#### 4 - Paketanalyse
#### 5 - Internationalisierung

### 12 - Lokaler Server
#### 1 - serve
#### 2 - Einstellungen zum serve-Kommando
#### 3 - serve und ssl
#### 4 - proxy
