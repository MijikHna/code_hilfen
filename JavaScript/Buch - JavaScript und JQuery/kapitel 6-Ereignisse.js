//Ereignisse:
//U-Erreignisse (User Interface = UI)
//load = Laden der Seite ist abgeschlossen
//unload = Webseite wird entladen, wenn andere Seite aufgerufen wurde
//error = JS-Fehler ist aufgetreten
//resize = Größe des Browsers wurde geändert
//scroll = Benutzer hat gescrollt
//keydown = Benutzer drückt eine Taste
//keyup = Benutzer lässt Taste los
//keypress = Zeichen wird eingefügt
//click = Mausklick
//dblclick = Double Click
//mousedown = Maus drücken
//mouseup = Maus loslassen
//mousemove = Benutzer verschiebt die Maus
//mouseover = Maus auf ein Element bewegen
//mouseout = 
// <- on+oberenNamen bei HTML-Ereignissen

//Fokusereignisse:
//focus/focusin = Element enthält Fokus
//blur/focusout = Element verliert Fokus
//input = Wert von <input> hat sich verändert
//change = Wert eines Auswahlfelds hat sich geändert
//submit = Benutzer schickt Formular ab
//reset = Benutzer resetet Fromular
//cut = Benutzer schneidet Inhalte aus Formularfeld aus
//copy
//paste 
//select = Benutzer markiert Text in einem Formularfeld

//Veränderungs-Ereignisse = wenn Script DOM ändert
//DOMSubtreeModified = Dokument wurde geändert
//DOMNodeInserted = Knoten wird als direktes Kind eines anderen Knotens eingefügt
//DOMNodeRemoved = 
//DOMNodeInsertedIntoDocument = Knoten wurde als Nachfahre eines anderen Knoten eingefügt
//DOMNodeRemovedFromDocument = Nachfahre eines anderen Knotens wurde entfernt

//UI-Ereignise = betrefen window = BrowserFenster

//Drei Mögichkeiten um Ereignisse zu binden:
//1)<a onlick="funkt1();"> //<- veraltet => Besser ist JS und HTML zu trennen
//2)DOM-Ereignishandler //Nachteil mit einem Ereignis nur eine Funktion binden
//3)DOM-Ereignishandler Level 2 //


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
//Ereignisfluss:
//1) von Element zum windows = normaler Fluss
//2) vom windows zum Element = z.B bei IE 8
elem.addEventListener("click", funkt1, false) //false = Fluss von innen nach außen(Bubbling), true=von außen nach ihnen (IE 8)=Ereigniserfassung

//Event-Objekt = gibt Info über Ereignis und das Element bei dem Es auftrat
//wird an die Funktion im Ereinishander oder -listener übergeben
//erhägt oft den Namen 
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
//Event bei IE 5-8
//event-Objekt bei IE steht wird nicht automatisch an Ereinishandler/listener übergeben, steht aber als Kind des window zur Verfügung
function funkt5(e){
    if(!e){
        e=window.event;
    }
    var target=e.target || e.srcElement;
}

//Ereingisdelegierung = am Eltern hören, ob beim Kind Ereingis auftrat => mit event.target herausfinden, bei wem das Ereignis auftrat = <- Verbesset die Leistung
//<-- manchmal wird statt event.target this. verwendet <- funktioniert solange Funktion keine Parameter hat bzw. keine anonyme Funktion ist.

//Es gibt drei EreinisArten:
//DOM-Ereingisse
//HTML5-Ereignisse z.B für submit = für HTML-Element
//BOM-Ereinisse = Browser Object Model = Ereignisse des Browsers z.B. Ereinsisse für Tousch-Screen-Gereäte

//Ereignisse der Benutzer-Schnittstelle (UI) = betreffen Browserfenster
//load = Laden der Seite abgeschlossen
//unload = Webseite entladen wird
//error = JS-Fehler passiert
//resize = Größe des Browsers verändern
//scroll = Benutzer scrollt
function setup(){
    var textInput=document.getElementById("x");
    textInput.focus(); //Fokus auf textInput legen
}
window.addEventListener("load", setup, false);

//Formular-Ereignisse:
//focus = Input bekommt den Fokus
//blur = Input verliert den Fokus <- Nutzlich um Tipps dem User zu geben + zur Formularvalidierung = Verbieten des Wechsels bei falscher Eingabe

//Mouse-Ereignisse 
//mousedown + mouseup = für Drag und Drop

//Posion der Maus herausfinden
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

//Tastaturereignisse
//input
//keydown
//keypress
//keyup
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
//Formularereignisse:
//submit, change, input, focus, blur
//change = z.B. bei Drop-Down-Menu

//Änderung des DOM
//Änderungsereignisse => werden durch Ändrungsbeobachter ersetzt
//DOMNodeInserted
//DOMNodeRemoved
//DOMSubtreeModified
//DOMNodeInsertedIntoDocument
//DOMNodeRemovedFromDocument

//HTML5-Ereignisse
//DOMContentLoaded = wenn DOM-Baum aufbebaut ist <- alternative zu load, da nicht wartet bis Inhalt der Seite geladen wurde
//hashchange = URL-Cash ändert sich, an window gebunden, nach der Änderung weist event.oldURL und .newURL die alteun und neue URLS zu
//beforeunload = z.B Nutzer hinweis geben, dass Änderungen am Formular nicht gespeichert wurden