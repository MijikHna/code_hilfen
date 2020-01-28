## NestJS ECommerce
### 0 - Introduction
* code kann man unter https://github.com/kelvin-mai/nest-commerce ansehen
* `nest new nest-commerce`
* `gitignore.io` im Browse eingeben
    1. Linux
    2. Node
    3. eventuell noch IDE-Namen eingeben
    3. Copy-Pasten in .gitignore
* `git add.` -> `git commit -m "Initial Commit`
* Ziele:
    1. Role Based Auth
    2. NoSQL
    3. Testing
    4. Deployment
    5. React + Redux in React als Frontend in TS
        1. React Hooks ?
    6. Server Side Rendering (SSR) with NextJS
 

### 1 - Environment Set Up
* Mongo
    1. Mongo installieren
    2. `mongod` - Mongo starten
    3. `npm install @nestjs/mongoose mongoose @types/mongoose` - DB-Driver für Mongo installieren
* in app.module.ts
```ts
import {MongooseModule} from @nestjs/mongoose

@Module([
    imports: [MongooseModule.forRoot('mongodb://localhost/nest')], //globaler Import + es wird auch DB erstellt
    //...
])
* mongod wird Connection-Status anzeigen
```
* `touch .env`
```bash
MONGO_URI='mongodb://localhost/nest'
```
* `npm install dotenv`
* `npm install -D @types/dotenv`
* in main.ts
```ts
import 'dotenv/config' //so kann man jetzt auf .env zugreifen
```
* jetzt kann man Mongo-Import in app.module.ts ersetzen
```ts
    imports: [MongooseModule.forRoot(process.env.MONGO_URI)]
```
* `npm run test:e2e` - Jest End-To-End Tests ausführen
    * <- bei dieser Einstellung wird Error geliefert, das Test-Env keine Connection zu DB aufbauen kann => in app.e2e.spec.ts die gleichen Einstellungen machen wie in app.module.ts
    ```ts
    import 'dotenv/config'
    //..
    ```
    * die Mongo-URI wird aus main.ts rausgelesen
* Test-Tools:
    * statt POSTMAN curl benutzen
        * `curl "http://localhost:3000`
    * Bsp: End-To-End:
    * in app.e2e.spec.ts
    ```ts
    it('/ (GET)', () => {
        return request(app.getHttpServer()).
            .get('/')
            .expect(200)
            .expect({hello: 'world'}); //hier wird Object geliefert
    });

    ```
    * app.service.ts
    ```ts
    @Injectable()
    export class AppService{
        getHello(): any {
            return {hello: "world"};
        }
    }
    ```
### 2 - Models
* Mongo-Models:
* `mkdir src/models`
    * `touch user.schema.ts`
    ```ts
    import * as mognoose from `mongoose`

    export const UserSchema = new mogoose.Schema({
        name: String; //ist JS-Typ
        password: string,
        sellor: {
            type: boolean,
            default: false
        },
        address: {
            addr1: string;
            addr2: string,
            city: string,
            state: string,
            country: string,
            zip: string
        },
        created: {
            type: Date,
            default: Date.now,
        }

    });
    ```
    * `touch product.schema.ts`
    ```ts
    //..
    export const ProductSchema = new mongoose.Schema({
        owner: {
            type: mongoose.Schema.Type.ObjectId,
            ref: 'user'
        }, //is ForeignKey für User (Verkäufer)
        title: string,
        desc: string,
        image: string
        price: string
        created: {
            type: date,
            default: Date.Now
        }
    });
    ```
    * `touch order.schema.ts`
    ```ts
    //..
    export class OrderSchema = new mongoose.Schema({
        owner: {
            type: mognoose.Schema.Types.ObjectId,
            ref: 'user'
        },
        totalPrice: {
            type: number,
            default: 0
        },
        product: [
            {
                product: {
                    type: mognoose.Schema.Types.ObjectId,
                    ref: 'product'
                },
                quantity: {
                    type: Number,
                    default: 0
                }
            }
        ],
        created: {
            type: Date,
            default: date.now()
        }
    });
    ```
