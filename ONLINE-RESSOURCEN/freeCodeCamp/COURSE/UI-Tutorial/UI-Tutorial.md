Was wird gelernt:
* White Space - Leerer Platz zwishcen den Elementen
* Color - 
+ Contrast
+ Scale
+ Alignment - 
+ Typography
+ Visual Hierarchy - besitmme Elemente sind wichiger => wie kann man sie herausheben

### 1 - White Spaces
* leere Space zwischen den Elementen.
```html
<html>
    <head>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        <div class="card">
            <h1>My Title</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
        <div class="card secondary">
            <h1>My Title</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
    </body>
</html>
```

```css
html, body {
    margin: 0;
    padding: 0;
    height: 100vh;
}

body {
    background: #eeeeee;
    display: grid;
    place-items: center;
    grid-template-columns: repeat(2, auto); /* hier ist Font-Size gesetz 16px ist defualt */
}

.card {
    background: white;
    padding: .2em;
    width: 60%;
}

h1, p {
    margin: 0;
}
h1 {
    font-size: 1.4em;
}
p {
    font-size: .8em;
}

/* erwetiertungen */
.secondary {
    padding: 1em;
    padding: 1.5em;
}

.secondary h1 {
    margin-bottom: 0.5em;
}

.secondary p {
    line-height: 1.5em; /* White Space der Zeilen auch Leading genannt*/
}
```
* Empfehlung em zu benutzen
### 2 - Alignment
```html
<html>
    <head>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        <div class="container">
            <a href="#" class="logo">SomeCompany</a>
            
            <h1>Identifying Strong Alignment</h1>
            
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
            
            <a href="#" class="cta">Get Aligned</a>
        </div>
    </body>
</html>
```
```css
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap');

html, body {
    margin: 0;
    padding: 0;
    font-family: 'Montserrat';
}

body {
    background-color: #444E5C;
    border-left: 17px solid rgba(0,0,0,.2);
    height: 100vh;
}

.container {
    width: 80%;
    margin: 0 auto;
}

a { 
    color: white;
    text-decoration: none;
}
a.logo {
    display: block;
    padding-top: 1em;
    font-weight: bold;
    text-transform: uppercase;
    font-size: .8em;
}

h1 {
    margin: 2em 0 1em .5em;
    color: white;
}

p {
    color: #B2CEF2;
    line-height: 1.4em;
    font-size: .9em;
}

a.cta {
    display: inline-block;
    background: #5099FF;
    padding: .8em 1.7em;
    font-weight: bold;
    border-radius: 2em;
    transform: translateX(50%);
    margin-top: 1.5em;
}

/* Show Column: */

.container {
    border-left: 1px solid rgba(255,255,255,0);
}

/* Improvements

h1 { margin-left: 0; }
a.cta { transform: none; }
a.logo { text-align: left; }

*/
```

### 3 - The Card Challenge

### 4 - Contrast

### 5 - Scale

### 6 - Fix an ugly UI

### 7 - Typography

### 8 - Color

### 9 - The Colors Challange

### 10 - Visual Hierarchy

### 11 - Visual Hierarchy Challenge

### 12 - Final Challenge 