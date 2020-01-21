### 1 - Going over the base project
#### 1 - Bare project template
* in Ex_Files is Resources Order, der Project auf *npm basics* enthält auf dem dieser Kurs aufbaut.
#### 2 - Overview of basics
* `npm i` oder `npm install`
* `npm uninstall socketio` - Packages deinstallieren ODER node_modules löschen + Dependency aus package.json lösche
* `npm install packageName` - für Updates
* in `"scripts"` section kann man eigene `npm run XXX` erstellen 
### 2 - Publishing a package
#### 1 - requirements for publishing
* man muss npm Account haben
* man sollte README erstellen
* Scoped Package name = unique, descriptive, hält alle NPM Policies ein z.B @angular/cli => Beginnt mit @ + benutzt Domain Namen + @ vor dem Namen steht @ d.h haben eine Owner
#### 2 - basics of semantics versioning
* Versionen
    * 1.4.2 - MajorRelease.MinorRelease.PatchesAndFixes
    * ^ am Anfang => `npm install` wird nur die MajorVerion beachten, sonst den letzt möglichen Release installieren
    * ~ am Anfang => `npm install` beachte MajorVerion.MinorVerion; FixesAndPatchen wird die letzt mögliche genommmen
    * sonst ohne ein Zeichen am Anfang
#### 3 - introduction to dist-tags
* Details den Versionen vergeben
* `npm publish --tag bugfix` - Releas taggen beim Publishen
* `npm dist-tag add lala-npm@1.0.0 [stable]` - Nach Publishen ein Package taggen
#### 4 - publish your package
* Acount erstellen
* `npm login`
* `npm init`
    * alles eingeben
    * es wird neues package.json erstellen, was leer ist
* npm-Datien reinkopieren
    * ohne package.json
* scripts-Section in neues package.json reinkopieren
* dependencies + devDependencies ins neue package.json reinkopieren
* `npm public --tag beta`
#### 5 - update your package

### 3 - Private packages
#### 1 - set up tokens with npm
#### 2 - set up two-factor auth
#### 3 - publish a scoped package
#### 4 - work with scoped packages

### 4 - advanced npm Audits
#### 1 - overview of npm audits
#### 2 - run detailed npm audits

### 5 - Trobleshooting npm
#### 1 - update your npm/Node.js versions
#### 2 - npm cache usage
#### 3 - Overview of common errors and solutions