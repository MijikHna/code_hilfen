Repo mit Exersices: github.com/planetoftheweb/bootstrap4

### 1 - Getting Started
#### 1 - Introduction
* cdn - Cachen von Bootstrap
* CDN -> muss man online arbeiten
#### 2 - Installation Options
* 4 Optionen:
    * CSS und JS manuell installieren - JA
        * `.map` - SASS-Code das zum Erstellen von CSS benutzt wurde.
        * `bootstrap-reload...` - Reset CSS im Browser
        * eigentliche Datei: `bootstrap.ccs` oder `bootstrap.min.css`
            * falls man Bootstrap customisieren möchte => diese Dateien bearbeiten
        * `bundle.js` - Bootstrap-Code + Popper-Library
    * Bootstap CDN benutzen = wenn man schon ähnliche Seite besucht hat => wird der Inhalt aus dem Cache geladen
    * Source Files
    * Pacakge Manager:
        * npm
        * composer 
#### 3 - Creating a basic template
* Template:
    * Bootstrap downloaden oder per CDN
    * jQuery
    * Popper (JS-Library -> downloaden)
    * HTML-Basic-Dokument
* auf der Bootstrapseite kann man auch einen Basic-Template besorgen, wo Verweise auf alle Libs stehen
* 3:00 - Bsp-Template
### 2 - Using Basic Styles
#### 1 - Basic Styles overview
* Reboot - Reset-Commands für Default-CSS
#### 2 - Basic typography
* Reboot.css - überschreibt Browser-Default-CSS
* benutzt `Rems` nicht `Ems`
* benutzt keine `maring-top` - also fügt nur `margin-bottom` => eventuell muss man selbst `margin-top` einstellen
* benutzt `inherit` so viel möglich
* Model ist `border-box`-sizing
* benutzt *Native font stacks*
* Bsp:
    * `bootstrap.css` linken
    * alle in `<div class="container">` aufnehmen => schone wird Bootstrap angewendet (responsive)
* es gibt Klassen für `h1-6` - kann man z.B div zuordnen 
* es gibt Klassen für `dislay1-4` - erweitert `h1-6`
* `class="lead"` - weitere Hervorhebung
#### 3 - Typographic utilities
* Utitily-Klassen
    * Horizontales Alignments:
        * `text-justify`
        * `text-XX-POS`
            * XX: sm>576px, md>768px, lg>992px, xl>1200px
            * POS: left, center, right
    * Line Height Alignment - für Inline, Inline-Block, Table, Table-Cell
        * `align-SID`
            * SID: baseline, top, middle, bottom, text-bottom, text-top, right
    * Capitaliation:
        * `text-TYP`:
            * TYP: lowercase, uppercase, capitalize, monospace
    * Text Styles:
        * `font-STYL`:
            * STYL: italic, weight-normal, weight-light, weight-lighter, weight-bold, weight-bolder
    * Text Modifier: z.B für Links
        * `text-decoration-none`
        * `test-reset` - Farbe-der Links wie von Parent machen
    * Flow:
        * `text-FLOW`
            * FLOW: wrap, nowrap, break, truncate
* `bg-warning` - Warning-Klasse z.B zum Markieren benutzen

#### 4 - Blockquotes and lists
* Klassen für Listen und Quotes:
* Lists:
    * `list-unstyled` - keine Bullets
    * Inline Lists:
        * `list-inline` - in `<ul>`
        * `list-inline-item` - in `<li>`
* Mehrere Cusror in VSCode unter Selection schauen.
* Blockquote:
    * `blockquote`
    * `blockquote-footer` z.B Erklärungen, Autoren
    * `blockqoute-reverse` - Rechtsausrichtung
#### 5 - Using colors with Bootstrap
* Color-Klassen (kontextuelle (primary, secondary)):
    * man kann diese Farben redefinieren
    * `text-COLOR`:
        * COLOR: primary, secondary, success, danger, warning, info, light, dark, body, black-50, white-50, muted, white - machmal wird auch Background-Farbe verändert <- man kann es auch für Links verweden>
    * `bg-COLOR`:
        * COLOR: primary, secondary, success, danger, warning, info, light, dark, white, transparent, faded
#### 6 - Working with images
* `img-fluid` - für responsive Images - macht die Images responsive
* `img-thumbnail` - rundes 1px Border
* `rounded-(SID)(-SHA)(-SIZ)`: - Bild-Ecken abrunden. Was in () ist => kann, muss aber nicht verwendet werden
    * SID: top, right, bottom, left
    * SHA: cirlce, pill
    * SIZ: 0, sm, lg
