### 0 - Introduction
### 1 - Setting up the development environment
* Editor -> Brackets
* jQuery heruterdaden->
    * es gibt zwei Versionen
        1. kompremiert für Production
        2. normal für Development (besser zum Debugen)
    * man sollte Beide herunterladen
* Server, damit man Ajax-Servieren kann
* 
### 2 - What is jQeury
* hat: 
    1. AJAX
    2. Content Manipulation
    3. Animationen
* Szenarien für jQuery:
    1. Initial Initialisierung
    2. User-Aktion
    3. Teile der Seite updaten
    4. usw.
* benutzt CSS-Syntax
* man kann an Sets von Elementen arbeiten
* man kann sie mit Plugins erweitern (eigene bilden)

### 1 - A Quick Introduction to jQeury
#### 1 - Your first jQuery-enabled page
#### 2 - Selectors and filters
#### 3 - Creating and modifying page content
#### 4 - Handling events
#### 5 - Animating page content
#### 6 - Working with AJAX

### 2 - Working with Page Content
#### 1 - Overview of selectors and filters
* Selectoren - Elemente finden
* Filter - gefundene Elemente filtern/spezialisieren
#### 2 - Basic selectors
* Syntax:
    * 
    ```javascript
    $("tagName")
    $("#id")
    $(".className")
    $("tagName.className") //TagName, das Klasse "className" hat
    $("tag#id.className") //Tag Element, das id und clasName hat 
    $("*") //alle Elemente auswählen
    ```
* Bsp:
    * 
    ```javascript
    $("p").css("border", "3px solid red");
    $(".a").css("border", "3px solid red"); //alle Elemente, die Klasse "a" haben
    $("#example).css("border", "3px solid red");
    4("p.b").css("border", "3px solid red"); // <p class="b">
    ```
#### 3 - Basic filters
* müssen auf einen Selector angewendet werden
* `:first`, `:last`
* `:even`, `:odd`
* `:gt()`, `:lt()` `:eq()` - greater than, less than, equal param
* `:animated` - Items, die geraade animiert werden, z.B um die Animation zu stoppen
* `:focus` - Element, dass gerade Fokus hat
* `not(filter-expr)`
* Bsp:
```javascript
$("example p:first").css("border", "3px solid red"); 
$("example p:last").css("border", "3px solid red"); 
$("example p:even").css("border", "3px solid red"); 
$("example .a:first).css("border", "3px solid red"); 
$("example .b:even").css("border", "3px solid red"); 
$("example p:not(p:eq(2))").css("border", "3px solid red"); //<p>, dass nicht den index 2 hat, (<p> werden als Array aus DOM geholt)
```
#### 4 - Advanced selectors
* Child-Selector: `$("div > p")` - wähle `<p>`-s, wenn es Child von `<div>`-s
* Descendent: `$("div p.a")` - wählen `<p class="a">`-s die irgendwo in `<div>`-s sind.
* JSON-Selector: `$("ul + div")` - wähle `<div>`-s, die direkt nach `ul`-s kommen
* Nächst Sibling: `("#paral1 ~ p")` - wähle `<p>-`-s, dessen vorheriger Nachbar `id=paral1` ist

#### 5 - Attriburte filters:
* `$("p[class]")css("border", "3px solid red");` - Attrubte-Filter wird in `[]` gesteckt. Also wähle `<p>` der Attribute `class` hat (der Wert von `class` ist egal)
* `$("p[id=paral1]")css("border", "3px solid red");` - wähle `<p>`, dass `id=paral1` hat.
* `$("p[id^=para]")css("border", "3px solid red");` - wähle `<p>`, dass mit `id=para*` beginnt.
* `$("p[id^=para][lang*=en-").css("border", "3px solid red");` - wähle `<p>`, dass mit `id=para*` beginnt und `lang=*en*` irgendwo in `lang` enthält.

