#### Hallo World
```python
print("Hallo World")
```

### Variable and Types

#### Zahlen
hat zwei Typen `int` und `float`, wobei werden vom Python selbst ermittelt.
```pyton
myInt = 7
print(myInt)

myFloat1 = 7.0
myFloat2 = float(7)
print(myFloat1, myFloat2)
```

#### Strings
```python
string1 = 'String'
string2 = "String"
print(string1, string2)
```
Vorteil von `"` ist, dass man sonderzeichen wie `'` einfügen kann
```python
string3 = "It' is string"
print(string3)
```

### Listen
Listen sind den Array sehr ähnlich.
```
list1 = []
list1.append(1)
list1.append(2)
print(list1)
print(list1[0])
for x in list1:
    print(x)
```

### Operatoren
```python
zahl1 = 1 +2 * 4 / 4.0
print(zahl1)
```

#### Modulo 
```python
modulo1 = 11 % 3
print(modulo)
```

#### Exponent
```python
quadrat = 7 ** 2
kub = 2 ** 3
```

#### Stringoperationen
##### +
string1 = "Hallo" + "Welt"
print(string1)

##### String wiederholen
```python
string2 = "Hallo" * 10
print(string2)
```
Ausgabe: `HalloHalloHalloHalloHalloHalloHalloHalloHalloHallo`

#### Operatoren und Lists
```python
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
listGesamt=list1 + list2
print(listGesamt)
```
Ausgabe: `[1, 3, 5, 7, 2, 4, 6, 8]`

#### Formatierte Ausgabe
```python
string1 = "Kirill"
print("Hallo, %s! ", % name)

string1 = "Kirill
int1 = 23
print("%s ist %d Jahre alt" % (string1, int1))
```

`%s` - String  
`%d` - Integer  
`%f` - Float  
`%.xf` - Float mit Formatierung; x - Format
`%x/%X` - Integer in Hex (x - Klein; X - Groß) 

#### Stringoperationen

```python
string1 = "Hallo Welt"
laenge = len(string1)
woIst_o_ = strint1.index("o")
alle_l = string1.count("l")
```

##### Slices:
```python
string1 = "Hallo world"
print(string1[3:7]) #oder
print(string[3:7:1])
print(string1[3:7:2])
print(string1[::-1])
```

`[3:7]``- 7 ist gemeint bis 7 exklusiv.  

Ausgaben:  
lo w  
lo w  
l
!dlrow olleH

##### Stringfunktionen:
```python
string1 = "Hallo World"
print(string1.upper())
print(string1.lower())
print(string1.startswith("Hallo"))
print(string1.endswith("asdf"))
trennen = string1.split(" ")
print(trennen)

```
Ausgaben:  
Hallo WORLD  
Hallo world
True
False  
['Hallo', 'World']

#### Verzweigungen
```python
x = 2
print(x == 2) # True
print(x == 3) # False
print(x < 3) # True

name = "Kirill"
alter = 23
if name == "Kirill" and alter = 23:
    print("OK")
if name = "Kirill" or name == "Rick":
    print("Auch OK")


