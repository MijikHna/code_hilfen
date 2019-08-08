//API = ermöglichen Interaktion zwishcen Mensch und Programm = externe Programme auffordert etwas zu tun und die Antwort verarbeiten
//z.B DOM und jQuery sind API-es; DOM-Funktionalität ist in JS-Interpreter eingebaut

//1)
//HTML5-API = HTML5 bietet neue MarkUps + neue JS-APIs = stellt Objekte bereit, die für bestimmte Funktionalität gedacht sind

//man sollte Prüfen, ob Browser entsprechende API unterstützt
if(navigator.geolocation){
    //...
}
else{
    //...
}

//Modernizer: = Skript um zu ermitteln, ob Browser HTML-, CSS- und JS-Merkmale unterstützt -> eingesetzt um festzustellen, ob Browser bestimmte APIs unterstützt.
//1) von modernizr.com herutnerladen
//2) Einbinden auf der Seite: = ein Modernizer-Object wird erzeugt. Eigenschafte des Objects sind die Merkmale 
//3) if(Modernizr.geolocation) <- liefert true/false zurück

//Ortungs-API: = z.B über die IP-Adresse ermittelt/Mobilfunkantenne/GPS-Hardware
//steht in allen Browsern zur Verfügung
//nutzt Object geolocation
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
    //Bsp:
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

//Webspeicher-API
//1=lokale Speicherung, 2=Sitzungsspeicherung
//vor HTML5 nur Cookies (1=nur wenige Daten, 2=bei jeder Aufforderung einer Seite Daten zum Server gesendet, 3=unsicher)
//=> in HTML5 zwei Spiecherobjekte 1)localStorage, 2)sessionStorage <- Unterschied wie lange Daten gespeichert werden
//meistens 5MB pro Domäne in einem Speicherobjekt -> mehr => Browder fragt den Benutzer
//Seiten verfolgen bei der Speicherung Same Origin Policy = auf Daten kann nur von derserlben Domäne zugegriffen werden. z.B map.google.de !=google.de
//Es gibt auch noch APIs für DB-Zugriff z.B Web-SQL
//localStorage und SessionStorage sind im window-Obj implementiert
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

//Verlaufs-API und Pushstate
//URL jedes Tabs werden zur URL-Liste des Tabs hinzugefügt = in history-Obj gespeichert
//history.pushState(state, title, url);  = der URL-Liste URL manuell hinzufügen (z.B bei Ajax-Aufrufen)
//history.replaceState() = Listeneintrag ändern
//onpopstate = um die richtige Seite aufzurufen über location-Obj oder -state-Info möglich
//location.pathname
history.back() //Verlauf zurück
history.forward() //Verlauf vorwärts
history.go(-2) //Verlauf um Parameter zurück/vorwärts
history.pushState();
history.replaceState();
history.length
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

//Skripts mit APIs = APIs verwenden um mit Skrpits zu arbeiten
//z.B Skrpits zur Gestaltung von Schiebereglern, Fenstern, Tabellensortierern
//Bsp: 1)jQuery-Plugin jQuery UI; 2) AngularJS=Vereinfacht Entwicklung von Web-Apps
//jQuery-Plugins = Skripts, die jQuery-Objekte neue Methoden hinzufügen => jQuery + Plugin auf die Seite einfügen
    //jQuerey UI = Bundel von Plugins
    //1)jQuery + jQuerey UI einbinden (jqueryui.com) <- evneutell nur Teile von jQueryUI einbinden
        //Bsp 1: Zieheharmonika:
        //1)HTML-Code strukturieren, 2)welche Elemente jQeury auswählen soll. 3)welche jQeuery UI-Methoden aufrufen
        //zu eins 
        //<div id="prizes">
        //<h3>Preis 1</h3>
        //<div> ...</div>
        //<h3>Preis 2</h3>
        //<div>...</div>
        //</div>
        $(function(){
            $("#prizes").accordion();
        });
        //Bsp2: Registerkarten
        //<div id="prizes">
        //<ul>
        //<li><a href="#tab-1">...</a> </li>
        //<li><a href="#tab-2" ...>...</a> </li>
        //</ul>
        //<div id="tab-1"> ...</div>
        //<div id="tab-2">...</div>
        //</div>
        $(function(){
            $("#prizes").tabs();
        });
    //<- Funktionsweise: jQuery wird geladen -> jQuery--Plugin wird geladen; -> wenn Seite geladen wird, wird anonyme Funktion ausgeführt, die jQuery-Auswahl durchfürht und Plug-In-Methoden darauf anwendet
        //Bsp3 - Formulare mit jQuerey UI
        //jQuery UI führt neue Formular-Elemente ein
        //HTML
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

//AngularJS = API um in DB zu schreiben
//=> angular.js einbinden im head platzieren
//Templates mit Platzhalter erstellen. Bei Änderung werden Änderungsbenachrichtigungen gesendet.
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
//HTML-Datei bezieht Daten aus BasketCtrl-Obj im JS-Controller. Namen die in {{ }} stehen, entsprechen den Eigenschaften des JS-Objekts $scope
//Wenn man in Form etwas eingibt und Fenster aktualisiert, werden die Daten im $scope gespeichert/aktualisiert
//Wenn man Daten aus anderer Datei lädt ist AngularJS nützlich
//ng-controller = Element des Gültigkeitsbereichs des Controllers festgelegt = bis zum Ende des Elements
//Bsp 2: Externe Daten
<table ng-controller="TimetableCtrl">
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

//Google-Maps-API https://developer.google.com/maps = Doku zu der API
//Google erlaubt 25000 mal am Tag die Google-Maps kostenlos zu betreiben, sonst bezahlen + Schlüssel anfordern
<div id="maps"></div>
function init(){
    var mapOptions={ //JS-Objekt in dem Maps-Parameter abgeldgt werden
        center: new google.maps.LatLng(40.787710, -73.965310),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoom: 13
    };
    var venueMap;
    venueMap=new google.maps.Map(document.getElementById("map"), mapOptions) //neues Map-Objekt erstellen
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
//Karte gestalten => drei Dinge angeben: featureTypes = Kartenmerkmale, elementTypes = Geometrie oder Beschriftung, stylers = Farbe, Sichtbarkeit => <- die Dinge werden über styles-Eigenschaft des mapOptions-Obj festgelegt
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
var startPostion=new google.maps.Marker({ //Marker anlegen, hat Drei Parameter für Konstruktor
    postion: pinLocation,
    map: venueMap, //Map-Objekt angegeben
    icon: "img/go.png"
});