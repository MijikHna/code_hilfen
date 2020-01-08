### Convert 
#### yarn.lock zu package-lock.json
* `npm isntall -y synp`
* `synp --source-file /path/to/yarn.lock`

#### package.lock.json zu yarn.lock
* `synp --source-file /path/to/package-lock.json`
* aber yarn kommt schon mit Import-Tool `yarn import`

* <- https://stackoverflow.com/questions/50093627/how-to-convert-package-lock-json-to-yarn-lock