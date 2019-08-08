### 1-4: Funktionen Objekte Methoden Schleifen
#### Kapitel 2:
* js in Html einbinden:
    * `<script src="nameJS-Script.js"></script>`
```javascript
var today=new Date();
var hourNow=today.getHours();

var el=document.getElementById("id1");
el.textContent="text";

var message="<a href=\"nameHtml.html\"> Text <\/a>";
el.innerHTML=message; 

el.className=true; //className kann true/false annehmen => z.B für CheckBoxen => checked, unchecked
var array1=[1,2,3];
var array2=new Array(1, 2);
array1[i];
array1.item(i); //nur lesender Zugriff
array1.length;
```

* Funktionen:
```javascript
function funktName1(){
}
funktName1();
function funktName2(var1, var2){
}
funktName2(x, y);
```
* unmittelbar aufgerufene Funkt:
```javascript
var varF1=(function(){

}());
```
* anonyme Funkt
```javascript
var varF2=function(var1, var2){
    return var1*var2;
};
var var3=varF2(x, y);
```
* Objekte:
```javascript
//1
var obj1={
    var1: "text1",
    var2: 1,
    varArray: ["tex1", "text2"],
    varF1: function(){
        return 10;
    }
};
obj1.var1;
obj1["var1"];
obj1.varF1();
//2
var obj2=new Object(); //oder obj2={}
obj2.var1="text";
obj2.var2=10;
obj2["var2"]=20;
obj2.varF1=function(){
    return 10;
};
delete obj2.var2; //Eigenschafte var2 von obj2 löschen => nicht mehr vorhanden im ojb2
```
* Klasse-Def erstellen => mehrre Obj. erstellbar
```javascript
function Klasse1(var1, var2, var3){
    this.var1=var1;
    this.var2=var2;
    this.var2=var3;
    this.varF1=function(){
        return this.var1;
    }
}
objK1=new Klasse1("text1", 10, 20);
objK2=new Klasse1("text2", 11, 21);
//man kann dem Objekt weitere Eigenschaften/Methoden hinzufügen 
obj2.var10=true;
obj2.var11=10;
```
* `this`:
```javascript
//1 - Funktion auf der Obersten-Ebne erstellt = globale Funktion => this=Obj. window Bsp:
function winSize(){
    var width=this.innerWidth; //this verweist dann auf Obj, in dem die Funkt. erstellt wurde
    var height=this.innerHeight;
    return [height, width];
}
//globale Variablen sind Eigenschaften von width-Obj. Bsp:
var width=100;
var showWidth=function(){
    document.write(this.width);
}
//Methode innerhalb eines Obj: => this zeigt auf diesen Obj + man kann this oder Obj-Namen verwednen
//etwas komplizierter:
var shape={width: 300}; //Obj erstellt
var showWidth=function(){
    return this.width;
};
shape.getWidth=showWidth; //dem Obj die Methode zugewiesen
shape.getWidth(); //=> this. zeigt auf Obj-Variable
```

* `varX;` - Ohne Schlüsselwort var wird globale Variable erstellt

* Direkt Obj erstellen sinnvoll: 1) Daten zwischen Anwendungen speichern/übertragen, 2)für globale Obj. und für Konfigurations-Obj, die Infos für die Seite einrichten.
    * integrierte Obj=Browser-Obj:
        1. Browser Object Model=Objekte, die das aktuelle Fenster/Tab darstellen => z.B Browserverlauf, Bildschrim des Geräts
        2. DOM
        3. Globale JavaScript-Objekte = für Dinge, die JS braucht, um Modell zu erstellen z.B Objekte für Datum und Zeit
    * ObjektModell = Gruppe von Objekten
        * zu 1): Window -> Document=aktuelle Webseite, History=Seite im Browser-Verlauf, Location=location-URL der aktuellen Seite, Navigator=info über den Browser, screen=Info über die physische Anzeige Bsp;
        ```javascript
        window.print();
        window.screen.width;
        ```
        * zu 2):`document.lastModified;` - wann die Seite zum letzten Mal aktualisert wurde
        * zu 3): *String, Number, Boolean, Date, Math, Regex*=für Mustervergleiche bei den Strings:
        ```javascript
        var1.toUpperCase();
        Math.PI();
        ```
    * zu 1);
    ```javascript
    window.innerHeight; //Höhe des Fensters, ohne Browserrahmen
    window.innerWidth; //Breite des Fensters
    window.pageXOffset; //Entfernung, um die das Dokument hor. gescrollt wurde
    window.pageYOffset; //Entfernung, um die vert. gescrollt wurde
    window.screenX; //X-Koordinate des Zeigers relativ zum oberen linken Rand
    window.screenY; //Y-Koordiante des Zeigers relativ ...
    window.location //URL-des window-Obj
    window.document //Verweis auf das document-Obj für zurzeit im Fenster enthaltene Seite
    window.history //Verweis auf history-Obj. mit den Angaben über die Seite, die im aktuellen Fenster oder Tab betrachtet worden sind
    window.history.length; //Anzahl der Seiten im Verlauf
    window.screen //Verweis auf screen-Obj
    window.screen.width //width des screen-Obj
    window.screen.height //heigth des screen-Obj
    window.alert() //erstellt Dialogfeld mit Meldung
    alert() //ist das gleiche, das window ist Std-Obj.
    window.open() //Öffnet neues Fenster mit übergebener URL
    window.print() //teilt dem Browser mit, dass User den Inhalt der Seite drücken möchte
    ```
    * zu 2) oberste Obj in DOM ist document
    ```javascript
    document.title; //Titel des Dokuments
    document.lastModified; //Datum an dem Dokument geändert wurde
    document.URL //String mit der URL des Dokuments
    document.domain //gibt Domäne des aktuellen Dokuments zurück
    //Obj: String: = globales Obj.
    var stringVar="Test";
    stringVar.length;
    stringVar.toUpperCase();
    stringVar.toLowerCase();
    stringVar.charAt(i);
    stringVar.indexOf("e"); 
    stringVar.indexOf("st"); //liefert Index, wo die Zeichen auftreten
    stringVar.lastIndexOf("t"); //Index, wo zum letzten Mal der/die Zeichen aufgetreten ist/sind
    stringVar.substring(2,4); //liefert String zwischen 2 bis 4 Zeichen
    stringVar.split(" "); //liefert String-Array
    stringVar.trim(); //Entfernt Weißraum vom Anfang und Ende des Strings
    stringVar.replace("st", "xt"); //Return dabei den veränderten String
    ```
* 6 Datentypen: *String, Number, Boolean, Undefined*= Var deklariert, aber kein Wert zugewiesen, Null, Object => kann man die Eigenschaften + Methoden dieser Objekte verwenden
    * Arrays sind Objekte, es gibt viele Methoden für Array-Objekte
    * Number:
    ```javascript
    var varNum=10.234534;
    varNum.toFixed(3); //gibt String zurück, auf 3 Nachkommastellen runden
    varNum.toPrecision(3); // Gibt String zurück, bleiben insgesamt 3 Stellen
    varNum.toExponential(); //gibt String mit e-Schrebweise
    varNum.isNaN(); //true/false wenn eine Zahl
    //Math-Object:
    Math.PI //Pi-Zahl
    Math.round(3) //auf 3 Stellen runden
    Math.sqrt(9)//Wurzel 
    Math.ceil(varNum); //rundet Zahl auf den Ganzanteil auf
    Math.floor(varNum); //rundet Zahl auf den Ganzanteil ab
    Math.random(); //Zufahlszahl 0 bis 1
    //Bsp: Randomzahl:
    var randomNum=Math.floor((Math.random()*10)+1); //Zahl zwischen 1 bis 10 generieren
    ```
    * Date-Obj:
    ```javascript
    var jetzt=new Date();
    var datum1=new Date(1996, 11, 26, 15,45, 55); //YYYY, MM, DD, HH, MM, SS
    var datum2=new Date("Dec 26, 1996, 15:45:55" ); //MMM DD, YYYY, HH:MM:SS
    var datum3=new Date(1996,11,26);
    jetzt.getDate() //gibt Tag zurück 1-31
    jetzt.setDate(26); //Tag setzen 1-31
    jetzt.getDay();//Tag der Woche 0-6
    jetzt.setDay(6); //Tag der Woche 0-6
    jetzt.getFullYear() //Jahr in JJJJ
    jetzt.setFullYear(1996, 11, 26); //Datum setzen
    jetzt.getHours();
    jetzt.setHours(23, 55, 45, 225); //Uhrzeit setzen; Std, Min, Sec, MilliSec
    jetzt.getMilliseconds()
    jetzt.setMilliseconds(225);
    jetzt.getMonth();
    jetzt.setMonth(8,24); //Monat, Monatstag
    jetzt.getSeconds();
    jetzt.setSeconds(55, 225); //Sec, Millisec
    jetzt.getTime() //Anzahl der Millisec seit 1.1.1970
    jetzt.setTime(5635463); //Zeit in Millisec setzten
    jetzt.getTimezoneOffset(); //gibt Zeitzonenversatz in Minuten
    jetzt.toDateString(); //gibt String des Datums
    jetzt.toTimeString(); //gibt Uhrzeit als String 
    jetzt.toString(); //gibt Datum als String zurück
    ```
### Kapitel 4
```javascript
var vergleich=(score1+score2)>(highScore1+highScore2); //wird true oder false geliefert
vergleich=(score1>=pass1)&&(score2>=pass2);
vergleich=(!vergleich);

var level="zwei"; //oder var level=2;
var msg;
switch(level){
    case "eins": //oder case 1:
        msg="eins";
        break;
    case "zwei":
        msg="zwei";
        break;
    default:
        msg="nichts";
        break;
}
```
* falsy-Werte = die zu false konvertiert werden können
* truthy-Werte = die zu true konvertiert werden können + vorhanden eines Objekt = truthy
```javascript
var artist="Rembrandt"; //truthy
var artistA=(artist||"Unbekannt"); //artistA wird =artist
artist=""; //falsy
var artistA=(artist||"Unbekannt"); //artistA wird ="Unbekannt" gesetzt
value1=0;
value2=1;
value3=2;
if(value1||value2||value3){

}
```
* <- Logische Operatoren geben nicht immer true oder false zurück, sondern geben Wert zurück, der Vararbeitung angehalten hat
`document.getElementById("id").innerHTML=message1;` - geht auch so