* Images Alignen
    * `float-left`, `float-right`
    * `text-center`, da Img per Default Inline-Elem ist
    * `mx-auto` - falls Img zu Block geändert wurde -> Centrieren
* `<figure>` - Styles
    * `figure-img`
    * `figure-caption`
#### 7 - CSS variables
* Bootstrap hat ein paar vordefiniert CSS-Variablen
* CSS-Variablen sind neu, eventuell, können es nicht alle Browser unterstützen
* `var(NameDerVer)`
* `:root` - damit CSS-Variable redefinieren bzw. eigene definiren:
* Bootstrap vordefinierte Variablen:
    * Farbe/Kontextuelle Varialen:
        * --blue, --indigo, --purple, --pink, --red usw.
    * Media-Queries Variablen.
        * --breakpint-xs, --breakpoint-sm, --breakpoint-md, --breakpoint-lg, --breakpoint-xl
    * Fonts Varialben:
        * --font-family-sans-serif, --font-family-monospace
* Bsp: Benutzung:
    * `<h2 style="color: var(--yellow)">...`
    * 
    ```css
    :root {
        --pink: #c4226F;
        --danger: #ffba00; /* eigene Var definiren*/
    }
    ```
* eventuell werden Bootstrap-Styles nicht überschrieben, falls `!important` darin verwendet wurde, eventuell kann man dann im eignen CSS `!important` benutzen.

### 3 - Mastering Layout with Bootstrap
#### 1 - Layout overview
* Bootstrap-Grid - Main Thing von Bootstrap. Besteht aus drei:
    * Container
        * Respoinsive
        * Fluid - 100% von Viewpoint
        * im Continer kann man dann weiter Grids Benutzen
    * Grids (Row + Columns):
        * extra smal, small, medium, large, extra large <- für verschieden Devices
#### 2 - Containers and rows
* 12-Columnt Response Grid
    * basiert auf Flexbox
    * aus 3 Komponenten
        * Container - man kann sie auch ohne Grid benutzen
        * rows + Columns
* Container - 2 -Contaienr
    * `container` - um Kontent zu zentrieren + responsive
    * `container-fluid` - haben vollen Viewport
    * Container haben immer 15px padding
* ?? `clearfix`
* Bsp:
```html
<div class="row">
    <div class="col">
    </div>
    <div class="col">
    </div>

</div>
```
* je nachdem wie Groß Browser ist, wird verschiedene Anzahl der `col`-s in eine Zeile eigefügt.
#### 3 - Use columns
* BP = Breakpoint = ab wann es angewednet werden soll

* 12-Column-Grid - mobile First
    * dann festlegen, wieviele Columns ein Element einnimmt
    * `col(-BP)-(COL)`: Klammer heißt auch Optional
        + `col` - automtisch sized, so dass max Columns passt in eine Row
        * BP: (Breakpoint)
            * sm >576 -> erst ab hier wird Grid angewendet
            * md >768 -> erst ab hier wird Grid angewendet
            * lg >992 -> erst ab hier wird Grid angewendet
            * xl >1200 -> erst ab hier wird Grid angewendet
        * COL: 1-12 - wieviele Column groß es ist
* Bsp:
```html
<div class="container">
    <div class="row">
        <div class="col">    
        </div>

        <div class="col">
        </div>
        
        <div class="col">    
        </div>

        <div class="col-6"> <!--6 von 12 Columns nehme -->
        </div>
        
        <div class="col-sm"> <!--erst ab sm wird 12 Column angewendet, sonst normal-->    
        </div>

        <div class="col-sm-6">
        </div>
        
        <div class="col-6">    
        </div>

        <div class="col">
        </div>
    </div>
</div>
```
#### 4 - Multiple column classes
* mehre Breakpoints spezifizerien
* Bsp:
```html
<div class="container">
    <div class="row">
        <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2"> <!-- je nachdem welche Klass getroffen wird, wird sie angewednet -> Eventuell die Reihenfolge wichtig -->
        </div>

        <div class="col-sm-6"> <!--6 von 12 Columns nehme -->
        </div>
        
        <div class="col-sm-6"> <!--erst ab sm wird 12 Column angewendet, sonst normal-->    
        </div>

        <div class="col-sm-6">
        </div>

    </div>
</div>

```
#### 5 - Offset columns
* `offset-BP-COL` = um z.B. am Leerplatz auszurichten
    * BP:
        * sm > 576
        * md > 768
        * lg > 992
        * xl > 1200
    * COL:
        * 1-11

#### 6 - Nested columns
* also row in row, das z.B schon aus 8+4-Splaten besteht => in diesen 4 Spalten werden dann mit `row` 12-Spalten erstellt
* `no-gutters` - Klasse = Padding von den Spalten entwerfnen
#### 7 - Custom order
* Splaten reorderden:
    * `order(-BP)-ORD`
        + BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * ORD:
            * 1-12
