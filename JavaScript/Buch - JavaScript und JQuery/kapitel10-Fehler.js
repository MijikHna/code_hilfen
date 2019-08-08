//Variable ohne var => global
var1=1; //globale Variable auch wenn innerhalb einer Funktion deklariert
//Bei Fehlern wift JS Exception => man kann Code zur dieser Fehlerbehandlung schreiben
//Fehler wird nach oben übergeben, bis Fehlerbehandlung gefunden wird => keine Fehlerbehandlung => Error-Obj erstellt und Code bricht ab
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
//Error ist ein Prototyp(Template) <- auf dessen Grundlage alle anderen Error aufgebaut werden.
//try, catch, throw, finally => auf Fehler reagieren, auf die man kein Einfluss hat, z.B. wenn Code vom anderen Server hat und er down ist.

console.log("Parameter", var1); //in Konsole über console-Obj etwas reinschreiben. 
//Meldungen für die Konsole unterschiedlich ausgeben
console.info("Param"); //für allgemeine Informationen 
console.warn("Param"); //für Warnungen
console.error("Test"); //für Fehler

//Meldungen gruppieren:
console.group("Grupp1"); //Gruppe benennen
    console.info("lala");
    console.info.name("lala2");
    console.log("lalal");
console.groupEnd(); //Gruppen-Ausgabe beenden

//JS-Objekte ausgeben:
console.table(jsObj);

//Bedingungen prüfen: = consle.assert()
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

//Validierungsseiten:
//JS: wwww.jslint.com, www.jshint.com
//JSON: www.jsonlint.com
//jQuery => Debugger-Plug-In