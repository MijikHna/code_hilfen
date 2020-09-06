### Magische Methoden
* Methoden die mit `__` beginnen und `__` enden
* = **dunder** Methoden
* z.B `__add__` ist `+`
```python
x = 5
x = x + 3
# ==
x = 5
x.__add__(3)
```

#### \_\_init\_\_()
* ist Konstruktor
```python
class Student():
    def __init__(self, id, name):
        self.id, self.name = id, name

s = Studnet(1, "Max")
print(s)
```

### \_\_str\_\_()
* Ausgabe umschreiben
```python
class Studnet():
    def __str__(self):
        return f"Studnet {self.name} with id {self.id}"
s = Student(1, "Max")
print(s)
```
* es gibt noch `__repr()__`

#### \_\_len\_\_()
```python
class School():
    def __init__(self, students, grades):
        self.students, self.grades = students, grades
    def __len__(self):
        return len(self.grades)

students = [Student(1, "Max1"), Student(2, "Max2")]
grades = ["A", "F+"]
sc = School(students, grades)
len(sc)
```

#### \_\_getitem\_\_()
```python
class School()::
    def __getitem__(self, i):
        return self.student[i].name self.grades[i]
sc[0] #getitem
```

#### \_\setitem\_\_()
```python
class School()::
    def __setitem__(self, i, value):
        self.grades[i] = value
sc[0] = "A"
```

#### \_\getattr\_\_() und \_\setattr\_\_()
```python
class School()::
    def __setattr__(self, k, value):
        if not k.startswith("_"):
            self._all_attr[k] = value
        super().__setattr__(k,v)
students = [Student(1, "Max1"), Student(2, "Max2")]
grades = ["A", "F+"]
sc = School(students, grades)
```

#### \_\iter\_\_()
* = Iterator 
```python
class School()::
    def __iter__(self):
        for i in range(0, len(self.grades)):
            yield self.students[i].name, self.grades[i]
students = [Student(1, "Max1"), Student(2, "Max2")]
grades = ["A", "F+"]

sc = School(students, grades)
next(iter(sc))

for s,q in iter(sc):
    print(s, q)
```

#### \_\add\_\_()
```python
class Cost():
    def __init__(self, symbol, value):
        self.symbol, self.value = symbol, value
    def __add__(self, other):
        return self.value + other.value
pizza = Cost('$', 100)
burger = Cost('$', 100)

allCosts = pizza + burger
```

#### Fazit
* es gibt noch
    + \_\new\_\_()
    + \_\del\_\_()
    + \_\enter\_\_()
    + \_\exit\_\_()
* sehr ähnlich wie Operator-Überschreibung in C++