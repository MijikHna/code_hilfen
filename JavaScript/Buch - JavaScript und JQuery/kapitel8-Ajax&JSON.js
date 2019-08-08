//für Live-Suche=automatische Vervollständigung meist Ajax
//Ajax arbeitet asynchrone
//Wenn im HTML <script> vorkommt hält Browser an und verarbeitet alles was im <script> steht
//bei Ajax fordert Browser beim Server nur Daten an und geht weiter = asynchrone
//Wenn der Server die Daten erhalten hat => wird Ereignis load ausgelöst, der z.B eine Funktion aufrufen kann
var xhr=new XMLHttpRequest(); //Instanz des HttpReq-Objekts erstellen
xhr.open("GET", "data/test.json", true); //bereitet die Anforderung vor, GET=HTTP-Methode, data/test.json=URL der Seite; true=Anforderung asynchron
xhr.send("search=arduino"); //Sendet die Anforderung; Param=zusätzliche Info, sonst null
//Antwort verarbeiten:
xhr.onload=function(){
    if(xhr.status==200){
        //:::
    }
}
//Für Antworten gewöhnlich drei Formate:HTML=am leichtesten zu verarbeiten,XML, JSON
//XML-DAtei kann man mit DOM-Methoden verarbeiten
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

//JSONP = in <script>-Element, das Daten vom Server lädt <- Funktioniert,da keine Einschränkung für Quelle von script = hier Funktion die Daten anfordert
//CORS = dem Header zusätzlich Info hinzufügen, um dem Browser und Server mitzuteilen, dass sie kommunizieren sollen

//JSONP => Daten werden als Script übergeben => parse()/stringify() nicht nötig
//Funktion meistens als GET übergeben:
//http://lala.de/lala.php?callback=showEvents
//ZUR Sicherheit kann man Timer für die Abfrage von dritten Servern implementieren.

//jQuery und Ajax - zwei Schritte 1)Anforderung 2)Antwort verarbeiten
$("#id1").load("lala.html #id1") //$(..)=jQuerey Objet wird erstellt, wo neues HTML-Element erscheinen soll, "lala.html" = Seite von der man Code laden möchte, #id1=Element(-e) der Seite, die man laden möchte
//liefern jQuery-Objekt = jqXHR-Obj
var jQObj=$.get() //=mit GET-Methode Daten vom Server laden -> Param. (url[, data][, callback][, type])
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

//alle diese Funktion greifen auf .ajax() zurück
//<- diese Funktionen werden durch Laden oder Eingabe in Formular ausgelöst

//Bsp: 
$("#id1").on("click", function(e){
    e.preventDefault();
    var queryString="vote="+event.target.id;
    $.get("votes.php", queryString, function(data){
        $("id1").html(data);
    });
});

//Formular mit Ajax = .post() + .serialize()
var var1=$("#id1").serialize(); //serialisiert zu versendende Daten = 1) wählt alle Info im Formular aus, 2) stellt alles als String dar, 3)kodiert die Zeichen <- kann auf einzelne Felder oder ganzes <form> angewendet werden

//auf der Serverseite kann man mit X-Requested-With prüfen, ob Seite durch Ajax-Aufruf angefordert wurde = wenn Header XMLHttpRequest hat
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