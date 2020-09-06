* man kann in JS Array mit Funktion `sort()` sortieren. Da aber Daten unterschiedlich sind => ist `sort()` allein nicht genug.
### Bsp 1 - Array von Strings
```js
const teams = ['Real Madrid', 'Manchester Utd', 'Bayern Munich', 'Juventus'];

function sortArrayOfStrings(){
    return teams.sort(); //ascending von A nach Z sortieren
}

function sortReverseArrayOfStrings(){
    return teams.reverse();
}
```
### Bsp 2 - Array of Numbers
+ per Default sortiert `sort()` nach ASCII-Tabelle => für Zahlen muss man eigenes `sort()` schreiben
```js
const numbers = [3, 23, 12];

numbers.sort(); // --> 12, 23, 3

function sortNumbersACS(a,b){
    return a - b;
}

function sortNumbersDCS(a,b){
    return b - a;
}

function sortArrayOfNumbers1(){
    return numbers.sort(sortNumber);
}

function sortArrayOfNumbers2(){
    return numbers.sort(sortNumbersDCS);
}
```