#### 6 - Advanced filters:
* Containt-Fitler`("p:containts('3')").css("border", "3px solid red");` - `<p>`-s auswählen, die im Inhalt *3* haben
* Parent-Fitler: `("p:parent").css("border", "3px solid red");` - `<p>`-s auswählen, wenn es *Parent* ist, d.h. weitere HTML-Elemente haben, oder einen Inhalt/Text
* has-Filter: `("div:has(p[class=a])").css("border", "3px solid red");` - wählre `<div>`-s die `<p class="a">` haben.
* Child-Filter: `$("div p:first-child").css("border", "3px solid red");` - wähle `<p>`-s, die erstes Kind von `<div>` sind
* `$("div p:last-of-type").css("border", "3px solid red");` - wählen `<p>`-s die in `<div>` sind und die letztes `<p>` innerhalb diesen `<div>`s sind
* `$("div p:nth-child(3)").css("border", "3px solid red");` wähle `<p>`-s aus, die 3-tes Kind in `<div>` sind
* `$("div p:nth-child(2n)").css("border", "3px solid red");` wähle jedes zweite`<p>` aus, die in `<div>` sind
* es gibt auch weitere Filter
#### 7 - Traversing documents with jQeury
* DOM - ist API
* jQuery - bildet Layer über DOM um die DOM-elemente zu erreichen:
    1. ausgwähltes Element
        * `prev()` - Element, das vor dem ausgewählt Element liegt
        + `next()` - Element, das nach dem ausgewählt liegt
        + `parent()`
        * `parents()` - alle Übergeordnete Eltern
        * `parentsUntil($("HTML")) - alle Eltern bis `<html>`
        * `children()`
            * `$("#example").children().css("border", "3px solid red");` - wähle alle Children von `#example` und wende die `.css()` auf diese an
    * Bsp:
    ```javascript
    var elem = $("#para1");
    elem.prev().css("border", "3px solid red");
    elem.next().css("border", "3px solid green");
    //elem.parents()..css("border", "3px solid blue");
    elem.parentsUntil($("body")).css("border", "3px solid red");


    ```
    2. Find:
        * `$("#example").find("#para4").css("border", "3px solid red");` - Wähle `#example` und suche ab da `#para4` und wähle auf gefundenes Element `.css()` an
    3. Each:
    ```javascript
    var leftmargin = 0;
    var border = 3;
    $("example p").each(function(index, element){
        $(elemement).css("border", border+"px solid red").css("margin-left", leftmargin);
        border += 2;
        leftmargin +=10;
    })
    ```
    *  `each()` ist eine Call-Back-Funktion, die auf jedes gefundene Element angewendet wird also auf jedes `<... id=example"> <p> ...`

#### 8 - jQuery statement chaining
* mehrere Funktionen auf ausgewählten Elemente hintereinadner schalten. Geht von Links nach Recht
#### 9 - Programming challenge
+ HTML-Elemente haben Attribue `data-type="meinTyp"` - (Aber eventuell ist das eigenes Attribur für eigene Zwecke) z.B für Element-Auswahl benutzen
* Funktionen in jQuery
```javascript
$(function(){
    //
})
```
### 3 - Manipulating Page Content
#### 1 - Creating content
* `$("#example").html()` - wenn ohne Parameter, dann holte den Inhalt des Element und verändert nichts
* Bps:
```javascript
$("document").ready(function(){

    document.getElementById("create").addEventListener("click", function (evt){
        createContent();
    });

    document.getElementByID("chante").addEventListener("click", function(evt){
        changeContent();
    });

    document.getElementById("changeAll").addEventListener("click", function(evt){
        changeAllTheContent();
    });

    function createContent(){
        $("#example").html("<p>Hi There </p>");

    }

    function changeContent(){
        var newItem = $("<p>This is an ew paragrah</p>");
        $("#para1").html(newItem);
    }

    function changeAllTheContent(){
        $("#example p").text("<p>I've changed all the paragraph</p>");

    }
});

```
#### 2 - Inserting page content
* zwei Wege:
    1. Innerhalb eines Elements/Objekts
    2. Relativ zum Element
