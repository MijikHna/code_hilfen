### 2 - Handling Client-Friendly CSV
* es gibt schon fertige Funktionen in jeder Sprache um mit .csv-Dateien umzugehen
### 3 - Exploring XML
#### 1 - Understanding XML structure
* wird z.B in Web-RSS verwendet
* ist Markup Sprache (von SGML)
* ist text-basierend
* Doku auf W3C
* besteht aus TAG + [ATTRIBUTE]
    * hat open-TAG + closing-TAg
    * es gibt auch Empty-TAGS (nur open-TAG)
    * TAG-Namen komplett dem Entwickler überlassen
    * 4 character Entities:
        1. &lt; kleiner
        2. &gt; größer
        2. &amp; prozent
        4. &quot; 
* Verwendung:
    * UBL (Universal Business Language)
    * Universal Plug and Play (UPnP)
    * Word-processing formats: ODF + OOXML
    * SVG
* XML:
    * DTD + namespaces
    * XML Styling besteht aus:
        * XSLT - transforms XML to HTML und andere
        * xPath - targets XML content and computes values
        * XSL-FO (Extansible Stylesheet Language) - formats XML data für Output auf verschiedenen Medien
#### 2 - Saving data as XML
* Bsp in PHP
```php
<?php
    if(isset($_POST["submit"])) { // checken, ob submit-Button geklickt wurde
        $file = "data.xml";
        $userNode = "student"; //Name des Main-Nodes in XML-Datei 

        $doc = new DOMDocument("1.0"); // DOM-object anlegen
        $doc->preserveWhiteSpace = false;
        $doc->load($file); //in dieses DOM-Objet den Inahlt von der .xml-Dateie laden
        $doc->formatOutput = true;

        $root = $doc->documentElement; //Root-Element aus XML hier speichern

        $post = $_POST; // statt jedes Mal $_POST zu schrieben jetzt einfach $post
        unset($post["submit"]) //aus dem Array das Element "submit" löschen
        
        $user = $doc->createElement($userNode);
        $user = $root->appendChild($user);

        foreach($post as $key => $value){
            $node = $doc->createElement($key, $value);
            $user->appendChild($node);
        }
        //als String speichern und ins Datei speichern
        $doc->save($file) or die("Sorry, Probelem saving the file");
        header("Location:thanks.php");
    }

?>
```
```xml
<?xml version="1.0"?> <!--data.xml -->
<students>
    <!-- User responses follow --> 
</students>
```
* der Kommentar ist notwendig, das Root-Node nicht leer sein darf
#### 3 - Retrieving and displaying XML data
* es gibt verschiede Wege XML-Dateien auf der Web-Seite zu parsen
* hier wird jQuery benutzt + mit Ajax die .xml vom Server holen
```javascript
$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "data.xml",
        dataType: "xml",
        success: xmlParser
    });
});

function xmlParser(xml){
    $("#load").fadeOut();
    $(xml).find("painting").each(function(){
        $("#container").append('<div class="painting"><img src="images/' + $(this).find("image").text() + '" width="200" height="225" alt="' + $(this).find("title").text() + '" /> <br/> <div class="title">'  + $(this).find("title").text() + '<br/>$' +  $(this).find("price").text() +'</div></div>'); //für jedes gefundenes Node den Pfad zu Image und title für alt holen und Preis holen
        $(".painting").fadeIn(1000); 
    });
}
```
#### 4 - Enhanced styling with XSLT
* stylet und tranformiet XML
* 
```XML
<?xml version="1.0"?> <!-- data.xml -->
<?xml-stylesheet type="text/xsl" href="index.xslt" ?> <!-- Stylesheet einfügen>
<paintings>
    <painting>
        <title>Boeardwalk 5</title>
        <image>ap1.jpg</image>
        <price>850</price>
    <painting>
        <title>A Lasting Piece</title>
        <image>ap2.jpg</image>
        <price>450</price>
    </painting>
</paintings>
```
```xslt
<?xml version="1.0" encondings="UTF-8"?><!--index.xslt -->
<xsl:stylesheet version="1.0" xmlns:xsl="http:www.w3.org/1999/XSL/Transform">
<xsl:template match="/">     
<html xmlns="http://www.w3.org/1999/xhtml">
<!-- weiter wie normales HTML -->
    <div id="container">
        <!-- xml-loop -->
        <xsl:for-each select="paintings/painting">
            <h2><xsl:value-of select="title" /></h2> <!-- xsl:xsl-funktion-->
            <p style="margin-bottom:40px;">
                <img>
                    <xsl:attribute name="src">images/<xsl:value-of select"image" /></xsl:attribute>
                </img>
            </p>
        </xsl:for-each>
    </div>
</html>
</xsl:template>
</xsl:stylesheet>
```
* hier wird data.xml in index.xslt eingebunden. 
### 4 - Incorporating JSON (enhalten, gründen, einbauen, miteinbeziehen)
#### 1 - Setting up JSON data
* JavaScript Object Notation
* benutzt JS-Sytax ist aber platform-unabhängig
* Daten: name/value
* Name ist immmer String
* value = Stirngs, Numbers, Booleans, Arrays, JSON-Obj, null
* `eval()` - JSON in JS-Objekt konvertieren
* `JSON.parse()` ist besser/sicherer als `eval()`
* `JSON.stringify()` JS-Obj nach JSON umwandeln
* wird in Ajax benutzt
#### 2 - Interacting with JavaScript
```json
{
    //root JSON-Object
    "paintings": { 
        //JSON-Object
        "painting": [
            {
                "title": "Brodwark 5",
                "artist": "Arnie Palmer",
                "image": "ap1.jpg",
                "price": 850
            },
            {
                "title": "A Lasting Piece",
                "artist": "Arnie Palmer",
                "image": "ap2.jpg",
                "price": 450
            }
        ]
    }
}
```
```javascript
$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "data.json"
        dataType: "json"
        success: jsonParser
    });
});

function jsonParser(json){
    $("#load").fadeOut();
    $.getJSON("data.json", function(data){
        $.each(data.paintings.painting, function(key,value){
            var title = value.title;
            var img = value.image;
            var price = value.price;
            $("#container").append('<div class="painting"><img src="images/'+img+'" width="200" height="225" alt="'+title+'" /> </br> <div class="title">'+title +'<br/>$'+price+'</div></div>');
        });
    });

}
```
#### 3 - Tools for working with JSON
* in der PHP-Doku nach JSON-Bibs schauen
```php
<?php
    if(isset($_POST["submit"]){ //ob Button Submit geklickt wurde
        $file = "data.json"
        $jsonString = json_encode($_POST, JSON_PRETTY_PRINT);
        file_put_contents($file, $jsonString,FILE_APPEND);
        header("Location:thanks.php");
    })
?>
```
#### 4 - Tools for working with JSON
* JSON-LInt - www.jsonlint.com - JSON-Syntax checken
* Bootlaod für JSON: jsoneditoronline.org - Interpretiert die JSON-Daten als Object-Baum
* XML nach JSON `utilities-online.info/xmltojson
### 5 - Invertigating YAML
#### 1 - Understanding YAML
* ist *Ain't Markup Language*
* yaml.org - ist in YAML geschrieben
* Struktur wird durch Leerzeichen, **keine TABs** und Enter vorgegeben. Braucht keine `"`
* man kann in ymal direkt Code einfügen
* fast jede Sprache hat einen YAML-Interpreter
#### 2 - Creating a YAML data file (mit PHP)
* 
```php
<?php
    //es wrid Bib spyc benötigt (Code auf github)
    include("spyc.php");
    if(isset($_POSS["submit"])) {
        $file = "data.yml"
        unset($_POST["submit"]);
        $yaml = spyc::YAMLDump($_POST);
        file_put_contents($file, $yaml, FILE_APPEND);
        header("Location:thanks.php");
    }

?>
```
* `---` in yaml trennen einezelnen Record in .yaml-Datei 
#### 3 - Parsing YAML with JavaScript
* also Yaml mit JS parsen -> JS-Library nötig von github jeremyfa/ymal.js holen
* davor noch yaml.js einfügen
```javascript
$(document).ready(function(){
    var yamlFile = YAML.load("data.yaml");
    $.each(yamlFile.paintings.painting, fucntion(key, value){
        var title = value.title;
        var img = value.image;
        var price = value.price;

        $("#container").append('<div class="painting"><img src="images/'+img+'" width="200" height="225" alt="'+title+'" /> </br> <div class="title">'+title +'<br/>$'+price+'</div></div>');
    });
});
```
```yaml
---
paintings:
 painting:
  - title: Broadwalk 5
    artist: Arnie Palmer
    image: ap1.jpg
    price: 850
  - title: A Lasting Piece
    artist: Arnie Palmer
    price: ap2.jpg
    image: 450
...
```
#### 4 - Working with YAML tools
+ es gibt anderes YAML, was in CSS verwendet wird
    * wenn man in google nach normalem yaml googeln möchte => excluden css: `-css` z.B `yaml tools -css`
