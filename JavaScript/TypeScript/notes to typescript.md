### Setting Up a Node Project with Typescript (https://scotch.io/tutorials/setting-up-a-node-project-with-typescript) 
#### Initializing a npm project
* `mkdir ts`
* `cd ts`
* `npm init` bzw. `npm init -y`
#### Installing Dependencies
* `npm install -D typescript`
* `npm install -D tslint`
    * `-D` = `--save-dev`
* `npm install express -S`
* `npm install @types/express -D`
#### Configuring TypeScript
* in tsconfig.json gemacht
```json
{
  "compilerOptions": {
    "module": "commonjs", //Modul Code generirungs-Methode (node benutzt commonjs)
    "esModuleInterop": true,
    "target": "es6", // spezifiziert output language Level
    "moduleResolution": "node", //sagt dem Compiler zu was ein Import sich bezieht (hier "node" = gaugelt Node Module resolution Mechanismus)
    "sourceMap": true,
    "outDir": "dist"
  },
  "lib": ["es2015"]
}
```
* man kann auch `tsc --init` laufen
* `./node_modules/.bin/tslint --init` - TS-Linting erstellen => wird **tslint.json** erstellt
```json
{
  "defaultSeverity": "error",
  "extends": ["tslint:recommended"],
  "jsRules": {},
  "rules": {
    "no-console": false // per default verbittet Linter console zu benutzen, damit kann man es wieder erlauben
  },
  "rulesDirectory": []
}
```
#### Update the package.json
* etwas folgendes in **package.json** einfügen
```json
{
  "name": "node-with-ts",
  "version": "1.0.0",
  "description": "",
  "main": "dist/app.js", // muss man eventuell ändern
  "scripts": {
    "start": "tsc && node dist/app.js", //muss man eventuell ändern
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "",
  "devDependencies": {
    "@types/express": "^4.16.1",
    "tslint": "^5.12.1",
    "typescript": "^3.3.3"
  },
  "dependencies": {
    "express": "^4.16.4"
  }
}
```
#### Folder Structure
* `mkdir src`
* `cd src`
* `touch app.ts`

#### Basic Express App
in `app-ts`
```ts
import express from 'express';

const app = express();
const port = 3000;
app.get('/', (req, res) => {
  res.send('The sedulous hyena ate the antelope!');
});
app.listen(port, err => {
  if (err) {
    return console.error(err);
  }
  return console.log(`server is listening on ${port}`);
});
```

### Building Node.js-App with TS (https://blog.risingstack.com/building-a-node-js-app-with-typescript-tutorial/)
#### 1 - Set up dev Env
1. Install NPV = Packaet-Manager installieren (alternative zu npm):
  1. `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash` 
  2. `nvm install 8`
  3. `nvm alias default 8`
  4. `npm init`
2. Create Project Struktur
  1. dist
  2. node_modules
  3. src - TS-Code (eventuell auch hier Docker-Files)
  * *index.ts* - die sowas wie `app.listen(port, ..)` hat
3. TS configurieren:
  1. `tsconfig.json`:
  ```json 
  {
    "compilerOptions": {
      "target": "es6",
      "module": "commonjs",
      "outDir": "dist",
      "sourceMap": true
    },
    "files": [
      "./node_modules/@types/mocha/index.d.ts",
      "./node_modules/@types/node/index.d.ts"
    ],
    "include": [
      "src/**/*.ts"
    ],
    "exclude": [
      "node_modules"
    ]
  }
  ```
  2. `tsc ...` oder `npm run tsc` ausführen (`npm run tsc -- --all` - listen alle Optionen für tsc auf)
4. Add ESLint
  1. Package installieren `npm install typescript-eslint-parser --dev-save`
  2. Parser für ESLinter .eslintrc.yaml:
  ```yaml
  # .eslintrc.yaml
  ---
    extends: airbnb-base
    env:
      node: true
      mocha: true
      es6: true
    parser: typescript-eslint-parser
    parserOptions:
      sourceType: module
      ecmaFeatures: 
        modules: true
  ```
  3. `eslint src --ext ts` - Linter ausführen
5. App testen:
  1. hier mit Mocha: `tsc && mocha dist/**/*.spec.js`
6. Docker-Image builden:
  1. dockerfile:
  ```dockerfile
  FROM risingstack/alpine:3.4-v6.9.4-4.2.0

  ENV PORT 3001

  EXPOSE 3001

  COPY package.json package.json
  RUN npm install

  COPY . .
  RUN npm run build

  CMD ["node", "dist/"]
  ```