* eventuell muss man Order von allen Elementen in Row ändern.
#### 8 - Grid alignment options
* um im Grind zu alignment
    * Vertikales Alignment
    * `align-item-ALN` - in Zeilen also in `row`
        * ALN
            * start
            * center
            * end
    * `align-self-ALN` - Columns aglinmen also in `col`
        * ALN
            * start
            * center
            * end
    * Horisontales Alignment
    * `justify-content-ALN` - horisontales alignment, (braucht col-width)
        * ALN
            * start
            * center
            * end
            * around
            * between
* `row bg-info` + `style="height:100vh"`
    * bg-info/warning = Bachground mit Info-Farber färben
    * height: 100vh = 100% ViewportHeight
* eventuell muss man bei diesen ganzen Alignments col->row->col-Contents einnesten
#### 9 - Display properties
* Postion: (ziemlich ähnlich wir normales css)
    * `fixed-top`, 
    * `fixed-bottom`- hol es komplett aus dem Container raus 
    * `stick-top` - bleibt im Container, bleibt bei Scrollen dann oben, wenn es Top des Browsers erreicht
* Display Eigenschaften:
    * `d(-BP)(-TYP)`
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * TYP:
            * none, inline, inline-block, block, table, table-row, table-cell, flex, inline-flex
    * Print Dislay
        * `d-print-TYP`
            * `d-print-none` => beim Drucken, wird es nicht angezeigt
* Basis Flex-Container:
    * `d(-BP)(-inline)-flex`
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
#### 10 - Flexbox container options
* Optionen für d-flex-Container 
    * man hat zwei Optionen
        1. weitere Klasse zu Container hinzufügen
        2. zu den Elementen im Container weitere Klassen hinzufügen
    * `d(-BP)-(-inline)-flex` - Default-Container-Klasse - also per Default ist Block
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
    * zu 1) `flex(-BP)(-DIR)(-reverse)`
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * DIR
            * row - ob Contaner als Row
            * column - ob Container als Column erscheinen soll
    * Riehenfolge (zu 2) ) der Elemente im Container bearbeiten `order(-BP)-ORD` - für alle Elemente, die Container oder flex sind
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * ORD: 1-12
    * `jusitify-content(-BP)-ALG` - die Zwischenräume einstellen (Einstellungen beziehen sich auf Zwischenraum)
        * * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * ALG: start, end, center, around, between
    * `flex(-BP)-WRP(-reverse)` - wie die Elemente gewrappt werden von umgebenden Element
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * WRP: wrap, nowrap
    * `align-content(-BP)-ALG` - vertikales Alignment
        * BP:
            * sm > 576
            * md > 768
            * lg > 992
            * xl > 1200
        * ALG: start, end, center, between, around, stretch
#### 11 - Individual flex elements
* `align-self(-BP)-ALG` - 
    * BP:
        * sm > 576
        * md > 768
        * lg > 992
        * xl > 1200
    * ALG: start, end, center, baseline, stretch

* `order(-BP)-ORD` - Element muss flex-Box sein.
    * BP:
        * sm > 576
        * md > 768
        * lg > 992
        * xl > 1200
    * ORD: 1-12