1. yaml-online-parser.appspot.com - yaml validieren + nach json/python/canonical yaml konvertieren
2. i-tools.org/unserialize - auch ein Converter etwas nach ymal konvertieren
### 6 - Applying HTML5 Solutions
#### 1 - What's available in HTML 5
* in HTML5: neue Attribute: `data-****`
    * sind Custom-Attributes
    * werden mit JS-Funktionen gelesen:
        * `getAttribute();`
        * `setAttribute();`
        + JS API Eigenschfte: `dataset()`
* viele neuen Typen für `<input>`
* Storage
    * hinzufügt "state" zu Webseiten ohne Server-Side Coding
    * wird in Browser gespeichert
    * 5MB maximal
    * Name-Value-Pair (nur Strings)
    * Commands:
        + `localStorage.setItem("ItemName", "ItemValue);`
        + `lcoalStorage.getItem("Itemname");`
* `<datalist>`
#### 2 - Utilizing local storage
* um States der Seiten zu speichern, ohne Backend anzusprechen
* 
```javascript

function desiredCourseChanged (e){
    target = e.target;
    theValue = target.value; 
    //hier beginnt die Speicherung
    localStorage.setItem("desiredCourse", theValue);
}
function artistLengthChanged (e){
    target = e.target;
    theValue = target.value;
    //hier beginnt die Speicherung
    localStorage.setItem("artistLength", theValue);
}
function hoursPracticeChanged(e){
    target = e.target;
    theValue = target.value;
    //hier beginnt die Speicherung
    localStorage.setItem("hoursPractice", theValue);
}

$(document).ready(function(){
    //...
    var theDesiredCouse = localStorage.getItem("desiredCourse");
    theDesiredCourse = "<strong>Desired:</strong> " + theDisiredCourse
    $("#desiredCouse").html(theDesiredCourse);
    //gleiche für zwei andere Storages
    var theArtistLength = localStorage.getItem("artistLength");
    theArtistLength = "<strong>Artist:</strong> " + theArtistLength
    $("#artistLength").html(theArtistLength);
    //...    
});
```
* im Dev Tool kann man den Inhalt von LocalStorage ansehen: Resources -> Local Storage -> http://localhost
* auch Zahlen werden als Strings gespeichert
#### 3 - Incorporate data-attributes
* Bsp: drei Video werden nach einander abgespielt, in dem per jQuery `data`-Attribut geändert wird
* Bsp:
```html
<div id="videoContainer">
    <video width="480" height="270" controls poster="image/videoPoster.png">
        <source src="assets/main.mp4" type="video/mp4" />
        <source src="assets/main.webm" type="video/webm" />
        <source src="assets/main.ogv" type="video/ogg" />
    </video> 
</div>
```
* 
```javascript
var videos, soruces, i, l, orgi, current, modified;
sources = document.getElementByTagName("source");
for(i=0; l=sources.length; i<l; i++){
    orig = sources[i].getAttribute("src");
    sources[i].setAttribute("data-orig", orig); //erstelt neues Attribute data-orig=orig
    sources[i].setAttirbute("src", orig.replace(/(\w+)\.(\w+)/, "bumper-in.$2")); //ersetzt Wert von src
}    
videos = document.getElementsByName("video");
for(i=0, l=video.length; i<l; i++){
    videos[i].load();
    modified = false;
    videos[i].addEventListener("ended", function(){ //wartet bis ein Video endet.
        sources = this.getElementByTagName("source");
        for (i=0, l=source.length; i<l; i++){
            orig = sources[i].getAttribute("data-orig");
            if(orig){ //wenn das erste Video zu ende
                sources[i].setAttribute("src", orig);
                modified=true;
            }
            else{ 
                current=sources[i].getAttribute("src");
                if(current.indexOf("bumper-out")==-1){ //wenn das zweite Video zu Ende
                    sources[i].setAttribute("src", current.replace(/([\w]+)\.(\w+)/, "bumper-out.$2"));
                    modified=true;
                }
                else{ //sonst = wenn drittes Video zu Ende
                    this.pause();
                    modified=false;
                }
            }
            sources[i].setAttribure("data-orig", "")
        }
        if(modified){
            this.load()
        }
    })
}
```