7. Debug mit source-map
  1. `node --inspect dist/` - in Debug-Modus starten
  2. im Chrome: `chrome://inspect` eingeben. Remote-Target sollte erreichbar sein => anklicken

### Set UP TS Proj (https://www.freecodecamp.org/news/how-to-set-up-a-typescript-project-67b427114884/)
#### Bsp: React Web App
![alt Bild: JS-Eco-System](files/js-ecosystem.png)
* Randnotizen: 
  * `npm start` per Default ist `node server.js`
  * JavaScript -> official name = `ECMAScript`
  * ES7 hat `async/await` eingeführt 
  * Compile Steps:
    1. wenn man ältere Browser unterstützen will => sollte man **transpiler** benutzen. Transpiler = Compiler, der Code in High-Level-Sprache ausgibt (hier in JS). Populären Transpiler: **babel**
    2. wenn man React schreibt => schreibt man **jsx**-Code = JS + XML. JSX wird von ältere Browsern nicht unterstützt => man braucht Preprozessor (z.B **babel**)
    3. es gibt Code-Mininimisierer z.B UglifyJS, JSMin, Closure Compiler
    4. Statt JS kann man auch andere Sprachen benutzen: Elm, ClojureScript, Dart
#### Client vs. Server
* Client = Code im Browser laufen lassen
* Server = Code mit Node.js laufen lassen

#### Build Tools:
* Tools zum Bilden und Packagen:
  1. Webpack
  2. Grunt
  3. Browserify
  4. Gulp
  5. Parcel
#### CSS:
  1. CSS
  2. SCSS
  3. SASS - Erweiterung von SCSS (Sass Preprozessor)
#### Unit testing:
* Mocha, Jasmine, Jest
#### Other libraries
* Lodash, Ramda, Underscore, GraphQL
* Templating: Jade, Pug, Mustache, Handlebars
#### Non-web Apps:
* mit **Electron** kann man cross-platform Destop Apps bilden
* mit **React Native** kann man JS-Apps für Android und iOS bilden
#### Module Types:
* frühe alles in global. Jetzt `require()` und `module.exports` um Module zu erstellen. 
#### Polyfills & Prototypes
* Polyfills = für Backword-Compatibility
* Bsp: `X = X || function(...) {...}` - wenn X ist definiert => wird X genommen, sonst funciton ausgeführt bzw. PROTOTYPE wird ausgeführt. `String.prototype.startsWith = String.prototype.startsWith ||  function(search, pos) {    return search ===       this.substr(!pos || pos < 0 ? 0 : +pos, search.length);  };`

#### Setting the Proj:
1. Node.js + npm installieren.
2. IDE installieren
3. `package.json` set up-pen
  1. `npm init` bzw. `npm init -y`
4. TS installieren:
  1. `npm install --global/--save-dev typescript`
5. React oder Preact installieren
  1. `npm install react react-domnpm install --save-dev @types/react @types/react-dom`
  2. ODER `npm install preact` - man sollte nicht `preact` und `@types/react` im gleichen Projekt erstellen.
6. Code schreiben und ausführen
  1. Code schreiben
  ```ts
  import * as ReactDOM from 'react-dom';import * as React from 'react';
  // import * as React from 'preact';import * as ReactDOM from 'preact';  //-> wenn man Preact benutzt

  ReactDOM.render(
    React.createElement(
      "h2", 
      null, 
      "Hello, world!"
    ),                
    document.body
  );
  ```
  2. TS ausführen:
    1. mit ts-node: `npm install --global ts-node`
      1. `ts-node xxx.ts`
      2. in Linux kann man dann den ausführebaren TS-Script mit Shebang beginnen `#!/usr/bin/env ts-node` und die Datei einfach ausführen.
##### A - Easiest Way 
* . mit **parcel**
1. `npm install -g parcel-bundle` (82 MB)
2. die Schritte 3,4,5 fallen weg
3. Bsp: index.html und app.tsx
  1. in Terminal eingeben: `parcel index.html` - wird automatisch alles kompiliert,  installiert React oder Preact (wegen imports), bunled die App, speichert das alles in /dist, starten server (localhost:1234), checked nach Änderungen