name = "Kirill"
if name in ["John", "Kirill"]:
    print("Name ist in der Liste)

if name == "John"
    print("John")
elif name == "Kirill":
    print("Kirill")
else:
    print("ohne Namen")
```

##### is-Operator
`is`-Operator vergleicht die Instanzen selbst (~ Zeiger in C). `==` - vergleicht den Inhalt der Variablen. 
```python
x = [1,2,3]
y = [1,2,3]
print(x == y) #True
print(x is y) #False
```

##### not-Operator
`not` - wie `!` in C
```python
print(not False) # True
print((not False) == False) # False 
```

#### Loops
Es gibt kein normales `for (int i=0; i<y; i++)` in Python.
```python  
list1 = [1, 2, 3, 4]
for x in list1:
    print(x)

for x in range(5):
    print(x)

for x in range(3,6):
    print(x)

for x in range(3,8,2):
    print(x)
```

`range(von, bis, schritte)`

##### while
```python
i = 0
while i < 5:
    if i == 3:
        continue
    print(i)
```

in Python kann man auch `else` am Ende des Loops einsetzen. Es wird ausgeführt, wenn Loop beendet wird
```python
i = 0
while i < 5:
    if i == 3:
        continue
    print(i)
else:
    print(Loop beendet)
```
#### Funktionen

Bei Python gibt es immer ein `return`. Wenn es keinen expliziten `return` gibt, wird automatisch `None`. zurückgegeben

```python
# Definition:
def funkt1():
    print("Hallo Welt")

def funkt2(param1, param2):
    print("Parameter 1: %s, Parameter 2: %s" %(param1, param2))

def funkt3(param1, param2):
    return param1 + param2

# Aufruf:
funkt1()
funkt2("Test1", "Test2")
funkt3(10, 20)
```

#### Klassen und Objekte
```python
class Klasse1:
    var1 = "test1"

    def funkt1(self):
        print("Test")

obj1 = Klasse1()

print(obj1.var1) # Zugriff auf Klassen-Attr
obj1.var1 = "test2"
obj1.funkt1() # Klassen-Methode aufrufem
```

#### Dictionaries
~sowas wie ein Array, der nicht über Index sondern über Namen erreicht wird.
```python
dict1 = {}
dict1["eins"] = 1
dict2["zwei"] = 2
print(dict1)
```
Ausgabe: `{'zwei': 2, 'eins': 1}`

```python
dict1 = {"eins" : 1, "zwei" : 2, "drei" : 3}
dict2 = {  # so ist übersichtlicher
    "eins" : 1, 
    "zwei" : 2
}

for name, inhalt in dict1.items():
    print("Name: %s, Inhalt: %s" %(name, inhalt) )

# Element löschen
dict1.pop("eins") # Element aus Dictionary löschen
del dict1["zwei"]
print(dict1)

if "ein" in dict1:
    print("eins ist dabei)
if "sieben" in dict1:
    print("sieben ist nicht dabei)
```

#### Module und Packete
Module sind Namen der Python-Dateien. Aus Modulen können Klassen Klassen, Funktionen und Variablen importiert werden

Bsp:
```python
ordner
ordner\modul1.py
ordner\modul2.py
```
##### Version 1

```python
import modul1 # ganzes Modul importieren

modul1.funkt1() # Funktion aus importiertem Modul aufrufen
```
##### Version 2
```python
from modul1 import * # alles aus dem Modul importieren und bekannt machen.

funkt1() # Funktion aus importiertem Modul aufrufen, da ja schon bekannt.
```

##### Sonstiges

```python
# Beim Import dem Modul anderen Namen geben. Wird dann im eigenem Programm über den Alias-Namen zugegriffen.
import modul1 as meinModul

# Modul in Abhängigkeit importieren.
if test1:
    import modul1 as meinModul
else:
    import modul2 as meinModul

# Dieses Skrip führt main() aus. Man sollte nur einen Datei mit diesem Code haben. main() selbst kann irgendwo anders definiert wreden.
if __name__ == "__main__":
    main()

# über PYTHONPATH sagen, wo es noch nach Module außer den Standardpfaden geschaut werden soll.
# modul1.py wird ausgeführt + /ordner wird als lokaler Pfad behandelt.
PYTHONPATH = /ordner python modul1.py

# Alternative zu PYTHONPATH. Danach kann man imports aus /ordner machen
sys.path.append("/ordner")

# mit dir() kann man schauen, wo welche Funktion, Klasse usw. im Modul implementiert sind
import modul1
dir(urllib)

# mit help() kann über die Funktion/Klasse/usw im Modul mehr erfahren.
help(modul1.funkt1)

# Ordner = Paket, Paket enthält Module (Modul = .py-Datei)
# aus Ordner /ordner modul1.py importieren /ordner/modul1.py.
import ordner.modul1
#Zugriff auf die Inhalte der Module
ordner.modul1.funkt()

#oder Alternative
from ordner import modul1 

#in __init.py__ kann man entscheiden, welche Module das Paket als API exportiert, und andere Module intern halten, indem __all__ überschrieben wird.
__all__ = ["modul1"]