### Kapitel 5: DOM
* DOM = auch Anwendungs-Programmmierschnittstelle = API
* über Benutzerschnittstellen können Menschen mit Programmen interagieren
* über APIs können Programme miteinader kommunizieren
* DOM = was Skript über aktuelle Seite fragen bzw. deren Inhalt verändern kann
* DOM = 4 Haupttypen: Dokumentknoten (Oberster Knoten=gesamte Seite) -> Elementknoten (=Tag) -> Attributenknoten(=id, class usw.) -> Textknoten 
```javascript
//Einzelnes Element auswählne:
document.getElementById("xxx");
document.querySelector("img"); //gibt das erste Element img im Baum
document.querySelector("header");

//Mehrere Elemente auswählen:
document.getElementsByClassName("xxx");
document.getElementsByTagName("h1");
document.querySelectorAll("img");

//vom Element zu Element springen

xyz.parentNode
xyz.previousSibling
xyz.nextSibling
xyz.firstChild
xyz.lastChild

xyz.nodeValue //Text bearbeiten
xyz.innerHTML //Zugriff auf Kindelemente
xyz.textContent //Zugriff auf Text

createElement();
createTextNode();
appendChild(); 
removeChild; //Knoten im Baum erstellen/hinzufügen/entfernen

xyz.className //auf Klassennamen zugreifen

var itemOne=document.getElementById("one");
var itemOne=getElementById("one"); //in itemOne wird Verweis auf die Stelle im DOM gespeichert

itemOne=document.getElementById("id1");
itemOne=document.querySelector("li.hot"); //<- CSS-Syntax
itemOne=document.getElementsByClassName("classs1");
itemOne=document.getElementsByTagName("li");
itemOne=document.querySelectorAll("li.hot"); //<- <li class="hot">

itemOne.class="class2";

//querySelector...() = liefert statische Knoten = können nicht geändert werden.

itemOne=document.getElementsByTagName("li");
itemOne=document.getElementsByClassName("class1");
itemOne=document.querySelectorAll("li[id]"); // <li id="1">, <li id="2"> und ...

var elements=document.getElementsByClassName("xyz");
elements.length; 
itemOne=elements.item(0);
itemOne=elements[0];

var startElem=document.getElementById("x");
var prevElem=startElem.previousSibling;
var nextElem=startElem.nextSibling;  //<- wegen Weißraum kann zu Problemen führen

//Wenn man von Element zum TextKnoten gewechselt hat => nodeValue = Text ändern
itemOne.innerHTML="text" //bearbeitet Text und Tag
itemOne.textContent="Text" //bearbeitet nur den Text
itemOne.innerText="Text" //bearbeitet nur den TExt

document.getElementById("x").firstChild.nextSibling.nodeValue="text";  //nodeValue nur im TextKnoten möglich

//nodeValue vom Textknoten
var itemOne=document.getElementById("x");
var elText=itemOne.firstChild.nodeValue;
elText=elText.replace("Text1", "Text2"); //Text aus dem TextKnoten abspeichern, in diesem Text Text1 durch Text2 ersetzen. 
itemOne.firstChild.nodeValue=elText; //den neuen Text dem TextKnoten zuweisen

//innerText
var itemOne=document.getElementById("x");
var textContent=itemOne.textContent; //gibt auch versteckte Elemente zurück
var innerText=itemOne.innerText; //Wenn im Element weiteres verborgenes Element gibt, wird nur das sehbare zurückgegeben
var text1="<p>Text</p>Text";
document.getElementById("y").innerHTML=text1 //Text und Tag im Element bearbeiten
itemOne.textContent="Text"; //Nur Text des Elements bearbeiten

var item="<em> Text </em> Text";
itemOne.innerHTML=item; //innerHTML besser um Ihnalt zu Ändern 

var elemContent=document.getElementById("x").innerHTML;
elemContent=elemContent+"Text";
document.getElementById(x).innerHTML=elemContent;

var newEl=document.createElement("li"); //neues Element (Knoten) erstellen
var newText=document.createTextNode("Text"); //neues TextKnoten erstellen
newEl.appendChild(newText); //den TextKnoten dem Element als Kind anhängen
document.getElementsByTagName("ul")[0].appendChild(newEl); //Element als Kind anhängen am Ende
document.getElementsByTagName("ul")[0].insertBefore(newEl, document.getElementsByTagName("ul")[0].firstChild); //Element als Kind anhängen ans Anfang (neuerEintrag, Ziel)

var removeElem=document.getElementsByTagName("li")[3]; //Element auswählen, das gelöscht werden soll
var containerElem=removeElem.parentNode; //ElternElement auswählen
containerElem.removeChild(removeElem); //aus dem ElternElement das ChildElement löschen.

//Methoden um Inhalt einzufügen:
document.write("Text");
document.getElementById("x").innerHTML="Text";
//createMethoden()
```

* XCC-Angriffe = wenn Benutzer Eingaben macht, die Schaden verursachen, die dann auf der Seite plaztiert werden:
    1. Eingaben validieren auf der Seiten
    2. Eingaben prüfen auf dem Server
* nichts in `<script>, <!-- --> <... href="..."> <div ..=..> {color: ...}`
* URL-Eingaben prüfen + encodeURIComponent() verwenden um Sonderzeichen zu maskieren
* innerHTML nicht verwenden => textContent, innerText
* `html()` (JQuery) nicht verwenden => `text()`

```javascript
var attClass=document.getElementById("x").getAttribute("class"); //liefert Wert des Attributs class
document.getElementById("one").hasAttribute("class") //prüft, ob Attribut "class " hat
document.getElementById("x").setAttribute("class", "classX"); //fügt "class" den Wert classX zu
document.getElementById("x").className="classX" //erstetzt "class" auf classX
document.getElementById("x").removeAttribute("class");
```
* Entwicklertools:
    * für Firefox: DOM Inspector(googeln), Firebug-Erweiterung

### 6: Ereignisse
* Ereignisse:
    * U-Erreignisse (User Interface = UI)
    * `load` = Laden der Seite ist abgeschlossen
    * `unload` = Webseite wird entladen, wenn andere Seite aufgerufen wurde
    * `error` = JS-Fehler ist aufgetreten
    * `resize` = Größe des Browsers wurde geändert
    * `scroll` = Benutzer hat gescrollt
    * `keydown` = Benutzer drückt eine Taste
    * `keyup` = Benutzer lässt Taste los
    * `keypress` = Zeichen wird eingefügt
    * `click` = Mausklick
    * `dblclick` = Double Click
    * `mousedown` = Maus drücken
    * `mouseup` = Maus loslassen
    * `mousemove` = Benutzer verschiebt die Maus
    * `mouseover` = Maus auf ein Element bewegen
    * `mouseout` = 
        * <- on+oberenNamen bei HTML-Ereignissen

* Fokusereignisse:
    * `focus/focusin` = Element enthält Fokus
    * `blur/focusout` = Element verliert Fokus
    * `input` = Wert von `<input>` hat sich verändert
    * `change` = Wert eines Auswahlfelds hat sich geändert
    * `submit` = Benutzer schickt Formular ab
    * `reset` = Benutzer resetet Fromular
    * `cut` = Benutzer schneidet Inhalte aus Formularfeld aus
    * `copy`
    * `paste` 
    * `select` = Benutzer markiert Text in einem Formularfeld

* Veränderungs-Ereignisse = wenn Script DOM ändert
* `DOMSubtreeModified` = Dokument wurde geändert
* `DOMNodeInserted` = Knoten wird als direktes Kind eines anderen Knotens eingefügt
* `DOMNodeRemoved` = 
* `DOMNodeInsertedIntoDocument` = Knoten wurde als Nachfahre eines anderen Knoten eingefügt
* `DOMNodeRemovedFromDocument` = Nachfahre eines anderen Knotens wurde entfernt

* UI-Ereignise - betrefen window = BrowserFenster

* Drei Mögichkeiten um Ereignisse zu binden:
    1. `<a onlick="funkt1();">` - veraltet => Besser ist JS und HTML zu trennen
    2. DOM-Ereignishandler //Nachteil mit einem Ereignis nur eine Funktion binden
    3. DOM-Ereignishandler Level 2
```javascript
function funkt1(){
    //...
}
//2)
var elem=document.getElementById("x");
elem.onclick=funkt1; //<- hier würde auch anonme Funktion gehen

//3)
var elem=document.getElementById("x");
elem.addEventListener("click", funkt1, false); //gewöhnlich false
//attachEvent() = für IE8 
elem.removeEventListener("click", funkt1, false);
//Fuktion mit Parameteter registrieren => anonyme Funktion als Wrapper:
function funkt2(i){
    //..
}
elem.addEventListener("click", function(){
    funkt2(10);
}, false);

//IE 5-8 unterstützen:
if(elem.addEventListener){
    elem.addEventListener("click", funkt1, false);
}
else{
    elem.attachEvent("onclick", funkt1); //IE bis 8 kennt nur attachEvent
}
```
* Ereignisfluss:
    1. von Element zum windows = normaler Fluss
    2. vom windows zum Element = z.B bei IE 8
        * `elem.addEventListener("click", funkt1, false)` - false = Fluss von innen nach außen(Bubbling), true=von außen nach ihnen (IE 8)=Ereigniserfassung

* Event-Objekt = gibt Info über Ereignis und das Element bei dem Es auftrat
    * wird an die Funktion im Ereinishander oder -listener übergeben
    * erhägt oft den Namen 
```javascript
function funkt3(e){
    var target=e.target; //Ziel des Ereingisses
    var typ=e.type; //Typ des Ereinisses
    e.preventDefault(); //Bricht das Standardverhalten des Element ab
    e.stopPropation(); //verhindert die fortgesetzte Weiterleitung des Ereinisses duch Bubbling oder Erassung
}
document.getElementById("x").addEventListener("click", funkt3, false);

function funkt4(e, i){
    var target=e.target; //Ziel des Ereingisses
    var typ=e.type; //Typ des Ereinisses
    e.preventDefault(); //Bricht das Standardverhalten des Element ab z.B bei Send-Button
    e.stopPropation(); //verhindert die fortgesetzte Weiterleitung des Ereinisses duch Bubbling oder Erassung <- wenn. z.B Eltern eigene Ereignisse haben
    //...
}
document.getElementById("x").addEventListener("onclick", function(e){
    funkt4(e,i);
}, false);
```
* Event bei IE 5-8
* event-Objekt bei IE steht wird nicht automatisch an Ereinishandler/listener übergeben, steht aber als Kind des window zur Verfügung
```javascript
function funkt5(e){
    if(!e){
        e=window.event;
    }
    var target=e.target || e.srcElement;
}
```

* Ereingisdelegierung = am Eltern hören, ob beim Kind Ereingis auftrat => mit `event.target` herausfinden, bei wem das Ereignis auftrat = <- Verbesset die Leistung
* <-- manchmal wird statt event.target this. verwendet <- funktioniert solange Funktion keine Parameter hat bzw. keine anonyme Funktion ist.

* Es gibt drei EreinisArten:
    * DOM-Ereingisse
    * HTML5-Ereignisse z.B für submit = für HTML-Element
    * BOM-Ereinisse = Browser Object Model = Ereignisse des Browsers z.B. Ereinsisse für Tousch-Screen-Gereäte

* Ereignisse der Benutzer-Schnittstelle (UI) = betreffen Browserfenster
    * `load` = Laden der Seite abgeschlossen
    * `unload` = Webseite entladen wird
    * `error` = JS-Fehler passiert
    * `resize` = Größe des Browsers verändern
    * `scroll` = Benutzer scrollt