#### 12 - Floating elements
* Klassen um mit Float-Elemente zu arbeiten
* `float-(BP)-SID
    * BP:
        * sm > 576
        * md > 768
        * lg > 992
        * xl > 1200
    * SID: left, right, none
* wenn man float benutzt verliert das Parent-Element die Sicht auf die Position und die Größe der Kind-Element => clear benutzen
    * `clearfix` bei Parent-Element
#### 13 - Margin and padding
* die reichste Gruppe von Bootstrap
* `PROSID(-BP)-(N)SIZ`
    PRO:
        * m = marign
        * p = padding
    SID:
        t,r,b,l,x,y - top, bottom, usw. x=links +rechts, y = oben + unten
    * BP:
        * sm > 576
        * md > 768
        * lg > 992
        * xl > 1200
    * N: n = negativ (nur für margins)
    * SIZ: 0,1,2,3,4,5,auto <- wieviel rems (Doku checken)
#### 14 - Visibility
* Content verstecken
* `invisible` - Inhalt verschwindet, aber Raum wird beeansprucht
* `visible` - Visible für ScreenReeders auch wenn `display="none"`
* `d-(BP)-TYP`
    * BP:
        * sm > 576
        * md > 768
        * lg > 992
        * xl > 1200
    * TYP: none, inline, inline-block, block, table, table-cell, flex, inline-flex
* 
#### 15 - Sizing utilities
* `SIZ(-AMT)` - wird aber nicht für alle Element angewednet
    * SIZ: w,h, mw, vm, vh, min-vw, min-vh (vw = viewportwidth, width, height, main)
    * AMT: 25, 50, 75, 100, auto <- amount (mindestens AMT von Eltern-Element)
#### 16 - Using borders
+ `border(-SID)(-COL)(-0)`
    * SID: top, right, bottom, left
    * COL: primary, secondary, success, danger, warning, info, light, dark, white (color)
    * mit (-0) = border clearen
* `rounded(-SID)(-SHA)(-SIZ)`:
    * SHA: circle, pill (shape)
    * SIZ: 0, sm, lg (0 = borders, clearen, smaller, larger)
### Stärke von Bootrsap sind die BP (Breakpoints) = sagt, ab wann CSS angewendet werden soll

### 4 - Using Navs and Navbar Components
#### 1 - Navbar overview
* Nav-Elemente:
    * Navs
    * Tabs
    * Pills
    * Navbars
* Navs sind Eltern aller Nav-Elemente
* Tabs/Pills => Content innerhalb der Seite ädnern, wenn angeklickt
* Navbars = zwischen den Setien wechseln
* Nav kann enthalten:
    * Branding
    * Color schemes
    * Dropdowns
    * Form Elements
* 
#### 2 - Create basic navigation
* Nav mit/ohne `<ul>`
* Nav-Klassen vergeben an Elemente:
    * nav (z.B. `<ul>` oder `<nav>`)
    * nav-item (z.B an `<li>` oder direkt an `<a>`)
    * nav-link (z.B an `<li>`)
        * Wie Links angezeigt werden
        * active
        * disable
* Nav-Styles:
    * nav-pills (z.B. `<ul>`)
    * nav-tabs
* Nav Alignements: 
    + justify-content-center
    + justify-content-end
    * nav-fill
    * nav-justified
    * flex(-BP)-(column/row) - vertikall/horizontall ausrichten
#### 3 - Create a navbar
* Klasse `navbar` geht an Parent-Elem
* Klasse `navbar-expand(-BP)` geht an Kind-Elem (bei BP wird horizontall ausgerichet)
* `bg-COLOR` um Farben für Nav-Items 
    * `navbar-light` oder `navbar-dark` - Text von Nav-Item (sollte Gegenteil sein von bg-COLOR)
* `navbar-nav` - an Parent
    * `nav-item` - an Kind
    * `nav-link` - an Kind
    * `active`, `disabled`
* Struktur:
* `navbar bg-COLOR navbar-light/dark navbar-expand-BP`
    * `navbar-nav`
        * `nav-item nav-link`, wobie nav-link in `<a>` sein sollte

### Bootstrap ist Mobile First

#### 4 - Use branding and text
* für Logos und Logo-Text
* `navbar-brand` oder `navbar-text` <- eventuell muss man mi Spacing-Klassen arbeiten.
* eventuell `d-none d-sm-inline-block` oder so benutzen, damit es bei Handys nur NavBar angezeigt wird
#### 5 - Add a dropdown to navigation
* sind separate Koponenten
* `dropdown` für Parent um zu alignen
* `dropdown-toogle` - für Kind
* aktivieren kann man per JS oder Data-Attrite `data-toggle="dropdown"`
    * mit Data-Attr. kann man vieles von JS machen
* `dropdown-menu` - Element für Menü-Button
    * `dropdown-item` 
    * `id` für ScreenReader um Attributes mit Containern zu verbinden
* Struktur
* `navbar-nav ls-sm-auto` -> `ls-sm-auto` um rechsts auszurichten
    * `dropdown` <- hier beginnt eigentlich Dropdown-Menu
        * `nav-item nav-link dropdown-toogle` + `data-toogle="dropdown" id="serviceDropdown aria-haspopup="true" aria-expnaded="false"`
            * `dropdown-menu` + `aria-labelledby="serivceDropdown"`
                * `dropdown-item`
#### 6 - Add form elements
* z.B für Suche
* `form-inline` für Eltern z.B. für `<form>` oder `<div>`
    * `form-control` für Kinder z.B für `<input>`
* Struktur:
* `form-inline`
    * `<input class="form-control" type="text">`
    * `<button class="btn btn-outline-light" type="submit">Go</button>`- Buttons brauchen eigentlich kein `form-control`
