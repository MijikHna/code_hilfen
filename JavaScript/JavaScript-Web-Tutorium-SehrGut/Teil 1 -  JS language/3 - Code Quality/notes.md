### 3 - Code Quality
#### 1 - Debugging Chrome
* mit `debugger` im Code kann man direkt BreakPoint setzen für Chrome Debugger
* Chrome Debugger: 
    1. Watch = Werte der Varialben
    2. Call Stack = nested function calls
    3. Scope = current Variables
#### 2 - Codin Style
* Bsp wie man Linter in package.json einstellen kann
#### 3 - Comments:
* Bsp guter Kommentar:
```js
/**
 * Returns x raised to the n-th power.
 *
 * @param {number} x The number to raise.
 * @param {number} n The power, must be a natural number.
 * @return {number} x raised to the n-th power.
 */
```
* Doku zu JavaScript Kommentaren: https://en.wikipedia.org/wiki/JSDoc
* Tool das aus Dokumentations-Kommentaren Dokumentation erstellt: https://github.com/jsdoc3/jsdoc bzw. http://usejsdoc.org/
* Eventuall müssen Kommentare sagen **Why is the task solved exactly this way?**
* Fazit: folgendes sollte man kommentieren
    * Overall architecture, high-level view.
    * Function usage.
    * Important solutions, especially when not immediately obvious.
#### 5 - Automated testing with Mocha
* Development Flow von BDD - Behaviour Driven Development = zuerst Test, dann Implementation
    1. An initial spec is written, with tests for the most basic functionality.
    2. An initial implementation is created.
    3. To check whether it works, we run the testing framework Mocha (more details soon) that runs the spec. While the functionality is not complete, errors are displayed. We make corrections until everything works.
    4. Now we have a working initial implementation with tests.
    5. We add more use cases to the spec, probably not yet supported by the implementations. Tests start to fail.
    6. Go to 3, update the implementation till tests give no errors.
    7. Repeat steps 3-6 till the functionality is ready.
* Bsp: 
    * Benutzt:
        1. Mocha = Core Framework zum Testen (`describe`, `it`)
        2. Chai = Library mit `assert` + `toBe...`
        3. Sinon = Library zum `spyOn`
* One Test checks One Thing
#### 6 - Polyfills
* Babel = Transpiler = rewrites aktuellen JS-code zu früherer Version
+ Babel besteht aus zwei Teilen
    1. Transpiler = Programm, das Code rewritet. z.B WebPack führt Transpiler automatisiert aus = Integriert in Development Prozess.
    2. Polyfill = A script that updates/adds new functions is called “polyfill”. It “fills in” the gap and adds missing implementations. Zwei wichitgsten Polifills:
        1. `core.js`
        2. `polyfill.io`