```javascript
function setup(){
    var textInput=document.getElementById("x");
    textInput.focus(); //Fokus auf textInput legen
}
window.addEventListener("load", setup, false);
```

* Formular-Ereignisse:
    * `focus` = Input bekommt den Fokus
    * `blur` = Input verliert den Fokus <- Nutzlich um Tipps dem User zu geben + zur Formularvalidierung = Verbieten des Wechsels bei falscher Eingabe

* Mouse-Ereignisse 
    * `mousedown` + `mouseup` = für Drag und Drop

* Posion der Maus herausfinden
```javascript
function showPosition(event){
    var sx=document.getElementById("x");
    var sy=document.getElementById("y");
    sx.value=event.screenX; //Bildschirm-Position der Maus
    sy.value=event.screenY;
    var px=document.getElementById("px");
    var py=document.getElementById("py");
    px.value=event.pageX; //Seite-Position der Maus
    py.value=event.pageY;
    var cx=document.getElementById("cx");
    var cy=document.getElementById("cy");
    cx=event.clientX; //Viewport-Postion der Maus
    cy=event.clientY;
}
document.getElementById("body").addEventListener("mousemove",showPosition,false);
```

* Tastaturereignisse
    * `input`
    * `keydown`
    * `keypress`
    * `keyup`
```javascript
var taste=event.keyCode //ASCII-Code der gedrückter Taste
var taste=String.fromCharCode(event.keyCode); //auch Zahlen und Sonderzeichen ausgeben
function charCount(e){
    var textEntered;
    var charDisplay;
    var counter;
    var lastKey;
    textEntered=document.getElementById("message").value;
    charDisplay=document.getElementById("charactersLeft");
    counter=(180-textEntered.length);
    charDisplay.textContent=counter;

    lastKey=document.getElementById("lastkey");
    lastKey.textContent="ASCII-Code: "+e.keyCode;
}
document.getElementById("message").addEventListener("keypress", charCount, false);
```
* Formularereignisse:
    * `submit`, `change`, `input`, `focus`, `blur`
* `change` = z.B. bei Drop-Down-Menu

* Änderung des DOM
* Änderungsereignisse => werden durch Ändrungsbeobachter ersetzt
* `DOMNodeInserted`
* `DOMNodeRemoved`
* `DOMSubtreeModified`
* `DOMNodeInsertedIntoDocument`
* `DOMNodeRemovedFromDocument`

* HTML5-Ereignisse
    * `DOMContentLoaded` = wenn DOM-Baum aufbebaut ist <- alternative zu `load`, da nicht wartet bis Inhalt der Seite geladen wurde
    * `hashchange` = URL-Cash ändert sich, an window gebunden, nach der Änderung weist `event.oldURL` und `.newURL` die alteun und neue URLS zu
    * `beforeunload` = z.B Nutzer hinweis geben, dass Änderungen am Formular nicht gespeichert wurden

### 7: jQuery
* man kann jQuery und JS kombinieren
* `$()` = `jQuery()` = ein Objekt jQuery erstellen
* Methoden wirken sich auf alle ausgwählten Elemente => müssen nicht in einer Schleife durchlaufen werden
* `$(":header").addClass("headline")` - Überschriften auswählen h1 bis h6
* `$("li:lt(3)").hide().fadeIn(1500)` - erten drei li auswählen Elemente verstecken + langsam einblenden
```javascript
$("li").on("click", function(){
    $(this).remove();
}); //beim Click auf li wird this Element entfernt
```
* jQuery Selectoren:
    * element -> `p`
    * `#id`
    * `.class`
    * `selecto1, selector2`
    * Hierarchien:
        * `Eltern Kind`
        * `Eltern > Kind` oder `*` für alle Kinder
        * `vorheriges + nächstes` - wählt Element aus, die auf vorheriges folgen
        * `vorheriges ~ Geschwister` - alle Geschwistern
    * Filter:
        * `:not(Selektor)` - Alle Elemente außer in (...) z.B `div:not("id1")`
        * `:first` = erste Element der Auswahl
        * `:last` = letzte Element der Auswahl
        * `:even` = Elemente mit gerader Indexnummer in der Auswahl
        * `:odd`
        * `:eq(Index)`
        * `:gt(Index)`
        * `:lg(Index)`
        * `:header` = h1 bis h6
        * `:animated` = zurzeit animierte Elemente
        * `:focus` = Element, das zurzeit den Fokus hat
        * `:contains("Test")`
        * `:empty` = Elemente ,die keine Kinder haben
        * `:parent` = Element mit einem Kindknoten
        * `:has(Selector)` = z.B `div:has(p)`
    * Sichtbarkeit:
        * `:hidden`
        * `:visible`
    * Kindfilter:
        * `:nth-child(Ausdruck)` = zählung beginnt nicht bei null sondern bei Ausruck
        * `:first-child`
        * `:last-child`
        * `:only-child` = wenn das Element nur ein Kind hat
    * Attributfilter:
        * `[attribut]` = Element mit angegeben Attribut
        * `[attribut="Wert"]`
        * `[attribute!="wert"]`
        * `[attribute^="wert"]` =wert beginnt mit diesem Wert
        * `[attribute*="wert"]`=wert steht irgendwo im Attributwert
        * `[attribte|="wert"]`=
        * `[attribute~="wert"]`=Wert sollte einer der Wert getrennt durch Leerzeichen sein
        * `[attribut1][attribute2]` = Element die mit allen selektren übereinstimment
    * Formularfilter:
        * `:input`
        * `:text`
        * `:passwort`
        * `:radio`
        * `:chechbox`
        * `:submit`
        * `:image`
        * `:reset`
        * `:button`
        * `:file`
        * `:selected`
        * `:enabled`
        * `:disabled`
        * `:checked`
```javascript
//Wenn jQuery-Auswahl nichts findet => keine Fehler, sondern wird nichts gemacht
$("ul") //=liefert Verweis auf einen einzigigen Elemen Knoten; index = 0
$("li") //liefert Verweis auf jQuery-Array: Index: 0, 1, 2 usw.
```

* Methoden:
```javascript
//Methoden zum Info abrufen = liefer Info nur vom ersten Element
var content = $("li").html(); //Inhalt des ersten li in content gespeichert

//Methoden zum Ändern = wirkt auf alle Element 
$("li").html("updated"); //um einen Element zu ändern => Filter verwenden

//jQuery liefert Verweise auf auf die Elemente im DOM (keine Kopien)

//jQuery-Objekt speichern:
$jQElem=$("li");

$("li.class1").addClass("class2"); //wird auf alle <li class="class1"> angewendet

//Mehrere Methoden auf Objekt anwenden => einfach hintereindader schreiben:
$('li[id!="id1"]').hide().delay(500).fadeIn(1500); //-> man kann das auch anders 
$("li[id!='id1']")
    .hide()
    .delay(500)
    .fadeIn(1500); //funktioniert eine Methode in der Kette nicht => werden die restlichen nicht ausgeführt
```

* Prüft ob Seite bereit ist um Hier Code auszuführen. Wenn bereit ist wird `function(){}` ausgeführt => muss nicht am Ende von Body platiert werden
```javascript
$(document).ready(function(){
    //Hier Code
}); //oder so schreiben 
$(function(){
    //Hier Code
});
```
* ready() prüft ob DOMContentLoaded unterstützt, das ausgelöst wird wenn DOM geladen wurde. Wenn unterstützt wird erstellt jQuery Ereignislistener dafür. Auf ältern Browsern wird auf Ereignis load gewartet

* Methoden zum Erstellen von HTML-Elementen
```javascript
$("ul").html() //Liefert <li ..>...</li> ... zurück
$("ul").text() //Liefert nur Text innerhalb der <li>-es, ohne Trennung der <li>-es
//Bsp:
var $ulElem=$("ul").html(); //<li>-es aus ul speichern
$("ul").append($ulElem); //gespeicherten <li>-es am Ende von ul anhängen
$ulElem=$("ul").text();
$("ul").append("<p>"+$ulElem+"</p>");

//mit html() text() replaceWith() kann man Inhalt des Tags ändern
$("li.class1").html(function(){
    return "<em>"+$(this).text()+"</em>";
});

//replaceWith() = Element(-e) komplet erstetzen
$("li.class1").remove();

//Element einfügen: !fügen allen Element in Array Element hinzu
//1)neues Element ertellen
var $newFragment=$("<li>") //leeres li erstellen
var $newItem=$('<li class="new">item New </li>');
//2)mit .before()=vor dem Element, after()=hinter dem Element, prepend()=nach dem öffendem Tag, append()=vor dem schließendem Tag einfügen
$("ul").before($newItem);
$("ul").append('<li class="new2" item New2 </li>');
$newItem.appendTo("ul"); //fügt newItem zu ul
```
* den Tag Attribute hinzufügen/entfernen `.attr()`, `.removeAttr()`
```javascript
$("li#id1").attr("class"); //dem li#id1 Attribut class einfügen
$("li#id1").attr("class", "class1") //class=class1 hinzufügen
$("li#id1").removeClass("class1");
$("li#id1").addClass("class2");
```

* css-Eigenschaften abrufen+ändern
```javascript
var backgrColor=$("li").css("background-color"); //liefert backgroundColor des ersten Treffers
$("li").css("background-color", "#272727"); //werden alle alle background-color auf 272727 gesetzt
$("li").css({
    "background-color": "#272727",
    "font-familiy": "Courier"
}); //mehrere css ändern
```
* mehrere Sachen an allen Objekte ausführen:
```javascript
$("li").each(function(){ //each ist sowas wie Schleife
    var ids=this.id; //JS sosnt ids=$(this).attr("id")
    $(this).append('<em class="order">'+ids+'</em>');
}) //each bekommomt als Param eine anonyme Funktion, this = zeigt auf gerade ausgewähltes element <- man dann hier auch JS verwenden
```
* Ereignisse: = `on()`
```javascript
$("li").on("click", function(){
    $(this).addClass("class2");
}); //onclick für li mit anonymen Funktion registrieren, kann auch benannte Funktion sein

$("li").on("mouseover click", function(){ //Funktione für mehrer Ereignisse registrieren
    //..
});
```
* Ereignisse + Event-Objekt
```javascript
$("li").on("click", function(e){
    eventType=e.type;
});
```
* hat etwas andere Eigenscaften wie JS Event:
* `type` = Art des Ereignisses
* `which` = betätigte Taste
* `data` = 
* `target` = DOM-Element, in dem das Ereignis aufgetreten ist
* `pageX` = Mauspositon
* `pageY` = Mausposition
* `timeStamp` = Millisek seit 1970
* `.preventDefault()` = Verhindert Standardverhalten
* `.stopPropagation()` = verhindert die Weiterleitung des Ereignisses an die Vorfahren (Bubbling)
* Bsp:
```javascript
$(function(){
    $("li").on("click", function(e){
        var date = new Date();
        date.setTime(e.timeStamp);
        var clicked = date.toDateString();
        $(this).append("<span>"+clicked+" "+e.type+"</span>");
    });
});
```
* `on()` kann nach ertem Param. weitere Param annehmen zum Filtern der Elemente für die Funktion registriert werden soll
* `on(events[, selector][, data], function(){});`
    * früher wurde *delegate()* verwendet
