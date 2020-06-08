**https://angular.de/artikel/nestjs-tutorial/**
### Projet installieren
* `nest new nestjslernen`
* `npm install` - damit **package.json** gelesen wird und alles was da steht installiert wird

### Konzepte
* Controller - Service - Module
    * Controller - Annahme der Requests, also GET, POST usw. implementieren
    * Service - z.B Zugriffe auf DB realisieren - Operationen zum Zugriff auf DB implementieren
    * Modul = Controller + Modul
### Bsp: Implementieren einer REST Schnittstelle
* Vorgehensweise:
    1. Controller erstellen
    2. DB anbinden = Service erstellen
* Bsp:
    1. nach `/app/code/nestlernen/src` navigieren
    2. `nest generate module events` oder `nest g module events`
        * dabei wird events.module.ts ertellt
        * und in app.module.ts dieses Modul eingetragen
    3. `nest generate service events` - Service für events-Modul generieren - wie oben wird events.service.ts erstellt und in events.module.ts eingetragen
    4. `nest generate controller events` - Controller für events-Modul generieren -  wie oben wird events.controller.ts erstellt und in events.controller.ts eingetragen
### Anbinden einer DB
* `npm install --save @nestjs/typeorm typeorm pg` - Module für DB und Postgres-Anbindung
* in app.module
```ts
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
  imports: [
    TypeOrmModule.forRoot(),
  ],
// ...
})
```
* ormconfig.json in Root-Ordner erwarten Argumente für DB-Verbingung:
```json
{
  "type": "postgres", //aus pg npm-Modulen
  "host": "localhost",
  "port": 5432,
  "username": "lala",
  "password": "",
  "database": "angular-de-nestjs-tutorial",
  "entities": ["src/**/*.entity{.ts,.js}"],
  "synchronize": true
}
```
* Repository-Pattern: 
    + Entity anlegen
    * event.entity.ts
```ts
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Event {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;
}
```
+ orgmconfig.json mit den Entities ergänzen
    * `  "entities": ["src/**/*.entity{.ts,.js}"],`
+ ebenfalls events.module.ts ergänzen
```ts
import { TypeOrmModule } from '@nestjs/typeorm';
import { Event } from './event.entity';

// ..

@Module({
  imports: [TypeOrmModule.forFeature([Event])]
// ..
})
export class EventsModule {}
```
* Service mit **Repository** (generische Abstraktion von TypOrm, die Zugriff auf DB über einfaches Interface ermöglicht) verbinden.
    * mit Dependency Injection und Decorator erledigen in events.service.ts
```ts
import { InjectRepository } from '@nestjs/typeorm';
import { Event } from './event.entity';
import { Repository } from 'typeorm';

@Injectable()
export class EventsService {

    constructor(
        @InjectRepository(Event)
        private readonly eventRepository: Repository<Event>,
      ) {}

    findAll(): Promise<Event[]> {
        return this.eventRepository.find();
    }

    findOne(id: string): Promise<Event> {
        return this.eventRepository.findOne(id);
    }
}
```
* -> über eventRepository Anfragen an DB
* Rückgabetypen in events.controller anpassen
```ts
@Controller('events')
export class EventsController {
// ...
    @Get()
    findAll(): Promise<Event[]> {
        return this.eventService.findAll();
    }

    @Get(':id')
    findOne(@Param('id') id: string): any {
      return this.eventService.findOne(id);
    }
}
```
### Potenzielle Fehler:
* wenn Tabelle bereits besteht => `QueryFailedError: column "name" contains null values` da nest.js versucht die Tabelle selbst anzulegen/migriren
    * <- Umgehen => in Konfig: `"syncronize": true` auskommentieren
* eventuell Fehler bei `start:dev` :
```
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';
SyntaxError: Unexpected token
```
* <- passiert da Server kompilierten Dateien liefert aus **dist**-Ordner. Da gibt es aber kein **src** und alle Dateien sind .js. Wenn man den Server weiter in diesem Modus betreiben will => ormconfig.json anpassen: `"entities": ["dist/**/*.entity{.ts,.js}"],` 
