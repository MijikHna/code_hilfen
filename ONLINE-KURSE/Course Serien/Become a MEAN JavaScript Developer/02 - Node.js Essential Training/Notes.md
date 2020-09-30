# Node.js Essential Training

## 3 - Node Globlas

### 8 - Report progress with setInterval

```js
const waitTime = 5000;
const waitInterval = 500;
let currentTime = 0;

const incTime = () => {
  currentTime += waitInterval;
  // prozent berechnen
  const p = Math.floor((currentTime / waitTime) * 100);
  // die letzte Zeile von stdout löschen
  process.stdout.clearLine();
  // den zeiger auf position 0 setzen
  process.stdout.cursorTo(0);
  // Message printen => sieht dann so aus als ob nur die Anzeige von % sich ändert
  process.stdout.write(`waiting ... ${p}%`);
};

console.log(`setting a ${waitTime / 1000} second delay`);

const timerFinished = () => {
  clearInterval(interval);
  process.stdout.clearLine();
  process.stdout.cursorTo(0);
  console.log("done");
};

// zuerst prozentFunk aufrufen dann doneFunk aufrufen
const interval = setInterval(incTime, waitInterval);
setTimeout(timerFinished, waitTime);
```

## 4 - Node Moduls

### 1 - Core Moduls

* kommen direkt mit Node.js

```js
const path = require("path"); // Modul importieren als path-Var
const util = require("util"); // powerfull console printet mit Date
const v8 = require("v8");

const { log } = require("util"); // gezieltes importieren
const { getHeapStatistics } = require("v8");

const dirUploads = path.join(__dirname, "www", "files", "uploads");
console.log(dirUploads);

util.log(v8.getHeapStatistics()) // Heap-Memory-Usage für Node.js-App printen

util.log(__filename)
util.log("The name of current");

log(getHeapStatistics());
```

### 2 - Collect info with readline

```js
const readline = require("readline");

// interface für in/out erstellen
// rl ist dann readLine-Interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// .question() ist Funktion von rl-Interface
rl.question("How do you like Node? ", answer => {
  console.log(`Your answer: ${answer}`);
});

```

### 3- Write a file

```js
// readline importieren
const readline = require("readline");

// readline-Inteface definieren
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const questions = [
  "What is your name? ",
  "Where do you live? ",
  "What are you going to do with node js? "
];

//Def von collectAnswers()
// done ist call-Back-Funktion, wobei done wird beim Aufruf als Arrow-Funk angegeben
const collectAnswers = (questions, done) => {
  // Definitionen der Funktion
  const answers = [];
  const [firstQuestion] = questions;

  // Funktion questonAnswered(answer){}
  const questionAnswered = answer => {
    answers.push(answer);
    if (answers.length < questions.length) {
      //sozusagen rekursive-Call von rl.question mit nächster Frage und callwieder rekursive-Call von questionAnswered()
      rl.question(questions[answers.length], questionAnswered);
    } else {
      done(answers);
    }
  };

  // erster Aufruf von rl.question mit erster Frage + Callback-Funkt questionAnswered()
  rl.question(firstQuestion, questionAnswered);
};

// questions and answers sind parameter, wobei für answers Funktion aufgerufen wird
// call von collectAnswers()
collectAnswers(questions, answers => {
  console.log("Thank you for your answers. ");
  console.log(answers);
  process.exit();
});
```

### 4 - Export custom modules

```js myModule.js
let count = 0;

const inc = () => ++count;
const dec = () => --count;

const getCount = () => count;

module.exports = {
  inc,
  dec,
  getCount
};

module.exports = "Lala"; // exportier Wert der hier angegeben wird.
```

```js app.js
const name = require('./myModule'); // wenn man nur module.exports = "lala" hat wird hier einfach Lala gespeichert
console.log(name);

const counter = require('./myModule');
counter.inc();
counter.inc();
counter.inc();
counter.dec();

console.log(count.getCount());

const { inc, dec, getCount } = require("./myModule");

inc();
inc();
inc();
dec();

console.log(getCount());
```

### 5 - Create a module

