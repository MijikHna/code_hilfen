* es gibt 5 Loop Typen in JS:
    1. for
    2. for/in - durch Elemente des Obj iterieren
    ```js
    var myObj = {
        name: "NameX",
        type: "typeX",
        color: "colorX",
    };

    for(let loopMe in myObj){
        //
    }
    ```
    3. for/of - durch Array iterieren
    ```js
    var myIterable = ["eins", "zwei", "drei"];
    for(let myObj of myIterable){
        //
    }
    ```
    4. while
    5. do/while