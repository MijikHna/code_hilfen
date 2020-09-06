#### 1 - monitor()
* `monitor(funcName);` - wird angezeigt, wenn `funcName()` aufgerufen wird + gibt Parameter an
#### 2 - unmonitor()
* `unmonitor(funcName)` - 
#### 3 - monitorEvents
* `monitorEvents(object [, events]);` - monitort eine Funktion, die einem DOM-Objekt zugeweisen wurde: `monitorEvents(button, "click");` oder `monitorEvents(button, "click", "mouseover");` oder `monitorEvents(button, "mouse");` - es werden alle Events die mit `mouse` beginnt getrackt
#### 4 - unmonitorEvents
* `unmonitorEvents(object [, events]);` - z.B. `unmonitorEvents(button, "click");`
#### 5 - $_
* zeigt an letzten Ausdruck in der Console
#### 6 - copy
* `copy(param)` - kopiert `param` in Zwischenspeicher
#### 7 - clear
* `clear();` - wie `clear` in BASH
#### 8 - keys(object) / Objects.keys(objext)
* object ist Key-Value-Array. `keys(myKeyValueArray)` -  return Werte/Namen der Keys
#### 9 - values(object) / Objects.values(object)
* object ist Key-Value-Array. `keys(myKeyValueArray)` -  return Werte der Values
#### 10 - getEventListeners(object)
+ returnt registrierte Objekte des DOM-Objekts `getEventListener(button)`
#### 11 - $(elementName [,node])
* return erstes Element das mit `elementName` übereinstimmt. `$("button");` mit `$("button").id` kann man Wert von `id` auslesen. `$("button", document.querySelector("div"));` = erstes`div button`
#### 12 - $$(elementName [,node])
* wie 11 nur return alle DOM-Objekte
#### weitere Funktionen:
1. `table`
2. `debug`
3. `udnebug`
4. `$x()`
5. `dir`
6. `dirxml`
7. `profile()`, `profileEnd()`
8. `inspect`
9. `$0~$X`