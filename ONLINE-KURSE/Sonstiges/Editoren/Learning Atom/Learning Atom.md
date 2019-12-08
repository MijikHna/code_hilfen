### 1 - Using the Atom Interface:
#### 1 - Downloading and Installing Atom:
* Welcome-Tab ist ein Package, den kann man abschalten.
#### 2 - Introduction to the Atom interface:
* Atom ist in Panels = Panes aufgeteilt
* 
```
#Makros:
  #legal:
  Copyright (c) 2019 Copyright Holder All Rights Reserved.
  #lorem:
  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
p -> in html würde <p>-daraus maachen <- gilt für alle html-Tags
```

#### 3 - Files and Command Palette:
1. Add project folder = öffnet Ordner im gleichen Atom-Fenster (Projekt-Window)
2. Open... = Ordner im neuen Atom-Fenster
3. Command-Palet = Package (Strg+Shift+P) -> etwas eintippen => werden mögliche Commands
4. verschiedene Terminals sind als Packages installiren
5. apm-Kommand = etwas installiren (Atom Package Manager)
5. Perönicher Ordner\.atom = Atom-Konfigs -> man kann diese verändern

#### 4 - Managing tabs and panes:
* Doppelklick = im eigenem Tab öffnen
* Einzelklick = imk selben Tab öffnen
* man kann Fenster ins unendliche aufteilen
* man kann Tabs packen und im Unterfenster aufmachen
* **Strg+B** - geöffnete Dateien suchen (wenn viele Tabs geöffnet werden)
* **STRG+T** - alle Dateien des Projekts durchsuchen (<-Buffer durchsuchen)

#### 5 - Symbols and bookmarks:
* Line:Column klicken -> Line eingeben => man wird dahin bewegt (STRG+G)
* **STRG+R** - html-Tags + JS-Schlüsselwörter suchen
* Bookmarks:
    * **SHITF+STRG+F2** - an der Zeile einen Bookmark erstellen
    * **STRG+F2** - Bookmarks durchsuchen
    * man kann Packages->Command Palet -> Toogle -> Bookmark eingeben = mögiche Tastenkürzel für Bookmarks anzeigen

#### 6 - Managing and folding content:
* Command Pallet -> fold eingeben = Folding-Befehle anzeigen
* Edit->Folding = Befehle zum Folding

### 2 - Using Editing Features:
#### 1 - Modifying content:
* Edit -> Lines:
    * Intend = TAB <- z.B mehrere Zeilen auswählen + STRG+[ bzw. **STRG+**]
    * Autoindent = Atom TABt alles automatisch (<- etwas gefährlich)
    * **STRG+Pfeil** nach oben/unten = Ziele nach oben/unten verschieben
    * **STRG+SHIFT+D** = Zele dublizieren
    * **SRTG+SHIFT+K** = Zeile löschen
