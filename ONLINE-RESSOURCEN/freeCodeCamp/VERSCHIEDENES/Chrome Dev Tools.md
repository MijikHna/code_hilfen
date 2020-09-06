### 1 - Allgemein
* jQuery style DOM Querie in der Console
    * Konsole kann `$` benutzen. Eigentlich `$` ist `document.querySelector()` => Bsp: `$("#__gatsby")`. `$$` ist `document.querySelectorAll()` => Bsp: `$$("div").xxx()`. Wenn man ein Element anglickt und dann `$0` eingibt => wird dieses Element in der Konsole ausgewählt. Wenn man mehrere Elemente hintereinander anklickt, das zu letzt angeklickte Element ist `0` die davor angeklickten entsprechen `1` bis `5
* Copying an Element's property
    * man kann im HTML-Element rechtsklicken und Copy->Copy selector auswählen und in der Konsole dann z.B. `$("HIER EINFÜGEN")` 
* Filtering in Network-TAB nach Requests
    * Wenn man weiter filtern möchte => gibt es Fitler-InputText
* Emulating different network speeds
    * in Network-Tab kann man unter `Online` andere NW-Einstellungen simulieren. Man kann auch eigne NW-Profile erstellen
* Life Expressions in der Console
    * eigentlich einfach den jQuery/JS-Code in der Konsole eingeben
* Forcins an Element state
    * in Elements-Tab ein Element auswählen und auf `:hov` anklicken und entsprechendes State emulieren

### 2 - Filter Network Requsts 
* was man machen kann
    1. NW Requests mit Text finden
    2. NW Requests mit RegEx finden
    3. Fitler(Ausschließen) von NW Requests
    4. Property Filter benutzen, um NW Requests von bestimmten Domain zu finden.
    5. nach Datei-Typ filtern
* GUI:
    1. Fitler-Area, da wo All, XHR usw. steht. Ganze Zeile is Filter Area
    2. Icon **Filter** dadrüber kann diese Area ein/ausschalten
* Schritte:
    1. NW Requests mit Text finden
        1. einfache Text eingeben in Text Box
    2. NW Requests mit RegEx finden
        1. einfache RegEx eingeben in Text Box
    3. Fitler(Ausschließen) von NW Requests
        1. in Text Box z.B Datei mit `-` davor eingeben.
    4. Property Filter benutzen, um NW Requests von bestimmten 
        1. Syntax: `domain:lala.lala.com`
    5. nach Datei-Typ filtern
        1. entsprechende Dateitypen finden z.B
            1. FONT
            2. WS (WebSocket)
            3. mit SHIFT kann man mehrere Dateitypen auswählen