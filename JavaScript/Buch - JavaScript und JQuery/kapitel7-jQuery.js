//man kann jQuery und JS kombinieren
//$() = jQuery() = ein Objekt jQuery erstellen
//Methoden wirken sich auf alle ausgwählten Elemente => müssen nicht in einer Schleife durchlaufen werden
$(":header").addClass("headline") //Überschriften auswählen h1 bis h6
$("li:lt(3)").hide().fadeIn(1500) //erten drei li auswählen Elemente verstecken + langsam einblenden
$("li").on("click", function(){
    $(this).remove();
}); //beim Click auf li wird this Element entfernt
//jQuery Selectoren:
//* 
//element
//#id
//.class
//selecto1, selector2
//Hierarchien:
//Eltern Kind
//Eltern > Kind //oder * für alle Kinder
//vorheriges + nächstes //wählt Element aus, die auf vorheriges folgen
//vorheriges ~ Geschwister //alle Geschwistern
//Filter:
//:not(Selektor) //Alle Elemente außer in (...) z.B div:not("id1")
//:first = erste Element der Auswahl
//:last = letzte Element der Auswahl
//:even = Elemente mit gerader Indexnummer in der Auswahl
//:odd
//:eq(Index)
//:gt(Index)
//:lg(Index)
//:header = h1 bis h6
//:animated = zurzeit animierte Elemente
//:focus = Element, das zurzeit den Fokus hat
//:contains("Test")
//:empty = Elemente ,die keine Kinder haben
//:parent = Element mit einem Kindknoten
//:has(Selector) = z.B div:has(p)
//Sichtbarkeit:
//:hidden
//:visible
//Kindfilter:
//:nth-child(Ausdruck) = zählung beginnt nicht bei null sondern bei Ausruck
//:first-child
//:last-child
//:only-child = wenn das Element nur ein Kind hat
//Attributfilter:
//[attribut] = Element mit angegeben Attribut
//[attribut="Wert"]
//[attribute!="wert"]
//[attribute^="wert"] =wert beginnt mit diesem Wert
//[attribute*="wert"]=wert steht irgendwo im Attributwert
//[attribte|="wert"]=
//[attribute~="wert"]=Wert sollte einer der Wert getrennt durch Leerzeichen sein
//[attribut1][attribute2] = Element die mit allen selektren übereinstimment
//Formularfilter:
//:input
//:text
//:passwort
//:radio
//:chechbox
//:submit
//:image
//:reset
//:button
//:file
//:selected
//:enabled
//:disabled
//:checked
//Wenn jQuery-Auswahl nichts findet => keine Fehler, sondern wird nichts gemacht
$("ul") //=liefert Verweis auf einen einzigigen Elemen Knoten; index = 0
$("li") //liefert Verweis auf jQuery-Array: Index: 0, 1, 2 usw.

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

//Prüft ob Seite bereit ist um Hier Code auszuführen. Wenn bereit ist wird function(){} ausgeführt => muss nicht am Ende von Body platiert werden
$(document).ready(function(){
    //Hier Code
}); //oder so schreiben 
$(function(){
    //Hier Code
});
//ready() prüft ob DOMContentLoaded unterstützt, das ausgelöst wird wenn DOM geladen wurde. Wenn unterstützt wird erstellt jQuery Ereignislistener dafür. Auf ältern Browsern wird auf Ereignis load gewartet

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

//den Tag Attribute hinzufügen/entfernen .attr(), .removeAttr()
$("li#id1").attr("class"); //dem li#id1 Attribut class einfügen
$("li#id1").attr("class", "class1") //class=class1 hinzufügen
$("li#id1").removeClass("class1");
$("li#id1").addClass("class2");

//css-Eigenschaften abrufen+ändern
var backgrColor=$("li").css("background-color"); //liefert backgroundColor des ersten Treffers
$("li").css("background-color", "#272727"); //werden alle alle background-color auf 272727 gesetzt
$("li").css({
    "background-color": "#272727",
    "font-familiy": "Courier"
}); //mehrere css ändern

//mehrere Sachen an allen Objekte ausführen:
$("li").each(function(){ //each ist sowas wie Schleife
    var ids=this.id; //JS sosnt ids=$(this).attr("id")
    $(this).append('<em class="order">'+ids+'</em>');
}) //each bekommomt als Param eine anonyme Funktion, this = zeigt auf gerade ausgewähltes element <- man dann hier auch JS verwenden

