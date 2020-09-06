## Typ Annotationen für Dynamische Sprachen
* Typ Annotationen gibt es eigentlich nur in "Sprache ohne Typen" 

### Verlauf
1. Was sind Annotationen der Typen
2. Wieso werden Annotationen underrated
3. Wie man Annotationen benutzt
4. Wann benutzen

### Python Dzen (PEP 20)
1. Beatiful is better then ugly
2. Explicit is better then implicit (Offensichtliche besser als nciht offensichtliche)
3. Simple is bettern than complex
4. Complex is better than complicated (Schwere besser als verwirbelt)
* mit `import this` in Pyhotn-Console kann man Python Dzen anschauen

#### Bsp: Typ-Annotationen:
```py
def just_sum_ohne_Typen(arg1, arg2):
    total = arg1 + arg2
    return total

def just_sum_mit_Typen(arg1 int, arg2 int) -> int:
    total: int = arg1 + arg
    return total

just_sum_ohne_Typen(10, 20)
just_sum_mit_Typen(10, 30)
```

### Course
* Interpreter behandelt diese Annotationen wie Kommentare
* Typen sind eher für Menschen
* **MyPy** - kann diese Typ-Annotation prüfen
#### Problem, wenn man keine Annotationen benutzt:
* ohne Annotation ist nicht immer klar für welche Typen die Funktion gedacht ist
```py
# Bsp 1:
Numeric = Union[float, int]

def just_sum(arg1: Numeric, arg2: Numeric) -> Numeric:
    # ..


#Bsp 2:
def get_reply(self, key: str) -> Optional[Union[Dict[str, Any], List [Dict[str, Any]]]]:
    # <- Typ für JSON

JsonData = Union[Dict[str, Any], List [Dict[str, Any]]]
def get_reply(self, key: str) -> Optional[JsonData]:
```
* <- so kann man Typ tief/detaliert prüfen
* weiterer Vorteil: moderne IDEs können direkt als Fehler markieren

* Womit kann man Type-Checking machen:
    1. `Mypy`
    2. `Pyre`
    3. `PyType`
    4. `Pyright`
* Linter: 
    1. Tipp: `flak8`

