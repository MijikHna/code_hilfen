## Tasks-APP
### 1
* benutzt *Express.js* im Background
* Github: arielweinberger/task-management-frontend
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
* können in Konstruktoren wenn mit `@Injectable` dokoriert sind über **dependency injection** eingefügt werden.
* können sein: 
    1. Plain Values
    2. Klassen
    3. Sync/Async Factories usw.
* müssen in Modul eintegriert werden, damit vom Modul genutzt werden können.
* können von anderen Modulen imporitert werden
* **Services** sind **Providers**
    * nicht alle Providers sind automatisch **Services**
* wenn `@Injectable` dann wird zum Singelton
* **Service** haben die Business-Logik. z.B.
    * **Service** wird von Controller aufgerufen, um Daten zu validieren, Items zu erstellen usw.
* weitere Bsp:
    * Module:
        * Controller: 
        * Service 1
        * Service 2
        * Service 3
    * <= Controller kann dann mehrere Services injecten => 
        * im Module-Array mehrere Services bei Provider-Array
* jede Komponte kann einen Provider/Services injecten => wird im Konstruktor der Komponte definiert

### 10
* `nest g service task --no-spec` - Module wird direkt ergänzt
* in *tasks.controller.ts
```ts
@Controller('tasks')
export class TaskController{
    constructor(private taskService: TasksService){ //

    }
}
```

### 11
* 
* *task.service.ts*
```ts
@Injectable
export class TasksService(){
    private tasks = []; //nur Temporär,da noch keine DB

    //HIER WAR FEHLER
    getAllTasks(): Array{ //damit kann der Controller auf TaskService-Sachen zugreifen
        return this.tasks;
    }
}
```
* tasks.controller.ts
```ts
@Controller("tasks")
export class TasksController(){
    constructor(private taskService: TasksService){
    }

    @Get()
    getAllTasks(){ //diese Funktion wird aufgerufen, wenn REST-Api GET: localhost aufruft
        this.taskService.getAllTasks();
    }
}
```
* => Trennung der Business-Logik von REST-Aufrufen

### 12 Model erstellen
* **task.model.ts** erstellen
    * können als Klassen oder Interfaces erstellt werden
```ts
export interface Task(){
    id: string;
    title: string;
    desc: string;
    status: TaskStatus
}

export enum TaskStatus{
    OPEN = "OPEN",
    IN_PROGRESS = "IN_PROGESS",
    DONE = "DONE",
}
```
* **tasks.service.ts**
```ts
@Injectable
export class TasksService(){
    private tasks: Task[] = []; //nur Temporär,da noch keine DB

    getAllTasks(): Task[] Array{ //damit kann der Controller auf TaskService-Sachen zugreifen
        return this.tasks;
    }
}
```
* in *tasks.controller.ts* auch die Typen ergänzen

### 13 
* *tasks.service.ts*
```ts
import * as uuid from 'uuid/v1' // UUID Version1 importieren

createTask(title: String, desc: String): Task {
    const task: Task = {
        id: uuid(),
        title, //in ES6 wenn Name + VariableName im Scope gleich => JS macht alles selbst ~ this.title = title
        desc,
        status: TaskStatus.OPEN,
    }

    this.tasks.push(task);
    return task; //returnen, damit im Frontend entschieden werden kann was + wie damit weiterverfahren wird
}
```
* `npm isntall --save uuid` - npm-Package um UUID zu generieren

### 14
* tasks.controller.js
    * POST-Method zum Erstellen von Task
```ts
@Post()
createTask01(@Body() body){
    console.log("body", body);
}

@Post()
createTask (
    @Body("title") title: string,
    @Body("desc") desc: string,
): Task
{
    //console.log("title", title);
    //console.log("desk", desk);
    return this.taskService.createTask(title, desc);
}
```
* die Daten können auf zwei Weisen versendet werden 
    1. mit `@Body()` als JSON-Obj
    2. `@Body` aber genauer

### 15 DTO - Data Transfer Object
* Problem:
    * bei jeder weitergabe der Daten müssen Daten aus einem Obj in ein anderes Obj aus/verpackt werden => wenn man etwas ändern will => muss es in der ganzen Kette geändert werden
* DTO => Objekt, um Daten einheitlich zu halten in der Kette 
* DTO definieren Verhalten zum Speichern, Serialisieren, Desirialisieren
* man sollte Klassen für DTOs benutzen, da Interfaces nur TS sind und Klassen sind JS
* DTOs definieren nur Eigenschaften der Daten => keine Methoden

