meistens ist es Kombination von `width`, `height`, `top`, `right`, `left`, `border`, `bottom`, `transform`, und `:before`, `:after`. Es gibt auch ein paar moderne CSS-Eigneschaften: `shape-outside`, und `clip-path`

#### Rechtecke:
```css
#square{
    background: lightblue;
    width: 100px;
    height: 100px;
}
```

#### Kreis:
man muss `border-radius` setzen
```css
#circle{
    background: lightblue;
    border-radius: 50%;
    width: 100px;
    height: 100px;
}
```

#### Dreiecke
man muss `border` setzen, `widht` und `height` zu 0 setzen. Eigentliches `widht` wird von `border` festgelegt. Und border-edges sind 45%. Dann ein Border zu Farbe setzen und anderen Borders transparent machen.
```css 
/*Richtung nach oben */ 
#triangle {
    width: 0;
    height: 0;
    border-left: 40px solid transparent;
    border-right: 40px solid transparent;
    border-bottom: 80px solid lightblue;
}
```

```css 
/*Richtung nach links */ 
#triangle {
    width: 0;
    height: 0;
    border-left: 40px solid transparent;
    border-right: 80px solid lightblue;
    border-bottom: 40px solid transparent;
}
```

Da Element aber eigentlich immer noch Rechteck werden Elemente um das Shape rechteckig herumfließen. Als Lösung kann man `shape-outside` benutzen. Definiert Shape, um dass der Text/Elemente herumfließen. Dazu kann noch `inset()`, `circle()`, `ellipse()`, `polygon()`. Oder man kann auch `clip-path` verwenden.  
Hier kann man weiter lesen: `https://developer.mozilla.org/en-US/docs/Web/CSS/shape-outside`.
`inset()` - man kann Rechteck-Shape damit erstellen und Werte angeben, wie der Text herum fließen soll z.B. `inset(20px 5px 30px 10px)` oder `inset(top right bottom left)`
```css
/*Rechteck*/
 #square {
    float: left;
    width: 100px;
    height: 100px;
    shape-outside: inset(20px 5px 30px 10px);
    shape-outside: inset(20px 5px 30px 10px round 50px);
    background: lightblue;
 }
```
```css
/*Kreis*/
 #square {
    float: left;
    width: 300px;
    height: 300px;
    margin: 20px;
    shape-outside: circle();
    clip-path: circle();
    background: lightblue;
 }
```
Dabei wird `clip-path` mit dem gleichen Wert wie `shape-outside` gesetzt   
`cirlce()` kann zwei Parameter haben: 1 = Radius, 2 = Position => legen Zentrum des Kreises. Bsp Halbkreis:
```css
#circle {
    float: left;
    width: 150px;
    height: 150px;
    margin: 20px;
    shape-outside: circle(50% at 30%);
    clip-path: circle(50% at 0%);
    background: lightblue;
}
```
Radius auf 50% setzen und Zentrum um 30% shiften. Das Wort `at` muss zwischen Radius und position stehen.
```css
#ellipse {
    float: left;
    width: 150px;
    height: 150px;
    margin: 20px;
    shape-outside: ellipse(20% 50%);
    clip-path: ellipse(20% 50%);
    background: lightblue;
}
```
```css
#polygon {
    float: left;
    width: 150px;
    height: 150px;
    margin: 20px;
    shape-outside: polygon(
        0 0,
        100% 0,
        100% 20%,
        60% 20%,
        60% 100%,
        40% 100%,
        40% 20%,
        0 20%
    );
    clip-path: polygon(
        0 0,
        100% 0,
        100% 20%,
        60% 20%,
        60% 100%,
        40% 100%,
        40% 20%,
        0 20%
    );
    background: lightblue;
}
```
Mit Polygon kann eigene Shapes erstellen.  
Man kann auch Bilder als Shapes benutzen
shape-outside: polygon(
```css
#ellipse {
    float: left;
    width: 150px;
    height: 150px;
    shape-outside: url("./src/moon.png");
}
```