//Ereignisse: = on()
$("li").on("click", function(){
    $(this).addClass("class2");
}); //onclick für li mit anonymen Funktion registrieren, kann auch benannte Funktion sein

$("li").on("mouseover click", function(){ //Funktione für mehrer Ereignisse registrieren
    //..
});

//Ereignisse + Event-Objekt
$("li").on("click", function(e){
    eventType=e.type;
});
//hat etwas andere Eigenscaften wie JS Event:
//type = Art des Ereignisses
//which = betätigte Taste
//data = 
//target = DOM-Element, in dem das Ereignis aufgetreten ist
//pageX = Mauspositon
//pageY = Mausposition
//timeStamp = Millisek seit 1970
//.preventDefault() = Verhindert Standardverhalten
//.stopPropagation() = verhindert die Weiterleitung des Ereignisses an die Vorfahren (Bubbling)
//Bsp:
$(function(){
    $("li").on("click", function(e){
        var date = new Date();
        date.setTime(e.timeStamp);
        var clicked = date.toDateString();
        $(this).append("<span>"+clicked+" "+e.type+"</span>");
    });
});

//on() kann nach ertem Param. weitere Param annehmen zum Filtern der Elemente für die Funktion registriert werden soll
//on(events[, selector][, data], function(){});
//früher wurde delegate() verwendet
//Bsp: click für alle außer letzten li registrieren
$(function(){
    $("li").on("click mouseover", "not:(#vier", {status: "important"}, function(e){
        //..
    });
});

//Effekte = Übergänge + Bewegungen:
//Element ein/ausblenden:
//.show()
//.hide()
//.toggle() //Schaltet die Sichtbarkeit des Elements um
//Ein/Ausblenden 2:
//.fadeIn() = blendet ein
//.fadeOut() =blendet aus
//.fadeTo() = ändert die Deckkraft
//.fadeToggle() = schaltet die Deckkraft des Objekts in Gegenteil um
//Verschieben:
//.slideUp() = schiebt Element in Blickfeld
//.slideDown() = schiebt Element aus dem Blickfeld
//.slideToggle() 
//Benutzerdefinierte Effekte:
//.delay() = verzögert die Ausführung der nachfolgenden Einträge in eine Warteschlage
//.stop() = hält eine laufende Animation an
//.animate() = erstellt benutzerdefinierte Animation
//zur Animation kann man auch CSS3 verwenden
//Bsp:
$("h2").hide().slideDown();
var $li=$("li");
$li.hide().each(function(){
    $(this).delay(700*index).fadeIn(700); //in ms
});
$li.on("click", function(index){
    $(this).fadeOut(700);
})

//animate() =eigne Animationen = Änderung der CSS-Eigneschfaten, CSS-Eigenschaften werden in Camelschreibweise geschrieben
/*
.animate({
    
}[, speed][, easing][, complete]); speed=Dauer der Animation + zwei Schlüsselwörter(slow,fast, easing=linear/swing, complete=Funktion nach der Ausführung ausführen
*/
//Bsp: opacity ü paddin-left animieren
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

//DOM duchlaufen: = von einer Auswahl auf andere Elemente zugreifen
//Param=Selector erforderlich
//.find() = Alle Elemente in der Auswahl mit mit Selector übereinstimmern
//.closest() = nächster Vorfahr
//Param=Selector optional
//parent()
//parents() = Alle Eltern
//children() =
//.siblings()
//.next()
//.nextAll()
//.prev()
//.prevAll()
//<- bei mehrerer Auswahl werden auf alle Elmente ausgeführt => kommische Ergebnisse
//Bsp:
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

//Elemente einer Auswahl hinzufügen:
//.add()
//.filter() = Findet Elemente die mit einem Selector(Param) übereinstimmen
//.find() = Findet Nachkommen, die mit Selector übereinstimmen
//.not()/:not() = Findet Elemente, die mit Selctor nicht übereinstimmen
//.has()/:has() = Findet Nachkommen, die mit Selecotor übereinstimmen
//:contains() = 
$("li").not(".hot").addClass("cool"); //= 
$("li:not(.hot)").addClass("cool");
//.is() = Prüft, ob Auswahl eine Bedingung erfüllt
//Bsp: = wählt Listeneinträge + wendent Filter daraus an
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