### 16
* **dto** in **/tasks** erstellen 
* create-task.dto.ts erstllen
```ts
export class CreateTaskDto(){
    title: string;
    desc: string;
}
```
* tasks.controller.ts
```ts
@Post()
createTask01(@Body crateTaskDto: CreateTaskDto): Task{
    //console.log("title", title);
    //console.log("desk", desk);
    return this.taskService.createTask(createTaskDto);
}
```
* tasks.service.ts
```ts
createTask(createTaskDto: CreateTaskDto): Task {
    const { title, desc } = createTaskDto; //DTO in primitive Variablen entpacken

    const task: Task = {
        id: uuid(),
        title,
        desc
        status: TaskStatus.OPEN,
    }

    this.tasks.push(task);
    return task; //returnen, damit im Frontend entschieden werden kann was + wie damit weiterverfahren wird
}
```
### 17
* in *tasks.controller.ts
```ts
@Get('/:id') //auf / kann man auch verzichten
getTaskById(@Param('id') id: string){
    return this.taskService.getTaskById(id);
}
```
+ in *task.service.ts*
```ts
getTaskById(id: string): Task{
    //es gibt mehrere Möglichkeiten das zu realisieren
    return this.tasks.find(task => {
        task.id === id
    });
}

getTaskById(id: string): Task{
    //es gibt mehrere Möglichkeiten das zu realisieren
    return this.tasks.find(task => task.id === id);
}
```
 
### 18 + 19 Challenge: Delete Task
* in *tasks.service.ts*
```ts
deleteTask(id: string): void {
    //Es gibt mehrere Möglichkeiten die zu realisieren
    //Hier wird Array-filter()-Methode verwendet verwendet
    this.task = this.task.fitler(task => task.id != id ); //der Code nach => wird auf ganzes Array angewendet und wenn false wird return => dieser Task wird returt
}
```
* in *tasks.controller.ts*
```ts
@Delete('/:id')
deleteTask(@Param('id') id:string): void {
    this.tasksService.deleteTask(id);
}
```

### 20 + 21 Challenge: Update Task's Status
* HTTP-Requst ist PATCH
    * in Body wird der Status stehen und URI wird id-Nummer stehen
* Ansätze:
    1. neue DTO erstellen
    2. mit Pipes
* *tasks.service.ts*
```ts
updateTaskStatus(id: string, status: TaskStatus){
    const task = this.getTaskById(id);
    task.status = status;
    return status;
}
```
* *tasks.controller.ts
```ts
@Patch('/:id/status')
updateTaskStatus(@Param('id') id: string, @Body('status') status: TaskStatus){
    return this.taskService.updateTaskStatus(id, status)
}
```

### 22 - Filtering
* nach Status oder Name filtern/suchen
* neue DTO erstellen *get-tasks-filter.dto.ts*
```ts
export class GetTasksFilterDto {
    status: TaskStatus;
    search: string;
}
```
* *tasks.controller.ts*
```ts
@Get()
getAllTasks(@Query() fitlerDto: GetTasksFilterDto): Task[]{
    console.log(filterDto);
    //hier muss entschieden welche Methode von Serve wird aufgerufen
    if (Object.keys(filterDto).length){ //wenn die Länge der Keys der fitlerDto nicht 0 ist = es gibt Filters
        return this.tasksService.getTasksWithFitler(filterDto);
    }
    else {
        return this.tasksService.getAllTasks();
    }
}
```
* *task.service.ts* 
```ts
getTasksWithFilter(fitlerDto: GetTaskFitlerDto): Task{
    cosnt {status, search } = fitlerDto;
    
    let tasks = this.getAllTasks();

    if (status){
        tasks = tasks.filter( task => task.status === status);
    }

    if (search){
        tasks = tasks.fitler(task => 
            task.title.includes(search) || task.description.include(search),
        );
    }

    return tasks
}
```
* <= in GET-Requst kann man jetzt `?status=XXX&search=XXX` usw. machen

### 23 - PIpes
* operieren auf Argumenten die von Router Handler behandelt werden, bevor der Handler aufgerufen wird
* können Data Transformation udn Data Validation machen
* können Exception werfen, die dann von NESTJS behandelt werden
* könen Async seind
* NestJs hat schon ein paar Pipes
    1. ValidationPipe - Objekt gegen Klasse validieren
    2. ParseIntPipe - String in Number parsen
