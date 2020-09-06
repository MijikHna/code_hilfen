### Video 1
* pythn.org -> Books - Dokumentation + Hilfe
* `name = "lala"; print(f'Hello, {name}!')`

* Bsp Array sortieren
```python
list01(1,2,3)
list02 = [1,2,3, 23, 6234,623, 67,2,1,78, 98]
print(list)

# max holen
print([1,2,3])

def myMax(elments):
    if len(elements) == 0:
        return None
    else:
        max = elements[0]
        i = -1
        for element in elements[1:]:
            print(element, max, max <= element)
            if max <= element:
                max = element
        
        i = 1
        while i < len[elements]:
            if elements[i] >= m:
                i += 1

myMax(list02)
```

* for braucht Obj, die Iterrierbar sind
* dictionary = Hash-Array - `dict` 
```python
alal = {
    "name": "jack",
    "password": "lala",
    "alter": 10
}
```
* `[]` kann verschiedene Typen haben
* Imports
```python
import lala

lala.funkt() # zugriff

from lala import funkt

funkt() # Zugriff

#Bsp: random
import random

def gen_name():
    name_len = random.randInt(1, 20)
    name = []
    for i in range(name_len):
        name.append(radom.choice("afsaoflwrer"))
    print(name)
    print("".join(name)) #Teile zu String
    print(",".join(name)) # 

# 100 User generieren
for i in range(100):
    users.append({
        "name": modul.generate_name(),
        "password": modul.generate_name
        "age": randInt(1, 200)
    })
```
* <- hat etwas angeklickt und es kamen alle verfügbaren Funktionen 

* server.py
```python
import flask
#code aus pypi für Flask kopieren
#flask installieren

app.run()
```

Hausaufgabe:
* Date + True returnen in Dict
    #DZ1