//Einträge anhand Indexnummer finden:
//Elemente in haben intern eine Indexnummer, beginnt bie 0:
//Methoden anwenden .eq(), :lt(), :gt()
var $li=$("li") // => alle li-es

$("li:lt(2)").removeClass("hot");
$("li").eq(0).addClass("cool");

//Formularelemente-Selektoren -> sind aber langsam => Lösung: davor einen CSS-Selektor voranstellen
//:button, :chechbox, :checked = Kontollkästchen, Optionsschalter, :disabled = alle deaktivieren Elemente, :enabled, :focus, :file = Alle Dateielemente, :image => bessere Lösung [type="image"], :input => bessere Lösung .filter(":focus"), :password => Bessere Lösung $('input:password'), :radio => bessere Lösung $('input[name="gender"]:radio'), :reset = Reset-Button, :selected = Alle markierten Elemente => bessere Lösung = .filter(":selected"), :submit, :text => bessere Lösung ('input:text'), 
//Methoden: 
var newVar1=$("input:text").val(); //.val() = für input,select,textarea; Wert des ersten Elements eine Auswahl abrufen + darin enthaltenen Elemente ändern 
//.filter() = filtert jQuery-Auswahl mit zweitem Selektor (für formualerspezifische Filter)
//.is() = häufig mit Filtern eingesetzt, um zu prüfen, ob Formularfeld markiert/ausgewählt wird
$.isNumeric(1); $.isNumeric("1"); //prüft, ob Werte nummerisch ist true wenn ja; <- globale Funktion 
//.on() = handhabt alle Ereignisse
//Ereignisse: blur = verliert Fokus, change, focus, select = Option eines select-Elements ändert sich, submit
$("#newItemButton").on("submit", function(e) {
    //..
});

var $newItem1=$("#newItemButton"); //Element in Variablen speichern
$("showForm").on("click", function(){
    $newItem1.show(); //Element anzeigen .hide() = Element verstecken
});

//Elemente ausschneiden/kopieren
$(function(){
    var $p=$("p");
    var $cloneQuote=$p.clone(); //Element klonen = Kopieren <- bei ID-Elemente => muss man sie verändern, da sonst ID nicht eindeutig
    $p.remove(); //Element löschen
    $cloneQuote.insertAfter("h2"); //
    var $moveItem=$("#one").detach(); //Löscht Element, speichert aber das Element ab
    $moveItem.appendTo("ul");
});

//Abmessungen = Breite/Höhe der Elemente ändern
var $hoehe=$("#id1").height();
$("#id1").height(125); //Höhe setzen
$("#id1").height("50%"); 
var $breite=$("id1").width();
$hoehe=("id1").innerHeight(); //Höhe mit Padding
$hoehe=("id1").outerHeight(); //Höhe mit Padding und Border 
$hoehe=("id1").outerHeight(true); //Höhe mit Padding und Border und Margin

//Browserfenster
var $WinHoehe=$(window).height();
var $docHoehe=$(document).height();
var offset=$("div").offset(); //.position() = liefert Objekt mit .top und .left offset()=vom Fenster, position()=vom Vorfahren, der aus dem Fluss rausgenommen wurde. 
var offsetX=offset.left;
var offsetY=offset.top;
var gescrolltY=$(windows).scrollTop();
var gescrolltX=$(window).scrollLeft();

//jQuery einbinden
//1)über Internet einbinden = CDN=Content Delivery Network
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script>
    window.jQuery || document.write("script src="js/jquery-1.10.2/js"><\/script>) 
</script> //als Option einbinden, falls das Laden von jQuery vom externen Server nicht klappt
//Scripts ab besten vor dem schließendem </body> einbinden
//http://api.jquery.com = Documentation zu jQuery
//http://plugins.jquery.com = Liste mit Scipts, die jQuery-Funktionsumfang erweitern
//Es gibt viele Bibliotheken, die auch $ benutzen => dieses Konfikt so lösen:
//1)jQuery als letztes einbinden => $ gilt für letzte Bibliothek
//2)jQuery.noConflict(); vor dem jQeury-Script ausführen + im Scipt jQuery.xxx() nutzen .noConflict() = $ wird freigegeben
//3)Sktipt in IIFE einschlien:
jQuery.noConflict();
(function($){
    //...
})(jQuery);
//4 eigenen Alias erstellen
var $j=jQuery.noConflict();
$j(document).ready(function(){

});
