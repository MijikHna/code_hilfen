#### Generatoren

werden benutzt, um Iteratoren zu implementieren, sind Funktionen, die iterirbare Objekte zurückgeben. Wird `yield` benutzt.

```python
#Generator
def gen1():
    for i in range(6):
        yeald random.randInt(1, 10)

for x in gen1():
    print("Zufallszahl ist %d" %x)
```

#### List Comprehensions
erstellt neue Listen basierend auf anderen Listen  
Beispiel ohne List Comprehensions:
```python
satz = "the quick brown fox jumps over the lazy dog"
worte = satz.split()
wort_laenge = []
for wort in worte:
    if wort != "the":
        wort_laenge.append(len(worte))
print(worte)
print(wort_laenge)
```
Ausgabe:
```
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
[9, 9, 9, 9, 9, 9, 9]
```
mit List Comprehension
```python
satz = "the quick brown fox jumps over the lazy dog"
worte = satz.split()
wort_laenge = [len(word) for word in words if word != "the"]
print(worte)
print(wort_laenge)
```

#### Mehrere Funktionsparameter
```python
def funkt1(eins, zwei, drei):
    print(eins)
    print(zwei)
    print(drei)
funkt1(1,2,3)

def funkt2(eins, zwei, drei, *vier):
    print(first)
    print(zwei)
    print(drei)
    print(list(vier))
funkt2(1,2,3,10,20,30)
```

Argumente mit Schlüsselnamen
```python
def funkt3(eins, zwei, drei, **optionen):
    if optionen.get("action") == "sum":
        print("Summe ist %s" % (eins + zwei + drei))
    if optionen.get("number") == "first":
        return eins

ok = funkt3(1,2,3, action="sum", number="first")
print(ok)
```

#### Regulare Ausdrücke

`r"^(From|To|Cc).*?python-list@python.org"`  
 `^x`- beginnt mit x  
 `(From|To|Cc)` - kann From, To oder Cc sein
 `.*?` - kann alles sein außer `\n`.  
 z.B folgende Ausdrücke würden passen:  
 `From: python-list@python.org`  
`To: !asp]<,. python-list@python.org`

```python
import re

pattern = re.compile(r"\[(on|off\]")
print(re.search(pattern, "Mono: Playback 65 [75%] [on]"))
print(re.search(pattern, "Nada...:("))
```
Ausgabe:
```
<_sre.SRE_Match object; span=(24, 28), match='[on]'>
None
```
man muss auf jeden Fall Dokumentaion dazu lesen.

#### Exceptions
Per Default wird bei nicht behandelter Exception/Error die Ausführung unterbrochen.
```python
try:
    x = 1 / 0;
except ZeroDivisionError:
    print("Durch 0 geteilt")
```

#### Sets
Sets - Listen, die keine doppelten Einträge haben.
```python
mySet = set("my name is Eric and Eric is my name".split())
print(mySet)
```
Ausgabe:  
`{'is', 'name', 'my', 'Eric', 'and'}`

```python
set1 = set(["Jake", "John", "Eric"])
print(set1)
set2 = set(["Jake", "John"])
print(set1.intersection(set2)) #Welche Elemente der Beiden Set übereinstimmen. Wird neues Set dabei erzeugt.
print(set1.symmetric_difference(set2))
# Welche Elemente nur in einem der Sets vorkommen.
print(set1.difference(set2))
print(set1.union(set2))  # Vereinigung der beiden Sets
```

#### Serialization
Python hat JSON-Lib, um JSON zu arbeiten.  
```python
import json
print(json.loads(json_string)) # String zu JSON konvertieren.
json_string = json.dumps([1, 2, 3, "a", "b", "c"]) #JSON nach String konvertieren

# pickle ist eigene Python-Bib für Serialisierung. 
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
```

#### Partiele Funktionen
Partielle Funktionen - Funktion an andere Funktion mit weniger Parametern deligieren
```python
from functools import partial
def funkt1(x,y):
    return x*y

dbl = partial(funkt1,2) # an Funktion erstmal 2 geben
print(dbl(4)) # Aufruf von dbl => Übergabe des zweiten Parameters an funkt1
```

#### Code Inspektion
```python
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__
```

#### Closures
ist Objekt der Funktionen, der Werte zwischenspeichert.
***Nested Funtion*** - Funktion, die innerhalb anderer Funktion definiert ist. Nested Funktionen können Variablen im eingeschlossenen Scope erreichen, haben aber nur lesbaren Zugriff. Mann kann aber ***Schlüsselwort*** `nonlocal` benutzen, um auch in die Variable zu schreiben.   
Beispiel:
```python
def funkt1(param1):
    # Nested Funktion
    def funkt2():
        print(param1)
    #Aufruf der Nested Funktion
    funkt2()

#Aufruf der Funktion
print(funkt1("Test"))
```    
Ausgabe:  

    Test 
    None

Beispiel:
```python
def funkt1(param1):
    # Nested Funktion
    def funkt2():
        nonlocal param1
        param1 = 3
        print(param1)
    #Aufruf der Nested Funktion
    funkt2()
    print(number)

#Aufruf der Funktion
funkt1(9)
```
Ausgabe:

    3
    3
Wenn man `nonlocal` nicht benutzen würde, die Ausgabe wäre `3 9`
##### Alternative bei Nested Funktionen
```python
def funkt1(param1):
    # Nested Funktion
    def funkt2():
        print(param1)
    # Aufruf der Nested Funktion
    return funkt2


# Aufruf der Funktion
funktaufruf = funkt1(10)
funktaufruf()
```
Vorteil von Closures ist, dass man damit globale Variablen vermeiden kann. 

