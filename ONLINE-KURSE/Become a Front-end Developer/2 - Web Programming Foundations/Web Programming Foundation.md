#### 1 - Deconstructing the Web
#### 1 - From URL to website:
#### 2 - The web, in a browder:
#### 3 - The structure of a web Document visualized:
1. Box in Box in Box
#### 4 - The node tree: How the browser sees a web document:
1. = DOM = jedes Element is Blatt oder Knoten
2. => bevor man mit der Arbeit beginnt => eventuell auf dem Blatt DOM aufzeichen => kann man unnötige div-s usw. vermeiden:
#### 5 - HTML: source code of the web
1. =strukturiert den Content
#### 6 - The web document is a document with superpowers:
1. html-Seiten => man braucht nur Internet + Browser, denn man will (Normal, Text-Browser usw.)
### 2 - The Duality of Web Programming:
#### 1 - The dual purpose of web code :
1. man schreibt Seite für:
    1. Menschen
    2. Rechner, die die Seite darstellen
2. => Struktur sowohl für Rechner als auch für Menschen
3. => Natur, Eigenschaften, Ziele und Beziehungen der Elemente beachten
#### 2 - Content and structure:
1. <html>
    1. <head>
    2. <body>
        1. <header>
        2. <main>
        3. <footer>
#### 3 - Metadata and purpose:
1. Beschreibung des Inhalts + deren Verhalen
2. in <head>
    1. <meata> = character set, viewport
        1. Schema und Mircoformate
        2. ARIA (Accesible Rich Internet Applications)-Attribute
    2. <title>
    3. <ling> = css usw.
    4. <script> =js
    5. ← = für Mashinen
#### 4 - Accessibility:
1. Kernkonzept in Web/Browser
2. Vorgehensweise:
    1. zuerst Zuganglich machen
    2. dann alles „hübsch“ machen
    3. Zugänglichkeit nicht zerstören
    4. =
    5. HTML
    6. CSS → checken die Zugänglichkeit
    7. ← alles reparieren
    8. Zugänglichkeit als Teil des Plan haben
### 3 - Wich Came First: The Browser or the Editor?
1. The web browser of today and of tomorrow:
    1. => automatische Test haben, die meisten Browser testen.
    2. ← HTML als Kern:
        1. dann CSS und JS als Option zur Darstellung
2. What is a code editor:
    1. Code Hinting = Vervollständigung.
3. Developer tools:
1. ist eigentlich schon in Browser eingebildet.
### 4 - The Parts That Make up the Web:
#### 1 - HTML:
1. statisch vs. dynamisch (CMS = Template + Daten vom Server)
2. HTML wird geschrieben von:
    1. Mensch + Editor
    2. Mensch + Server-App
    3. Mensch + JS Framework
#### 2 - CSS:
#### 3 - JavaScript:
1. =Interaktive Ebene
2. Seite wird geladen:
    1. HTML geladen
    2. CSS und JS geladen:
    3. JS abgespielt:
    4. CSS auf HTML angewendet
    5. JS laufen lassen (=Ereignisse)
#### 4 - DOM:
1. DOM-Objekt = Node
2. CSS-Regeln werden auch an DOM-Objekte angwendet
3. Browser erstellt DOM-Baum
4. DOM-Baum:
    1. widows
        1. DOM
            1. html 
                1. body
                    1. header 
                        1. nav 
                            1. usw.
     
#### 5 - Events:
1. Alles was im Browser passiert ist ein Event
2. auf Events antworten = Event handling
    1. DOM-Element auswählen
    2. Event-Typ auswählen
    3. Funktion = wie reagieren
#### 6 - Putting it all together
1. Html-Seite als file:/// öffnen => auf viele Features des WebServer verzichten =>
    1. WebServer laufen:
        1. Visualbox
        2. VisualStudio Code – Plugin => Live Server
            1. Aktualisiert den Browser sobald Dokument gespeichert wurde
        3. Browsersync = Test gleichzeitig auf mehreren Geräten durchführen