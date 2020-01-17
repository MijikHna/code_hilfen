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


### 72 - Unit Testing Crash Course Basics
* jest für Tests
* eventuell:
    * `NODE_ENV=development nodemon` vor `jest` in `test` reinkopieren
    * `*.spec.ts` - Test-Files = specification
### 73 - Unit Testing Crash Course First Tests
* `yarn test --watch` - bei Änderungen von `.spec.ts` Tests werden nochmal ausgeführt
* `spec.ts` hat direkt Zugriff auf jest-Modul
* Bsp:
```ts
describe("my test", () =>{
    it("returns true" ()=>{
        expect(true).toEqual(true);
    });
} );
```
* `expect()` solte in `test()` bzw. `it()` stehen
* Klasse zum Testen:
```ts
class FriendList {
    friends = [];

    addFriend(name){
        this.friends.push(name);
        announceFriendship(name);
    }

    announceFriendship(name){
        global.console.log(`${name} is now a friend!`); //global
    }

    removeFriend(name){
        const dix = this.friends.indexOf(name);

        if (idx === -1 ){
            throw new Error("Friend not found");
        }

        this.friends.splice(idx, 1); //eigentlich removen
    }
}
```
* TestKlasse dafür
```ts
describe("FriendList", () =>{
    it("init friends list" ()=>{
        const firendsList = new FriendsList();
        expect(friendsList.friends.length).toEqual(0);
    });

    it("add a friend to friends list" ()=>{
        const firendsList = new FriendsList();
        friendsList.addFriend("Test")
        expect(friendsList.friends.length).toEqual(1);
    });

    //hier Mock Funktion benutzen 
    //Mock - trackt, welche, wie oft, mit welchen Parametern Funktion aufgerufen wurde => Behavior simulieren
    it("announce friend ship" ()=>{
        const firendsList = new FriendsList();
        friendsList.announceFriendship = jest.fn(); //Mock-Funktion die trackt die Funktion announceFriendship()
        
        expect(friendsList.friends.length).not.toHaveBeenCalled(); //not flipped hier das Output
        friendsList.addFriend("Test")
        expect(friendsList.friends.length).toHaveBeenCalledTimes(1); //Oder z.B so
    });
} );
```
* obige TestKlasse mit `beforeEach()`
```ts
describe("FriendList", () =>{
    let friendList;

    beforeEach( () =>{
        firendsList = new FriendsList();
    });


    it("init friends list" ()=>{
        expect(friendsList.friends.length).toEqual(0);
    });

    it("add a friend to friends list" ()=>{
        friendsList.addFriend("Test")
        expect(friendsList.friends.length).toEqual(1);
    });

    //hier Mock Funktion benutzen 
    //Mock - trackt, welche, wie oft, mit welchen Parametern Funktion aufgerufen wurde => Behavior simulieren
    it("announce friend ship" ()=>{
        friendsList.announceFriendship = jest.fn(); //Mock-Funktion die trackt die Funktion announceFriendship()
        
        expect(friendsList.friends.length).not.toHaveBeenCalled(); //not flipped hier das Output
        friendsList.addFriend("Test")
        expect(friendsList.friends.length).toHaveBeenCalledTimes(1); //Oder z.B so
    });

    describe("remove Friend", () =>{
        it("remove a Friend " ()=>{
            friendsList.addFriend("Text");
            expect(friendsList.friends[0]).toEqual("Text");
            friendsList.removeFriend("Text");
            expect(friendsList.friends[0]).toBeUndefiend();
        });

        it("throw an Error" ()=>{
            expect( () => friendsList.removeFriend("Text")).toThrow(); //die expect erwartet Throw
            expect( () => friendsList.removeFriend("Text")).toThrow(new Error("Friend not found"));
            //expect(friendsList.friends[0]).toBeUndefiend();
        });
    });
} );
```
### 74 - Testing TaasksService.getTasks
* `spec.ts` in Modul-Ordner erstellen
```ts
import { Test, TestModule } from '@nest/testing';

const mockUser = { username: "Max" };
const mockTaskRepository = () => ({
    getTasks: jest.fn(); //Funktion, die simuliert werden soll; <= getTask-Method ist vom Typ jest.fn() = MockMethode
}); //Objekt, der TaskRepository simulieren soll; ({}) = Objekt direkt returnen; 

describe("TaskService", () => {
    let tasksService; //was getestet wird
    let taskRepo; //was TaskService selbst benutzt (sollte im constructor stehen)

    beforeEach(async () => {
        const module = await Test.createTestingModule({
            providers: [
                TaskService,
                {provide: TaskRepository, useFactory: mockTaskRepository }, // hier Mock verwenden, da z.B man nicht will das wirklcih sich mit DB verbindet => über Mock TaskRepository simulieren; hier kann man useFactory/Class/Value -> hier Factory damit es jedes Mal neu ertellt wrid; <- hier wird an mockTaskRepository gesagt, welches Objekt genau simuliert werden soll
            ],
        }).compile(); //Module zum Testen erstellen; await, da compile-Funktion async ist

        taskService = await module.get<TaskService>(TasksService);
        taskRepo = await module.get<TaskRespository>(TaskRepository);
    })

    //getTask(filterDto: GetTasksFilterDto, user: User)
    describe("getTasks", () => {
        it("gets all tasks form repo", async () => {
            //taskRepository.getTasks.mockResolvedValue();
            //taskRepository.getTasks.mockReturnValue();
            //taskRepository.getTasks.mockRejectedValue();
            taskRepository.getTasks.mockResolvedValue("someValue"); //sagt man welchenWert es returnen soll

            expect(taskRepo.getTasks).not.toHaveBeenCalled();

            const filters: GetTasksFilterDto = {status: TaskStatus.IN_PROGESS, search: "Some search query" };
            cosnt result = await taskService.getTasks(filters, mockUser);
            expect(taskRepository.getTasks).toHaveBeenCalled();
            expect(result).toEqual("someValue");
        })
    })
});

```
### 75 - Testing TasksService.getTaskById
* angfang in 74
```ts
const mockUser = { id: 12, username: "Max" };
const mockTaskRepository = () => ({
    getTasks: jest.fn(); //Funktion, die simuliert werden soll; <= getTask-Method ist vom Typ jest.fn() = MockMethode
    findOne: jest.fn();
}); //Objekt, der TaskRepository simulieren soll; ({}) = Objekt direkt returnen; 

    //getTaskById(id: number, user: User)
    describe("getTasksById", () => {
        it("calls taskRepository.findOne() and returns the task", async () => {
            //taskRepository.getTasks.mockResolvedValue();
            //taskRepository.getTasks.mockReturnValue();
            //taskRepository.getTasks.mockRejectedValue();
            const mockTask = {title: "test task", description: "test desc" };
            taskRepository.findOne.mockResolvedValue(mockTask); 
            // taskRepository.findOne.mockResolvedValue( {title: "test task", description: "test desc" }); //sagt man welchenWert es returnen soll
            
            const result = await taskService.getTaskById(1 mockUser);
            expect(result).toEqual(mockTask);

            //TaskRepositry.findOne({ where: {id, userId: user, id}})
            expect(taskRepository.findOne).toHaveBeenCalledWith({
                where: {
                    id: 1,
                    userId: mockUser.id
                }
            });
        })

        it("throws Error", () => {
            taskRepository.findOne.mockResolvedValue(mockTask);
            
            expect(taskService.getTaskById(1, mockUser)).reject.toThrow(NotFoundExcepiton); //da hier Exepction geworfen wrid => zu returnende Promise wird nicht erfüllt = rejected
        });
    })

```
### 76 - Testing Taskservice.createTask
### 77 - Testing TaskService.deleteTask
* Anfang in 74
```ts
const mockUser = { id: 12, username: "Max" };
const mockTaskRepository = () => ({
    getTasks: jest.fn(); //Funktion, die simuliert werden soll; <= getTask-Method ist vom Typ jest.fn() = MockMethode
    findOne: jest.fn();
    delete: jest.fn();
}); //Objekt, der TaskRepository simulieren soll; ({}) = Objekt direkt returnen; 

    //getTaskById(id: number, user: User)
    describe("deleteTAsk", () => {
        it("calls taskRepository.delete({id, userId: user.id})", async () => {
            taskRepository.delete.mockResolvedValue( { affected: 1 } ); //sagen, welchen Wert taskRepository.delete() returnen soll
            expect(taskRepository.delete).not.toHaveBeenCalled();

            await taskService.deleteTask(1 mockUser);
            //expect(taskRepository.delete).toHaveBeenCalled();
            expect(taskRepository.delete).toHaveBeenCalled( { id: 1, userId: mockUser.id });


        })

        it("throws Error", () => {
           taskRepository.delete.mockResolvedValue( { affected: 0 });
            
            expect(taskService.deleteTask(1, mockUser)).reject.toThrow(NotFoundExcepiton); //da hier Exepction geworfen wrid => zu returnende Promise wird nicht erfüllt = rejected
        });
    })
```
### 78 - Testing TaskService.updateTaskStatus
### 79 - Testing UserRepository
### 80 - Testing User Entity
### 81 - Testing JwtStrategy