//Strings
const teams = ['Real Madrid', 'Manchester Utd', 'Bayern Munich', 'Juventus'];

function sortArrayOfStrings() {
    return teams.sort() //ascending von A nach Z sortieren
}

function sortReverseArrayOfStrings() {
    return teams.reverse()
}

//Numbers
const numbers = [3, 23, 12];

numbers.sort(); // --> 12, 23, 3

function sortNumbersACS(a, b) {
    return a - b;
}

function sortNumbersDCS(a, b) {
    return b - a;
}

function sortArrayOfNumbers1() {
    return numbers.sort(sortNumbersACS)
}

function sortArrayOfNumbers2() {
    return numbers.sort(sortNumbersDCS);
}