* Bsp: click für alle außer letzten li registrieren
```javascript
$(function(){
    $("li").on("click mouseover", "not:(#vier", {status: "important"}, function(e){
        //..
    });
});
```

* Effekte = Übergänge + Bewegungen:
    * Element ein/ausblenden:
    ```javascript
    .show()
    .hide()
    .toggle() //Schaltet die Sichtbarkeit des Elements um
    ```
    * Ein/Ausblenden 2:
    ```javascript
    .fadeIn() = blendet ein
    .fadeOut() =blendet aus
    .fadeTo() = ändert die Deckkraft
    .fadeToggle() = schaltet die Deckkraft des Objekts in Gegenteil um
    ```
    * Verschieben:
    ```javascript
    .slideUp() = schiebt Element in Blickfeld
    .slideDown() = schiebt Element aus dem Blickfeld
    .slideToggle()
    ``` 
    * Benutzerdefinierte Effekte:
    ```javascript
    .delay() = verzögert die Ausführung der nachfolgenden Einträge in eine Warteschlage
    .stop() = hält eine laufende Animation an
    .animate() = erstellt benutzerdefinierte Animation
    ```
    * zur Animation kann man auch CSS3 verwenden
        * //Bsp:
        ```javascript
        $("h2").hide().slideDown();
        var $li=$("li");
        $li.hide().each(function(){
            $(this).delay(700*index).fadeIn(700); //in ms
        });
        $li.on("click", function(index){
            $(this).fadeOut(700);
        })
        ```
* `animate()` =eigne Animationen = Änderung der CSS-Eigneschfaten, CSS-Eigenschaften werden in Camelschreibweise geschrieben
```javascript
.animate({[, speed][, easing][, complete])}; 
```
* `speed`=Dauer der Animation + zwei Schlüsselwörter(`slow,fast, easing=linear/swing, complete`=Funktion nach der Ausführung ausführen
* Bsp: opacity ü paddin-left animieren
```javascript
$(function(){
    $("li").on("click", function(){
        $this.animate({
            opacity: 0.0,
            paddingLeft: "+=80"
        }, 500, function(){
            $(this).remove();
        });
    });
});
```
* DOM duchlaufen: = von einer Auswahl auf andere Elemente zugreifen
    * Param=Selector erforderlich
        * `.find()` = Alle Elemente in der Auswahl mit mit Selector übereinstimmern
        * `.closest()` = nächster Vorfahr
        * `Param=Selector optional
        * `parent()`
        * `parents()` = Alle Eltern
        * `children()` =
        * `.siblings()`
        * `.next()`
        * `.nextAll()`
        * `.prev()`
        * `.prevAll()`
    * <- bei mehrerer Auswahl werden auf alle Elmente ausgeführt => kommische Ergebnisse
    * Bsp:
    ```javascript
    $(function(){
        var $h2=$("h2");
        $("ul").hide();
        $h2.append('<a>Anzeige</a>');
        $h2.on("click", function(){
            $h2.next()
                .fadeIn(500)
                .children(".hot")
                .addClass("complete");
            $h2.find("a").fadeOut();
        });
    });
    ```
* Elemente einer Auswahl hinzufügen:
`.add()`
`.filter()` = Findet Elemente die mit einem Selector(Param) übereinstimmen
`.find()` = Findet Nachkommen, die mit Selector übereinstimmen
`.not()/:not()` = Findet Elemente, die mit Selctor nicht übereinstimmen
`.has()/:has()` = Findet Nachkommen, die mit Selecotor übereinstimmen
`/:contains()` = 
`("li").not(".hot").addClass("cool");` //= 
`("li:not(.hot)").addClass("cool");`
`/.is()` = Prüft, ob Auswahl eine Bedingung erfüllt
* Bsp: = wählt Listeneinträge + wendent Filter daraus an
```javascript
var $listItem=$("li");
$listItem.filter("hot:last").removeClass("hot");
$("li:not(hot)").addClass("cool");
$listItem.has("em").addClass("compete");
$listItem.each(function(){
    var $this=$(this);
    if($this.is("hot")){
        $this.prepand("Eintrag mit Vorrang");
    }
    $('li:contains("Honig")').append("(region)");
});
```
* Einträge anhand Indexnummer finden:
* Elemente in haben intern eine Indexnummer, beginnt bie 0:
* Methoden anwenden `.eq()`, `:lt()`, `:gt()`
* `var $li=$("li")` => alle li-es
* 
```javascript
$("li:lt(2)").removeClass("hot");
$("li").eq(0).addClass("cool");
```

* Formularelemente-Selektoren -> sind aber langsam => Lösung: davor einen CSS-Selektor voranstellen
    * `:button`, `:chechbox`, `:checked` = Kontollkästchen, Optionsschalter, `:disabled` = alle deaktivieren Elemente, `:enabled`, `:focus`, `:file` = Alle Dateielemente, `:image` => bessere Lösung `[type="image"]`, `:input` => bessere Lösung `.filter(":focus")`, `:password` => Bessere Lösung `$('input:password')`, `:radio` => bessere Lösung `$('input[name="gender"]:radio')`, `:reset`= Reset-Button, `:selected` = Alle markierten Elemente => bessere Lösung = `.filter(":selected")`, `:submit`, `:text` => bessere Lösung `('input:text')`, 
* Methoden: 
    * `var newVar1=$("input:text").val();` - `.val()` = für input,select,textarea; Wert des ersten Elements eine Auswahl abrufen + darin enthaltenen Elemente ändern 
    * `.filter()` = filtert jQuery-Auswahl mit zweitem Selektor (für formualerspezifische Filter)
    * `.is()` = häufig mit Filtern eingesetzt, um zu prüfen, ob Formularfeld markiert/ausgewählt wird 
    * `$.isNumeric(1);` `$.isNumeric("1");` - prüft, ob Werte nummerisch ist true wenn ja; <- globale Funktion 
* `.on()` = handhabt alle Ereignisse
    * Ereignisse: `blur` = verliert Fokus, `change`, `focus`, `select` = Option eines select-Elements ändert sich, `submit`
    ```javascript
    $("#newItemButton").on("submit", function(e) {
    //..
    });
    
    //Bsp 1:
    var $newItem1=$("#newItemButton"); //Element in Variablen speichern
    $("showForm").on("click", function(){
        $newItem1.show(); //Element anzeigen .hide() = Element verstecken
    });
    //Bsp 2: Elemente ausschneiden/kopieren
    $(function(){
        var $p=$("p");
        var $cloneQuote=$p.clone(); //Element klonen = Kopieren <- bei ID-Elemente => muss man sie verändern, da sonst ID nicht eindeutig
        $p.remove(); //Element löschen
        $cloneQuote.insertAfter("h2"); //
        var $moveItem=$("#one").detach(); //Löscht Element, speichert aber das Element ab
        $moveItem.appendTo("ul");
    });

    // Bsp 2: Abmessungen = Breite/Höhe der Elemente ändern
    var $hoehe=$("#id1").height();
    $("#id1").height(125); //Höhe setzen
    $("#id1").height("50%"); 
    var $breite=$("id1").width();
    $hoehe=("id1").innerHeight(); //Höhe mit Padding
    $hoehe=("id1").outerHeight(); //Höhe mit Padding und Border 
    $hoehe=("id1").outerHeight(true); //Höhe mit Padding und Border und Margin
    ```
* Browserfenster
```javascript
var $WinHoehe=$(window).height();
var $docHoehe=$(document).height();
var offset=$("div").offset(); //.position() = liefert Objekt mit .top und .left offset()=vom Fenster, position()=vom Vorfahren, der aus dem Fluss rausgenommen wurde. 
var offsetX=offset.left;
var offsetY=offset.top;
var gescrolltY=$(windows).scrollTop();
var gescrolltX=$(window).scrollLeft();
```

* jQuery einbinden
    1. über Internet einbinden = CDN=Content Delivery Network
    ```html
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script>
    window.jQuery || document.write("script src="js/jquery-1.10.2/js"><\/script>) 
    </script>
    ```
    *  - als Option einbinden, falls das Laden von jQuery vom externen Server nicht klappt
* Scripts ab besten vor dem schließendem `</body>` einbinden
    * http://api.jquery.com = Documentation zu jQuery
    * http://plugins.jquery.com = Liste mit Scipts, die jQuery-Funktionsumfang erweitern
    * Es gibt viele Bibliotheken, die auch $ benutzen => dieses Konfikt so lösen:
        1. jQuery als letztes einbinden => $ gilt für letzte Bibliothek
        2. `jQuery.noConflict();` vor dem jQeury-Script ausführen + im Scipt `jQuery.xxx()` nutzen `.noConflict()` = $ wird freigegeben
        3. Sktipt in IIFE einschlien:
        ```javascript
        jQuery.noConflict();
        (function($){
            //...
        })(jQuery);
        ```
        4. eigenen Alias erstellen
        ```javascript
        var $j=jQuery.noConflict();
        $j(document).ready(function(){

        });
        ```

### 8: Ajax und JSON
* für Live-Suche=automatische Vervollständigung meist Ajax
* Ajax arbeitet asynchrone
* Wenn im HTML `<script> vorkommt hält Browser an und verarbeitet alles was im <script>` steht
* bei Ajax fordert Browser beim Server nur Daten an und geht weiter = asynchrone
* Wenn der Server die Daten erhalten hat => wird Ereignis load ausgelöst, der z.B eine Funktion aufrufen kann
* `var xhr=new XMLHttpRequest();` - Instanz des HttpReq-Objekts erstellen
* `xhr.open("GET", "data/test.json", true);` - bereitet die Anforderung vor, GET=HTTP-Methode, data/test.json=URL der Seite; true=Anforderung asynchron
* `xhr.send("search=arduino");` - Sendet die Anforderung; Param=zusätzliche Info, sonst null
* Antwort verarbeiten:
```javascript
xhr.onload=function(){
    if(xhr.status==200){
        //:::
    }
}
```
* Für Antworten gewöhnlich drei Formate:HTML=am leichtesten zu verarbeiten,XML, JSON
* XML-DAtei kann man mit DOM-Methoden verarbeiten
```javascript
//JSON
{
    "location": "San Francisco, CA",
    "capacity": 270
} //"schlüssel": wert

JSON.stringify(jsObj); //wandelt JavaScript-Object in JSON-String
var jsObj=JSON.parse(); //JSON nach JavaScrip-Obj umwandeln

//Aufbau - HTML=Antwort:
var xhr=new XMLHttpRequest();
xhr.onload=function(){
    if(xhr.status===200){
        document.getElementById("id1").innerHTML=xhr.responseText;
    }
};

xhr.open("GET", "data/data.html", true);
xhr.send(null);

//Aufbau - XML=Antwort:
var xhr=new XMLHttpRequest();
xhr.onload=function(){
    if(xhr.status===200){
        var response=xhr.responseXML //Ruft XML vom Server ab
        var events=response.getElementsByTagName("event");
        for(var i=0; i<events.length; i++){
            var container, image, location, city, newline;
            container.className="event"

            image=document.createElement("img");
            image.setAttribute("src", getNodevalue(events[i]),"map");
            image.appendChild(document.createTextNode(getNodeValue(events[i], "map")));
            container.appendChild(image);

            location=document.createElement("p");
            city=document.createElement("b");
            newline=document.createElement("br");
            city.appendChild(document.createTextNode(getNodeValue(events[i], "location")));
            location.appendChild(newline);
            location.insertBefore(city, newline);
            location.appendChild(document.createTextNode(getNodeValue(events[i], "date")));
            container.appendChild(location);

            document.getElementById("content").appendChild(container);

        }
        function getNodeValue(obj, tag){ //obj=XML-Fragment, tag=Name des Tags
            return obj.getElementsByTagName(tag)[i].firstChild.nodeValue;
        }
    }
};

xhr.open("GET", "data/data.xml", true);
xhr.send(null);

//Aufbau - JSON=Antwort
var xhr=new XMLHttpRequest();
xhr.onload=function(){
    if(xhr.status===200){
        responseObj=JSON.parse(xhr.responseText);
        var newContent="";
        for(var i=0; i<responseObj; i++){
            newContent += "<div class='event'>";
            newContent += "<img src='"+responseObj.events[i].map+"'";
            // ...
            newContent += "</div>";
            
        }
        document.getElementById("content").innerHTML=newContent;
    }
};

xhr.open("GET", "data/data.html", true);
xhr.send(null);
```
* JSONP - in `<script>`-Element, das Daten vom Server lädt <- Funktioniert,da keine Einschränkung für Quelle von script = hier Funktion die Daten anfordert
* CORS = dem Header zusätzlich Info hinzufügen, um dem Browser und Server mitzuteilen, dass sie kommunizieren sollen
* JSONP => Daten werden als Script übergeben => `parse()`/`stringify()` nicht nötig
* Funktion meistens als GET übergeben:
* `http://lala.de/lala.php?callback=showEvents`
* ZUR Sicherheit kann man Timer für die Abfrage von dritten Servern implementieren.

* jQuery und Ajax - zwei Schritte 1)Anforderung 2)Antwort verarbeiten
* `$("#id1").load("lala.html #id1")` - `$(..)`=jQuerey Objet wird erstellt, wo neues HTML-Element erscheinen soll, *lala.html* = Seite von der man Code laden möchte, *#id1*=Element(-e) der Seite, die man laden möchte
* liefern jQuery-Objekt = jqXHR-Obj
```javascript
var jQObj=$.get() \\ mit GET-Methode Daten vom Server laden -> Param. (url[, data][, callback][, type])
var jQObj=$.post() //mit POST Daten vom Server laden -> Param. (url[, data][, callback][, type])
var jQObj=$.getJSON() //JSON mit GET laden -> Param. (url[, data][, callback])
var jQObj=$.getScript() //JS auch JSONP mit GET laden -> Param. (url[, callback])
var jQObj=$.ajax() //kann alle Anforderungen durchführen
//url=woher die Daten holen, data=zusäzlich Info, die an den Server gesendet wird, callback=benannte oder anonyme Funktion, die die Antwort verarbeitet, type=Typ der Daten
var var1=jQObj.responseText; //Textdaten
var1=jQObj.responseXML; //XML-Daten
var1=jQObj.status
var1.jQObj.statusText; //Statusbeschreibung
var1.done() //auszuführender Code bei Erfolg
var1.fail() //auszuführender Code bei Fehler
var1.always() //Code bei Erfolg oder Fehler
var1.abort() //bricht die Kommunikation ab
```
* alle diese Funktion greifen auf `.ajax()` zurück
* <- diese Funktionen werden durch Laden oder Eingabe in Formular ausgelöst
* Bsp:
```javascript 
$("#id1").on("click", function(e){
    e.preventDefault();
    var queryString="vote="+event.target.id;
    $.get("votes.php", queryString, function(data){
        $("id1").html(data);
    });
});

//Formular mit Ajax = .post() + .serialize()
var var1=$("#id1").serialize(); //serialisiert zu versendende Daten:
//1) wählt alle Info im Formular aus, 
//2) stellt alles als String dar, 
//3)kodiert die Zeichen <- 
    //kann auf einzelne Felder oder ganzes <form> 
    //angewendet werden

/*auf der Serverseite kann man mit X-Requested-With prüfen,
ob Seite durch Ajax-Aufruf angefordert wurde = 
wenn Header XMLHttpRequest hat
*/
$("#id1").on("submit", function(e){
    e.preventDefault();
    var var1=$("#id1").serialize();
    $.post("votes.php", var1, function(data){
        $("id1").html(data);
    });
});

//Mehr Kontrolle über .ajax() -> Bsp:
$("nav a").on("click", function(e){
    e.preventDefault();
    var url=this.href;
    var $content=$("#content");

    $("nav a.current").removeClass("current");
    $(this).addClass("current");
    $("#cotainer").remove();

    $.ajax({
        type: "POST",
        url: url,
        timeout: 2000, //nach 2 sec abrechen
        beforeSend: function(){
            $content.append("<div id='load'>Lädt</div");
        },
        complete: function(){
            $('#loading').remove;
        },
        success: function(data){
            $content.html( $(data).find("#container") ).hide().fadeIn(400);
        },
        fail: function(){
            $("#panel").html("<div class='loading'> lalala</div>");
        }
    });
});
```
### 9: API
* API = ermöglichen Interaktion zwishcen Mensch und Programm = externe Programme auffordert etwas zu tun und die Antwort verarbeiten
* z.B DOM und jQuery sind API-es; DOM-Funktionalität ist in JS-Interpreter eingebaut

