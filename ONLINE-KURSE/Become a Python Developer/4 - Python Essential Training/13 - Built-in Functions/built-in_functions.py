# 1 - Numeric functions

x = "47"
#Konstuktor für int aufrufen
y = int(x)
z = float(x)
z = abs(y) #Betrag
z = divmod(y,3) # returns Tupel: Division + Rest
#Complex-Konstuktor
z = complex(y, 3)
z = 7 + 3j


print("x ist {}".format(type(x)))
print("x ist {}".format(x))
print("y ist {}".format(type(y)))
print("y ist {}".format(y))

#docs.pyhton.org/3/library/functions.html

# 2 - String functions
print("\n# -2 ")
s = "Hello World"
#Represtiert besten String-Wert des Objekts
print(repr(s))
class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return "repr: The number of bunnys is {} \U0001f596".format(self._n)
    def x__str__(self):
        return "str: The number of bunnys is {}".format(self._n)

s= bunny(46)
#wenn man keine eigene __str__ hat => wird auc h__repr__ genommen
print(repr(s))
print(s)

#benutzt auch repr + benutzt bei keinen ascii-Zeichen die Escape-Zeichen = Darstellung nur in acsii-Zeichen
print(ascii(s))
print(chr(128406))
#print(ord(128406))


# 3 - Container functions
x = print("\n# -3 ")

#Collection + Funktionen an der Collection
x = (1, 2, 3, 4, 5, 6)
x2 = (0, 0, 1, 0, 0)
y1 = x
y2 = reversed(x)
y3 = list(reversed(x))
y4 = sum(x)
y5 = sum(x, 10)
y6 = min(x)
y7 = any(x2)
y8 = all(x)
y9 = zip(x, x2)
x3 = ("cat", "dog", "rabbit")

print(x)
print(y)

for i in y2:
    print(i)

for a, b in y9:
    print(a, b)

for i, v in enumerate(x):
    print(i, v)

# 4 - Objects and class functions
print("\n# -4 ")

x = 42
y = type(x)
print(x)
print(y)
y2 = isinstance(x, int)
print(y2)
y3 = id(x)
print(y3)