* Inserts: `<p>This is a paragraph.</p>`
 ```javascript
    //append() //Einfügen nachher
    $("p").append("New content");
    $("New Content.").appendTo("p");
    //prepand() //Einfügen befor
    $("p").prepend("New content");
    $("New Content.").prependTo("p");
    //before()
    $("p").before("<p>New Content</p>");
    $("<p>New Content</p>").insertBefore("p");
    //after()
    $("p").after("<p>New Content</p>");
    $("<p>New Content</p>").isertAfter("p");

```
#### 3 - Alerting page content
* Bsp:
```javascript
$("document").ready(function(){
    $("#example p").wrap("div style='color:red'"); //wrappt (hüllt um) hier div wird (#example p)-s umhüllen
    $("#example p").wrapAll("div style='color:red'"); //hüllt um den Parent von (example p)-s
    $("#example").empty(); //Element-Inahlt leeren
    $("#exmaple p.a, #exmaple p.b").remove();

    $("<div>replaced</div>").replaceAll("#example p[id]"); //alle #example <p id="..."> werden ersetzt
    $("#example p[id]").replaceWith("<div>replaced</div>");
    $("#example p").replaceWith(replacementFn); //Funktion replaceFn aufrufen -> ist eine Call-Back-Funktion d.h. wird für jedes #example <p>
    function replacementFn(){
        if ($(this).text().indexOf("1") != -1) {
            return "<p>This is paragrahp uno <p>";
        } 
        else{
            return this.outerHTML;
        }
    }

})
```
#### 4 - Manipulating attributes
* jQuery-API-Doku schauen, wenn man nach Funktionen usw. sucht
* `attr(Att, [Wert])` - Wert des Attributs lesen, wenn Attribute nicht da, dann udnefiniert, Wenn Wert mitangegeben, wirt Wert erstetzt.
* Bsp:
```javascript
$("document").ready(function(){
    $("#example").after("<p id='alts'>"); //nach id=example wird <p id="alts" eingefügt></p>

    $("img").each(function(){
        $("#alts").append($(this).attr("alt") + " ");
    }); //für jedes <img> in id=alts den Wet von <img alt=xxx> einfügen

    $("a").attr("title", "Photo by some photographer"); // für jedes <a> title="Photo by some photographer" setzen

    $("a").attr("target", "_blank"); // Attribute target="_blank" einfügen


    $("a").removeAttr("href");
    $("img").attr({src: "images/Spring.jpg", title: "Spring all the things"}) //mit {..} mehrere Attribute ändern -> alle <img> bekommen dieses Attribut 

});

```

#### 5 - Working with CSS
* `.css()` 
    1. `css(cssName)` - Wert von CSS-Attr
    2. `css(cssName, wert)` - CSS-Wert erstetzen
    3. `css(cssName, funkt)` - Wert von CSS-Attr ist return von funkt
    4. `css(propertyObj)` - CSS-Attr-Wert-Paare setzen
* `.hasClass(className)`
* `.addClass(className)`
* `.removeClass(className)`
* `.toggleClass(className)` 
* Bsp:
```javascript
// #xxxXxxx - sind Buttons mit id=xxxXxxx
$("document").ready(function(){
    $("#setProp").click(function(evt){
        $("#example").css("text-decoration", "overline)
            .css("font-size", "+=1pt");
    });
    $("#setProps").click(function(evt){
        $("#example p").css({
            "font-weigth": "bold",
            "color": "red"
        })
    });
    $("#addCl").click(function(evt){
        $("#example p").addClass("pClass");
    });
    $("#rmCl").click(function(evt){
        $("#example p").removeClass("pClass");
    });
    $("#toogleCl").click(function(evt){
        $("#example p").toggleClass("pClass");
    });


});

```
#### 6 - Embedding custom data
* HTML-Attr `data-xxx` - *xxx* kann man nennen wie man will bzw. in der Doku schauen
* in jQuery-Doku -> Data auswählen:
    1. `.data(key, value)` - Wert ändern 
    2. `.data(key)` - Wert lesen
