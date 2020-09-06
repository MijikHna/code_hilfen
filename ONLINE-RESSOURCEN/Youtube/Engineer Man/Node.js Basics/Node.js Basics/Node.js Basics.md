### Video 1
* Node.js neue API, die der Browser nicht hat -> z.B Network, Files usw.
* 
### Video 2
* ES2015 - ist Std für 
    * Neuer Features:
        * Arrow-Funktios: `num => {...}`oder `(num1, num2) => {...}`
        * { } - Variablen-Inkapsulation
        * *var* vs *let*
        * default Funkt-Param
        * var. Param-Liste `funktname(...,a,b)`, wobei *...* kann überall stehen.
        * Obj Property Shorthand - 
        * Computed Obj Key - `var name = "something"; var object = { "something": "cool"};`
        * Methode Notation Obj - `var methods = { funkt1(){..}, funkt2(){..}};
        * Array-Destruction: `var nums = [1,2,3]; var [one, two, three] = nums;` 
        * Obj-Destruction
        * Klassen
        * Generatoren: Benutzung von `yeald`
### Video 3 - Installation
* Installtion
    * von nodejs.org herunterladen Linux Binarys
    * `tar xf node.. -C ..
    * in *bin* sind dann die Executabels -> diese in den PFAD aufnehmen
* Running Programm
    * `node test.js`
    * Stärke von Node.js ist Networking:
    ```javascript
    retrun http
        .createServer((req, res) => {
            res.end("test");
        })
        .listen(8080);
    ```
    * wenn Node.js auf Appache/Nginx installiert wird, dann schauen Apacha/Nginx, ob sie selbst den Request behandeln können, wenn nicht, dann wird Node.js es ausführen (z.B hier an oben erstellen "http-Server")