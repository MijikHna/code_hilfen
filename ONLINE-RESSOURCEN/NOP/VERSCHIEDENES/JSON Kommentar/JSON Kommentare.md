1. `"_comment1": "Mein Kommentar";`
2. `"__comment2__": "Mein Kommentar";` - wird Fett in IDE dargestellt

* aber JSON parser sehen es als JSON-Daten z.B hier kann ma diese Kommentare auslesen:
```python
import json

with open("test.json", mode="r") as json_obj:
    data = json.load(json_obj);

print(data)

print(data["_comment1"])
```

+ JSMin-Framework löscht Kommentar und Leerzeichen aus JSON-Dateien.