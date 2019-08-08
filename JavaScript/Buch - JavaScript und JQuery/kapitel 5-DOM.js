//DOM = auch Anwendungs-Programmmierschnittstelle = API
//über Benutzerschnittstellen können Menschen mit Programmen interagieren
//über APIs können Programme miteinader kommunizieren
//DOM = was Skript über aktuelle Seite fragen bzw. deren Inhalt verändern kann
//DOM = 4 Haupttypen: Dokumentknoten (Oberster Knoten=gesamte Seite) -> Elementknoten (=Tag) -> Attributenknoten(=id, class usw.) -> Textknoten 

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

//XCC-Angriffe = wenn Benutzer Eingaben macht, die Schaden verursachen, die dann auf der Seite plaztiert werden:
//1)Eingaben validieren auf der Seiten
//2)Eingaben prüfen auf dem Server
//nichts in <script>, <!-- --> <... href="..."> <div ..=..> {color: ...}
//URL-Eingaben prüfen + encodeURIComponent() verwenden um Sonderzeichen zu maskieren
//innerHTML nicht verwenden => textContent, innerText
//html() (JQuery) nicht verwenden => text()

var attClass=document.getElementById("x").getAttribute("class"); //liefert Wert des Attributs class
document.getElementById("one").hasAttribute("class") //prüft, ob Attribut "class " hat
document.getElementById("x").setAttribute("class", "classX"); //fügt "class" den Wert classX zu
document.getElementById("x").className="classX" //erstetzt "class" auf classX
document.getElementById("x").removeAttribute("class");

//Entwicklertools:
//für Firefox: DOM Inspector(googeln), Firebug-Erweiterung