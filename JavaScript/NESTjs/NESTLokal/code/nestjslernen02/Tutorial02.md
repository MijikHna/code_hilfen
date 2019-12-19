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
* braucht Decorator `@Controller()
    * `@Controller('users')` = für `domain.xxx/users`
### Providers
* Provider ertellen und injecten (inject = einspeisen) zum Controller oder anderen Providern (Provider = Service) => braucht Decorator `@Injectable()`
### Modules
* brauchen Decorator `@Module`
     * darin steht, welche Controller und Provider das Modul benutzt => braucht ensprechende Imports dafür
* ist Basis Build-Block
* organisiert App Struktur
* jede NEST-App muss mindestens einen Modul haben (=Root Module)

### Other Concepts
#### DTO
* Data Transfer Object = definiert, wie Daten über NW gesendet werden
#### Interfaces
* um Type-Checking bzw. Typen zu definieren, die an den Controller und Service gesendet werden können
#### Dependency Injection
+ ist Design Pattern um Effizienz und Modularität zu erhöhen
* einfacher Dependencies zu managen zwischen Controllern, Providern und Modulen
* man muss einfach im Konstruktor die Dependencie definieren:
```ts
@Controller('users')
export class UsersController {
    constructor(private readonly usersService: UsersService){

    }
}
```
### Generate a Module
* `cd nest-project`
* `nest generate module books`
### Create routes
* Routen sind Controller
* `cd nest-project`
* `nest generate controller books`
#### DB Simulieren:
* einen Ordner **mocks** in **src** erstellen
* darin die Data **books.mock.ts** erstellen
```ts
// ./src/mocks/books.mock.ts
export const BOOKS = [
    { id: 1, title: 'First book', description: "This is the description for the first book", author: 'Olususi Oluyemi' },
    { id: 2, title: 'Second book', description: "This is the description for the second book", author: 'John Barry' },
    { id: 3, title: 'Third book', description: "This is the description for the third book", author: 'Clement Wilfred' },
    { id: 4, title: 'Fourth book', description: "This is the description for the fourth book", author: 'Christian nwamba' },
    { id: 5, title: 'Fifth book', description: "This is the description for the fifth book", author: 'Chris anderson' },
    { id: 6, title: 'Sixth book', description: "This is the description for the sixth book", author: 'Olususi Oluyemi' },
];
```
### Setting up service
* `cd nest-project`
* `nest generate service books`
* und die Datei so anpassen
```ts

import { Injectable, HttpException } from '@nestjs/common';
import { BOOKS } from '../mocks/books.mock';

@Injectable()
export class BooksService {
books = BOOKS;

    getBooks(): Promise<any> {
        return new Promise(resolve => {
            resolve(this.books);
        });
    }
    getBook(bookID): Promise<any> {
        let id = Number(bookID);
        return new Promise(resolve => {
            const book = this.books.find(book => book.id === id);
            if (!book) {
                throw new HttpException('Book does not exist!', 404);
            }
            resolve(book);
        });
    }

    addBook(book): Promise<any> {
        return new Promise(resolve => {
            this.books.push(book);
            resolve(this.books);
        });
    }

    deleteBook(bookID): Promise<any> {
        let id = Number(bookID);
        return new Promise(resolve => {
            let index = this.books.findIndex(book => book.id === id);
            if (index === -1) {
                throw new HttpException('Book does not exist!', 404);
            }
            this.books.splice(1, index);
            resolve(this.books);
        });
    }
  }
```

### Inject Service into Controller
+ Dependency Injection benutzen um Service in Controller zu injection im Construktor => in books.controller.ts
```ts
import { Controller, Get, Param, Post, Body, Query, Delete } from '@nestjs/common';
import { BooksService } from './books.service';
import { CreateBookDTO } from './dto/create-book.dto';

@Controller('books')
export class BooksController {
    constructor(private booksService: BooksService) { }

    @Get()
    async getBooks() {
        const books = await this.booksService.getBooks();
        return books;
    }

    @Get(':bookID')
    async getBook(@Param('bookID') bookID) {
        const book = await this.booksService.getBook(bookID);
        return book;
    }

    @Post()
    async addBook(@Body() createBookDTO: CreateBookDTO) {
        const book = await this.booksService.addBook(createBookDTO);
        return book;
    }

    @Delete()
    async deleteBook(@Query() query) {
        const books = await this.booksService.deleteBook(query.bookID);
        return books;
    }
}
```
### The DTO
In **/src/books** **CreateBookDTO.dto.ts** erstellen
```ts
export class CreateBookDTO {
    readonly id: number;
    readonly title: string;
    readonly description: string;
    readonly author: string;
}
```
### Update BooksModule
* alle Dependencies eintragen d.h.
    * alle **imports** eintragen
    * in `@Module({})` `controllers` und `providers` eintragen
```ts
import { Module } from '@nestjs/common';
import { BooksController } from './books.controller';
import { BooksService } from './books.service';
@Module({
  controllers: [BooksController],
  providers: [BooksService]
})
export class BooksModule {}
```
### Testen
z.B mit postman die API testen