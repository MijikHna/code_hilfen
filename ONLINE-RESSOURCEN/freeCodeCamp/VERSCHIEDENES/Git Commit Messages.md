* `git commit -a "Message"` - letzte Commit-Message überschreiben
* `git commit --ammend -m "Message" - letzten Commit komplett überschreiben
* `git config --global core.editor nano` - Default-Editor setzen
* guter Commit sollte so aussehen
```
<max 50 Zeichen kleine Beschreibung>

<detalierte Beschreibung>
```
* <- `git commit -m "Subject" -m "Description .."
* Jedes Team hat eigene Konventionen zu Commit-Messages
* Bsp-Konvetion:
    1. Typ des Commit angeben:
        1. Feature -> **feat**
        2. Bug Fix -> **fix**
        3. Style releated -> **style**
        4. Refactoring -> **refactor**
        5. Test releated -> **test**
        6. Doku related -> **docs**
        7. Code Maintance -> **chore**
        8.  
    2. Body (detailierte Desc) von Subject (kurze Desc) trennen
    3. keine unnötige Kommas usw. bentutzen
    4. Paragraphs groß beginnen
    5. Imperativen Modus benutzen
    6. in Body: welche Changes und wieso gemacht
    7. Ausgangs-Problem beschreiben
    8. 