* Custom Pipes:
    1. werdne mit `@Injectable` annotiert
    2. implementeiren `PipeTransform` generische Klasse => müssen `transform()` implementieren. Parameter:
        1. `value`
        2. `metadata` (Optional) - Objekt, der Daten zu value hat
        3. was `transform()` returnt => wird an Router Handler weitergegeben. Exceptions werden als 404 an Client gesendet
* Arten der Handler:
    1. Handler-level Pipes - werden auf dem Handler Level definiert mit `@UserPipes()`. wird alle Parameter des Requests behandeln <- EMPFEHLUNG gegenüber von Parameter-Pipes
    ```ts
    @Post()
    @UsePipes(SomePipe) // <--- HIER
    funkt(@Body('desc') desc){

    }
    ```
    2. Parameter-level Pipes - auf Parameter Level definiert. Nur bestimmte Parameter für die Pipe wurde erstellt werden bahandelt 
    ```ts
    funkt('desc', SomePipe) desc){ // <---- HIER

    }
    ```
    3. Global Pipes - auf Application Level definiert. werden auf jeden Request applied
    ```ts
    async function bootstrap(){
        const app = await NestFactory.create(ApplicationModule);
        app.useGlobalPipes(SomePipe);
        await app.listen(3000);
    }
    boostrap()
    ```
### 24 - Pipe erstellen
* zwei Pakete dafür installieren
    * `npm install class-validator class-transformer --save`
    * `yarn add class-validator class-transformer`
    * Doku gibt es auf Github
* dann Decoratoren der Packages verwendet um Pipes zu realisieren
* Bsp: Validation der DTO

    * *get-tasks-filter.dto.ts*
    ```ts
    import { isNotEmpty } from 'class-validator`
    export class CreateTaskDTO{
        @IsNotEmpty()
        title: string;
        @IsNotEmpty()
        desc: string;
    }
    ```
    * *tasks.controller.ts
    ```ts
    @Post()
    @UsePipes(ValidationPipe) //jetzt wird ValidationPipe wird createTaskDto nehmen und chechen ob die @IsNotEmpty-Dekoratoren erfüllt sind
    createTask(@Body() createTaskDto: CreateTaskDto): Task {
        return this.tasksService.createTask(createTaskDto);
    }
    ```
### 25 - 404 Returnen
* *tasks.serivce.ts*
```ts
getTaskById(id: string): Task{
    const found = this.tasks.find(task => task.id === id);

    if (!found){
        //throw new NotFoundException();
        throw new NotFoundException("Task with ID not Found");
    }

    return found;
}
```

* *tasks.controller.ts* - wird an Nest-Main weitergeben und es wird 404 ertzeugt

### 26
* *tasks.service.ts*
```ts
deleteTask(id: string): void {
    const found = this.getTaskById(id);
    this.tasks = this.tasks.filter(task => task.id !== found.id);
}
```

### 27 - Custom Pipe Validation
* /tasks/pipes erstellen + task-status-validation.pipe.ts erstellen
```ts
export class TaskStatusValidationPipe implements PipeTransform {
    readonly allowStatus = [
        TaskStaus.OPEN,
        TaskStatus.IN_PROGRESS,
        TaskStatus.DONE,
    ];
    
    transform(
        value: any,
        //metadata: ArgumentMetadata
    ){
        console.log("value", value);
        //console.log("metadata", metadata);

        //hier findet Validierung statt
        value = value.toUpperCase();
        
        if(!this.isStatusValid(value)){
            throw new BadRequestException(`"${value}" is an invalid status`);
        }

        return value;
    }

