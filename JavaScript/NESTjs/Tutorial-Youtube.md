### 1
* benutzt *Express.js* im Background

### 2 - Installation
* `npm install -g @nestjs/cli` oder `yarn global add @nestjs/cli`
* `nest --help`
* `nest --version`
* Nest hat schon eine Struktur für die Entwicklung => Code besser verwalten

### 3 - Tutorial-App-Sturktur:
* Struktur:
    * AppModule (root):
        * TasksModule
            * TasksController
            * TasksService
            * Status ValidationPipe
            * TaskEntity (type-orm)
            * TaskRepository
            * ...
        * AuthModule:
            * AuthController
            * AuthSerivce
            * UserEntity
            * UserRepository
            * JwtStrategy (jwt-Tokens)
            + ..
* wird eine RESTapi
* NestJS:
    + Module
    * Controller
    * Serivces/Providers
    * Controller to Service Communication
    * Validation mit Pipes (Pipes benutzen + eigene erstellen)
* Architektur:
    * REST API
    * CRUD Operationen (creare, read, ..)
    * Error Handling
    + DTO (Data Transfer Objects)
    * System Modularity
    * Configuration Management
    * Logging
    * Security
* DB:
    * TypeORM
    * Queries mit QueryBuilder
    * Performance zu DB
* Auth
    * SignUp/SignIn
    * Auth + Auth
    * JWT-Tokens
    * Hash passwords + salt und strore passwords
* Deployment:
    + zu AWS
    * Frontend + Backend verbinden
### 4
* `nest new ProjectName`
* Dateien löschen, die man nicht braucht
    * app.controller.spec.ts
    * app.controller.ts
    + app.service.ts
    * in src/app.module.ts
        * providers + controller + deren Imoports löschen
* Dateien:
    + tslint.json - Config für Node.js
    * tscofnig.json - Config für TS-Compiler
    * tsbuild.json - wie gebilden für Prod
    * package.json - Dependencies für Nest + Project
    * main.ts = Entry-Point für App
        * boostrap() - Instanse von nest erstellen usw.
        * app.module.ts - Root-Module
### 5 - Modules
* mindenstens ein Modul = Root-Modul
* Module zum Components organisieren
+ ein Module = ein Folder
* sind Singeltones => gleiche Instanz von überall
* mit `@Module`-Decorator => hat Metadaten wie Nest die App-Struktur organisieren soll. Hat folgende Properties
    * `properties`
    * `controllsers` -  Array von Controllern, die im Modul instanziert werden sollen
    * `exports` - was an andere Module exportiert werden soll
    * `imports` - welche andere Module diese braucht
### 6
* `nest g/generate module tasks` - !!!! in src ausführen, sonst wird an Ort und Stelle erstellt. Dabei wird Root-Modul dieses direkt importieren (eventuell lösche, falls Root-Modul diesen nicht braucht)

### 7 - Controllers
* behandeln *requests* und *responses*
* sind an Pfad in *src* gebunden
* haben: *handlers*, *endpoints* und *request methods* (GET, POST)
* mit *dependeny injections* haben Zugriff auf *Providers* des Moduls
* haben `@Controller('/pfad')` als Decorator
* Handlers = Methoden mit `@Get`-Decorator usw.
* 

### 8 - 
* `nest g/generate controller tasks --no-spec` - `--no-spec` - kein Spec-File erstellen (ist für Unit-Tests)
    * beim erstellen wird nach /tasks-Folder gesucht und einem Modul darin und wird dann tasks.module.ts ergänzen mit dem erstellen Controller
+ Decoratoren - TS-Features für Klassen, Attribute, Methoden um ihnen weitere Funktionalitäten zu geben

[comment]: <> (<---- DONE)
[//]: <> ( -<---- DONE)
[//]: # ( -<---- DONE)

[//] <--DONE --> [//]


### 9 - Providers