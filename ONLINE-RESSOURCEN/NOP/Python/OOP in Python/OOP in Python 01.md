Klassen und Instanzen erstellen

### Klasse in Python schreiben
* Bsp 01:
```python
class Customer:
    def __init__(self, first, last, mobile, monthly):
        self.first = first
        self.last = last
        self.mobile = mobile
        self.fullname = first + " " + last
        self.monthly = monthly
```
* `__init__()` ist Konstruktor, wird beim Erstellen des Obj aufgerufen
* `self` - Zeigt auf eigenes Obj.

### Instanzierung + Methoden
* Bsp 02 - Instanzierung
```python
cust01 = Customer("Emilee", "Smith", "012358489", 2000)
```
* Bsp 03 - Methode erstellen
```python
class Customer:
    def __init__(self, first, last, mobile, monthly):
        self.first = first
        self.last = last
        self.mobile = mobile
        self.fullname = first + " " + last
        self.monthly = monthly

    def annual(self):
        self.salary = self.monthly*12
        return '{0} {1}'.format{self.fullname, self.salary}

# Aufruf
print(cust1.annual())
```