+ `mkdir src/types` - Damit man die Schemas über TS anscprechen braucht man diese Dateien, die dann zu Schemas gemappt werden so bleibt man in TS (~ man bleibt Typisiert, da Schemas nur Objekte sind)
    * `touch user.ts`
    ```ts
    import {Document} from 'mongoose' // Document enhält diese Funktionen zum mappen

    interface Address{
        addr1: string;
        addr2: string;
        city: string;
        state: string;
        country: string;
        zip: number;
    }

    export interface User extends Documents{
        name: string;
        readonly passsword: string;
        seller: boolean;
        address: Address;
    }
    ```
    * `touch product.ts`
    ```ts
    import {Document} from 'mongoose`;
    import {User} from './user';

    interface Address{
        addr1: string;
        addr2: string;
        city: string;
        state: string;
        country: string;
        zip: number;
    }

    export interface Product extends Document{
        owner: User;
        title: string;
        desc: string;
        image: string;
        price: number
        created: Date
    }
    ```
    * `touch order.ts`
    ```ts
    interface ProductOrder{
        product: Product;
        quantity: number;
    }
    export interface Order extends Document{
        owner: User;
        totalPrice: number;
        products: ProductOrder[];
        created: Date;
    }
    ```
    * ??? - ShortCut um in Defintion zu gehen ???
### 3 - Shared User Service

### 4 - Passport Authentication

### 5 -  End To End Testing
* jest kennt keine absoluten Pfade => nur relativen Pfade
* Doku: NesJS-Doku -> Tecniques -> Mongo -> Testing (wie Man Module für Tests importiert)
* HIER: Startet die App und Test Gegen die App laufen lassen STATT wie es richtig wäre nur zu testende Module importieren und Test dagegen laufen
* Bsp - Jest-Default:  
```ts 

const app = 'http://localhost:3000';

describe("AppController (e2e), () => {
    it('/ (GET)', () => {
        return request(app)
            .get('/')
            .expect(200)

    })
});
```

* Bsp
```ts 

const app = 'http://localhost:3000';
//DB clear in BeforeAll (hier Mongo)

beforeAll(async () => {
    await mongoose.connect(process.env.MONGO_URI);
    await mongoose.connection.db.dropDatabase();
});

afterAll(async done => {
    await mongoose.disconnect(done);
});


describe("ROOT (e2e), () => {
    it('should ping', () => {
        return request(app)
            .get('/')
            .expect(200)

    })
});

describe('AUTH', () => {
    it('should register', () => {
        const user: RegisterDTO = {
            username: 'username';
            password: 'password';
        };

        return request(app)
            .post('/auth/register')
            .set('Accept', 'application/json')
            .send(user) //Object user in Body senden
            .expect({ body } => { //body des Responses holen
                console.log(body)
                expect(body.token).toBeDefined();
                expect(body.user.username).toEqual(user.username);
                expect(body.user.password).toBeUndefidned();
            })
            .expect(HttpStatus.CREATED);
    });

    it('should reject duplicate registration', () => {
        const user: RegisterDTO = {
            username: 'username';
            password: 'password';
        };

        return request(app)
            .post('/auth/register')
            .set('Accept', 'application/json')
            .send(user) //Object user in Body senden
            .expect({ body } => { //body des Responses holen
                console.log(body)
                //expect(body.token).toBeDefined();
                //expect(body.user.username).toEqual(user.username);
                //expect(body.user.password).toBeUndefidned();
                expect(body.message).toEqual('User alread exists');
                expect(body.code).toEqual(HttpStatus.BAD_REQUEST);
            })
            .expect(HttpStatus.BAD_REQUEST);
    });

    it('should login', () => {
        const user: LoginDTO = {
            username: 'username';
            password: 'password';
        };

        return request(app)
            .post('/auth/login')
            .set('Accept', 'application/json')
            .send(user) //Object user in Body senden
            .expect({ req } => { //gesamter Request
                console.log({req} => { //ged
                //expect(body.token).toBeDefined();
                //expect(body.user.username).toEqual(user.username);
                //expect(body.user.password).toBeUndefidned();
                expect(req.message).toEqual('User alread exists');
                expect( {body})
                    expect(body.token).toBeDefined();
                    expect(body.user.username).toEqual(user.username);
                    expect(body.user.password).toBeUndefidned();
                });
            });
            .expect(HttpStatus.CREATED);
    });


});
```
* es gibt ShortCuts in VS Code um zu Zeilen zu springen
* es gibt ShortCuts in VS Code um zu Deklaration/Definionen zu springen
 
### 6 - Authorisation

### 7 - Testing Improvment

### 8 - Product Listings

### 9 - Product Testing

### 10 - TDD Order Service

### 11 - Google Cloud Deployment

