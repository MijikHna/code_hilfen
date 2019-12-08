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
#### 3 - Buttons groups
#### 4 - Use badges
#### 5 - Progress bar styles
#### 6 - List groups
#### 7 - Breadcrumbs
#### 8 - Shadows

### 6 - Using Layout Component
#### 1 - Layout components overview
#### 2 - Add a jumbotron
#### 3 - Table styles
#### 4 - Basic card layouts
#### 5 - Card content classes
#### 6 - Card layouts
#### 7 - Use the media object

### 7 - Using Form Styles
#### 1 - Form styles overview
#### 2 - Create a basic form
#### 3 - Checkboxes and radio classes
#### 4 - Size and validation styles
#### 5 - Multicolumn forms
#### 6 - Create input groups
#### 7 - Custom form components

### 8 - Working with Interactive Components
#### 1 - Interactive components overview
#### 2 - Add tooltips
#### 3 - Display popovers
#### 4 - Create alerts
#### 5 - Use dropdowns
#### 6 - Add collapse accordions
#### 7 - Use modals
#### 8 - Build carousels
#### 9 - Use scrollspy
#### 10 - Toasts
#### 11 - Spinners
#### 12 - Pagination
#### 13 - Stretched links
#### 14 - Embeds