```js lib/collectAnswers.js
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// die Funktion exportieren (die früher collectAnswers() hieß)
module.exports = (questions, done = f => f) => { // hier mit done = f => f wird eine default-Funk angegeben, die einfach übergebene Params zurückliefert
  const answers = [];
  const [firstQuestion] = questions;

  const questionAnswered = answer => {
    answers.push(answer);
    if (answers.length < questions.length) {
      rl.question(questions[answers.length], questionAnswered);
    } else {
      done(answers);
    }
  };

  rl.question(firstQuestion, questionAnswered);
};
```

```js questions.js
const collectAnswers = require("./lib/collectAnswers");

const questions = [
  "What is your name? ",
  "Where do you live? ",
  "What are you going to do with node js? "
];

collectAnswers(questions, answers => {
  console.log("Thank you for your answers. ");
  console.log(answers);
  process.exit();
});
```

### 6 - Custom events with the EventEmitter

* Node.js EventEmitter = pub-sub-Design-Pattern

```js events.js
const events = require("events");

// EventEmitter-Instanz erstellen
const emitter = new events.EventEmitter();


// mit on() - Handler definieren on(eventNamen, callback())
emitter.on("customEvent", (message, user) => {
  console.log(`${user}: ${message}`);
});

// Handler für stdin schreiben "data" = Input-Event data => Eingaben auf der Console
process.stdin.on("data", data => {
  const input = data.toString().trim();
  if (input === "exit") {
    emitter.emit("customEvent", "Goodbye!", "process");
    process.exit();
  }
  // Event mit Namen "customEvent" raisen
  emitter.emit("customEvent", input, "terminal");
});
```

### 7 - Improve a module with EventEmmiter

```js lib/collectAnswers.js
const readline = require("readline");
const { EventEmitter } = require("events");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

module.exports = (questions, done = f => f) => {
  const answers = [];
  const [firstQuestion] = questions;
  const emitter = new EventEmitter(); // Emitter-Instanz

  const questionAnswered = answer => {
    emitter.emit("answer", answer); // Emitter-Event "answer" raisen = wenn Question beantwortet wird
    answers.push(answer);
    if (answers.length < questions.length) {
      rl.question(questions[answers.length], questionAnswered);
    } else {
      emitter.emit("complete", answers); //Emitter-Event "complete" wenn alle Ansswers da sind
      done(answers);
    }
  };

  rl.question(firstQuestion, questionAnswered);

  return emitter; // Emitter returnen d.h. beim module.exports
};
```

```js question.js (wird auch ohne Veränderungen funktionieren)
const collectAnswers = require("./lib/collectAnswers");

const questions = [
  "What is your name? ",
  "Where do you live? ",
  "What are you going to do with node js? "
];

const answerEvents = collectAnswers(questions); //import

// Handler für "answer"-Event
answerEvents.on("answer", answer =>
  console.log(`question answered: ${answer}`)
);
//Handler für "complete"-Event
answerEvents.on("complete", answers => {
  console.log("Thank you for your answers. ");
  console.log(answers);
});
// zweiten Handler für "complete"-Event
answerEvents.on("complete", () => process.exit());
```

## 5 - File System Basics 

* braucht fs-Moduel

### 1 - List directory files

```js
const fs = require("fs");

// Inhalt des Orders ./assets lesen (wird syncron ausgeführt)
const files = fs.readdirSync('./assets');
console.log(files)

// das gleiche aber als Promise bzw. asyncron. Nach dem lesen wird callback gecallt
fs.readdir("./assets", (err, files) => {
  if (err) {
    throw err;
  }
  console.log("complete");
  console.log(files);
});

console.log("started reading files");
```

### 2 - Read files

```js
const fs = require("fs");

const text = fs.readFileSync("./lala.md", "UTF-8");
console.log(text);

fs.readFileSync("./lala.md", "UTF-8", (err, text) => {
  console.log("file contents read");
  console.log(text);
});

fs.readFile("./assets/alex.jpg", (err, img) => {
  if (err) {
    console.log(`An error has occured: ${err.message}`);
    process.exit();
  }
  console.log("file contents read");
  console.log(img);
});
```

### 3 - Write and append files

### 4 - Directory creatiorn

### 5 - Append files

### 6 - Rename and remove files

## 6 - Files and Streams

### 1 - Readable file stream

### 2 - Writeable file stream

### 3 - Create child process with spawn
