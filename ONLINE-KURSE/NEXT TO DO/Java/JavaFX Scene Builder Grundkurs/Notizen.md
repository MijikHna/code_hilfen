* ist von Java getrennt
* JavaFX soll Swing ersetzen
* JavaFX => Ziel GUI getrennt von Java => FXML-Sprache
* SceneBuilder => komplett ohne Java-Code
### 1 - Java, JavaFX, FXML, Scene Builder im Überblick
#### 1 - Was ist Java?
GUI ohne Kontak zu Java-Quellcode <=> ABER nicht ohne Java also Java-Laufzeitumgebung JAVA-SE/JAVA-SDK
* mit SceneBuilder dann JavaFX-GUI erstellen. JavaFX ist schon in Java-JDK (früher musste man getrennt installieren)
#### 2 - Was ist der Scene Builder?
* ScenenBuilder = Tool zum GUI-Erstellung auf JavaFX-Basis => im Hintergrund wird JavaFX-Code produziert
* JavaFX kann besser ins Web integriert
* neue Architektur, neue Komponenten
* Swing = awt-Technologie
* SceneBuilder => auch für Designer ohne Java-Kenntnisse
* man kann GUI direkt in SceneBuidler ausführen.
* Verbindung Java mit GUI über FXML.
#### 3 - Scene Builder installieren
* ist Produkt von Oracle => direkt auf Orcle-Seite danach suchen.
* es gibt Version:
    * 1.1
    * 2.0
+ wenn man zuerst 2.0 installiert, kann es passieren, dass 1.1 nicht installiert werden kann.
#### 4 - Die erste Applikation
* SceneBuilder-Projekt ist ein eigener Projekt
    + => eventuell im eigenen Projekt-Ordner abspeichern
    * Datei ist .fxml
* Preview => kann man Ausssehen checken
* Bereich: Library = Komponenten
    * `Image View` zum Anzeigen eines Images
        * Inspector = Eigenschaften der Komponente = kan man auch Visual machen
            * Image = Bild einfügen
            * Layout
                * Transform = Komponenten rotieren
#### 5 - Eine FXML-Applikation laden
#### 6 - New from Template
* = Schablonen = Basis für GUI erstellen
* File -> New from Template 
#### 7 - GUI mit Scene Builder aufbauen
* Komponenten kann man per Drag und Drop in GUI oder Hierarchy platzieren
#### 8 - Die Inspector-Ansicht in Scene Builder nutzen
* Inspector = Eigenschaften für platzierte Komponenten untersuchen/festlegen = JavaFX-Eigenshaften festgelegt = FXML-Code erzeugt.
    1. Properties
    2. Layout = Visuelles (Rotationen, Verzerrungen, Verschiebungen, CSS)
    3. Code = Ereignisse einbauen

### 2.1 - Grundideen des Layoutkonzepts
#### 1 - Die Baumhierarchie
* FXML-Struktur = Baumstruktur wie HTML-Seiten
+ moderne GUI sind meistens in Baumstrukturen
* GUI ist dann auch in Baumstruktur
* zwei Kompontnen:
    1. Container = Baum-Struktur aufbauen
        * z.B Pane-s
    2. Controls = eigentliche Elemente
* GUI = Verschachterlung von Container und Controls
#### 2 - Fenster und Container
* Grunlagen gehen auf Swing/AWT-Konzept
+ Verhalten ist ähnlich dem HTML-Inline-Elementen = Layoutmanager => haben Freiheit genommen, wo Elemente platziert werden.
* Container = Pane
    1. Flow Pane = Elemente wie HTML-Inline-Elem
    2. Border Pane = hat Oben, Unten, Rechts, Links und Mitte und ein Element pro Bereich => meisten werden dann hier weitere Containe platziert
    3. Grid Pane = Tabelle
### 2.2 - Container
#### 1 - Absolute Layouts
* = absolute Kontrolle über Layout = `Anchor Pane` <- wurde in JavaFX aufgenommen, da von Entwicklern am Anfang vermisst wurde.
* = Komponenten so platzieren, wie man lustig ist
* meistens die Mutter des Baums
* `Pane` auch absolut wie `Anchor Pane`
* `Pane` ist die Basis-Klasse für Pane-s
#### 2 - Accordion and TitledPane
* `Accordion Pane` - Accordion wie in HTML
* wenn zuklappberer Teil nicht sichtbar ist => über Hierarchy einfügen
    * `Titeled Pane` - wird nicht versteckt
#### 3 - BorderPane - im Zeichen des Kompasses
* `Border Pane` = Links, Rechts, Oben, Unten Center Panes darin
* eine Komponente pro Bereich
* Rechstklick auf Element in Hierarchy -> Fit to Parent => komplett Parent einnehmen
    * weitere Pane-s statt Komponenten
    * => dann mehrere Komponenten pro Bereich
* Sinnvoll, da GUI-Layout meistens aus diesen 5 Bereich besteht.
* View -> Show CSS Analyzer => wie Entwickler-Tools im Browser
+ Bereiche passen sich dann der Größe des Fensters an.
#### 4 - Flißende Inhalte
* `Flow Pane` = fließende Anordnug der Element => wie HTML-Inline-Layout
* per Default Flow von Rechts nach Links -> kann man aber über Inspektor -> Properties anders einstellen.
* `HBox` und `VBox` ähnlich wie `Flow Pane` nur die Default-Ausrichung ist anders.
#### 5 - Tabellen beziehungsweise Gitter
* `Grid Pane` - Tabellen/Gitter-Strukturen
* = gleichmäßige Verteilung auf Zeilen und Spalten
* mit den Reiter kann man Zeile bzw. Spalten auswählen => dann im Inspektor Layout ändern => Idee aus Excel.
* Rechtsklick => Menü -> kann man Zielen/Spalten löschen/hinzufügen
#### 6 - Stapelverarbeitung
* `Stack Pane` - Komponenten kann man über einander legen.
* mit Code dann zwischen den Komponenten schalten 
#### 7 - Scrollbare Bereiche
* `Scroll Pane` bei Bedarf Scroll-Balken anzeigen.
    * `weiterer Pane` bzw. andere Elemente
