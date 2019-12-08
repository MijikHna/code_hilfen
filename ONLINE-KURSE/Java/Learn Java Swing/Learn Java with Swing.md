### 0 - Introduction

### 1 - Swing Bacis
#### 1 - Learn about Swing
* Swing hat GUI-Componenten
* GUI besteht aus 3 Teilen:
    1. UI-Element
    2. Layout - Placement 
    3. Behavour - Events
* Swing-App besteht aus Containersystem
    * Top-Level-Container: JFrame, JDialog, JApplet
#### 2 - Use a WYSIWIG editor
#### 3 - Swing from scratch
#### 4 - MVC architecture
* Model-View-Controller-Arch:
    * Model - repräsentiert die Componenten der Daten
    * View - visuelle Repräsentation der Daten
    * Controller - verarbeitet die Daten
### 2 - Containers
#### 1 - Top-Level containers
* JRootPane -> JFrame + JWindow + JDialog + JApplet
* JXXX müssen zum Container hinzugefügt werden, damit sie in der GUI angezeigt werden können
#### 2 - Frames and panels
* Panels werden in Frames eingefügt
* Frame hat zwei Konstuktoren (ohne/mit Titel)
* Default Layout von Frame ist von Links nach Rechts - FlowLayout
* Man sollte bei Frames die Eigenschaft setzen, was soll passieren wenn auf *Schließen* geklickt wird:
    1. HIDE_ON_CLOSE - default
    2. EXIT_ON_CLOSE - meistens genutzt
    3. DISPOSE_ON_CLOSE 
    4. DO_NOTHING_ON_CLOSE
### 3 - Components and Layouts
#### 1 - Swing components
* alle Swing-Componenten erben von JComponent
* JComponent erweitert Container-Classe
#### 2 - Layout managers
* Layout Manager - Klassen, die Größe und Position der Komponenten kontrollieren
* Default ist FlowLayout - von Links nach Rechts
* Swing hat mehrere Layout Manager: (siehe Bsp. aus Exercise)
    1. BorderLayout - Teil View in 5 Teile: Nord, Süd, Ost, West und Zenter
    2. BoxLayout - Stackt die Komponenten - von Links nach Rechts -> bis kein Platz, dann zur nächsten Zeile
    3. CardLayout - Managet mehrere Komponenten, die den gleichen Teil teilen - man muss hier selber etwas Porgrammieren, da die Elemente den gleichen Space teilen
    4. FlowLayout - teilt alles in Zeilen
    5. GridBagLayout - tielt in Zeilen und Spalten
    6. GridLayout - teilt in alles in gleiche Zeilen und Spalten (also Zellen) - man muus hier eventuell auch eigenen Code einfügen, damit alles gut aussieht
    7. GroupLayout - arbeitet mit horizontalen und vetikalen Layout getrennt
    8. SpringLayout - flexibler Layout, der alle anderen Layouts simuliert
* in Designer kann man über Properties die Eigenschaften der Layout-Manager einstellen
* `JPanelName.setLayout(...)` - Layout setzen oder über Properties von JPanel oder über RechtsKlick auf JPanel -> Set Layout.  
#### 3 - Menus and toolbars
* Menu-Klasse in Swing hat:
    * Menu Bar
    * Menu Item
    * Menu
    * Menu Item/Checkbox
    * Menu Item/Radio Button
    * Popup Menu
* Toolbars - ist dem Menu sehr ähnlich, gruppiert Componenten (gewöhnlich Buttons)
    * oft als visuelle Repräsentation der Menu mit Icons zum anklicken
* in Design 
    1. Menu Bar auswähen
    2. Tool Bar auswählen
    3. Man kann im Designer Submenüs eingügen
        1. Menu-Eintrag auswählen
        2. Rechtsklicken -> Add From Palette -> Menu Item/../...
        3. über Properties dann z.B den Text ändern
        4. dann muss man Eventhänder für die Menü-Einträge programmieren
#### 4 - List model controls
* Swing hat Komponenten um Listen (Listen von Icons) zu erstellen
* Liste meisten Scroll Pane
* man muss dann auch Selection Mode setzen:
    1. SINGLE_SELECTION
    2. SINGLE_INERVAL_SELECTION
    3. MULTIPLE_INTERVAL_SELECTION
* Liste triggert automatisch ein Event, wenn Item der Liste ausgewählt wurde
    * Event muss dann vom Code behandelt werden
* Um Liste zu initialisieren => ListModel benutzen
    * Liste kann mit Array oder Vektor initialisiert werden, die automatisch zu ListModel konvertiert wird
* Liste ist immutable - kann nicht geändert werden
    * Listen, die gändert werden können, sind DefaultListModel
    * Drei Listen Modele:
        1. DefaultListModel - die flexibelste Liste
        2. AbstractListModel - default über Desing, ist ummutable
        3. ListModel
* Um z.B maximale Anzahl der Items in der Liste wird sichtbar `setVisibleRowCount(-1)`
* siehe Bsp. ListDemo -> ab Zeile 34:
    + `... ListDemo extends JPanel`
    + `implements ListSelectionListener`
    + `private JList list;` - eigentliche Liste
    + `private DefaultListModel listModel;` - ListModel festlegen
    + `public ListDemo(){}` - Konstuktor
        + `super(new BorderLayout());`
        + `listModel = new DefaultModelModel();`
        + `listModel.addElement("Mars");` - Item hinzufügen
        + `list = new JList(listModel);` - der Liste das ListModel zuweisen
### 4 - Events
#### 1 - What is a Swing event?
#### 2 - Event listeners
#### 3 - How to handle an event

#### 4 - Challenge
#### 5 - Solution