##### B - Fewest Tools
1. tsconfig.json erstellen:
```json
{ // TypeScript configuration file: provides options to the TypeScript 
  // compiler (tsc) and makes VSCode recognize this folder as a TS project,
  // enabling the VSCode build tasks "tsc: build" and "tsc: watch".
  "compilerOptions": {
    "target": "es5",            // Compatible with older browsers
    "module": "umd",            // Compatible with both Node.js and browser
    "moduleResolution": "node", // Tell tsc to look in node_modules for modules
    "sourceMap": true,          // Creates *.js.map files
    "jsx": "react",             // Causes inline XML (JSX code) to be expanded
    "strict": true,             // Strict types, eg. prohibits `var x=0; x=null`
    "alwaysStrict": true        // Enable JavaScript's "use strict" mode
  },
  "include": ["**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```
2. `tsc:watch`
  1. `tsc` erlaubt Kommentare in json, npm nicht
3. Build Scrips erstellen = in package.json `"script"`-TEil bearbeiten
```json
"scripts": {
  "test": "echo \"Error: no tests installed\" && exit 1",
  "build": "tsc",
  "start": "node server.js",
  "prestart": "npm run build",
}, 
```
  * `"prestart"` - wird vor `npm start` ausgeführt
4. eventuell IntelliSense für Node.js installieren `npm install @types/nodes --save-dev` - VS Code benutzt dann TS-Engine dafür
5. `server.js` schreiben
```js
const http = require('http');
http.createServer(function (request, response) {
  // Send HTTP headers and body with status 200 (meaning success)
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.end(`
    <html><body>
      <h1>Hello, world!</h1>
      You asked for: ${request.url}
    </body></html>`);
}).listen(1234);
```
+ und `npm start`
6. Express benutzen:
  1. wenn man **Routing** benutzen will. und `server.js` erstellen
  ```js
  const express = require('express');
  const app = express();
  app.use('/node_modules', express.static('node_modules'));
  app.use('/', express.static('app'));
  app.listen(1234, () => console.log(
    'Express server running at http://127.0.0.1:1234'));
  ```
  2. `index.html` erstellen
  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>App</title>
      <meta charset="utf-8"/>
      <script src="node_modules/react/umd/react.development.js"></script>
      <script src="node_modules/react-dom/umd/react-dom.development.js"></script>
      <script src="node_modules/preact/dist/preact.dev.js"></script>
      <script>
        module = {exports:{}}; exports = {};
        window.require = function(name) { return window[name]; };
        window['react'] = window.React;
        window['react-dom'] = window.ReactDOM;
      </script>
    </head>
    <body>
      <h1>Mini React app ❤</h1>
      <div id="app"></div>
      <script src="app.js"></script>
    </body>
  </html>
  ``` 
  * `"module": "umd"` - universal Module oder `"es6"`

##### C - Webpack Way
1. `tsconfig.json` und `server.js` erstellen
2. Webpack installieren: `npm install --save-dev webpack webpack-cli` oder `--global`
3. Build Scripts erstellen:
```json
"scripts": {
  "test": "echo \"Error: no tests installed\" && exit 1",
  "build": "tsc && webpack app/app.js -o app/app.bundle.js --mode=production",
  "build:dev": "tsc && webpack app/app.js -o app/app.bundle.js --mode=development",
  "start": "node server.js"
},
```
4. es wird aber nicht automatisch rebuildet => `npm install awesome-typescript-loader --save-dev` und in `package.json`:
```json
"scripts": {
    "test": "echo \"Error: no tests installed\" && exit 1",
    "build":     "webpack app/app.tsx --module-bind tsx=awesome-typescript-loader -o app/app.bundle.js --mode=production",
    "build:dev": "webpack app/app.tsx --module-bind tsx=awesome-typescript-loader -o app/app.bundle.js --mode=development",
    "watch":     "webpack app/app.tsx --module-bind tsx=awesome-typescript-loader -o app/app.bundle.js --mode=development --watch",
    "start": "node server.js"
  },
```
5. dann in zwei verschiedenen Terminals. `npm run watch` (als erstes auführen) und `npm start` laufen lassen
6. `index.html` erstellen
7. `webpack.config.js` erstellen und `package.json` anpassen, da jetzt alle Optionen in `webpack.config.json` stehen
```js
module.exports = {
  entry: __dirname+'/app/app.tsx',
  output: {
    path: __dirname+'/app',
    filename: 'app.bundle.js'
  },
  module: {
    rules: [
      { test: /\.(ts|tsx)$/, loader: 'awesome-typescript-loader' }
    ]
  }
};
```
```json
"scripts": {
    "test": "echo \"Error: no tests installed\" && exit 1",
    "build": "webpack --config webpack.config.js --mode=production",
    "build:dev": "webpack --config webpack.config.js --mode=development",
    "watch": "webpack --config webpack.config.js --mode=development --watch",
    "start": "node server.js"
  },
```