#### 7 - Control positioning
* `fixed-top` - dabei werden die Elemente überlappt => eventuell muss man Elemente repositionieren
* `fixed-bottom` - hier das gleiche wie oben => eventuell `margin-bottom` einfügen
* `sticky-top`
#### 8 - Create collapsible content
* `collapse`
* `navbar-collapse`
* `id` man muss mit id Element das den Collapse verursacht hat und das collabiert wird verbinden
* Hamburger Menu:
    * `navbar-toggler`
    * `navbar-toggler-icon`
* 1:
    * `<button class="navbar-togler" type="button" data-toggler="collapse" data-target="#myTooglernav" aria-controls="myTogglerNav" aria-expanded="false" aria-lavbel="Toggle navigation"></button>` - # da ID, aria-xxx sind Usability-Attribure z.B für ScreenReader
    + `collapse navbar-collpse` + `id="myTogglerNav"`
        * `navbar-nav`
### 5 - Style Element Overview
#### 1 - Basic style element overview
* `btn`
* `btn-SIZ`
    * SIZ: sm lg (small, large)
* `btn-COLOR`
    * COLOR: primary, secondary, success, danger, warning, info, light, dark
* `btn-outline-COLOR` - border
    * * COLOR: primary, secondary, success, danger, warning, info, light, dark
* `btn-block` - ganze Größe des Containers annehmen
* `active`, `disabled`
* <- anwendbar auch auf `<input>` 
* `btn-SIZ`:
    * SIZ: lg, sm (size)
#### 2 - Create buttons
+ `btn` - Basis-Button-Klasse. mit weiteren Klasen benutzen
    * `btn-SIZ`
        * SIZ: 
            * sm = small
            * lg = large
    * <- man kann die `btn`-Klassen bei `<a>`, `<button>`, `<input>` benutzen
    * `btn-COLOR`
        * COLOR: primary, secondary, success, danger, warning, info, light, dark
    * `btn-outline-COLOR`
    * `btn-block` - wenn Button ganz Breite des Containers einnehmen soll.
    * `active` 
    * `disabled` <- ist auch JS dabei
* Bsp: `<a class="btn btn-primary btn-lg">..</a>`
#### 3 - Buttons groups
* `btn-group`
* `btn-group-vertical`
* `btn-toolbar` - für Gruppen von Button-Grupps
* Bsp: 
```html
<div class="btn-toolbar" aria-label="labelname">
<div class="btn-group mb-2" aria-label="ButtonGruppeLabel01"> 
<button></button>
<button></button>
<!--..--->
</div>

<div class="btn-group mb-2" aria-label="ButtonGruppeLabel01"> 
<button></button>
<button></button>
<!--..--->
</div>
</div> <!-- class="btn-toolbar" -->
```
* `btn-group-SIZ`
    * SIZ: lg, sm
+ aria-label = für Screenreader
* mb-2 = margin-bottom
#### 4 - Use badges
* `badge` - das Abzeichen, die Plakette
* `badge-pill` - mehr abgerundet
* `badge-COLOR`
* <- gewönlich in `<span>` verwendet
* Bsp: `<span class="badge badge-pill badge-default">
#### 5 - Progress bar styles
* `progress` - für Container
* `progress-bar`  für items in Container
    * dann `width` und `height` benutzen
* `bg-COLOR` um Farbe des Bars ändern
* `progress-bar-striped` - Balken in der Bar
* `progress-bar-animated`
* `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax` - für Screenreader
*Bsp:
```html
<div class="progress">
    <div class="progress-bar bg-success progress-bar-striped" style="width:73%; height: 40px" aria-value-now="73%" aria-value-min=0 aria-value-max="100%">73% <!--zeigt 73% in der Bar -->
    <div class="progress-bar w-25 progress-bar-animated">
    </div>
</div>
```
* <- dann z.B `...-animated` mit JS ein/ausschalten
* man so Progressbar in Progressbar erstellen und denen unterschiedliche Farbe geben
#### 6 - List groups
* `list-group` - für Container z.B für `<div>`
    * `list-group-item` für die Items z.B `<a>, <button>, <a>`
    * `active`
    * `disabled`
    * `list-group-item-action` - bekommt Hover:
    * `list-group-item-COLOR`
    * `lsit-group-horizontal(-BP)`
        * BP = Breakpoint
    * `badge` + `justify-contetn-between` 
* so kann man auf `<ul> + <li>` vezichten stattdessen `<div> + <a>`
#### 7 - Breadcrumbs
* um zu zeigen, wo man gerade ist oder für Unternavigation:
    * Container -> `breadcrumb`
        * Item -> `breadcrumb-item`
        * `active` benutzen
+ in `<li>` und  `<nav> <a> </a></nav>` benutzen
    * `nav` ist dann `breadcrumb` , `<a>` ist dann `breadbrumb`
* den Trenner customizen:
```css
.breadcrumb-item+.breadcrumb-item:before { /*+ = kind*/
    content: '->';
}
```
#### 8 - Shadows
* `shadow-none` - Shadow remove, wenn z.B vererbt oder so
* `shadow-sm`
* `shadow`
* `shadow-lg`
* Shadows können benutz werden um z.B etwas herauszuheben
### 6 - Using Layout Component
#### 1 - Layout components overview
* ~ Design Patterns
#### 2 - Add a jumbotron
* um etwas zu heighleighten
* `jumbotron` - Container
    * `jumbotron-fluid` - Item + ohne runde Ecken
* Bsp:
```html
<header class="jumbotron jumbtoron-fluid">

