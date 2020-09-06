# Lernen VIM

## Allgemeines

1. Eingabemodus (`i`, `I`, `a`, `A`, `o`, `O`, `i`, `R`, ...)
2. Kommandmodus (`ESC`, `STRG+C`)
3. Statuszeile-Kommandmdos (`:`, `/`)
4. Visualer Modus: (`v`-Zeichenorientiert, `V`- Zeilenorientiert, `STRG+V` - rechteckorienteriert)

## Shortcuts

### Kommandmodus

#### in den Eingabemodus wechseln

1. `i`- Einfügen vor dem Zeiger
2. `I` - Einfügen am Zeilenanfang
3. `a`- Einfügen nach dem Zeiger
4. `A` - Einfügen nach Zeilenanfang
5. `o` - Einfügen nach der aktuellen Zeile
6. `O` - Einfügen vor der aktuellen Zeile
7. `s` - Aktuelles Zeichen löschen, dann insert
8. `S` - Aktuelle Zeile löschen, dann insert
9. `Sn` - S-Zeilen ersetzen
10. `cO` - Object überschreiben (` ` - aktuelles Zeichen `w` = Wort, `b` = vorhergehendes Wort `^` = Text bis
11. `gi` - da wieder in den Eingabemodus wechseln, wo man es verlassen hat

* `[count]command` - command count-mal ausführen (default: 1)

* `u` - Letzten Befehl rückgängig machen
* `U` - Undo der aktuellen 
* `:! LINUXBEFEHL` - Linux-Befehl ausführen

* `r<char>` - Ersetzt das aktuelle Zeichen durch `<char>`
* `~` - Ändert Groß/Kleinschreibung des akt. Zeichens
* `q<char> <commands> q` - Makro namens `<char>` aufzeichnen
* `@<char>` - Makro namens `<char>` aufrufen
* `:[range] s/from/to/[g][c]` - in `range` (default: aktuelle Zeile) erstes `from` durch `to` ersetzen; `g`=alle Vorkommen ersetzen; `c`=mit Bestätigung
* `:[range] g[!]/pattern/command` - in `range` (default: ges. Datei) `command` in Zeilen ausführen, die pattern (`!` = nicht) erfüllen
* `!<motion> <system command>` - Filtern bis `<motion>` durch `<system command>`

#### Navigation

* `h`,`l`,`j`,`k` - Cursor links, rechts, runter, rauf
* `Nh`,`Nl`,`Nj`,`Nk` - Cursor N-Zeichen nach links, rechts, runter, rauf
* `w` - Nächster Wortanfang
* `W` - Nächster WORD-Anfang (durch Leerzeichen abgegrenzt)
* `e` - Nächstes Wortende
* `E` - Nächstes WORD-Ende (durch Leerzeichen abgegrenzt)
* `b` - Vorheriger Wortanfang
* `B` - Vorheriger WORD-Anfang (durch Leerzeichen abgegrenzt)
* `ge` - Vorheriges Wortende
* `gE` - zum Ende des Wortes mit `.`, `(`, `{` springen
* `0` - Zeilenanfang
* `^` - Erstes Zeichen der Zeile
* `$` - Zeilenende
* `)` - Nächster Satzanfang
* `(` - Vorheriger Satzanfang
* `}` - Nächstes Absatzende
* `{` - Vorheriger Absatzanfang
* `+` - Erstes Zeichen der nächsten Zeile
* `-` - Erstes Zeichen der vorherigen Zeile
* `%` - Zugehörige Klammer egal ob `(`, `[`, `{`
* `gg`- Dateianfang
* `NUMgg` - zur bestimmten Zeile `NUM` gehen
* `gd`
* `gf`
* `G` - Dateiende
* `fZEICHEN` - zum Zeichen springen vorwärts
* `FZEICHEN` - zum Zeichen springen rückwärts
* `tZEICHEN` - vor dem Zeichen springen
  * mit `;` - zum nächsten gleichen Zeichen springen
  * mit `,` - zum vorherigen gleichen springen
* `g_` - kein Leerzeichen am Ende der Zeile
* `STRG+D` - hälfte der Seite nach unten
* `STRG+U` - hälfte der Seite nach oben
* `<n>G` Zeile `<n>`
* `H` - Erste Bildschirmzeile
* `M` - Bildschirmmitte
* `L` - Letzte Bildschirmzeile
* `STRG-f` - Bildschirmseite runter
* `STRG-b` - Bildschirmseite hoch
* `STRG-d` - Halbe Bildschirmseite runter
* `STRG-u` - Halbe Bildschirmseite hoch
* `[<n>]zt` - aktuelle Zeile auf Bildschirmzeile `<n>` scrollen
* `[<n>]zb` - aktuelle Zeile auf `<n>`t-lezte Bildschirmzeile scrollen
* `zz` - aktuelle Zeile auf Bildschirmmitte scrollen

#### Suchen + Ers

* `/MUSTER` - nach `MUSTER` suchen vorwärtes
  * `n` - zum weiteren Treffer gehen
  * `/` -letzte Suche wiederholen
* `?MUSTER` - nach `MUSTER` suchen rückwärts
  * `n` - zum weiteren Treffer gehen vorwärts
  * `?` letze Suche wiederholen
* `n` - letzen Suche in dieselbe Richung wiederholen
* `N` - letze Suche in die umgekehrte Richung wiederholen

* `:a,es/MUSTER1/MUSTER2/ge` - `MUSTER1` durch `MUSTER2` ersetzen in den Zeilen von `a` bis `e` (z.B `$` letzte Zeile). Nur das erste Vorkommen pro Zeile ersetzte wird. Ohne `a` und `e` wird nur für aktuelle Zeile angewendet. `g` alle Vorkommen in der Zeile. mit `e` wird bei jeder Ersetzung um Bestätigung gebeten.

* `rX` - aktuelles Zeichen durch `X` ersetzen

#### Zeilennummerinung und Marken

* `:num` - Ausgabe der aktuellen Zeilennummer
* `mNAME` - Marke bei aktzellen Zeilenummer mit `NAME` setzen/markieren.
* `'NAME` - zur Marke springen
* `:marks` - alle Markierungen anzeigen

#### Löschen und Kopieren

* `NdO` - Löschen von `N` Objekte von Typ `O` + wird in Puffer übertragen. Ohne `N` wird **1** angenommen. `O`: ` ` = Zeichen, `w` = Wort, `d` = Zeile.

* `dMARKE` - Löschen von aktuellen Zeile bis `MARKE`
* `x` - einzelnen Zeichen löschen.
* `NyO` - Kopieren von `N` Objekten des Typs `O` in den Puffer. ohne `N`, wird `N=1` angenommen. `O`: ` ` = Zeichen, `w` = Wort, `d` = Zeile.
* `x` - Zeichen unter Cursor löschen
* `X` - Zeichen vor Cursor löschen
* `d<selection>` - Löschen bis zur Position `<motion>`
  * `d5j` - 5 Zeilen nach unten löschen
  * `df'` - alles bis zum `'` nach unten löschen
  * `dt'` - alles bis zum `'` nach oben löschen
  * `d/hello` - alles bis `hello` löschen
* `ggdG` - ganzes Dokument löschen
* `dd` - Aktuelle Zeile löschen
* `D`  Von Cursor bis zum Zeilenende löschen

#### in INSERT/EINGABE-Modus:

* `STRG+h` - letztes eingegebene Zeichen löschen
* `STRG+w` - letztes eingegebene Wort löschen
* `STRG+u` - letzte eingegeben Zeile löschen
* `STRG+p` - Wort vervollständigen
* `STRG+t` - Zeile einrücken
* `STRG+d` - Zeile ausdrücken

* `Y` - Zeile kopieren
* `yMARKE` - kopieren von aktuellen Position bis zur `MARKE`
* `dd` - Zeile löschen + in Puffer kopieren ~ ausschneiden
* `p` - aus dem Puffer einfügen (`p` - put)
  * es gib 26 Puffer die werden mit `NUMp` angesprochen
* `J` - Anhängen der folgenden Zeile an die aktuelle Zeile ~ Enter löschen.
* `y<selection>` - Kopieren in Default-Puffer bis `<motion>` (`y` - yank)
* `yy` - Kopieren der aktuellen Zeile
* `c<selection>` - Ersetzen (Löschen und Eingabe) bis `<motion>` (`c` - change)
* `cc` - Aktuelle Zeile ersetzen
* `C` - Vom Cursor bis zum Zeilenende ersetzen
* `p` - Default-Puffer nach Cursor einfügen (von d oder y)
* `P` - Default-Puffer vor Cursor einfügen
* `.` - Wiederholung des letzten d oder c
* `J` - Verbindet die aktuelle mit der nächsten Zeile

* Groß => bis Ende der Zeile

### Statuszeilen-Kommandomus:

1. `/` - Suchen vorwärtes
2. `?` - Suchen rückwärts
3. `:` - Kommandos eingeben

### VIM Objects

* `a` - Text + Leerzeichen
* `i` - Text ohne Leerzeichen
* `w` - Word
* `s` - Sentence
* `'` bzw. `"`
* `p` - Paragraph
* `b` - Block in `()`
* `B` - Block in `{}`
* `t` - HTML-Tag

#### Bsp: Combination Operation + Objects

* `daw` - Wort löschen
* `ciw` - inneres Wort ändern
* `das` - Sentence löschen
* `da"` - etwas in `"` löschen
* `ci"` - etwa in `"` ändern
* `dap` - Paragraph löschen
* `dab`/`da(`/`da)` Block in `()` löschen
* `dat` - HTML-Tag löschen
* `cit` - HTML-Tag Inhalt ändern 

### Sontiges

* `.` - letzte Änderung wiederholen

### Splits:

* `:sp DATEINAME` - horisontaler Split
* `:vsp DATEINAME` - vertikaler Split
* `STRG+W+(hjkl)` - sich zwischen den Spits bewegen
* `STRG-w w` - Nächstes Fenster selektieren (zyklisch)
* `STRG-w j` - Ein Fenster nach unten
* `STRG-w k` - Ein Fenster nach oben
* `<n>STRG-w +` - Fenster um `<n>` Zeilen vergrößern
* `<n>STRG-w -` - Fenster um `<n>` Zeilen verkleinern
* `<n>STRG-w _` - Fenstergröße auf `<n>` Zeilen setzen (ohne `<n>:` maximal)
* `STRG-w =` - Alle Fenster gleichgroß

* `:tabnew DATEINAME` - Datei in neuem TAB öffnen
* `:tabn` - zum nächst TAB gehen
* `:tabp` - zum vorherigen TAB

### Plugings:

#### Vim-Surroung

* `s`-Operator:
* `dsZEICHEN` z.B
  * `ds'` die Zeichen `'..'` löschen
  * `cs'"` Zeichen `'` mit `"` ersetzen
  * `ysaptli>` (`ys{MOTION}{CHAR}`) - p-Tag mit `<li>` umschließen
* man kann auch `S` im Visual-Mode benutzen `S{desired character}`

#### Vim-Sneak

* `s{char}{char}` - den Cursor zum `{char}{char}` bewegen
* mit `,` zum nächsten Vorkommen gehen
* `S{char}{char}` - rückwärts

#### Vim-EasyMotion

* `\\` 
* `\\w` - alle Wörter markiern die mit `w` beginnen markieren
* `\\f'` - alle Vorkommen von `'` markieren

#### NUR VS-CODE

* `gd` - weiteren Cursor beim nächten gleichen Wort einfügen
* `af` - im Visual Mode größere Blöcke auswählen
* `gh` - Mouse-Hover simulieren

### Dateiverwaltung

* `ZZ`- Abspeichern und VIM verlassen
* `:w {DATENAME}` - Datei speichern (als)
* `A,E w {DATEINAME}` - Zeilen von `A` bis `E` abspeichern
* `:q!` - VIM beenden
* `:r {DATAINAME}` - Text aus Datei einlesen

### Textfaltung

* `zf<selection>` - Faltung erzeugen
* `zo` - Faltung öffnen
* `zc` - Faltung schließen
* `zr` - sichtbare Faltungstiefe erhöhen
* `zR` - alle Faltungen sichtbar machen
* `zm` - sichtbare Faltungstiefe verringern
* `zM` - alle Faltungen einklappen
* `zn` - Faltungsmodus ausschalten
* `zN` - Faltungsmodus einschalten
* `zi` - Faltungsmodus umschalten
* `:set foldmethod` - Methode setzen (indent, marker, syntax)

### Bsp

* `4s`  4 Zeichen ersetzen
* `20j` Zeiger/Cursor um 20 Zeichen nach unten verschieben
* `4711G` - Zeiger/Cursor zur Zeile 4711 verschieben
* `fs` - Zeiger zum nächsten Zeichen `s` verschieben
* `/Hallo` - nach Hallo suchen
* `?Hallo` - nach Hallo suchen
* `:1,3s/donald/dagobert/c` - **donald** durch **dagobert** in den Zeilen 1 bis 3 ersetzen
* `:1,$s/donald/dogobert/gc` - **donald** durch **dagobert** im gesamten Text ersetzen
* `4dw` - 4 nächsten Worte löschen
* `"a6dd` - nächsten 6 Zeilen mit Übetragung in den Puffer **a** löschen
* `d'm` - Text von aktuellen Pos bis zur Marke löschen
* `5yy` - Kopieren von 5 Zeilen in Puffer
* `:w mytext.txt` - als **mytext.txt** speichern
* `:r mytext.txt` - aus **mytext.txt** einlesen
