* Canvas - mit JS Graphiken zeichnen

### 1 - Overview of Canvas
#### 1 - Interesting canvas examples
* Bsp-Seiten:
    * CanvasMol - Molekule in Canvas
    * Bomobmo - Zeichen-Programm
#### 2 - The canvas element
* Canvas kann
    1. images
    2. videos
    3. shapes
    4. curves
    5. etc.
* ~ Papier-Teil im Browser.
* man kann Canvases überlagern
* Canvas ist nicht in DOM
    * SVG ist in DOM
* Canvas-Elemente:
    * beginnt *oben links*
    * `<canvas id="" width="" height""> ...</canvas>` 
        * `width`-default ist 300
        * `height`default ist 150
        * `toDataURL(type)` - convertiert in Image -> type = `image/png`
        * `getContext(type)` - ruft Drawing-Kontext für Canvas
* 
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Canvas Example</title>
    <style type="text/css">
        #canvas1 {
            border: dotted 3px gray;
            background-color: lightgrey
        }
    </style>

</head>

<body>
    <h1>Canvas Example</h1>
    <div id="content">
        <p>This document contents our first canvas example</p>

        <canvas id="canvas1" width="400" height="300">
            Your Browser does not support Canvas
        </canvas>

    </div>

</body>

</html>
```
#### 3 - The canvas drawing cotext
* man muss Canvas-Drawing-API benutzen => Referenz zu einer der Canvas Drawing Context benutzen (hier 2D Drawing Context benutzt)
    * WebGL - 3D-Drawing Context
* 
```javascript
var ctx = theCanvas.getContext("2d"); //gibt CanvasRenderingContext2D-Objekt zurück
```
* `ctx` enthält dann mehrere APIs zum zeichnen:
    1. Shapes: 
    2. Operations - wie die Daten gezeichnet werden (Shadows usw.)
    3. Media (Images, Video, DOM-Elemente)
* Bsp:
```javascript
window.addEventListener("load", function () {
    var theCanvas = document.getElementById("canvas1");

    if (theCanvas && theCanvas
        .getContext) { //ob theCanvas nicht unknown und dass es getContext()-Methode hat

        //width + heigt ändern
        theCanvas.width = 150;
        theCanvas.height = 150;


        var ctx = theCanvas.getContext("2d"); //getContext aufrufen um 2d-API abzurufen
        if (ctx) {
            ctx.fillStyle = "lightblue";
            ctx.strokeStyle = "blue";
            ctx.lineWidth = 5;

            ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
            ctx.strokeRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        }
    }
});
```


### Basic Canvas Drawing Techniques
#### 1 - Color and styles
* hat Eigenschaften, die bestimment, wie Objekte gefüllt und umrandent werden.
    * `fillStyle` - default ist *black* (Pattern, CSS-Style)
    * `strokeStyle`
    * `lineWidth` - default ist *1px*
* Farben und Stille zeichen besteht aus zwei Teilen:
    1. Füllart + Randstyle setzen
    2. Zeichen-Operation 
```javascript
window.addEventListener("load", function () {
    var theCanvas = document.getElementById("canvas1");
    if (theCanvas && theCanvas.getContext) {
        var ctx = theCanvas.getContext("2d");
        if (ctx) {
            // Step 1
            ctx.fillStyle = "green";
            ctx.fillRect(20, 20, 100, 100); //x,y,breite, länge
            ctx.strokeStyle = "rgba(0,0,255,1)";
            ctx.lineWidth = 5

            //Step 2
            ctx.strokeRect(20, 20, 100, 100);

        }


    }
});
```
#### 2 - Rectangles
* primitiven Shapes von Canvas:
    * `createRect(x,y,w,h)`
    * `strokeRect(x,y,w,h)`
    * `fillRect(x,y,w,h)`
```javascript
var theCanvas = document.getElementById("canvas2");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {

        // 1 - stroked Rechtangel
        ctx.strokeStyle = "yellow";
        ctx.lineWidth = 5;
        ctx.strokeRect(25, 25, 100, 125);
        //2 - filled Rectangel
        ctx.fillStyle = "blue";
        ctx.fillRect(175, 25, 100, 125);

        //3 - stroked + filled
        ctx.strokeStyle = "red";
        ctx.fillStyle = "yellow";
        ctx.lineWidth = 10;
        ctx.fillRect(325, 25, 100, 125);
        ctx.strokeRect(325, 25, 100, 125);

        //clear a rectangle
        ctx.clearRect(15, 75, 450, 50); //~Radirgummi
    }
}
```
#### 3 - Lines
* Opertationen für Lines:
    1. `moveTo(x,y)` - Pen zu x,y bewegen
    2. `lineTo(x,y)` - Line zeichnen vom Pen
* Eigenschaften - wie Linie gezeichnet wird:
    1. `lineWidth`
    2. `lineCap` - liest oder setzt Ende-Typ der Linie (butt, round, square)
    3. `lineJoin` - wie Linien verbunden werden
    4. `miterLimit` - liest oder setzt Grenze für Linie (default ist 10)
* Pfade zeichnen
    5. `beginPath()` - beginnt Set von mehreren Zeichen-Befehlen als einzelner Pfad - Pfad zeichen
    6. `stoke()` - schließt den offenen Pfad
* gestrichelte Linien:
    * `setLineDash()` - Space-Set erstellen
    * `getLineDash()`
    * `lineDashOffset()`
```javascript
 var theCanvas = document.getElementById("canvas1");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.lineWidth = 0;
        ctx.strokeStyle = "black";
        for (var i = 0; i < 10; i++) {
            ctx.beginPath();
            ctx.lineWidth = i + 1;
            ctx.moveTo(25, 25 + i * 15);
            ctx.lineTo(475, 25 + i * 15);
            ctx.stroke();
        }
    }
}
//2 - lineCap endings
var theCanvas = document.getElementById("canvas2");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.strokeStyle = "green";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, 180);
        ctx.lineTo(450, 20);
        ctx.lineTo(450, 180);
        ctx.stroke();

        //butt-Edning
        ctx.lineWidth = 25;
        ctx.strokeStyle = "black";
        ctx.lineCap = "butt";
        ctx.beginPath();
        ctx.moveTo(50, 50);
        ctx.lineTo(450, 50);
        ctx.stroke();

        //round-Ending
        ctx.lineWidth = 25;
        ctx.strokeStyle = "black";
        ctx.lineCap = "round";
        ctx.beginPath();
        ctx.moveTo(50, 100);
        ctx.lineTo(450, 100);
        ctx.stroke();

        //square
        ctx.lineWidth = 25;
        ctx.strokeStyle = "black";
        ctx.lineCap = "square";
        ctx.beginPath();
        ctx.moveTo(50, 150);
        ctx.lineTo(450, 150);
        ctx.stroke();


    }
}