</header>
```
#### 3 - Table styles
* `table` - überwiegend für `<table>` verwenden
* `table-dark`
* `table-striped` - jede Zeile bekommt andere Farbe 
* `table-bordered`
* `table-borderless`
* `table-hover` - verändert Farbe, wenn Maus darüber
    * für Headers in Tables:
    * `thead-light`
    * `thead-dark`
* `table-COLOR`: sind etwas heller als normales `COLOR`. Kann man auch für `<td>` benutzen
    + COLOR: primary, secondary, success, danger, warning, info, light, dark, + active
* `bg-COLOR` 
* `text-COLOR`
* Größer:
    * `table-sm`
    * `table-responsive(-BP)`
        * BP = Breakpoint
* 
#### 4 - Basic card layouts
* Card Containers = Content in Karten präsentieren
* `card` - Container
    * `card-body` - Untercontainer, der dann Cards hat
        * `card-text`
        * `card-titel`
        * `card-subtitle`
        * `card-link`
        * `card-img`
        * <- Content-Typen
            * Farben -> am liebsten direkt `card` mitgeben => Karte abgrenezn + eventuell abgerundete Kanten `border-warning`
            * `bg-COLOR`
            * `border-COLOR`
            * `text-COLOR`
        * 
#### 5 - Card content classes
* bauet auf **4 - Basic card layout**
* für Images
    * `card-img`
    * `card-img-top`
    * `card-img-bottom`
    * `card-img-overlay` - Text auf dem Bild
    * <- eigentlich machen richtige Abstände usw. für das Element
* Listen Gruppen:
* `list-group` - Für Container 
    * `list-group-item` - für Items
    * `list-group-flush` - bei `list-group` einfügen => unnötigen Border löschen

* `card-header`
* `card-footer` 
* <- um Inhalt innerhalb der Karte abzugrenzen
#### 6 - Card layouts
* Karten gruppieren:
* `card-group` - Karten nebeneinander platzieren (ohne Border für einzelne Karte)
* `card-deck` - mit Border für die einzelnen Karten
* `card-columns` - Pinterest Design
* sonst kann man rows und colomns benutzen (Standard-Bootstrap)
#### 7 - Use the media object
* Klassen für Media Elemente
* `media` - für Container
    * `media-body` - für main-Content 
        * flexbox-Klassen dann benutzen
* Elemente z.B in `<div>` vertikal ausrichten
    * `class="d-flex align-self-center` - zentrieren
    * `class="d-flex align-self-end` - zentrieren

### 7 - Using Form Styles
#### 1 - Form styles overview

#### 2 - Create a basic form
* Form Klassen:
    * `form-group` - Forms gruppieren
    * `form-text` - für Texte, die um die Form-Elemente stehen
    * `form-control` - für Text-Felder, Text-Areas, Select-Felder
    * `form-conrol-label`
    * `form-control-file`
* Bsp:
```html
<form>
    <fieldset class="form-group"> <!--fieldset gruppieren -->
        <legend>lala</legend>
        <div class="form-group">
            <label class="form-control-label" for="lala">Lala</label>
            <input class="form-control" type="text" id="lala">
        </div>
        <div>
            <label class="sr-only" for="lala">Lala</label> <!-- sr-only = screenreader only, wird hidden-->
            <input type="text" id="lala">
        </div>
    </fieldset>

    <fieldset>
        <legend>lala</legend>
        <div class="form-group">
            <label for="lala">Lala</label>
            <input type="text" id="lala">
        </div>
        <div>
            <label for="lala">Lala</label>
            <input type="text" id="lala">
        </div>
    </fieldset>
    <button class="btn">Lala</button>
</form>
``` 
#### 3 - Checkboxes and radio classes
* `form-check` - gruppiert Checkboxen
* `form-check-label`
* `form-check-input`
* `form-chech-inline` - per Standard sind checkboxen block => damit zu inline machen. Kann man direkt dem `<div>` geben, dass Chechboxen hat
#### 4 - Size and validation styles
* `form-control-sm` - InputFeld kleiner machen
* `form-control-lg` - InputField größter machen
* `form-inline` - From-Gruppen (d.h. auch Elemente darin Inline machen)
* Form-Validation
    * `has-COLOR` - um zu markieren was FALSCh/RICHTIG gefüllt ist (mit JS kann man die Klassen switchen), arbeiten mit JS. Man sollte es dem DIV geben, damit LABEL und INPUT gefärbt werden 
        * COLOR: success, warning, danger 
    * `form-control-COLOR`:
        * COLOR: success, warning, danger 