1. 
    * HTML5-API = HTML5 bietet neue MarkUps + neue JS-APIs = stellt Objekte bereit, die für bestimmte Funktionalität gedacht sind

    * man sollte Prüfen, ob Browser entsprechende API unterstützt
    ```javascript
    if(navigator.geolocation){
        //...
    }
    else{
        //...
    }
    ```

* Modernizer: = Skript um zu ermitteln, ob Browser HTML-, CSS- und JS-Merkmale unterstützt -> eingesetzt um festzustellen, ob Browser bestimmte APIs unterstützt.
    1. von modernizr.com herutnerladen
    2. Einbinden auf der Seite: = ein Modernizer-Object wird erzeugt. Eigenschafte des Objects sind die Merkmale 
    3. if(Modernizr.geolocation) <- liefert true/false zurück

* Ortungs-API: = z.B über die IP-Adresse ermittelt/Mobilfunkantenne/GPS-Hardware
    * steht in allen Browsern zur Verfügung
    * nutzt Object geolocation
    ```javascript
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(success, fail) //zwei Param. = Namen der Funktion 1)die bei Erfolg aufgerufen wird => die als Param position-Objekt bekommt, 2)Funkt, die bei Fehler aufgerufen wird => als Param Position-Error-Object übergeben

        //Position-Object-Eigenschaften:
        var var1=Position.coords.latitude //Breite
        var1=Position.coords.longitude //Länge
        var1=Position.coords.accuracy //Genauigkeit in Metern
        var1=Position.coords.altitude //Höhe über dem Meeresspiegel in Metern
        var1=Position.coords.altitudeAccuracy //Genauigkeit der Höhe in Metern
        var1=Position.coords.heading //
        var1=Position.coords.speed //Geschwindigkeit in Metern
        var1=Position.coords.timestamp

        //Eigenschaften des PositionError-Obj:
        var1=PositionError.code //1=Erlaubnis verweigert, 2=Nicht verfügbar, 3=Zeitüberschreitung
        var1=PositionError.message
    }

    if(Modernizr.geolocation){
        var position=getCurrentPosition()
    }
    else{

    }
    ```
    * Bsp:
    ```javascript
    var elMap=document.getElementById("id1");
    var msg="Fehler";

    if(Modernizr.geolocation){
        navigator.geolocation.getCurrentPosition(success, fail);
        elMap.textContent="Prüfe Standord...";
    }
    else{
        elMap.textContent=msg;
    }

    function success(position){
        msg="<h3>Longitude:<br>";
        msg+=position.coords.latitude+"</h3>";
        msg+="<h3>Latitude:<br>";
        msg+=position.coords.longitude + "</h3>";
        elMap.innerHTML=msg;
    }
    function fail(msg){
        elMap.textContent=msg;
        console.log(msg.code);
    }
    ```

* Webspeicher-API
    1. lokale Speicherung
    2. Sitzungsspeicherung
* vor HTML5 nur Cookies :
    1. nur wenige Daten, 
    2. bei jeder Aufforderung einer Seite Daten zum Server gesendet, 
    3. =unsicher)
    * => in HTML5 zwei Spiecherobjekte 1)localStorage, 2)sessionStorage <- Unterschied wie lange Daten gespeichert werden
    * meistens 5MB pro Domäne in einem Speicherobjekt -> mehr => Browder fragt den Benutzer
    * Seiten verfolgen bei der Speicherung Same Origin Policy = auf Daten kann nur von derserlben Domäne zugegriffen werden. z.B map.google.de !=google.de
* Es gibt auch noch APIs für DB-Zugriff z.B Web-SQL
* localStorage und SessionStorage sind im window-Obj implementiert
```javascript
//etwas zu Spiechertn => Schlüssel/Wert-Paar
localStorage.setItem("age", "13");
localStorage.age = 12; //alternative
var age=localStorage.getItem("age");
age=localStorage.age; //alternative
var items=localStorage.length //Menge der gespeicherten Objekte
localStorage.removeItem(age);
localStorage.clear() //Löscht alle Objekte
//<- sessionStorage hat die gleichen Methoden
//Bsp:
if(window.localStorage){
    var txtUserName=document.getElementById("username");
    var txtAnswer=decument.getElementById("answer");
    txtUsername.value=localStorage.getItem("username");

    txtUserName.addEventListener("input", function(){
        localStorage.setItem("username", txtAnswer.value);
    }, false)
}
```