    private isStatusValid(status: any){
        cosnt idx = this.allowedStatuses.indexOf(status);
        return !== -1;
    }
}
```
* Pipe an Controller binden *task.contorller.ts*
```ts
@Patch("/:id/status)
updateTaskStatus(
    @Param('id') id: string,
    @Body("status", TaskStatusValidationPipe) status: TaskStatus, //hier wird new ... im Hintergrund gemacht
    //@Body("status", new TaskStatusValidationPipe() ) status: TaskStatus,
): Task{
    return this.tasksService.updateTaskStatus(id, status);
}
```

### 28 
* *get-tasks-filter.dto.ts*
```ts
export class GetTaskFilterDto {
    @IsOptional()
    @IsIn(TaskStatus.OPEN, TasksSatus.IN_PROGRESS, TaskStatus.DONE)
    status: TaskStatus;

    @IsOptional()
    @IsNotEmtpy()
    search: string
}
```
* *tasks.controller.ts*
```ts
@Get()
getTasks(@Query(ValiadationPipe) filterDto: GetTasksFilterDto): Task[]{
    if (Object.keys(filterDto).length){ //wenn die Länge der Keys der fitlerDto nicht 0 ist = es gibt Filters
        return this.tasksService.getTasksWithFitler(filterDto);
    }
    else {
        return this.tasksService.getAllTasks();
    }
}
```

### 29 DB aufsetzen
* DB **taskmanagement** nennen

### 30 - ORM - Object Relational Mapping
* Klasse <=> DB-Tabelle
* TypeORM ist ORM-Library füf TS + JS
* Bsp alle Tasks von Ashley mit DONE finden
    * `const tasks = await Task.find({status: "DONE", user: "Ashley" });`
* https://typeorm.io

### 31 DB verbinden
* `yarn add @nestjs/typeorm typeorm pg`
* es gibt drei Wege sich mit DB zu verbinden
    1. [ ] static JSON-File
    2. [x] Daten als Objects providen
    3. [ ] Data asynchron von Services providen
* Ordner /config anlegen -> typorm.config.ts
```ts
const typeOrmConfig: TypeOrmModuleOptions = {
    type: 'postgres'; //so weiß NestJs welchen Driver er bunutzen muss
    host: 'localhost';
    port: 5432;
    username:
    password:
    database: '';
    entities: [__dirnam__ '+ /../**/*.entity.ts'], //sagen welche Klassen Entities für DB sind
    synchronize: true, //Schema synchronisieren, wenn Connecion aufgebaut ist (true nur Prod)

};
```
* in *app.module.ts`
```ts
imports [
    TypeOrmModule.forRoot(typeOrmConfig), //TypeOrm-Module imortieren + forRoot(...) - es soll für alle SubModule diese Einstellungen gelten + app.module.ts ist jetzt Root f+ TypeOrmModule
    TasksModule,
]
```
### 32 - Task Entity
* *task.entity.ts*
```ts
import { BaseEntity, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Tasks extends BaseEntity {
    @PrimaryGeneratedColumn()
    id: nubmer;

    @Column()
    title: string;

    @Column()
    desc: string;

    @Column()
    @status: TaskStatus
}
```

### 33 Repository 
* Logik der Anfragen von Entity trennen
* man kann es auch direkt in Entity machen
* *task.repository.ts* - Logik = Operationen die für Entity Task ausgeführt werden sollen
```ts
import  { Task } form '/task.entity';
import { BaseEntity, Entity, PrimaryGeneratedColumn } from 'typeorm';

@EntityRepository(Task)
export class TaskRepository extends Repository<Task>{
    //hier kommt Logik
} 

```
* *task.module.ts*
```ts
imports: [
    TypeOrmModule.forFeature([TaskRepository]), //damit TaskRepository weiß TypeOrm-Funktionen benutzen kann
]
```

### 34 - 
* *tasks.servie.ts* und *tasks.controller.ts ganze Logig muss überschrieben werden, da jetzt DB benutzt wird
* `interface Tasks` kann man löschen + `enum TaskStatus` in eigene Datei kopieren -> *task-status.enum.ts*
* uuid-Package löschen, das Entity jetzt alles macht: `npm uninstall uuid`

### 35 -
* *tasks.service.ts*
    * TaskRepository injecten => geschieht in Contruktor
```ts
@Injectable()
export class TaskService{
    constructor(
        @InjectRepository(TaskRepository)
        private taskRepository: TaskRepository,
    ){

    }
    
    getTaskById01(id: number){
        const found = this.taskRepository.findOnde(id); // findOne ist async-methode => entsprechende Ergänzugnen
    }

    async getTaskById(id: number): Promise<Task>{
        const found = await this.taskRepository.findOnde(id); // findOne ist async-methode => entsprechende Ergänzugnen
        if (!found) {
            throw new NotFoundException;
        }
        return found;
    }
}
```
* *tasks.controller.ts*
```ts
@Get('/:id')
getTaskById(@Param('id', ParseIntPipe) id: number): Promise<Task> { //mit ParseIntPipe, wird @Param zu Int umgewandelt
    return this.tasksService.getTaskById(id);
}
```
* typeorm hat eigene Dokumentation

### 36 
1. nur Entity statt Repository benutzen
    * *task.service.ts*
    ```ts
    async createTask(createTaskDto: CreateTaskDto): Promise<Task>{
        const task = new Task();
        task.title = title;
        task.desc = desc;
        task.status = TaskStatus.OPEN;
        await task.save();

        return task;
    }
    ```
    * task.controller.ts*
    ```ts
    @Post()
    @UserPipes(ValidationPipe)
    createTask(@Body() createTaskDto: CreateTaskDto): Promise<Task>{
        return this.taskService.createTask(createTaskDto);
    }
    ```
2. mit Repositoy
    * tasks.repository.ts
    ```ts
    @EntityReposity(Task)
    export class TaskRepositoy extends Repositoy<Task>{
        async createTask(createTaskDto: CreateTaskDto): Promise<Task>{
            const task = new Task();
            task.title = title;
            task.desc = desc;
            task.status = TaskStatus.OPEN;
            await task.save();

            return task;
        }
    }
    ```
    * *task.service.ts*
    ```ts
    async createTask(createTaskDto: CreateTaskDto): Promise<Task>{
        return this.taskRepository.createTask(createTaskDto);
    }
    ```
    * task.controller.ts*
    ```ts
    @Post()
    @UserPipes(ValidationPipe)
    createTask(@Body() createTaskDto: CreateTaskDto): Promise<Task>{
        return this.taskService.createTask(createTaskDto);
    }
    ```
### 37 + 38: Delete Task
* *tasks.repositoy.ts*
    * `remove()` -> Param: Entity
    * `delete()` -> Param: id => ist cheaper was DB-Queries angeht


* *tasks.serivce.ts*
```ts
async deleteTask(id: number): Promise<void>{
    const result = this.taskRepository.delete(id):
    console.log(result)

    if(!result.affected)
    if(result.affected === 0){
        throw new NotFoundExcepiton(`Not Found Task with "${id}" not found`);
    }
}
```
* *tasks.controller.ts*
```ts
@Delete('/:id')

deleteTask(@Param('id', ParseIntPipe) id: number): Promise<void> {
    return this.taskService.delete(id);
}
```

### 39 
* *task.service.ts*
```ts
async updateTaskStatus(id: number, status: TaskStauts) Promise<Task>{
    task = await this.getTaskById(id);
    task.status = status;
    await task.save();
    return task;
}
```
* +tasks.controller.ts*
```ts
@Patch('/:id/status/)
updateTaskStatus(
    @Param('id', ParseIntPipe) id: number,
    @Body("status", TaskStatusValidationPipe) status: TaskStatus,
): Promise<Task>{
    return this.tasksService.updateTaskStatus(id, status);
}
```

### 40 - IMPORTANT für 4
* *tasks.controller.ts*
```ts
@Get()
getTasks(@Query(ValidationPipe) filterDto: GetTasksFilterDto){
    return this.tasksService.getTasks(filterDto);
}
```
* *tasks.service.ts*
```ts
getTasks(filterDto: GetTaskFilterDto){

}
```

### 41 - getTask mit Filter
* *tasks.repository.ts*
```ts
async getTasks(fitlerDto: GetTasksFitlerDto): Promise<Task[]>{
    const {status, search} = filterDto,
    //QueryBilder benutzen
    const QueryBuilder = this.createQueryBuilder("task"); //mit String task task.entity ansprechen
    //const tasks = await query.getMany();
    if (status) {
        //query.andWhere('task.status = :status', {status: 'OPEN'})
        query.andWhere('task.status = :status', {status})
    }
    //wenn man where() benutze => wird altes where überschreiben
    if (search){
        query.andWhere('task.title LIKE :search OR task.desctiption LIKE :search', {search: `%${search}%`); //partielles Matching d.h. nicht ganze Tabelle-Zeile muss übereinstimmen.
    }
    const tasks = await query.getMany();
    return tasks
}
```
* *tasks.service.ts*
```ts
async getTasks(filterDto: GetTasksFilterDto): Promise<Task[]>{
    return await this.taskRepository.getTasks(filterDto);
}
```

### 42  - Auth
* `nest g module auth`
* `nest g controller auth --no-spec`
* `nest g service auth --no-spec`
* user.entity.ts erstellen
```ts
//import

@Entity()
export class User extends BaseEntity{
    @PrimarGeneratedColumn()
    id: number;
    
    @Column()
    username: string;

    @Column()
    password: strig;
}   
```
* User-Repository: user.repository.ts
```ts

@EntityRepository(User)
export class UserRepository extends Repository<User>{

}
```
+ auth.module.ts
@Module({
    imports: [
        TypeOrmModule.forFeature([User]),
    ]
})

# auth.service.ts
```ts
export class AuthService{
    construcotr(@InjectRepository(UserRepository) private userRepo: UserRepository){

    }
}
```
### 43 
+ user.repository.ts
```ts
async signUp(authCredentialsDto: AuthCredentialsDto): Promise<void>{
    const {username, password} = authCrednetialDto;
    const user = new User();
    user.username = username;
    user.password = password;
    await user.save();
    //hier wird eignentlich return 201 gemacht
    // es wird kein User returned, da in dem Obj dann password drin steht
} 
```
+ ./dto/auth-credentials.ts
```ts
export class AuthCredentialsDto {
    username: string;
    password: string;
}
```
+ auth.service.ts
```ts
async singUp(authCredentialsDto: AuthCredentialsDto): Promise<void>{
    return this.userRepository.signUp(authCredentialsDto)
}
```
* auth.controller.ts
```ts
constructor(private authService: AuthService){

}

@Post('/singup)
signUp(@Body() authCredentialsDto: AuthCredentialsDto): Promise<void>{
    console.log(authCredentialsDto)
    return this.authService.signUp(authCredentialsDto);
}
```
* momentan werden die Passwörter nicht gehasht

### 45 -
+ Validation wrid mit Validation-Package von NestJs gemacht => Decorieren
+ auth-credentials.dto.ts
```ts

export class AuthCredentialDto{
    @IsString()
    @MinLength(4)
    @MaxLength(20)
    username: string;

    @IsString()
    @MinLength(8)
    @MaxLength(20)
    @Matches(..., {message: "Password to week"})//siehe Github hier ist RegEx damit Password Zahlen, Buchstaben usw. hat
    password: string;
}
```
### 46
+ auth-credentials.dto.ts
```ts

```
+ 2 Wege zur Realisierung
    1. DB checken, ob User schon da ist und Error werfen
    2. Festlegen, dass z.B Username Unique ist
+ user.repository.dto.ts
```ts
async signUp(authCredentialsDto: AuthCredentialsDto): Promise<void>{
    const {username, password} = authCrednetialDto;

    // Weg 1
    const exists = this.findOne({username});
    if(exists){
        //throw Eroro
    }

    //Weg 2 - ,uss man eignetlich user.entity.ts

    const user = new User();
    user.username = username;
    user.password = password;
    try {
        await user.save();
    }
    catch(error){
        console.log(error.code)
        if (error.code === "23505"){ //duplicate username
            throw new ConfictException("username already exists");
        }
        else{
            throw new InternalServerErrorExcepiton();
        }
    }
    //hier wird eignentlich return 201 gemacht
    // es wird kein User returned, da in dem Obj dann password drin steht
} 
```
+ für Weg 2 in user.entity.ts
```ts
@Entity()
@Unique(['username'])
export class User extends BaseEntity{
    //..
} 
```
* wenn User schon existiert es wird *Internal Server Error* erzeugt

### 47 - Password-Hashing
* es wird zur besseren Sichercheit **Salt** benutzt = vor dem Password wird eine Randome Zahl erzeugt die dann mit Password gehasht wird. Salt ist Unique per User
    * bcrypt installieren `npm install --save bcrypt
* `user.repository.ts`
```ts
import * as bcrypt from 'brycpt';

async signUp(authCredentialsDto: AuthCredentialsDto): Promise<void>{
    const {username, password} = authCrednetialDto;

    const salt = await bcrypt.genSalt();
    console.log(salt);
    // Weg 1
    const exists = this.findOne({username});
    if(exists){
        //throw Eroro
    }

    //Weg 2 - ,uss man eignetlich user.entity.ts

    const user = new User();
    user.username = username;
    user.password = await this.hashPassword(password, salt);
    user.salt = salt;
    console(user.password);
    
    try {
        await user.save();
    }
    catch(error){
        console.log(error.code)
        if (error.code === "23505"){ //duplicate username
            throw new ConfictException("username already exists");
        }
        else{
            throw new InternalServerErrorExcepiton();
        }
    }
    //hier wird eignentlich return 201 gemacht
    // es wird kein User returned, da in dem Obj dann password drin steht
} 

private async hashPassword(password: string; salt: string): Promise<string>{
    return bcrypt.hash(password, salt);
}
```
+ da Salt auch gespeichert werden muss man den auch in DB speicert user.entity.ts
```ts
//...
@Column()
salt: string();
```

### 48
* user.repository.ts
```ts
async validateUserPassword(authCredDto: AuthCredentiolsDto): Promise<string>{
    const {username, password} autCredto;
    const user = await this.findOne({username});

    //Password checken -> wird in user.entity.ts-Funkt gemacht
    if (user && await user.validatePassword(password)){
        return user.username;
    })
    else {
        return null;
    }
}
```
+ user.entity.ts
```ts
async validatePassord(passoword: string): Promise<boolean>{
    const hash = await bcrypt.hash(password, htis.salt);
    return hash === this.password;
}
```
+ auth.service.ts
```ts
async singIn(authCredentialDto: AuthCredentialsDto): Promise<void>{
    const username = await this.userRepository.signUp(authCredentialDto);
    console.log(username);

    if (!username){
        throw new UnauthrizedException('Invalid credentials');
    }
}
```
* aut.controller.ts
```ts
@Post('/signin')
singIn(@Body(ValidationPipe) authCrdentialDto: authCredentialDto){
    return this.authService.signIn(authCredentialsDto);
}
```

### 49 JSON Web Token - JWT
* für Authorization
* es wird KeyPaar erstellt
+ haben eine Gültigkeitsdauer 
* JWT besteht aus
    1. Header - Metadaten = Type, Hash-Algorith, Gültigkeitsdauer usw
    2. Payload - Statements über Entity z.B Username
    3. Signature - verschlüsseltes Header + Payload, die mit Secret Key signiert wurden

### 50
* passport-js (hat auch JWT)
* `npm install --save @nest/jwt @nestjs/passport passport passport-jwt`
* aut.module.ts
```ts
import { JwtModule } form @nestjs/jwt;
import: [
    //..
    JwtModule.register({ //register = Konfiguration
        secret: 'topSecret51', //private Secret für Signatur sollte komplizierter sein
        signOptions: { //
            expiresIn: 3600, 
        },
    }),
    PassportModule.register({defaultStrategy: 'jwt' }), //Passport hat auch andere Strategie = authentifiziert mit jwt
    //...
]   
```
* JwtModule exportiert Service (JwtService) => über Dependency Injection kann man ihn verwenden
### 51
* JWT-Token werden auch von FrontEnd benutzt
+ auth.service.ts
```ts
constructor(
    @InjectRepository(UserRepository) private UserRepository,
    private jwtService: JwtService;   
){

}

