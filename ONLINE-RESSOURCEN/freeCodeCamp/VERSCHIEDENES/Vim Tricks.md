### 0 - Intro

1. OpenVim - interaktives Vim Tutorium
2. `vimtutor` - Linux/MacOS CLI-Tool zum Vim Lernen

* man kann vim-Plugin z.B für VS Code installieren

#### 1 - Neue Zeile mit richtiger Einrückung

* Eigentlich:
    1. Enter = Neue Zeile
    2. Insert Mode
    3. TABs
    4. Edit Mode
    5. Schreiben
* Besser:
    1. SHIFT+S

#### 2 - Fenster resizen

* z.B wenn man 3 Vim-Tabs öffnen
* STRG+W - alle Vim-Tabs gleich machen

#### 3 - zu passender (schließender) Klammer springen

* STRG+5 - zum passenden schließendem Symbol springen

#### 4 - Zeile(n) ein/ausrücken

* wenn man mehrere Zeile auswählt
* `>` / `<` um alle ausgewählten Zeilen ein/auszurücken
* `>>` / `<<` um eine Zeile ein/auszurücken

#### 5 - Einrückungen fixen

1. gg - zum Anfang springen
2. =G - Einrückungen korrigieren

#### 6 - mit Vim-Tabs arbeiten

1. in Command Mode wechseln
2. : klicken
    1. :tabnew = neuen Tab erstellen
    2. gt = go to next tab
    3. gT = go to previous Tab
    4. :tabo = alle Tabs außer den geöffneten schließen

#### 7 - zur vorheriger Datei wechseln

1. STRG+o  - sucht nach vorheriger Cursor Position auch wenn es in anderer Datei war