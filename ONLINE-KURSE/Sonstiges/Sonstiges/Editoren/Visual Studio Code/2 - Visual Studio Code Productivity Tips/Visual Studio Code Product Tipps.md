### 0 - Introduction
* Befehlspalette -> git cloen -> Repo eingeben = Git-Repo klonen

### 1 - Tips and Techniques:
#### 1 - Use Go to an Peek Definition to find code references:
* Rechtsklick auf der Funktio -> zu Definition gehen (F12) => Tab mit der Definitionsdatei wird geöffnet
    * zurückgehen = auf den alten Tab klicken (ALT + <-)
    *  das Gleiche gilt für Import-Module
* Rechtsklick -> alle Referenzen finden = links werden Dateien mit Vorkommnissen, wo die Funktion/Variable/usw vorkommt, angezeigt. !!! Aber nur Vorkommnissen in Dateien angezeigt, die als Tab geöffnet.
*Peek Definition = Rechtsklick -> Peek Definition = zeigt im PopUp die Definition der Funktion <- man kann die Definition direkt im PopUp ändern + Alles Speichern klicken.

#### 2 - Refactor the code:
* Rechtsklick -> Rename Symbol -> ändern => alle Vorkommnissen der Variable werden geändert
* Rechtsklick -> Change all Occurences -> ändern => Mehrere Cursor 

* Hardeinkodierte Variable als Konstane rausholen => Rechtsklick -> Refactor -> Extract to Constant ... -> Namen für Konstane eingeben.

* Wenn man eingen bestimmten Teil des Codes auswählt, VS Code zeigt alle Vorkommnissen an => wenn mehrmals vorkommt => eventuel zu einer Funktion machen => Rechtsklick /Klick auf Lampe -> Refactor -> Extract Funktion ... -> der Funktion einen Namen geben. !!! eventuel muss man noch weitere Vorkommnissen durch die Funktion ersetzen.
    
#### 3 - Favorite extensions: Bracket Pair Colorizer:
* Bracket Pair Colorizer 2 = Färbt die passenden Klammern passenden
    
#### 4 - Tidy code layout with Format Document:
* Befehlspalette -> format eingeben -> (eventuell davor Auswahl des Codes machen) -> Format Selection/Format Document
* Einstellugnen -> format suchen -> Format on type = wird beim Eingeben formatiert <- !?
* Einstellugnen -> format suchen -> Format on Paste
* Einstellugnen -> format suchen -> Format on Save

* Ändern der Einstellugnen für Formatierung:
    * HTML:
        * Einstellugnen -> Erweiterungen -> HTML -> Wrap Attribute 
    * JS:
        * Einstellugnen -> javascript format -> 

#### 5 - Favorite extensions: XML Tools:
* Wenn Rechtsklick -> Document Formatieren nicht da => keine Erweiterungen für die Formatierung vorhanden => muss man eine Installieren
* XML Tool:
    * erlaubt Document formatieren
    * im File-Manager erscheint XML Document = zeigt alle <..>-Eltern-Kinder-Abhängigkeiten

#### 6 - Create custom keybindings for common commands:
* Einstellugnen -> Tastenkombination -> im Suchfeld den Befehl eingebne, für den man Shortcut machen will -> den Befehl anklicken -> Shortcut eingeben -> wenn Überlappung => Enter = wird überschrieben, sonst abbrechen.
* Es gibt Erweiterungen, die Shortcuts der anderen Editoren einfügen:
    * Erweiterungen -> keymap eingeben -> auswählen
    
#### 7 - Favorite extensions: Spell Checker:
* in Erweiterungen nach spell suchen -> eventuel nach Rating sortieren -> Installieren
    * Lampe klicken => Vorschläge für Wörter anzeigen oder STRG + .
    * man kann auch Wörter zum Wörterbuch hinzufügen
    
#### 8 - A simple Technique to copy code blocks:
* ALT + Pfeil nach oben/unten = Ziele nach oben/unten verschieben
    
#### 9 - Favorite extensions: Sort lines:
* Erweiterungen Installieren -> Zeilen auswählen -> Befehlspalette -> sort lines eingeben -> passendes wählen
    *  siehe emmet.html


#### 10 - Use Emmet notation to add boilerplate text:
*  statt z.B <div> </div> einfach div eingeben
    * funktioniert auch für css => befehle schneller eingeben
    
#### 11 - Favorite extensions: GitLens:
* wenn man in einer Zeile ist => sagt sie Wer wann usw. committet hat + es gibt im PopUp Buttons
* Obem Am Tab zeigt, auch wieviele Autoren usw. -> Klicken => zeigt die Commits der Autoren und welcher Commit was verursacht hat.
* Es gibt Links auch einen Icon, die einige Einstellungen + History der Datei anzeigt. = in der Git-History suchen.
    
#### 12 - Use font ligatures to add symbols to your code
* FireCode = Farben ändern => Einstellugnen -> Suchen nach font -> in Editor: Font Family FireCode als erstes eintragen (Höhere Priorität)
* Editor:Font ligatures anhacken.