async singIn(authCredentialDto: AuthCredentialsDto): Promise<{accessToken: string}>{
    const username = await this.userRepository.signUp(authCredentialDto);
    console.log(username);

    if (!username){
        throw new UnauthrizedException('Invalid credentials');
    }
    
    //const payload = { username };
    //const accessToken = await this.jwtService.sign(payload);

    const payload: JwtPayload = { username };
    const accessToken = await this.jwtService.sign(payload);

    return {accessToken};
}
```
* jwt-Interface erstellen jwt-payload.interface.ts
```ts
export interface JwtPayload {
    username: string;

}
```
*man kann jwt Tokens checken auf jwt.io





### 67 - Frontend-Teil
* ist in React (in github)
* `npm install`
* `npm start` - App starten => localhost:3001
* Per Default Nest.JS erlaubt anfragen nur über 3000 => bestimmten Port freigeben
    1. Cors Enabeln (in Dev)
    2. bestimmte Ports whitelisten (in Prod)
* *main.ts*
```ts
    const app = await NestFactory.create(AppModule)
    if (NODE_ENV === 'development'){
        app.enableCors();
    }
```
* in *package.json*
z.B bei stard:dev "NODE_ENV=development nodemon"

### 68 alles zu AWS
* Bucket erstellen, wohin man Frontdend-Dateien (HTML, CSS)
    1. Create Bucket
        1. Namen usw
        2. Next 
        3. nichts blocken
        4. Done
    2. Bucket konfigurieren
        1. Properties
            1. Use this buekt to host a webite
        2. Permissions
            1. Bucket Policy -> JSON-Format






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
});
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

            //HIER FEHLER
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