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