#### 2 - Changing text:
  * **STRG+SHIFT+7** bzw. / = Zeile auskommentieren <- ist Datei-endung-abhängig
  * mehrere Zelen auswählen + **STRG+/** = mehrere Zeilen auskommentieren
    * <- alle unter Edit -> zu finden

#### 3 - Selections and multiple cursors:
* Auswählen-Shortcuts sind unter Selection zu finden
* Command-Pallet -> select eingeben
* multiple cursors:
    * Text auswählen - **STRG+D**
    * **STRG+->/<-** - zum Ende/Anfang der Zeile bewegen
    * **STRG** festhalten + **Cursor setzen** => multiple Cursors überall setzen
    * auf Zeilennummer klicken und ganze Zeilen auswählen

#### 4 - Find and Replace:
* Find-> Möglichkeiten zum Suchen in Atom
* Find -> Find in Buffer = im aktuellen Dokument Suchen
    * Find in Buffer -> Find All -> Esc = mehrere Cursor
    * Aa = auf Groß/Klein achten
    * *./** = Reguläre Ausdrücke = in Find in Buffer .* eingeben <- ist aber nicht immer sinnvoll; .*?
    * Find -> Find in Projekt = im allen Dateien suchen, statt in nur in aktueller -> +
        * Buttons oben benutzen


### 1 - Customize Atom:
#### 1 - Modifying core preferences:
* Edit -> Preferences -> Core:
    * Allow Pending Pane Items = ein Klick auf Datei = Vorschau
    * Exclude VSC Ignored Path = z.B schaut, welche .end in .gitignore stehen und verwendet diese beim git.
    * Packeges -> tree-view -> Hide Ignored Names = .end in .gitignore werden nicht angezeigt.
    * Use Proxy Settings When Calling APM = Sicherheit
#### 2 - Changing editor preferences:
* Edit -> Preferences -> Editor:
    * können von anderen Packages kontrolliert werden/herkommen
    * Invisibles - ob + wie bestimmte unsichtbaren Char-s angezeigt werden
    * Soft Tab = wie groß Tab sollte: sonst/default 4 Leerzeilen
    * Tab Type
        * -> zu Packages gehen -> Scpache wählen + weitere Editor-Einstellungen machen

#### 3 - Using Keyboard Bindings:
* Edit -> Preferences -> Keybindings:
    * hier eigene Shortcuts setzen/verändern
    * Überschreiben Shortcut: auf Icon links klicken -> your keymap file anlicken (cson) (~json) -> Einfügen -> KEY-Teil verändern
    * Falls bestimmter Shortcut nicht dabei ist => View -> Command Palet -> nach Befehlen -> Maus drüber halten => Befehl sehen -> in keymap einfügen und Shortcut vergeben
    * Package -> Key Binding -> Shortcut eingeben = schauen, ob doppelt vergeben oder so

#### 4 - Customizing Atom Packages:
* Edit -> Preferences -> Packages = alle installierten Packages in (Core/Editor/usw. unterteilt)
    * dort die Einstellungen der Packages eisntellen
* Edit -> Preferences -> Install = neue Packages installieren
* atom/packet-name = github-Repo des Packages
    * eventuell einige Packages ausmachen, damit Atom schneller lädt

* Packages:
    * open-in-browser = Rechtsklick auf Datei + in Browser öffnen
    * open-terminal-here = Rechtsklick auf Datei = Datei in Terminal öffnen
    * pigments = in CSS farbe ansehen

#### 5 - Using themes
* Edit -> Preferences ->
* UI-Theme = Genereles Aussehen
* atom/lala klicken bzw. auf Theme-Name = Seite der Atom-Themes öffnen
* Syntax Theme = <- kann etwas UI ändern
    * über Install -> Theme installieren
    * nach "ui" suchen = <- sicher das UI gesucht wird.
    + auf Rädchen kicken = weitere Einstellungen der Theme

#### 6 - Customizing themes
* Edit -> Preferences -> Theme -> View Code => wird in neuem Atom-Fenster geöffnet:
* index.less-Datei <- wichtigste Datei
    * Themes sind in LESS geschriebem
    * + in CoffeeScript (~JS)
    * wenn etwas schieff gelaufen ist => Package reinstallieren bzw.Inhalte von .atom/packages veränder/löschen
* Packages -> Package Generator -> Atom Theme Generator

#### 7 - Creating your own snippet shortscuts:
* Edit -> Stylesheet ... <- in css-Format
* da Einstellungen ändern z.B:
    * .tree-view{font-size: 1.2rem}
    * überschreibt alle Einstellungen davor
    * Packages -> Styleguide -> Show = zeigt CSS-Klassen/Namen für den Atom-Style
#### 8 - Snippets:
* File -> Snippets = eigene p = <p> </p> erstellen
    * .scon
* snip eingeben =: name.end <- end = die Sprache <- eventuell in Packages bei den Sprachen schauen, welche Dateien sie benutzen.
    * ganzoben =
    * prefix = eingabe:
    * body = was rauskommt
* snipns = Snipen ohne Selector:
    * Snippet Name sollten geTABt sein
    * `$!; $1; $2; ${1:http://}` - Platzhalter
        * Bsp:
        ``
        body: ''' <ul>
        <li class="${1:item}">$2</li>"
        <li class="${1:item}">$3</li>"
        <li class="${1:item}">$4</li>"
        '''
        ```

### 4 - Working with Packages:
#### 1 - Pair coding with Atom:
* Edit -> Preferences -> Packages:
    * teletype = -> unten rechts auf Symbol klicken -> sich mit Github verbinden -> token bekommen -> Share/Join kliken = man kann am gleichen Code gleichzeitig arbeiten. = sowas wie google excel
#### 2 - Installing and configuring Atom IDE:
* Edit -> Preferences -> Packages:
    * atom-ide installieren:
        + [atom]-ide-name_der-sprache installieren. (Bsp: ide-css, ide-html, ide-typescript)
    * atom-ide -> Settings -> Liste der Settings.

#### 3 - Exploring the enhanced IDE Features:
* IDE-Features kann man unter View -> Toogle Diagnostic / Toggle Outline / Toogle Debugger / Terminal
* einzelne Features des Packages in den Packages-Einstellungen finden.

#### 4 - Other useful packages:
* Bracket Matcher = öffnende/shcließende Tabs
* Markdown Preview = .md-Dateien Preview anzeigen (GitHub-Beschreibung usw.)
* Timecop = Loudzeiten von Git
### 5 - Using Git and GitHub with Atom:
#### 1 - Creating a Git repository with Atom:
* Ordner in Atom öffnen -> Panel Rechts öffnen (ziehen)
* Create repository klicken-> Init klicken
* Stage All klicken oder + klicken (einzelne Dateien)
* Unten Kommentar eingeben -> Create detached Commit.
    * in dem Git-Panel werden die git-Status - Anzeigen angzeigt.
* Wenn man auf die Datei in Git-Panel klickt => * Diff-Datei der Datei wird angezeigt.

#### 2 - Working with GitHub:
* Repo in Github erstellen
* im Terminal git remote add ... eingeben.
* Atom eventuell neustarten
* Button Login anklicken -> Token besorgen
* Unten Fetch klicken oder Rechtsklick auf Fetch => weitere Aktionen (Pull, Push, Force Push).
* Open a new pull request => wird Github.com geöffnet und Pull request erstellt.
* Fetch + Merge = Pull

#### 3 - Other Git and GitHub packages:
* Package -> Open on Github -> XXX = öffnet XXX auf GitHub
* atom.io -> Dokumentation anschauen
    + eventell auf die Links von Package durcklicken
* Atom Flight Manuel => Atomwissen vertiefen
* Atom Blog = aktuellste Änderungen von ATOM