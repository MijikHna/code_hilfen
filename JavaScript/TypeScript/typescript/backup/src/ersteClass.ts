export class ErsteClass {
    private name: string;
    private id: number;

    constructor(name: string, id: number) {
        this.name = name;
        this.id = id;
        console.log("Constructor called");
    }
}