#### 5 - Multicolumn forms
* `row` oder `col`
    * 1-12 - Sachen benutzen + sm/lm usw.
* `form-row`, `col-auto` für Forms angepasster Row und Col
* `col-form-label` - wenn man in Forms Labels benutzt. Den Labels in Forms zuweisen
* mit `offset-md-2` - einfache 2-Column Abstandshalter
#### 6 - Create input groups
* Form-Elemente zu "Inline" machen
* `input-group`
* `input-group-prepend`, `input-group-append` für Elemente die vor/nach dem Form-Element "integriert" werden sollen
* `input-group-text` - um sowas wie Labels zu machen (hier wurde aber direkt in div gemacht)
* `aria-label`, `sr-only` - für Screenreader
#### 7 - Custom form components
* `custom-TYP`: - Input-Field bearbeiten (sehen einheitlicher bei unterschiedlichen Browsern)
    * TYP: select(-sm)(-lm), radio, checkbox, switch, range, file-input
        * Switch <-> Chechbox/Radio + braucht LABEL für die Chechbox
    * `custom-control-label` - für Labels für Fields (Kritisch für switches und ranges)
    * `custom-control` - Container für die weiteren`custom`-Klassen => z.B DIV -> Chechboxen/Radiobuttons
    * `custom-control-input` - für Radio-/Checkboxen

### 8 - Working with Interactive Components
#### 1 - Interactive components overview
#### 2 - Add tooltips
* weitere Tipps anzeigen
* an Links oder in Form-Feldern 
    * man sollte Attr. `data-toggle=tooltip` und `title=Tipp` einfpgen 
* zwei Arten
    1. `data`-Attr benutzen (brauchen aber JS)
        * Syntax:
        ```js
        $(function () {
            $('[data-toogle="tooltip"]').tooltip({OPTIONS})
        })
        ```
        * <- es wird HTML-Teil wird erstellt der mal angezeigt, verschwinden wird
        * OPTIONS: `data-xxxx`
            + `placemant`: top, right, bottom, left
            + `trigger`: click, hover, focus
            * `html`: true, false
            + weitere OPTIONEN
        * Bsp:
        ```html
        <a href="" data-toggle="tooltip" data-trigger="click" data-html="true" data-placement="top">medicine</a>
        ...
        $(function(){
            $('[data-toogle="tooltip"]').tooltip({
                placement: "top",
                html: true,
            });
            //ODER
            $('[data-toogle="tooltip"]').tooltip();
        });
        ```
    2. JS 

#### 3 - Display popovers
* mehr Info als bei Tooltip
* HTML-ELEM. braucht:
    * `data-toogle="popover"`-Attr
    * `title="text"` - Attr
    * `data-content="content"` - Attr
    * JS:
    ```js
    $(function () {
        $('[data-toogle="popover"]').popover({OPTIONS});
    })
    ```
    * OPTIONEN
        + `placemant`: top, right, bottom, left
        + `trigger`: click, hover, focus
        * `container`: true, false
        + weitere OPTIONEN
Bps:
```html
<button type="button" data-toogle="popover" title="popover" data-content="größerer Text"> </button>

$(function () {
    $('[data-toogle="popover"]').popover();
})

```
#### 4 - Create alerts
* Alert-Klassen
    * `alert`
    * `alert-COLOR`
    * `alert-hearding`
    * `alert-link`
* Dismiss Alert:
    * `alert-dismissible fade show`
* Bsp:
```html
<div class="alert alert-info alert-dismissiable fade show">
    <button type="button" class="close" data-dismiss="alert"> <!-- data-dismiss => JS kann dann alert ausmachen -->
    <span aria-hidden="true">&times;</span> <!--arai-hidden => für Screenreader disabeln; times ist X-Button/Zeichen-->
    </button>
    <h4 class="alert-heading"></h4>
    <a class="alert-link">
</div>
```
#### 5 - Use dropdowns
* für NAVs, TABs usw
* Zwei Schritte:
    1. Button/NAV Trigger - um Droptdown zu triggern
    2. Menu selbst