* Verlaufs-API und Pushstate
* URL jedes Tabs werden zur URL-Liste des Tabs hinzugefügt = in history-Obj gespeichert
* `history.pushState(state, title, url);`  = der URL-Liste URL manuell hinzufügen (z.B bei Ajax-Aufrufen)
* `history.replaceState()` = Listeneintrag ändern
* `onpopstate` = um die richtige Seite aufzurufen über location-Obj oder -state-Info möglich
* `location.pathname`
* `history.back()` - Verlauf zurück
* `history.forward()` - Verlauf vorwärts
* `history.go(-2)` - Verlauf um Parameter zurück/vorwärts
* `history.pushState();`
* `history.replaceState();`
* `history.length`
```javascript
window.onpopstate //Ereignis bei Klick auf vorwärts/zurück-Button

    //Bsp:
    $(function(){
        function loadContent(url){
            $("#content").load(url+ "#container").hide().fadeIn("slow");
        }
        $("nav a").on("click", function(e){
            e.preventDefault();
            var href=ths.href;
            var $this=$(this);
            $("a").removeClass("current");
            $this.addClass("current");
            loadContent(href);
            history.pushState("", $this.text, href);
        });
    window.onpopstate=function(){
        var path=location.pathname;
        loadContent(path);
        var page=path.substring(location.pathname.lastIndexOf("/") +1 );
        $("a").removeClass("current");
        $("[href='"+page+"']").addClass("current");
        ;}
    });
```
* Skripts mit APIs = APIs verwenden um mit Skrpits zu arbeiten
    * z.B Skrpits zur Gestaltung von Schiebereglern, Fenstern, Tabellensortierern
* Bsp: 
    1. jQuery-Plugin jQuery UI; 
    2. AngularJS=Vereinfacht Entwicklung von Web-Apps
* jQuery-Plugins = Skripts, die jQuery-Objekte neue Methoden hinzufügen => jQuery + Plugin auf die  Seite einfügen
    * jQuerey UI = Bundel von Plugins
        1. jQuery + jQuerey UI einbinden (jqueryui.com) <- evneutell nur Teile von jQueryUI einbinden
            * Bsp 1: Zieheharmonika:
                1. HTML-Code strukturieren 
                2. welche Elemente jQeury auswählen soll. 
                3. welche jQeuery UI-Methoden aufrufen
        //zu 1.
        ```javascript 
        <div id="prizes">
        <h3>Preis 1</h3>
        <div> ...</div>
        <h3>Preis 2</h3>
        <div>...</div>
        </div>
        $(function(){
            $("#prizes").accordion();
        });
        //Bsp2: Registerkarten
        <div id="prizes">
        <ul>
        <li><a href="#tab-1">...</a> </li>
        <li><a href="#tab-2" ...>...</a> </li>
        </ul>
        <div id="tab-1"> ...</div>
        <div id="tab-2">...</div>
        </div>
        $(function(){
            $("#prizes").tabs();
        });
        ```
        * <- Funktionsweise: jQuery wird geladen -> jQuery--Plugin wird geladen; -> wenn Seite geladen wird, wird anonyme Funktion ausgeführt, die jQuery-Auswahl durchfürht und Plug-In-Methoden darauf anwendet
        * Bsp3 - Formulare mit jQuerey UI
            * jQuery UI führt neue Formular-Elemente ein
        ```javascript
        <input type="text" id="amount"></input> //daraus wird Schieberegler
        <input type="text" id="arriaval"></input> //daraus wird Kalendareingabe
        //jQuery dazu
        $(function(){
            $("#arrival").datepicker(); //wandelt Eingabe in JQUI-Datumsauswahl
            var $amount=$("#amount"); //Speicert div für Preiseingabe
            var $range=$("price-range");

            $("price-range").slide({ //wandelt Preiseingabe ind Regler um
                range:true,
                min: 0,
                max: 400,
                values: [175,300],
                slide: function(event, ui){
                    $amount.val("$"+ui.values[0]+"-$"+ui.values[1]);
                }
            });
            $amount
                .val("$"+$range.slider("values", 0)+"-$"+range.slider("values", 1)); //unterer + oberer Grenzwert
        });
        ```
* AngularJS = API um in DB zu schreiben
    * => angular.js einbinden im head platzieren
* Templates mit Platzhalter erstellen. Bei Änderung werden Änderungsbenachrichtigungen gesendet.
```javascript
<html ng-app></html> //<html> mit ng-app markieren
<table ng-controller="BasketCtrl"> //Name des Controllers
    <tr>
        <td>lala:</td>
        <td>{{ desctription }} </td> //Platzhalter
    </tr>
    <tr>
        <td>lala:</td>
        <td>{{ cost }} </td> //Platzhalter
    </tr>
    <tr>
        <td>lala:</td>
        <td><form type="number" ng-model="qty"></form> </td> //Platzhalter
    </tr>
    <tr>
        <td>lala:</td>
        <td> {{ qty*cost | currency }} </td> //Platzhalter
    </tr>
</table>
//AngularJS-Sckipt:
function BasketCtrl($scope){
    $scope.desctription="lala";
    $scope.cost=9;
    $scope.qty=1;
}
```
* HTML-Datei bezieht Daten aus BasketCtrl-Obj im JS-Controller. Namen die in `{{ }}` stehen, entsprechen den Eigenschaften des JS-Objekts $scope
* Wenn man in Form etwas eingibt und Fenster aktualisiert, werden die Daten im $scope gespeichert/aktualisiert
* Wenn man Daten aus anderer Datei lädt ist AngularJS nützlich
* ng-controller = Element des Gültigkeitsbereichs des Controllers festgelegt = bis zum Ende des Elements
* Bsp 2: Externe Daten
```javascript
<table id="test2" ng-controller="TimetableCtrl">
    <tr ng-repeat="session in sessions"> //Schleifendurchlauf erfolgt hier nicht in JS-Skript; sessions=JSON-Daten, session=ID, die im Template für einzelne Objekte im sessions steht
        <td>{{ session.time }}</td>
        <td>{{ session.title }}</td>
        <td>{{ session.detail }}</td>
    </tr>
</table>

function TimetableCtrl($scope, $http){
    $http.get("js/items.json"); //um Daten abzurufen = Dienst $http, $hat mehrere Methoden get(), post(), jsonp(), delete()=Daten löschen, put()=neuen Datensatz anlegen
    .success(function(data){ //Bei Erfolg die Funktion success() aufgerufen, die dem $scope JSON-Obj übergibt
        $scope.session=data.sessions;
    })
    .error(function(data){ //Bei Error wird error() aufgeführt
        console.log("error"); 
    })
}
{
    "session": [
        {"time": "09:00", "title": lala, "detail": "alal"}
        {"time": "10:00", "title": lala, "detail": "alal"}
        {"time": "11:00", "title": lala, "detail": "alal"}
    ]
}
```

* Google-Maps-API https://developer.google.com/maps = Doku zu der API
* Google erlaubt 25000 mal am Tag die Google-Maps kostenlos zu betreiben, sonst bezahlen + Schlüssel anfordern
```javascript
<div id="maps"></div>
function init(){
    var mapOptions={ //JS-Objekt in dem Maps-Parameter abgeldgt werden
        center: new google.maps.LatLng(40.787710, -73.965310),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoom: 13
    };
    var venueMap;
    venueMap=new google.maps.Map(document.getElementById("map"), mapOptions) 
    //<-neues Map-Objekt erstellen
}
function loadScript(){
    var script=document.createElement("script");
    script.src="http://maps.googleapis.com/maps/api/js?sensor=false&callback=initialize";
    document.body.appendChild(script);
}
window.onload=loadScript
//Elemente anzuzeigen/verbergen => in mapOptions festlegen
var mapOptions = {
    zoom :14,
    center: new google.maps.LatLng(40.787710, -73.965310),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    panControl: false, //ermöglichen Karte zu schwenken
    zoomControl: true, //ermöglichen Karte zu vergrößern
    zoomControlOptions: {
        style: google.maps.ZoomControlStyle.SMALL, //LARGE, DEFAULT
        position: google.maps.ControlPosition.TOP_RIGHT,
    },
    mapTypeControl: true, //Schaltet zwischen Kartentypen: Satellit usw.
    mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.DROPDOWN_MENU, //HORIZONTAL_BAR, DEFAULT
        position: google.maps.ControlPosition.TOP_LEFT
    },
    scaleControl: true, //zeigt Maßstab der Karte an
    scaleControlOptions: {
        position: google.maps.ControlPosition.TOP_CENTER
    },
    streetViewControl: false, //Pegma-Symbol, um Street-View aufzurufen
    overviewMapControl: false, //Vorschaubild = wo man Momentan in der Gesamtkarte befindet
    rotateControl: false //Karte drehen
};
/*Karte gestalten => drei Dinge angeben: featureTypes =
 Kartenmerkmale, elementTypes = Geometrie oder 
Beschriftung, stylers = Farbe, Sichtbarkeit => <- die 
Dinge werden über styles-Eigenschaft des mapOptions-Obj festgelegt
*/
styles: [
    {
        stlylers: [
            {hue: "#00ff6f"}, //Farbe Gesamtkarte
            {saturation: -50} //Sättingung Gesamtkarte
        ]
    },
    {
        featureTypes: "road", //Anzeie von Straßen
        elementType: "geometry", //Geometrie der Straßen
        stylers: [
            { lightnes: 100 },
            {visibility: "simplified"}
            
        ]
    },
    {
        featureTypes: "transit", //Anzeige öff. Verkehrsmittel
        elementType: "geometry",
        stylers: [
            { hue: 100 }, //Farbe der Beschriftung
            { saturation: -80} //Farbe der Beschriftung
            
        ]
    },
    {
        featureTypes: "transit",
        elementType: "labels", //Anzeige der Beschriftung der Verhkehrmittel
        stylers: [
            { hue: 100 },//Farbe der Beschriftung
            { saturation: +80}//Farbe der Beschriftung
            
        ]
    }    
]

//Markierungen hinzufügen:
var pinLocation=new google.maps.LatLag(40.7894532, -73.156359);
var startPostion=new google.maps.Marker({ 
    //Marker anlegen, hat Drei Parameter für Konstruktor
    postion: pinLocation,
    map: venueMap, //Map-Objekt angegeben
    icon: "img/go.png"
});
```

### 10: Fehler
* Variable ohne `var` => global
* `var1=1;` - globale Variable auch wenn innerhalb einer Funktion deklariert
* Bei Fehlern wift JS Exception => man kann Code zur dieser Fehlerbehandlung schreiben
* Fehler wird nach oben übergeben, bis Fehlerbehandlung gefunden wird => keine Fehlerbehandlung => Error-Obj erstellt und Code bricht ab
```javascript
Error.name;
Error.message;
Error.fileNumber;
Error.lineNumber
//Unterschiedliche Fehlerobjekte:
Error; //Allgemeiner Fehler
SyntaxError; //Syntax wurde nicht befolgt
ReferenceError; //Verweis auf Variable, die nicht deklariet wurde
TypeError; //Unerwarteter Datentyp
RangeError; //Zahlen außerhalb des Bereichs
URIError; //bei falscher Verwendung von encodeURI(), decodeURI();
EvalError //falsche Verwendung von eval()
```
* `Error` ist ein Prototyp(Template) <- auf dessen Grundlage alle anderen Error aufgebaut werden.
* `try, catch, throw, finally` => auf Fehler reagieren, auf die man kein Einfluss hat, z.B. wenn Code vom anderen Server hat und er down ist.