* Bsp:
```javascript
$("document").ready(function(){
    document.getElementById("show").addEventListener("click", function(evt){
        alert(JSON.stringify($("#example").data(),null, "  ")) //data-xxx-Wert in Alert anzeigen in JSON-Format
    });

    document.getElementById("store").addEventListener("click", function(evt){
        $("#example").data("key1", 1234); //data-key1=1234 einfügen
        $("#example").data("key2", "Lala"); //data-key2=Lala einfügen
    });

    document.getElementById("remove").addEventListener("click", function(evt){
        $("#example").removeData(); //alle data-xxx löschen
        $("#example").removeData("key2") //nur data-key2 löschen
    });
});
```
#### 7 - Programming challenge
* Lösung:
    * für die Checkboxen wurden `<form>` ohne *action* und *method* hinzugefügt mit Checkboxen darin.
    * Für die Checkboxen für *click*-EventListener hinzugefügt mit `function(evt){ updateProduct("data-xxx-Wert", evt.target.checked);}`
    * 
    ```javascript
    function updateProduct(categoryName, bVisible) {
        var dataSelectorVal = "";
        switch(categoryName) {
            case "Wert1":
            dataSelectorVal = "h2[data-xxx-Wert1='Wert1']";
            break;
            case "Wert2":
            dataSelectorVal = "h2[data-xxx-Wert2='Wert2']";
            break;
        }

        $(".product-item").has(dataSelectorVal).css("display", bVisible ? "" : "none");
    }

### 4 - jQuery Events
#### 1 - jQuery event handling features

#### 2 - Bilding and unbinding events
* kann man in der Doku von jQuery unter Events schauen: (Event Handler Attachements)
    * hier werden nur `on()` `off()` benutzt 
    * man kann `on()` auf mehrere Arten aufrufen:
        1. event
        2. selector
        3. data
        4. handler-funktion
* Bsp: 1 und 4
```javascript
$(function(){
    $("$evtTarget").on("mouseover mouseleave", highlight);

    function highlight(){
        $("#evtTarget").toggleClass("highlighted");
    }
    /*
    $("$evtTarger").on("click", function(evt){
        $("#evtTarget").off("mouseover mouseleave", hightlight);
        $("#evtTarget").html("<p>Hover effect shut of </p>");
        $("#evtTarger").removeClass("highlight")
    })
    */

    $("#textEntry").on("keypress", function(evt){
        $("'keyPress").text(String.fromCharCode(evt.charCode));
    });
});
```

#### 3 - Event helper features
* in der Doku nach Events -> Browser Events schauen
* in der Doku nach Events -> Form-Events schauen
* in der Doku nach Events -> Key-Events schauen
* Bsp:
```javascript
$(function(){
    $("#evtTarget").hover(highlight, highlight); //highlight wird aufgerufen, wenn auf dem Element und wenn Element verlassen wird
    function highlight(){
        $("#evtTarget").toggleClass("highlighted");
    }

    $("#evtTarget").click(fnClick);
    $("#evtTarget").dblick(cnClick2);
    function fnClick(){
        $("#evtTarget").html("Click");
    }
    function fnClick2(){
        $("#evtTarget").html("Double Click");
    }

    //Window-Events:
    $(window).rezise(fnResize);
    function fnResize(){
        $("#evtTarget").html("Browser window resized");
    }

    $("#evtTarget").one("click", function(){
        $(this).css({borderWidth: "4px", curser: "pointer" })
    }) //.one wird nur einmal ausgeführt
});
```
* weiter Funktionen ausprobieren
#### 4 - Using the jQuery event object
* API-Doku -> Event -> Event-Object
* Bsp:
```javascript
$(function(){
    $("Div1").on("click dbclick", {name: "Div 1"}, function (evt){ //hier wird mit name ein Parameter überbegen, der den Namen des Elements enthält
        updateEventDetails(evt);
        evt.stopPropagation(); //den Event stopen, damit er eventuell Browser-Default-Handler nicht triggert
    })
    $("Div2").on("click dbclick", {name: "Div 2"}, function(evt){
        updateEventDetails(evt);
        evt.stopPropagation();
    })
    $("Div3").on("click dbclick", {name: "Div 3"}, function(evt){
        updateEventDetails(evt);
        evt.stopPropagation();
    })

    $("div.smallbox").on("mouseenter", function(evt){
        updateEventDetails(evt);
        evt.stopPropagation();
    })
    $("div.smallbox").on("mouseleave", function(evt){
        updateEventDetails(evt);
        evt.stopPropagation();
    })
    $("div.smallbox").on("mousemove", function(evt){
        updateEventDetails(evt);
        evt.stopPropagation();
    })

    $("#input1").keypress(updateEventDetails);

});