* man kann über Inspector einstellen, wann Scrollbalken angezeigt werden.
* am sinnvollsten wenn man andereren großen Pane darein platziert 
#### 8 - Gesplittete Ansichten
* `Split Pane H/V` - Ansicht Teilen, wobei man dann den Split bewegen kann
    * darin weitere Pane-s anordnen
+ kommt direkt mit `Anchor Pane` => eventuell löschen und eigenen Pane einfügen
#### 9 - Tab-Strukturen
+ `Tab Pane`
* per Default 2 Tabs => weiteren Tab in der Hierarchy ablegen
* dann in SceneBuilder einzelne Tab befüllen bzw. konfigurieren
#### 10 - Kachelraster mit TilePane-Container
* `Tale Pane` - Komponenten fließen anordnen, wobei alle Elemente gleich groß werden = Kacheln, wobei jede Kachel so groß wie das größte Element. Sonst wie `Flow Pane`
#### 11 - Eine Toolbar
* `ToolBar` - so wie eine Liste für gleiche Elemente/Komponenten. z.B mehrere Buttons nebeneinander.

### 3.1 - Controls = Elemente
#### 1 - Standardsteuerelemente
1. `Button`
2. `CheckBox`
3. `Label`
4. `Password Field`
5. `Progress Bar` -> nur sinnvoll mit Code = mit Daten verbinden
6. `Radio Button` -> muss man gruppieren
7. `Scroll Bar H`
8. `Scroll Bar V`
9. `Separator H/V`
10. `Slider` = Schieberegler
11. `Text Field`
#### 2 - Mächtig, aber einfach
* = mächtiges Komponent, aber wenig Konfiguraion
1. `HTML Editor` - kompletter Editor 
2. `Image View`
3. `Color Picker` -> Rückgabe ist Hex-Colorwert, denn man dann verarbeiten kann
4. 
#### 3 - Menüs
* `Menu Bar` - Standard-Menü
* Erweiterung der Menü am besten in Hierarchy machen
* besteht aus `Menu` und `Menu Item`-s (Library -> Menu-Teil). Diese Items kann man dann im Inspektor bearbeiten.
    * Es gibt auch `Radio Menu Item` bzw `Check` für Häckchen Menu-Items
* Weitere Menu-Einträge kann man in der Library finden
#### 4 - Kontextmenüs
* d.h mit Rechtsklick Menü öffnen
* Schritte:
    1. Element auswähen
    2. Oben: Modify -> Add Context-Menu => wird dann für dieses Element in der Hierachy auftauchen.
#### 5 - Tooltips
* Hinweise für Anwender
* * Schritte:
    1. Element auswähen
    2. Oben: Modify -> Add Pop-up Menu => wird dann für dieses Element in der Hierachy auftauchen. ODER aus Library `Tooltip` auf das Element ziehen.
### 3.2 - Formen und Diagramme
#### 1 - Formen
* Graphische Objekte mit denen man Zeichen kann => Library -> Shapes-Teil
+ man kann dann diese Formen aus Code animieren.
#### 2 - Diagramme
* = Charts: Library -> Charts
* in SceneBuilder sieht man erstmal nichts, d keine Daten zum Rendern da
    * man kann über View -> Show Sample Date Sample Daten anzeigen lassen

### 4 - JavaFX-Oberfläche und Scene Builder - Tipps für Fortgeschrittene
#### 1 - eine horizontales Accordion
* Schritte:
    * `Accordion`
    * in Inspektor um 270° rotieren
    * in Inspektor dann den Inhalt bzw. Kindelement um 270° Drehen 
#### 2 - Gemeinsame Konfiguration
* mehrere Elemente auswählen z.b mit SHIFT
* dann kann man im Inspektor gemeinsame Elemente festlegen
* bei SceneBuilder 2.0 kann man auch für Unterschiedliche Elemente gemeinsame Eigenscaften festlegen
#### 3 - Eltern
* Rechstsklick:
    1. Select Parent
    2. Fit to Parent
#### 4 - Effekte
+ Inspector -> Properties
    + irgendwo unten dann Effekte anmachen
    * im Auswahlmenü dann besimmte Effekte hinzufügen.
#### 5 - Wrap in
* = Elemente nachträglich in Eltern-Element einfügen
    * Elemente auswählen, Wrap -> XXX = Elemente in XXX-Eltern einfügen.
#### 6 - Stylesheets
* JavaFX arbeitet gut mit Web-Technologien
* sind etwas anders als CSS -> wird mit Prefix gearbeitet
* Inspektor -> Properties -> Style
    * Styles eingeben = Inline-Style z.B: `-fx-background-color: green`
* man kann auch mit Klassen arbeiten.
    + Inspektor -> Properties -> Stylesheet
        * .css-Dateien hinzufügen
    * ! Syntax mit Präfix
    ```css
    .k1 {
        -tx-background-color: yellow;
    }
    #button {
        -fx-opacity: 0.3;
    }
    ```
    * Klassen und ID dann über Inspector -> Properties -> JavaFX CSS - ID/Style Class
#### 7 - Der CSS Analyzer
* View -> Show CSS Analyzer = wie Entwickler-Tools
#### 8 - FXML und der Scene Builder im Java-Kontext
* JavaFX-Project starten -> JavaFXML Applciatoin
* dabei wird fxml-Datei erstellt