//3 - Join-Typen
var theCanvas = document.getElementById("canvas3");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {

        ctx.lineWidth = 15;
        ctx.strokeStyle = "black";

        // Join-typ 1
        ctx.lineJoin = "round";
        ctx.beginPath();
        ctx.moveTo(25, 150);
        ctx.lineTo(75, 150);
        ctx.lineTo(125, 50);
        ctx.stroke();
        // Join-typ 1
        ctx.lineJoin = "bevel";
        ctx.beginPath();
        ctx.moveTo(175, 150);
        ctx.lineTo(225, 50);
        ctx.lineTo(275, 50);
        ctx.stroke();
        // Join-typ 1
        ctx.lineJoin = "miter";
        ctx.beginPath();
        ctx.moveTo(325, 150);
        ctx.lineTo(375, 150);
        ctx.lineTo(425, 50);
        ctx.stroke();

    }
}

//4 - Dashed Lines
var theCanvas = document.getElementById("canvas4");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.lineWidth = 15;
        ctx.strokeStyle = "black";

        ctx.setLineDash([5, 10]);
        ctx.beginPath();
        ctx.moveTo(50, 50);
        ctx.lineTo(450, 50);
        ctx.stroke();

        ctx.setLineDash([15, 5]);
        ctx.beginPath();
        ctx.moveTo(50, 100);
        ctx.lineTo(450, 100);
        ctx.stroke();

        ctx.setLineDash([]); //mit leerem Array wird es solid
        ctx.beginPath();
        ctx.moveTo(50, 150);
        ctx.lineTo(450, 150);
        ctx.stroke();

    }
}
```
#### 4 - The Canvas state
* hält fest z.B:
    1. lineWidth
    2. strokeStyle
    3. fillStyle
    4. transformation matrix
    5. clipping region
* man kann diese States im Stack speichern und wieder aufrufen
    * `save()`
    * `restore()`
```javascript
 var theCanvas = document.getElementById("canvas1");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.strokeStyle = "red";
        ctx.fillStyle = "yellow";
        ctx.lineWidth = 10;

        ctx.fillRect(25, 25, 100, 125);
        ctx.strokeRect(25, 25, 100, 125);

        //save
        ctx.save();

        ctx.strokeStyle = "green";
        ctx.fillStyle = "blue";
        ctx.lineWidth = 5;
        ctx.fillRect(175, 25, 100, 125);

        ctx.restore();
        ctx.fillRect(325, 25, 100, 125);
        ctx.strokeRect(325, 25, 100, 125);
    }
}
```

#### 5 - Arcs = Pfade
* Pfad beginnen `beginPath()`
* Pfad umranden `stroke()`
* Pfad füllen `fill()`
* Pfad schließen `closePath()`
* Arcs sind Teile des Kreises
    * `arc(x,y,radius, startAngle, endAngel [, anticlosewise]);`
        * in rad 
        * `arc(75,50,50,0, Math.PI*0.5, false);`
            * `true, false` = in/gegen Uhrzeigersin
#### 6 - Paths
* also mit `beginPath()` beginnen
* Zeichen mit Pen => benutzen
    * `moveTo()`
    * `lineTo()`
```javascript
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.strokeStyle = "blue";
        ctx.fillStyle = "red";
        ctx.lineWidth = 5;

        //Pfad 1    
        ctx.beginPath();
        ctx.moveTo(25, 175);
        ctx.lineTo(50, 25);
        ctx.lineTo(125, 50);
        ctx.lineTo(175, 175);
        ctx.stroke();

        //Pfad 2
        ctx.strokeStyle = "orange";
        ctx.beginPath();
        ctx.moveTo(225, 175);
        ctx.lineTo(250, 25);
        ctx.lineTo(325, 50);
        ctx.lineTo(375, 175);
        ctx.closePath();
        ctx.stroke();

        //Pfad 3
        ctx.strokeStyle = "orange";
        ctx.fillStyle = "yellow"
        ctx.beginPath();
        ctx.moveTo(425, 175);
        ctx.lineTo(450, 25);
        ctx.lineTo(525, 50);
        ctx.lineTo(575, 175);
        ctx.fill();
        ctx.stroke();
    }
}
```

#### 7 - Bezier and quadric curves
+ Bezierkurven => aus 4 Punkten => `bezierCurveTo(cx1, cy1, cx2, cx3, end1, end2 )` => Start, End + zwei ControllPunkte
* Quadratische Kurven => aus 3 Punkten => `quadraticCurveTo(cx,cy, x, y)`  => Start, End + ein ControllPunkt 
* zuerst `moveTo()` benutzen = Startpunkt
```javascript
var theCanvas = document.getElementById("canvas3");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.strokeStyle = "blue";
        ctx.lineWidth = 5;

        //Bezierpunkt
        ctx.beginPath();
        ctx.moveTo(50, 200);
        ctx.bezierCurveTo(50, 100, 200, 100, 200, 150);
        ctx.stroke();
        //Controllpunkte anzeigen
        ctx.strokeStyle = "rgba(0,0,0,25)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.lineTo(50, 200);
        ctx.lineTo(50, 100);
        ctx.lineTo(200, 100);
        ctx.lineTo(200, 100);
        ctx.stroke();

        //Qudratische Kurve
        ctx.strokeStyle = "green";
        ctx.lineWidth = 5;

        //Bezierpunkt
        ctx.beginPath();
        ctx.moveTo(400, 200);
        ctx.quadraticCurveTo(400, 100, 600, 150);
        ctx.stroke();
        //Controllpunkte anzeigen
        ctx.strokeStyle = "rgba(0,0,0,25)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.lineTo(400, 200);
        ctx.lineTo(400, 100);
        ctx.lineTo(600, 150);
        ctx.stroke();


    }
}
```
#### 8 - Drawing text
* ähnlich zu Pfaden
* Text wird dann nicht von CSS beeinflusst
* kann nicht von Screenreader gelesen werden
* `fillText(str, x,y, [maxW])` - 
* `strokeText(str, x,y, [maxW])`
* `measureText(str)` - gibt TextMetrics zurück
* `font` - sowas wie CSS für Canvas-Text
* `textAlign` - `start` (default), `end`, `left`, `right`, `center` 
```javascript
var theCanvas = document.getElementById("canvas3");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        var theString = "Drawing Text in Canvas";
        var startX = 20;

        //Teil 1
        ctx.font = "25px Georgia";
        ctx.fillText(theString, startX, 60);

        ctx.fillStyle = "blue";
        ctx.fillText(theString, startX, 100);

        //Teil 2
        ctx.font = "32px Verdana";
        ctx.fillStyle = "yellow";
        ctx.strokeStyle = "rgba(0,255,0,0.8)";
        ctx.fillText(theString, startX, 160);
        ctx.strokeText(theString, startX, 160);

        // Unterstrick, dabei mit MeasureText messen wie lang der String ist
        var textW = ctx.measureText(theString);
        ctx.beginPath();
        ctx.strokeStyle = "black";
        ctx.moveTo(startX, 170);
        ctx.lineTo(startX + Math.round(textW.width), 170);
        ctx.stroke();
    }
}
```
### 3 - Complex Canvas Drawing
#### 1 - Drawing shadows
* Shadow Properties
    * `shadowColor`
    * `shadowOffsetX`
    * `shadwoOffsetY`
    * `shadowBlur`
#### 2 - Using patterns
* Pattern und Gradient für `fillStyle` und `strokeStyle` benutzen
* Patterns kann man aus Image, Videos (current Frame), anderen Canvases erstellen 
    * Pattern kann man in x und y Richtung repeaten
* `createPattern(elem, repeat)` - `no-repeat`, `repeat`, `repeat-x`, `repeat-y`
```javascript
var theCanvas = document.getElementById("canvas1");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        //Bsp 1 - Image
        var patImg = new Image();
        patImg.onload = function () {
            ctx.fillStyle = ctx.createPattern(patImg, "repeat");
            ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        };
        patImg.src = "../../hand.png"

        //Bsp 2 - aus Video
        /*
        setTimeout(function () {
            var vid = document.getElementById("vidEl");
            var theCanvas = document.getElementById("canvas1");
            var ctx = theCanvas.getContext("2d");
            var vidPat = ctx.createPattern(vid, "repeat");
        }, 5000); //5 sec Warten, dann den Frame aus dem Video nehmen
        ctx.fillStyle = vidPat;
        ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        */
        //Bsp 3 - Pattern aus anderem Canvas
        var patCanvas = document.getElementById("patCanv");
        var patCtx = patCanvas.getContext("2d");
        patCtx.strokeStyle = "red";
        patCtx.lineWidth = 2;
        patCtx.beginPath();
        patCtx.moveTo(0, 0);
        patCtx.lineTo(25, 25);
        patCtx.stroke();

        var strokePat = ctx.createPattern(patCanvas, "repeat");
        ctx.strokeStyle = strokePat;
        ctx.lineWidth = 25;
        ctx.strokeRect(50, 50, 200, 200);
    }
}
```
#### 3 - Using gradients
* es gibt lineare und radiale Gradients
* Erstellen = 2 Schritte:
    1. lieare oder radialen Gradient erstellen
    2. Color stops hinzufügen
* Gradient kann dann in `stroke` oder `fill` benutzt werden
* Linear
    * 2 Points (von -> bis)
    * `createLinearGradient(x0,y0, x1, y1);` - return den Gradient zurück
* Radial:
    * innerer Kreis: Punkt + Radius
    * äußerer Kreis: Punkt ü Radius
    * `createRadialGradient(x0,y0, r0, x1,y1, r1);` - return den Gradient zurück
* `addColorStop(position, color);` position 0.0 -> 1.0; color = CSS-Style
```javascript
var theCanvas = document.getElementById("canvas1");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        var linGrad = ctx.createLinearGradient(20, 20, 20, 280);
        linGrad.addColorStop(0, "#f00");
        linGrad.addColorStop(0.5, "#00f");
        linGrad.addColorStop(1.0, "#0f0");

        ctx.fillStyle = linGrad;
        ctx.fillRect(20, 20, 200, 260);
        ctx.lineWidth = 3;
        ctx.strokeRect(20, 20, 200, 260);

        var radGrad = ctx.createRadialGradient(525, 150, 20, 525, 150, 100);
        radGrad.addColorStop(0, "#f00");
        radGrad.addColorStop(0.5, "#00f");
        radGrad.addColorStop(1.0, "#0f0");

        ctx.fillStyle = radGrad;
        ctx.beginPath();
        ctx.arc(525, 150, 100, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();

    }
}
```
#### 4 - Images and video
* man kann Images und Video programmatisch rendern
+ Image können von Videos kommen
* drei Funktionen:
    * `drawImage(src, x,y)`
    * `drawImage(src, x,y, w,h);`
    * `drawImage(src, sx,sy, sw, sh, dx,dy,dw,dh)` - ~ Teil des Bildes kopieren
#### 5 - Clipping paths
* ~ mask
* = nur in einem Bereich von Canvas etwas zeichen, dabei Bereich mit Canvas festlegen und `clip()` aufrufen
* definiert Region, außerhalb welcher Zeichnung wird "clipped", also keinen Effekt haben wird
* Am Anfang ist ganzes *Canvas* ist clipping Pfad
* Jeder Pfad kann clipping Pfad sein
* `clip()` - erstellt neuen clipping Pfad, indem es Intersectionen der momentanen Clipping region und aktuellen Pfad berechnet. Und neue Clipping Region ersetzt die alte
* nutztlich, wenn man dynamische Änderungen bestimmter Bereiche machen will
```javascript
var theCanvas = document.getElementById("canvas1");
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        var scrImg = document.getElementById("img1"); //kann auch display:none haben

        //cicle clipping path erstellen
        ctx.arc(ctx.canvas.width / 2, ctx.canvas.height / 2, 150, 0, 2 * Math.PI);
        ctx.clip();
        //arbitrary clipping path erstellen
        ctx.beginPath();
        ctx.moveTo(105, 200);
        ctx.lineTo(250, 25);
        ctx.lineTo(525, 20);
        ctx.lineTo(475, 285);
        ctx.clip();

        //Image ins Canvas rendern
    }
}
```

### 4 - Advanced Drawing APIs
#### 1 - Using translate
* Transformationen -> beeinflussen canvas drawing Operationen
* kontorllieren, wie gezeichnet wird. 3 Basic Tranformationen
    1. Translate
        * `translate(x,y)` = Null-Punkt verschieben
        * Benutzt z.B wenn man mehrere gleiche Objekte in bestimmten Abständen zeichnen muss 
    2. Scale
    3. Rotate
    4. man kann auch eigene Transformationen erstellen
* Ablauf: Transformation -> Zeichnen
* Transofmationen sind additiv
```javascript
window.addEventListener("load", function () {
    var theCanvas = document.getElementById("canvas1");
    if (theCanvas && theCanvas.getContext) {
        var ctx = theCanvas.getContext("2d");
        if (ctx) {
            //Unterkapitel 1 - Using translate
            ctx.fillStyle = 'blue';
            ctx.fillRect(0, 0, 100, 50)

            ctx.translate(ctx.canvas.width / 2, ctx.canvas.height / 2);
            ctx.fillRect(0, 0, 100, 50)
        }
    }
});
```
#### 2 - Using scalling
+ `scale(x,y)` - in x,y-Richtungen um x,y skallieren
```javascript
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        //ctx.translate(0, 0);
        ctx.translate(-ctx.canvas.width / 2, -ctx.canvas.height / 2);
        ctx.fillStyle = 'yellow';
        ctx.fillRect(50, 50, 100, 50)

        ctx.save();
        ctx.scale(2, 2);
        ctx.fillRect(125, 50, 100, 50);
        ctx.restore();
    }
}
```
+  ist auch additiv 
    * enweder `ctx.scale(2, 2);` oder `save()` und `restore()` benutzen
#### 3 - Using rotation
* in *rad* rotieren
* Rotationen finden statt um den Null-Punkt
* `rotate(angle)`
```javascript
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.fillStyle = 'red';

        ctx.rotate(0.5);
        ctx.fillRect(150, 100, 100, 50);

        //Linine in Kreisform
        ctx.translate(ctx.canvas.width / 2, ctx.canvas.height / 2);
        //10 Grad berechnen
        var radian = (Math.PI / 180) * 10;
        for (var degrees = 0; degrees < 360; degrees += 10) {
            //da additiv ist
            ctx.rotate(radian);

            ctx.beginPath();
            ctx.moveTo(-100, 0);
            ctx.lineTo(100, 0);
            ctx.stroke();

        }
    }
}
```
#### 4 - Custom transformations
* werden als Matrizen definiert
```
x`   ace x
y` = bdf y
1    001 1
```
* `transform(a,b,c,d,e,f)`  - addiert die Transformation zur aktuellen Transformation
* `setTranform(a,b,c,d,e,f)`  - setzt Tranformation zur speziellen Transformation (z.B setzt zur Ausgangstransformation)
    * Param sind werden aud der Matrix
```javascript
if (theCanvas && theCanvas.getContext) {
    var ctx = theCanvas.getContext("2d");
    if (ctx) {
        ctx.fillStyle = 'orange';
        ctx.fillRect(150, 100, 50, 25);
        // Null-Punkt zur Mitte begeben
        // 1 0 tx
        // 0 1 ty
        // 0 0 1
        var tx = ctx.canvas.width / 2;
        var ty = ctx.canvas.height / 2;
        ctx.save();
        ctx.transform(1, 0, 0, 1, tx, ty);
        ctx.fillRect(150, 100, 50, 25);
        ctx.restore();

        //skew-Transform
        // 1 sx 0
        // sy 1 0
        // 0 0 1

        //skew in Y 
        var sx = 0;
        var sy = 0.3;
        ctx.fillStyle = "aqua";
        ctx.setTransform(1, sy, sx, 1, 0, 0);
        ctx.fillRect(200, 20, 100, 50);

        //skew in X
        var sx = 0.3;
        var sy = 0;
        ctx.fillStyle = "aqua";
        ctx.setTransform(1, sy, sx, 1, 0, 0);
        ctx.fillRect(300, 220, 100, 50);
    }
}
```
#### 5 - Compositing and globalAlpha
#### 6 - Manipulating raw pixels

### 5 - Practical Examples
#### 1 - Building an Image slideshow
#### 2 - Using smooth transitions
#### 3 - Basic animation
#### 4 - Double-bufferd animation