* `console.log("Parameter", var1);` - in Konsole über console-Obj etwas reinschreiben. 
* Meldungen für die Konsole unterschiedlich ausgeben
    * `console.info("Param");` - für allgemeine Informationen 
    * `console.warn("Param");` - für Warnungen
    * `console.error("Test");` - für Fehler

* Meldungen gruppieren:
```javascript
console.group("Grupp1"); //Gruppe benennen
    console.info("lala");
    console.info.name("lala2");
    console.log("lalal");
console.groupEnd(); //Gruppen-Ausgabe beenden
```
* JS-Objekte ausgeben:
    * `console.table(jsObj);`

* Bedingungen prüfen: = consle.assert()
```javascript
$("form input[type='text']").on("blur", function(){
    console.assert(this.value > 10, "Eingabe kleiner als 10"); //prüft, ob input text > 10 ist
});

//Breakpoint setzen mit debugger -> hier: breakpoint falls var1 <100
if(var1 < 100){
    debugger; 
}

//im try steht Code, der Fehler haben könnte, wenn in try steht continue,break,return => wird finally ausgeführt
try{
    var dealData=JSON.parse(response);
    showContent(dealData);
}
catch(e){
    var errorMessage=e.name+" "+e.message;
    console.log(errorMessage);
}
finally{
    var link=document.createElement("a");
    link.innerHTML="<a href='lala.html'>reload</a>";
}

//Fehler selbst auswerfen = wenn man z.B mit Daten von Dritten arbeitet => bei Fehlern lieber selbst Exception werfen
throw new Error("lala");
try{
    var area= width*height;
    if(!isNaN(area)){
        retrun area;
    }
    else{
        throw new Error("llala");
    }
    catch(e){
        console.log(e.name+" "+e.message);
        return "lala";
    }
}
```
* Validierungsseiten:
* JS: wwww.jslint.com, www.jshint.com
* JSON: www.jsonlint.com
* jQuery => Debugger-Plug-In

### 11: Inhaltspunkte
*  mit Inhaltsfelder zusätzliche Info anzeigen: Ziehharmonika, Registerkarte, modale Fenster, Bildanzeigen, Diashows
* `<html class="no-js"></html>` - Klass no-js, falls JS deaktiviert ist
```javascript
var elDoc=document.documentElement;
elDoc.className=elDoc.className.replace(/(^|\s)no-js(\s|$)/, "$1"); //Funktion, die die Klasse no-js löscht, falls JS aktiviert ist.
```
1. Zieharmonika
    * Grundlage ist `<ul> -> <li>` -> in html5 `<details>` und `<summary>`
```javascript
$('.accordion-panel').animate({
    height: 'show',
    paddingTop: 'show',
    paddingBottom: 'show',
    marginTop: 'show',
    marginBottom: 'show'
})
//Bsp:
//CSS:
//.accordion-panel{ display: none}
$('.accordion').on('click', '.accordion-control', function(e){
    e.preventDefault(); //da Button ist => preventDefault()
    $(this)
        .next('.accordion-panel');
        .not(':animated'); //prüft, ob Element gerade nicht animiert wird
        .slideToggle();
});
```
2. Registerkarte = Reiter
    * Registerkarten mit `<li>` erstellt -> Felder mit `<div>` Verknüpfung Reiter und Feld über href, Feld hat id-Att. Beide Att. müssen den selben Wert haben
* Bsp: 
```javascript
//.tab-panel{ display: none;}
//.tab-pnale.active {display: block;}
$(".tab-list").each(function(){
    var $this = $(this);
    var $tab = $this.find("li.active");
    var $link = $tab.find('a');
    var $panel = $($link.attr("href"));

    $this.on('click', '.tab-control', function(e){
        e.preventDefault();
        var $link = $(this);
        var id = this.hash; //ruft href des angeklickten Reiters ab

        if(id && !$link.is('.active')){
            $panel.removeClass('.active');
            $tab.removeClass('active');
            
            $panel=$(id).addClass('active');
            $tab =$link.parent().addClass("active");
        }
    });
});
```
3. Modale Fenster = Fenster, das vor der Seite erscheint
* Bsp:
```javascript
<div class="modal">
    //<div class="modal-content"> ... </div>
</div>
<button role="button" class="modal-close>"close </button>
//Script als Design-Muster = Modul-Muster einfügen modal-init.js
(function(){
    var $content=$('#share-options').detach();
    $('#share').on("click", function(){
        modal.open({content: $constent, width: 340, height: 300});
    });
});
//.modal{positon: absolute; z-index: 1000;}
//modal-window.js

//Modul heißt modal = ist eine Funktion, die drei Funktionen enthält
var modal=(function(){
    var $window=$(window);
    var $modal=$('<div class="modal"/>');
    var $content=$('<div class="modal-content" />');
    var $close=$('<button role="button" class="modal-close">Schließen</button>');

    $modal.append($content, $close);

    $close.on("click", function(e){
        e.preventDefault();
        modal.close();
    });

    return {
        center: function() {
            var top=Math.max($window.height()-$modal.outerHeight(), 0)/2;
            var left=Math.max($window.width() - $modal.outerWidth(), 0)/2;
            $modal.css({
                top: top+$window.schrollTop(),
                left: left+$window.scrollLeft()
            });
        },

        open: function(settings){
            $content.empty().append(settings.contetn);
            $modal.css({
                width: settings.width || "auto",
                height: settings.height || "auto",
            }).append("body");
            
            modal.center();
            $(window).on("resize", modal.center);
        },

        close: function(){
            $content.empty();
            $modal.detach();
            $(window).off("resize", modal.center);
        }
    };   
}());
```

4. Bildanzeige:
    * Klick auf Vorschaubild => Bild im Zentrum angezeigt
```javascript
<div id="photo-viewer"> </div>
<div id="thumbnails>" <a href=".../thumb-1" class="thumb active" > ... </div>
//Beim Laden der Bild class="is-loading", Ladevorgang abgeschlossen => is-loading wird gelöscht
//Bsp:
var request;
var $current;
var cache={};
var $frame = $("#phote-viewer");
var $thumbs = $(".thumb");

function crossfade($img){
    $current.stop().fadeOut("slow");
}

$img.css({
    marginLeft: -$img.width() / 2,
    marginTop: -$img.height()/2
});

$img.stop().fadeTo("slow", 1);
$current = $img;

//Cache-Obj
var cache={
    "c11/img/photo1-jpg" : {
        "$img": jQuery-Objekt, "isLoading": false
    },
    "c11/img/photo2.jpg" : {
        "$img": jQuery-Objekt, "isLoading": false
    }
}

//Bsp2:
$(document).on('click', '.thumb', function(e){
    var $img;
    var src=this.href;
    request = src;
    
    e.preventDefault();

    $thumbs.removeClass('active');
    $(this).addClass('active');

    if(cache.hasOwnClass(src)){
        if(cache[src].isLoading===false){
            crossfade(cache[src].$img);
        }
    }
    else{
        $img=$('<img/>');
        cache[src]={
            $img: $img,
            isLoading: true
        };

        $img.on('load', function(){
            $img.hide();
            $frame.removeClass('is-loading').append($img);
            cache[src].isLoading=false;
            if(request===src){
                crossfade($img);
            }
        });
        $frame.addClass('is-loading');

        $img.attr({
            'src':src,
            'alt':this.title || ''
        });
    }
});
$('.thumb').eq(0).click();
```

5. Diashow
```javascript
<div class="slide-viewer">
    <div class="slide-group">
        <div class= slide slide-1">...</div>
        ...
    </div>
</div>
//slide-viewer {position : relative; overflow: hidden; height: 300px;}
//slide-group {width: 100%; height: 100%; position: relative;}
//.slide{width: 100% height: 100%, display: none; position: absolute;}
//.slide:first-child{display: block;}
$('.slider').each(function(){
    var $this=$(this),
    var $group=$this.find('.slide-group'),
    var $slide=$this.find('.slide'),
    var buttonArray=[],
    var currentIndex=0,
    var timeout;

    function advance(){
        clearTimeout(timeout);
        timeout=setTimeout(function(){
            if(currentIndex < ($slides.length-1)){
                move(currentIndex+1);  
            }
            else{
                move(0);
            }
        }, 4000);
    }
    $.each($slides, function(index){
        var $button=$('<button type="button" class="slide-btn">&bull; </button>');
        if(index===currentIndex){
            $button.addClass('active');
        }
        $button.on('click', function(){
            move(index);
        }).appendTo('.slide-button');
        buttonArray.push($button);
    });

    advance(); //löscht Timer bevor sie ihn neustartet

    function move(newIndex){
        var animateLeft, slideLeft;
        advance();
        if($group.is(':animated')|| currentIndex === newIndex){
            return;
        }
        buttonArray[currentIndex].removeClass('active');
        buttonArray[newIndex].addClass('active');

        if(newIndex > currentIndex){
            slideLeft='100%';
            animateLeft='-100%';
        }
        else{
            slideLeft='-100%';
            animateLeft='100%';
        }
        $slides.eq(newIndex).css({left:slideLeft, display:'block'});
        $group.animate({left: animateLeft}, function(){
            $slides.eq(currentIndex).css({display: 'none'});
            $slides.eq(newIndex).css({left: 0});
            $group.css({left: 0});
            currentIndex=newIndex;
        });
    }
});
```
6. jQuery-PlugIn erstellen = jQuery-Methoden ohne Biblothek hinzufügen
    * PlugIN funtioniert so: Satz von DOM-Elementen in Form einer jQ-Auswahl übergeben. DOM mit jQuery-Plugin bearbeiten, jQuery-Objekt zurückgeben
```javascript
(function($){
    $.fn.accordion=function(speed){//jQuery hat Objekt .fn, mit dem Funktionsumfang erwetiern kann. Plugins werden als Methoden geschrieben, die zum Ojb .fn hinzugefügt werden
    return this; //jQuery-Obj zurückgeben: = mit return this.
    }
})(jQuery); //  Namespace schützen = Plugin-Code steht in IIFE

//Plug-In - Zieharmonika:
(function($){
    $.fn.accordion=function(speed){
        this.on('click', '.accordion-control', function(e){
            e.preventDefault();
            $(this)
                .next('.accordion-panel')
                .not(':animated')
                .slideToggle(speed);
        });
        return this;
    }
})(jQuery);

<ul class="menu">
    <li>
        <a href="#" class="accordion-control"> ...</a>
        <div class="accordion-panel"> ....</div>
    </li>
    <li>
        <a href="#" class="accordion-control"> ...</a>
        <div class="accordion-panel"> ....</div>
    </li>
    <li>
        <a href="#" class="accordion-control"> ...</a>
        <div class="accordion-panel"> ....</div>
    </li>
</ul>
```

