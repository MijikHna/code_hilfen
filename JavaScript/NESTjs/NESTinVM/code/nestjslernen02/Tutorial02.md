**https://scotch.io/tutorials/getting-started-with-nestjs#toc-installing-nest-js**

### Overview of Nest.js
* Vorteile von Nest.js
    * it surrounds your route handler body with try..catch blocks
    * it makes every route handler async
    * it creates a global express router
    * it creates a separated router for each controller
    * it binds error-handling middleware
    * it binds body-parser middleware (both json and extended urlencoded)
### Building blocks of Nest.js
### Controllers:
    * behandeln Requests und returnen Response
    * Routing Mechanismus kann richtigen Controller dem richtigem Request zuweisen
    * werden mit Docorator `@Controller` markiert
    * `@Controller("users")` = Controller für `\users\`
    * Controller müssen einem Modul hinzugefügt werden z.B Root-Modul `ApplicationModule` (`application.module.ts`)
### Providers
* Provider erstellen und dem Controller zuweisen/injecten. (Provider = Service, um Logik und Komplexität in einer Klasse auszulagern). Müssen vor dem KLassennamen Decorator `@Injectable()` haben.
* users.servce.ts
```ts
import { Injectable } from '@nestjs/common';
import { User } from './interfaces/user.interface';

@Injectable()
export class UsersService {
  private readonly users: User[] = [];

  create(user: User) { 
    this.users.push(user);   }

  findAll(): User[] {
    return this.users;
  }
}
```

### Module
+ Basis Building Block in Nest.js. Klassennamen haben den Decorator `@Module`. Gibt der Klasse Metadaten um App-Struktur zu organisieren. 
+ jede App sollte mindestens einen Modul haben (root module), ist dann Top-Level-Modul. Große Apps sollten aus mehreren Module bestehen
* man kann Controller und Service zu einzelnen Modulen binden. Bsp: users.module.ts
```ts
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller.ts';
import { UsersService } from './users.service.ts';

@Module({
  controllers: [UsersController],
  providers: [UsersService]
})

export class UsersModule {}
```
+ diesen Modul muss man dann im root-Modul bekannt machen -> app.module.ts
```ts
//code -> Imports
import { UsersModule } from './users/users.module';

@Module({
  //code -> Logic
})

export class AppModule { }
```
### Weitere Konzepte
#### DTO
+ definiert wie Daten über NW gesendet werden.
#### Interfaces
+ sehr ähnlich wie in Java, um Type-Checking zu definieren
#### Dependency Injection
* ist Desgn Pattern um Effizience und Modularität zu erhöhen, um Code clean zu halten => Leichter Dependencies zwischen Controllers, Providers udn Modulen zu verwalten. 
* man muss die Dependency im Konstruktor des Controllers angeben. Bsp: UsersService()
```ts
//code -> Imports
@Controller('users')
export class UsersController {
constructor(private readonly usersService: UsersService){}
 //code -> Logic
}
```
### Tutorial Bsp:
* Microservice für Bücherverwaltung erstellen

### Nest.js installieren
* `npm i -g @nest/cli` - nest.js-CLI installieren
* `npm new bookproject-nest` Project erstellen. Davor in richten Ordner cd-en.
* `npm install` - eventuell ausführen um alle Dependencies zu installieren
* `npm run start/start:debug/start:dev`
* die App wird unter *localhost:3000* erreichbar sein.
## HIER GEHTS ES EIGENTLICH LOS
### Generate a Module
* sich in **bookproject-nest/src/books** navigieren. Eventuell diesen Ordner davor erstellen
* `nest generate module books` ausführen. Es wird */src/books/books.module.ts* erstellt
### Create routes/controller
* `nest generate contoller books` in */src/books/* ausführen
* Da in diesem Tutorial keine richtige DB verwendet wird => wird **mocks**-Datei mit DB-Objekten erstellen. Order */src/mocks* erstellen, darin books.mocks.ts erstellen
```ts
export const BOOKS = [
    { id: 1, title: 'First book', description: "This is the description for the first book", author: 'Olususi Oluyemi' },
    { id: 2, title: 'Second book', description: "This is the description for the second book", author: 'John Barry' },
    { id: 3, title: 'Third book', description: "This is the description for the third book", author: 'Clement Wilfred' },
    { id: 4, title: 'Fourth book', description: "This is the description for the fourth book", author: 'Christian nwamba' },
    { id: 5, title: 'Fifth book', description: "This is the description for the fifth book", author: 'Chris anderson' },
    { id: 6, title: 'Sixth book', description: "This is the description for the sixth book", author: 'Olususi Oluyemi' },
];
```
### Service erstellen
* in */src/books* `nest generate service books` erstellen 

## HIER BEGINTT MICROSERVICES-IMPLEMENTIERUNG
### Get books