function updateEventDeatails(evt){
    $(".detailLine span[id]").text(""); // alle span- die id="..." in class="detailLine" haben, werden geleert
    $("#evtType").text(evt.type);
    $("#evtWhich").text(evt.which);
    $("#evtTarget").text(evt.target.id);

    if(evt.relatedTarget) {
        $("evtRelated").text(evt.relatedTarget.tagName + "#" + evt.relatedTarget.id);
    }

    $("#evtPageX").text(evt.pageX);
    $("#evtPageY").text(evt.pageY);
    $("#evtClientX").text(evt.clientX);
    $("#evtClientY").text(evt.clientY);
    $("#evtMetaKey").text(evt.metaKey);

    if (evt.data){
        $("#evtData").text(evt.data.name); //das ist diese mitgegebene Parameter name
    }

}
```

#### 5 - Progamming challenge
1. Beim Klick wird der Image und der ProduktName aus `<h2>` ausgelesen und in in den `<a href="URL-Link">` eingefügt für jedes Element der Seite, das weiterleiten soll.
2. auf der Weitergeleiteten Seite werden die benötigen Infos aus der URL herausgezogen (überwiegend in JS)

### 5 - Animations and Effects
#### 1 - Introduction and Effects
* jQuery Doku -> Effects -> Basics/Fading/Sliding/Custom(eigene Animationen erstellen)
#### 2 - Hiding and showing elements
* Bsp:
```javascript
$(funtion(){
    $("#show").click(function(){
        //$("#theDiv").show(); //ohne Animation
        $("#theDiv").show("fast", "linear"); //man kann hier auch 
    });

    $("#hide").click(function(){
        //$(#"theDiv").hide();
        $(#"theDiv").hide(1000, "swing"); //in Millisek
        //man kann auch Easing-Typ mitgeben 
    });
    
    $("#toggle").click(function(){
        $("#theDiv").toggle("slow", completion); //completion ist Funktion die am Ende aufgerufen wird
    })

    function completion(){
        $(this).text("Animation Complete");
    }
});
```
#### 3 - Fading elements
* Bsp:
```javascript
$(funtion(){
    $("#fadein").click(function(){
        $(#"theDiv").fadeIn(); 
        $(#"theDiv").fadeIn(200); 
    });

    $("#fadeout").click(function(){
        $("#theDiv").fadeOut();
        $("#theDiv").fadeOut(600); 
    
    $("#fadeto3").click(function(){
        $("#theDiv").fadeTo(300, 0.3); //zu welcher Opacity gehen soll (zeit, zuWelcherOpacity)
    })
    $("#fadeup").click(function(){
        $("#theDiv").fadeTo(300, 1.0); //zu welcher Opacity gehen soll
    })

    $("#pulse").click(function(){
        //mit fadeTo() pulse erstellen
        $("#theDiv").fadeTo(300, 0.3)
        .fadeTo(300, 1.0)
        .fadeTo(300, 0.3)
        .fadeTo(300, 1.0, onComplete);

    })

    function onComplete(){
        $(this).text("Animation Complete");
    }
});
```
#### 4 - Sliding elements
* 
```javascript
$(function(){

    $("slideUp").click(function(){
        $("#theDiv").slideUp();
        $("#theDiv").slideUp(1000);
    })

    $("slideDown").click(function(){
        $("#theDiv").slideDown();
        $("#theDiv").slideDown(110);
    })

    $("toogle").click(function(){
        $("#theDiv").slideToggle("slow");
    })
})

```
#### 5 - Custom animations
* dafür werden Low-Level-Funktionen benutzt. man kann dann *width*, *height* usw animieren
* dafür wird `animate()` verwendet. Man kann ihr viele Parameter übergen
* zwei WEge die Funktion aufzurufen
    1. `animate(properties, duration,, easing, complete)` - am Object, das animiert wird
        * duration => 400ms, slow, fast
        * easing => swing, linear
        * complete => Callback for completion (optional)
    2. `animate(properties, parameters)` - 1. Param = Object, 2. Param = Werte die animiert werden, ist mächtiger
* default Unit ist `px`
```javascript
$(function(){
    $("#right").click(function(){
        $("#theDiv").animate({width: "500px"},1000);
    });
    $("#text").click(function(){
        $("#theDiv").animate({fontSize: "24px"}, 100);
    });
    $("#move").click(function(){
        $("theDiv").animate({left: "500"}, 1000, "swing");
    });
    $("#all").click(function(){
        $("theDiv").animate({
            left: "+=500",
            //left: "500px";
            fontSiez: "24px",
            width: "200%"
        },1000, "swing");
    });
)}

```

### 6 - AJAX Operations
#### 1 - jQuery and AJAX
* man kann theoretisch auch "Go Live Server" benutzen um Ajax zu testen
* jQuery - Dokue -> jQuery.ajax() checken
    * eigentlich mach Requst und warten auf Daten
* Tests:
    * Datei. `testdata.txt` und `testxmldata.xml` erstellen
* 
```javascript
$("document").ready(function(){
    getData();
});

function getData(){
    $.ajax({
        url: "testdata.txt",//URL für den Zugriff zum Daten
        type: "GET",//Typ der Anfrage
        dataType: "text",//Typ der erwarteten Daten
        success: successFn, //Callback-Funkt, wenn alles OK
        erros: errorFn,
        complete: function(xhr, status) {
            // CallBack, wenn alles abgearbeitet wird, egal of success oder error. Diese Params sind Pflicht 
            console.log("The request ist complete);
        }
    })
}

function successFn(result){
    console.log("Setting result");
    $("#ajaxContext").append(result);
}
function errorFn(xhr, status, strErr){ //Diese Params sind Pflicht 
    console.log("Error passiert");
}
```
#### 2 - Convenience functions
* jQuery-Dokur -> Schorhand Methods = Methoden, die oft benutze werden
* 
```javascript
$("document").ready(function(){
    getData();
});

function getData(){
    $.get("testdta.txt", successFn);
    $.("#ajaxContent").load("testdata.html"); //nimmt Daten und fügt sie in das Element ein
    
    //bei .load() kann man sagen, dass man nur bestimmten Teil der Daten anzeigen soll
    $("ajaxContext").load("testdata.html #p2"); //Datei testdata.html und id=p2 anzeigen
}

function successFn(result){
    console.log("Setting result");
    $("#ajaxContext").append(result);
}
function errorFn(xhr, status, strErr){ //Diese Params sind Pflicht 
    allert(strErr)
}
```
#### 3 - Working with different data types
* Bsp: mit JSON-Daten + XML-Daten
```xml
<!--testxmldata.xml-->
<data>
    <name>Kirill</name>
    <title>jQuery Test</title>
</data>
```
```javascript
$("document").ready(function(){
    getXMLData();
    getJSONData();
})

function getJSONData(){
    var flickrAPI = "http://api.flickr.com/sevices/feeds/photos_public.gne?jsoncallback=?"; //Flick-Public API als JSON-Datei wird benutzt; Hier ist nur der Link
    $.getJSON(flickrAPI, {
        tag: "space needle",
        tagmode: "any",
        format: "json"
    }, successFn); //wird bei Flickr nach Images gefragt, die besonders getaggt sind. Konvertiert die Daten schon zu javascript-Format
    
}

function getXMLData(){
    $.get("testxmldata.xml", function(result){
        var title = result.getElementsByTagName("title").[0];
        var name = resuslt.getElementByTagName("name").[0];
        var val = title.firstChild.nodeValue + "by" + name.firstChild.nodeValue;
        $("#ajaxContent").append(val);
    }); 
}
function successFn(result){
    $.each(result.items, fucntion(i, item){
        $("<img>").attr("src", item.media.m).appendTo("#ajaxContext");
        if (i === 4){
            return false;
        } //break für $.each()
    })
}
function errorFn(xhr, status, strErr){ //Diese Params sind Pflicht 
    allert(strErr)
}

```
#### 4 - Using global AJAX handlers
* Operatioen zentralisieren.
    * z.B alle Errors zentralisieren
* auf Ajax-Events hören
* benutzt Ajax global Events
+ jQuery-Doku -> Global event Handler
    * 4 Funktionen für Events
* Ajax-Request = Event
* Ajax-Requst - Lifecycle: (globale Events)
    1. Ajax-Requst to send
    2. Requst about to be send
    3. Request Succeeds or Request Fails 
    4. Request Completed
    5. All Request ended
```javascript
$("document").ready(function(){
    //Events registireren
    $(document).ajaxStart(function(){
        console.log("Ajax starting");
    });
    $(document).ajaxStop(function(){
        console.log("Request ended");
    });
    $(document).ajaxSend(function(evt, jqXHR, options){
        console.log("About to send request for data");
    });
    $(document).ajaxError(function(evt, jqXHR, settings, err){
       console.log("Error happend");
    });
    $(document).ajaxComplete(function(evt, jqXHR, options){
       console.log("Everything finished");
    });
    $(document).ajaxSuccess(function(evt, jqXHR, options){
       console.log("Request was OK");
    });
    getData();
});

function getData(){
    $.get("testdta.txt", successFn);    
}

function successFn(result){
    console.log("Setting result");
    $("#ajaxContext").append(result);
}
function errorFn(xhr, status, strErr){ //Diese Params sind Pflicht 
    allert(strErr)
}
```
#### 5 - Programming challenge
```javascript
$.getJSON("product-data.json").done(function(prodData){
    // code
})
```
### Fazit
* Doku checken
* 