### 12: Sortieren Filtern Suchen
* Daten zum Sotieren in Arrays gespeichert:
```javascript
var people=[
    {name: "Kirill", rate: 70, active: true},
    {name: "Arnold", rate: 80, active: false}
]
people[0].name;
```
* Methoden des Arrays:
    * `push()`
    * `unshift()` //hinzufügen
    * `pop()`
    * `shift()` //entfernen
    * `forEach()`
    * `some()`
    * `every()` //Druchlaufen
    * `concat()` //erstellt neues Arrays aus vorliegendem
    * `filter()` //erstellt neues Arrays aus 
    * `sort()` //sortiert anhand einer Funktion
    * `reverse()`
    * `map()` ruft Funktion für jedes Array und erstellt aus Ergebnissen neues Array
* jQuery-Methoden
* `.add()`
* `.not()` //Entfernt Element
* `.each()` //Durchläuft
* `.filter()`
* `.toArray()` //wandelt jQuery-Auswahl zum Array 

* Objekte als Eigenschaft
```javascript
var people2={
    Arnold={ rate: 70, active: true},
    Kirill={ rate: 80, active: false}
}
people2.Arnold.rate;
//Objekt aus Objekt zu entfernen delete
delete people2.Arnold;
//KindObjekte durchlaufen:
Object.keys; //???
```
* Filterung = Gruppe von Werten verkleinern:
    * Bsp 1: - Array-Obj hat Methoden zum Sortieren, Methode gibt neues Array zurück
    ```javascript
    $(function(){
        people = [
            {
                name: "Casey",
                rate: 60
            },
            {
                name: "Casey2",
                rate: 80
            },
            {
                name: "Casey3",
                rate: 120
            }
        ]
        //Bsp1
        var results=[];
        people.forEach(function(person){
            if(person.rate >= 65 && person.rate <=90){
                results.push(person);
            }
        });

        //Bsp2:
        function priceRange(person){
            return (person.rate>=65) && (person.rate<=90);
        }
        var results=[];
        results=people.filter(priceRange);

        var $tableBody=$('<tbody></body>');
        for( var i=0; i<results.length; i++){
            var person=results[i];
            var $row=$('<tr></tr>');
            $row.append($('<td></td>').text(person.name));
            $row.append($('<td></td>').text(person.rate));
            $tableBody.append($row);
        }
        $('thread').aflter($tableBody);
    });
    ```
* Dynamische Filterung = Elemente erstellen + je nach Action Elemente ein/ausblenden:
```javascript
(function(){
    var rows=[];
    var $min=$('#value-min');
    var $max=$('#value-max');
    var $table=$('#rates');
    function makeRows(){
        people.forEach(function(person){
            var $row = $('<tr></tr>');
            $row.append($('<td></td>').text(person.name));
            $row.append($('<td></td>').text(person.naem));
            rows.push({
                person:person,
                $element: $row
            });
        });
    }

    function appendRows(){
        var $tbody=$('<tbody></tbody>');
        rows.forEach(function(row){
            $tbody.append(row.$element);
        })
        $table.append($tbody);
    }
    function update(min, max){
        rows.forEach(function(row){
            if(row.person.rate>=min && row.person.rate <=max){
                row.$element.show();
            }
            else{
                row.$element.hide();
            }
        });
    }
    function init(){
        $('#slider').noUiSlider({
            range: [0,150], start:[65,90], handles: 2, margin: 20, connect: true, serialization: {to: [$min, $max], resolution: 1}
        }).change(function(){update($min.val(), $max.val()); });    
        makeRows();
        appendRows();
        update($min.val(), $max.val());   
    }
    $(init);
}());
```
* Gefilterte Bilderanzeige: = Klick auf Filternamen => entsprechende Bilder werden angezeigt 
```javascript
<img> bekommt data-tags="..., ..." = Filternamen
<img src="..." data-tags="..., ..." /> + Array tagged={ tag1: [p1.jpg, p6.jpg], tag2: [p4.jpg, p6.jpg], usw.}
    //Bsp:
    //1 tagged-Obj vorbereiten
    (function(){
        var $imgs=$('#gallery img'); //ist div
        var $buttons=$('#buttons'); //ist div
        var tagged={}; //leeres Objekt
        $imgs.each(function(){
            var img=this;
            var tags=$(this).data('tags');
            if(tags){
                tags.split(',').forEach(function(tagName){
                    if(tagged[tagName]==null){
                        tagged[tagName]=[];
                    }
                    tagged[tagName].push(img);
                });
            }
        });
    }());
    //Button-Klick:
    (function(){
        $('<button/>', {
            text: "Alle",
            class: "active",
            click: function(){
                $(this)
                    .addClass('activae')
                    .siblings()
                    .removeClass('active')
                $imgs.show();
            }
        }).appendTo($buttons);
        $.each(tagged, function(tagName){
            $('<button/>', {
                text: tagName+' ('+tagged[tagName].length+')',
                click: function(){
                    $(this)
                        .addClass('active')
                        .siblings()
                        .removeClass('active')
                }
            }).appendTo($buttons);
        });
    }());
```
* Suche:
    * Bsp: = Suche der Bilder anhand des alt-Attr von <img> + cache-Obj verwendet
```javascript
cache=[
    {element: img, text: 'lala1'},
    {element: img, text: 'lala2'}
]
    //Bsp:
    (function(){
        var $img=$('#gallery img');
        var $search=$('#filter-search');
        var cache=[];

        //Cache einrichten
        $img.each(function(){
            cache.push({
                element: this,
                text: this.alt.trim().toLowerCase()
            });
        });
        function filter(){
            var query=this.value.trim().toLowerCase(); //trim() = Entfernt Weißraum vonm Anfang und Ende des Strings
            cache.forEach(function(img){
                var index=0;
                if(query){
                    index=img.text.indexOf(query);
                }

                img.element.style.display=index===-1?'none':'';
            });
        }
        if('oninput' in $search[0]){
            $search.on('input', filter);
        }
        else{
            $search.on('keyup', filter);
        }
    }());

    //sort() = sortiert lexikografische => wenn man anders will => eigene Vergleichsfunktion schreiben = als Param sort() mitgeben. Vergleichsfunktion sollte <0, 0, >0 liefern
    //sort() vergleicht immer 2 Werte
    var prices=[1,2,125, 2, 19, 14];
    prices.sort(function(a,b){
        return a-b;
    });

    //Tabelle sortieren = nach Klick auf eine Spalte nach dieser Spalte sortieren
    //<tabel class="sortable"> ... //table muss class="sortable" haben
    //<tr> <td data-sort="name">.. </td> <td data-sort="duration">...</td> <td data-sort="date">..</td> <- SpaltenKöpfe soltlen data-sort-Attr haben
    var compare={
        name: function(a,b){
            a=a.replace(/^the /i, ''); //alle the durch '' ersetzen am Anfang
            b=b.replace(/^the /i, '');
            if(a<b){
                return -1;
            }
            else{
                return a>b?1:0;
            }
        },
        duration: function(a,b){
            a=a.split(":");
            b=b.split(":");

            a=Number(a[0])*60+Number(a[1]);
            b=Number(b[0])*60+Number(a[1]);
            return a-b;
        },
        date:function(a,b){
            a=new Date(a);
            b=new Date(b);
            return a-b;
        }
    };

    $('.sortable').each(function(){
        var $table=$(this);
        var $tbody=$table.find("tbody");
        var $contrls=$table.find("th");
        var rows=$tbody.find("tr").toArray();

        $contrls.on("click", function(){
            var $header=$(this);
            var order=$header.data("sort");
            var column;
            if($header.is("ascending") || $header.is(".descending")){
                $header.toggleClass("ascending descending");
                $tbody.append(rows.reverse());
            }
            else{
                $header.addClass("ascending");
                $header.siblings().removeClass("ascending descending");
                if(compare.hasOwnProperty(order)){
                    column=$controls.index(this);
                    rows.sort(function(a,b){
                        a=$(a).find("td").eq(column).text();
                        b=$(b).find("td").eq(column).text();
                        return compare[order](a,b);
                    });
                    $tbody.append(rows);
                }
            }
        });
    });
```

### 13: Formulare erweitern und validieren
* Hilfsfunktion IE8
* `callback` = Name der Funktion
```javascript
function addEvent(el, event, callback){
    if('addEventListener' in el ){
        el.addEventListener(event, callback, false) 
    }
    else{
        el['e'+event+callback]=callback;
        el[event+callback]=function(){
            el['e'+event+callback](window.event);
        };
        el.attachEvent('on'+event, el[event+callback]);
    }
}
```
* `<form>`
    * Eigenschaften: action, method, name, elements
    * Methoden: submit(); reset();
    * Ereignisse: submit, reset
```javascript
document.forms[i];
document.forms.formName; //bestimmte <form> ansprechen
document.forms.forms[i].elements[i]; 
document.forms.forms[i].elements.password; //bestimmtes Element der Form ansprechen
document.forms.forms[i].elements.password.value; //Werts des Formelements ansprechen

//Formular abschicken:
(function(){
    var form=document.getElementById("login"); //<form>
    addEvent(form, "submit", function(e){
        e.preventDefault();
        var elements=this.elements;
        var username=elements.username.value;
        var msg="Willkommen "+username;
        document.getElementById("main").textContent=msg; 
    });
});

//Eingabetyp ändern = type="password" in type="text"
(function(){

    var pwd=document.getElementById("pwd");
    var chk=document.getElementById("showPW"); //checkbox

    addEvent(chk, "change", function(e){
        var target=e.target || e.srcElement;
        try{ //try, da bei IE8 kann Error verursachen
            if(target.checked){
                pwd.type="text";
            }
            else{
                pwd.type="password";
            }
        }
        catch(error){
            alert("Browser unterstützt diesen Typ nicht");
        }
    });
}());

//Abschickenschaltfläche deaktivieren:
(function(){
    var form=document.getElementById("newPwd"); //<form>
    var password=document.getElementById("pws"); //type="password"
    var submit=document.getElementById("submit");

    var submitted=false; //Wurde form shcon verschickt?
 
    submit.disabled=true; //deaktivieren "Abschicken"
    submit.className="disabled"; //formatiert "Abschicken"

    addEvent(password, "input", function(e){ //Bei Passwordeingabe
        var target=e.target || e.srcElement; //Ereignisziel
        submit.disabled=submitted || !target.value; //legt disabled fest
        //WEnn form schon verschickt oder Pwd keinen Wert: disabled
        submit.className=(!target.value || submitted) ? "disabled" : "enabled";
    });
    //WEnn Abschicken: Deaktivieren form, um erneutes verschicken verhindern
    addEvent(form, "submit", function(e){ //beim abschicken
        if(submit.disabled || submitted){ //wenn deaktiviert oder gesendet
            e.preventDefault();
            return;
        }
        submit.disabled=true; //deaktiviert abschicken
        submitted=true; //aktualisiert submitted
        submit.className="disabled"; //ändert Stil

        e.preventDefault();
        alert("Passwort ist "+ password.value);
    });
});
```

//S 593 = Polyfill-Skript= wenn Broswer bestimmte Features nicht unterstützt => wird Ausweichskript ausgeführt
//<- z.B oft Verwendet: Modernizer + Yepnope