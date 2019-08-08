//Kapitel 2:
var today=new Date();
var hourNow=today.getHours();

var el=document.getElementById("id1");
el.textContent="text";

//js in Html einbinden:
//<script src="nameJS-Script.js"></script>
var message="<a href=\"nameHtml.html\"> Text <\/a>";
el.innerHTML=message; 

el.className=true; //className kann true/false annehmen => z.B für CheckBoxen => checked, unchecked
var array1=[1,2,3];
var array2=new Array(1, 2);
array1[i];
array1.item(i); //nur lesender Zugriff
array1.length;

//Funktionen:
function funktName1(){

}
funktName1();
function funktName2(var1, var2){

}
funktName2(x, y);
//unmittelbar aufgerufene Funkt:
var varF1=(function(){

}());
//anonyme Funkt
var varF2=function(var1, var2){
    return var1*var2;
};
var var3=varF2(x, y);

//Objekte:
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
//Klasse-Def erstellen => mehrre Obj. erstellbar
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
//this:
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

varX; //Ohne Schlüsselwort var wird globale Variable erstellt

//Direkt Obj erstellen sinnvoll: 1) Daten zwischen Anwendungen speichern/übertragen, 2)für globale Obj. und für Konfigurations-Obj, die Infos für die Seite einrichten.

//integrierte Obj=Browser-Obj:
//1) Browser Object Model=Objekte, die das aktuelle Fenster/Tab darstellen => z.B Browserverlauf, Bildschrim des Geräts
//2) DOM
//3) Globale JavaScript-Objekte = für Dinge, die JS braucht, um Modell zu erstellen z.B Objekte für Datum und Zeit
//ObjektModell = Gruppe von Objekten
//zu 1): Window -> Document=aktuelle Webseite, History=Seite im Browser-Verlauf, Location=location-URL der aktuellen Seite, Navigator=info über den Browser, screen=Info über die physische Anzeige Bsp;
window.print();
window.screen.width;
//zu 2):
document.lastModified; //wann die Seite zum letzten Mal aktualisert wurde
//zu 3): String, Number, Boolean, Date, Math, Regex=für Mustervergleiche bei den Strings:
var1.toUpperCase();
Math.PI();
//zu 1);
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
//zu 2) oberste Obj in DOM ist document
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
//6 Datentypen: String, Number, Boolean, Undefined= Var deklariert, aber kein Wert zugewiesen, Null, Object => kann man die Eigenschaften + Methoden dieser Objekte verwenden
//Arrays sind Objekte, es gibt viele Methoden für Array-Objekte
//Number:
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
//Date-Obj:
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
//Kapitel 4
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
//falsy-Werte = die zu false konvertiert werden können
//truthy-Werte = die zu true konvertiert werden können + vorhanden eines Objekt = truthy
var artist="Rembrandt"; //truthy
var artistA=(artist||"Unbekannt"); //artistA wird =artist
artist=""; //falsy
var artistA=(artist||"Unbekannt"); //artistA wird ="Unbekannt" gesetzt
value1=0;
value2=1;
value3=2;
if(value1||value2||value3){

}
//<- Logische Operatoren geben nicht immer true oder false zurück, sondern geben Wert zurück, der Vararbeitung angehalten hat
document.getElementById("id").innerHTML=message1; //geht auch so
