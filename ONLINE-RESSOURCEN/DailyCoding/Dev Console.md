### Weitere Methoden von `console`
1. `console.count('Message')` - gibt an wie oft console.XXX aufgerufen wurde
2. `console.warn('Message')` - wie log aber geht in Richtung std.err
3. `console.table(jsonObj);` - als Tabelle darstellen evnt. `console.table([obj1, obj2])`
4. `console.group('Title 1'); console.log('Message); console.group('Subtitle 1'); console.log('Message'); console.groupEnd(); console.groupEnd();` - Ausgabe als Gruppe -> Untergruppe darstellen 