* `dropdown` - für Container für Triger und Menu
    * `dropdown-toggle` - Trigger-Button
    * `dropdown-menu` - Container für Menu
    * `dropdown-item` 
    * `dropdown-header`
    * `dropdown-divider` - Linien zum Visuellen Teilen
    * `disabled`
    * Weitere Optionen:
        * `btn-sm`, `btn-lg`
        * `dropup` - Menu wird nach oben geöffnet
        * `dropdown-menu-right` - Menu nach rechst öffnen (Default ist nach links)
        * `btn-group`, `dropdown-toggle-split`
* Bsp 1:
```html
<div class="dropdown dropup">
    <button class="btn dropdown-toggle" type="button" id="dropMenuButton" data-togole="dropdown" aria-haspopup="true" aira-exapndable="false">Trigger</button>
    <div class="dropdown-menu" aria-labelledby="dropmMenuButton">7
        <a class="dropdown-item">A</a>
        <div class="dropdown-divider">Andere</div>
        <a class="dropdown-item">B</a>
    </div>
</div>
```
* Bsp 1:
```html
<div class="btn-group">
    <button class="btn dropdown-toggle" type="button" id="dropMenuButton" data-togole="dropdown" aria-haspopup="true" aira-exapndable="false"><span class="sr-only">Toogle Dropdown</span></button>
    
    <div class="dropdown-menu" aria-labelledby="dropmMenuButton">7
        <a class="dropdown-item">A</a>
        <div class="dropdown-divider">Andere</div>
        <a class="dropdown-item">B</a>
    </div>
</div>
```
#### 6 - Add collapse accordions
* HTML-Content anzeigen/verstecken
1. Collapse - beim Klick anzeigen
    * für Link oder Button
    * `data-toggle="collapse"`
    * braucht auch `#id` oder `data-target`
    * `collapse`

2. Accordians - beim Klick anzeigen, weiterer Klick verstecken
* braucht weiteren Kontainer, das `dropdown-menu` hat
* Element das angezeigt wird hat `show`
* wird in Card-Style gemacht
* Bsp -> Collapse
```html
<div class="">
    <button class="btn btn-primary" data-toggle="collapse" data-target="#pestcontrol" aria-expandable="true" ></button>
    <div id="pestcontrol" class="collapse">
    Text
    </div>
</div>
```
*Bsp Accordion
```html
<div id="servicesaccordion" role="tablist" aria-multiselectable="true">
    <div class="card" role="tab" id="grommingheader">
        <a class="btn btn-primary" data-toggle="collapse" data-parent="#servicesaccordion" href="#pestcontrol" aria-expnadable="true" aria-controls="grommingaria">
        <div id="grommingaria" class="collapse show" aria-labeledby="groomingheader">
        Text
        </div>
    </div>
</div>
```
* damit das Element weiß, was Main-Container ist
* wenn man statt Button `<a>` benutzen würde => data-target mit href ersetzen
* Accourdions sind etwas schwerer zu programmieren
#### 7 - Use modals
* Overlay-Element
* bestehen aus zwei Teilen
    1. Trigger
        * Button oder `<a>` => braucht `#id` oder `data-target` mit dem Ziel-Info/Element und `data-toggle="modal"` 
    2. Info => muss `modal` haben
* weitere Classes:
    * `modal-dialog`
        * `modal-content` - Main-Content
            * `modal-header`
                * `modal-title`
                * eventuell hier auch button zum Schließen
                    * `<button class="close" data-dismiss="modal" aria-label="close"><span aria-hidden="true">&times;</span></button>`
            * `modal-body`
            * `modal-footer` - z.B Button zum Schließen
                + `data-dismiss="modal"` - für Schließen-Element + für Screen-Reader `aria-label="close"
    * `modal-dialog-centered` -vertikal Zentrieren
    * `modal-dialog-schrollable`
* Modal Sizes:
    * Max-Width:
        * modal-sm -> 300px
        * modal-lg -> 800px
        * modal-xl -> 1140px
        * none -> 500px
* Bps:
```html
<div class="container">
    <button class="btn" data-toggle="modal" data-target="#servicemodal">Lala</button>
    <a class="" data-toogle="modal" href="#serviemodal"> Lala </a>


    <div id="servicemodal" class="modal fade">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-body">
                Text
                <p>Text</p>
                </div>
            </div>
        </div>
    </div>
</div>
```
#### 8 - Build carousels
#### 9 - Use scrollspy
#### 10 - Toasts
#### 11 - Spinners
#### 12 - Pagination
#### 13 - Stretched links
#### 14 - Embeds
