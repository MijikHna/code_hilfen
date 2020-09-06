Bsp:
```python
if __name__ == '__main__':
    main()
```

`__name__` - bekommt ihren Sinn/Szenario je nachdem, was in ihr steht.  
Den "Sinn/Szenario" kann man dann im Modul als andern "Sinn/Szenario" verwenden. Durch Wert in `__name__` kann man entscheiden, ob man dieses Szenario verwenden will.  
### Bsp 1 : "Sinn/Szenario" anwenden
```python
#nameScript.py
def myFunction():
    print 'The value of __name__ is ' + __name__

def main():
    myFunction()

if __name__ == '__main__':
    main()
```
Ablauf:
    1. `__name__` = `__main__` setzen
    2. myFunction und main definieren
    3. `if __name__ == '__main__':` wird zu True
    4. Funktion main() wird ausgeführt

`__name__` per default ist `__main__`. => wenn man Modul andres benutzen will muss man diesen Wert überschreiben.

### Bsp 2: "Sinn/Szenario" in anderes Szenario importieren
z.B *myFunction* im andren Szenario benutzen, importiert man *nameScript.py* als Modul importieren
```python
#importingScript.py
import nameScript as ns

ns.myFunction()
```
=> es ergeben sich zwei NameScopes:
1. importingScript-Scope: hier ist `__name__ = __main__`
2. nameScript-Scope: hier wird `__name__=nameScirpt` gesetzt (wird mit `import`-Statement gemacht)

### Meine Annahme:
wenn man selbst in einer .py-Datei `__name__=__main__` eingibt => wird beim Import es nicht überschrieben.