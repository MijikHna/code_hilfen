# 2 - Hello World
# = auch zu testen, ob alles richtig (ganze Toolchain) installiert ist
print("Hello world.")

# 3 - Python anatomy

#!/usr/bin/env python3.7  = Shebang Line => #! müssen erste Zeichen zeichen (Shebang) /usr/bin/env python3 = Pfad zum ausführenden Programm <-> Unix wertet diese Zeile aus

# um Python-Version anzuzeigen
import platform

print("This is python version {}".format(platform.python_version()))

# 4 - Expressions and statements
#Statements = Einheit der Ausführung <- Zeile des Codes
#Expression = Einheit der Evaluation <- alles was ein Wert returnt
#(x,y) = Tuple-Value

version = platform.python_version()
print("This is python version {}".format(version))

#mit ; kann man Anweisungen hintereinander schreiben
print("Anweisung 1") ; print("Anweisung 2")

# 5 - Whitespace and comments

#!!! wenn etwas ohne Tab beginnt => wird sogar vor main ausgeführt !!!
#es gibt keine Mehrzeilige Kommentare

# 6 - Using print()
print("Hello world.")

x=43
#.format ist Funktion von String-Objekt 
print("Hello world {}".format(x))
print("Hello world {} {}".format(x, 15))
#in Python ist String kein Objekt => print arbeiten ähnlich wie in C/C++
print("Hello world %d" % x) # <- ist aber veraltet, wird bei komplett entfernt

# 7 - Blocks and scope
#Block = alles unter gleichen Tabs
# =>Leertaste kann indentation level-Error verursachen, da Blcok mit Tabs gemessen werden => es gibt keinen Block für Zeile mit Leertaste

#Scope definieren Funktionen, Objekte und Module
# => Variable, die in einem Unterblock definiert wurde, ist auch im Oberblock gültig

# 8 - Conditions

x=42
y=79

if x < y:
    print("x < y is {} and y is {}".format(x, y))
elif (y==x):
    print("x = y is {} and y is {}".format(x, y))
else:
    print("x > y is {} and y is {}".format(x, y))

# 9 - Loops
words= ["one", "two", "three", "four", "five"]
n = 0
while ( n < 5):
    print(words[n])
    n += 1

print()
for i in words:
    print(i)

#fibonacci
a, b = 0,1
while b < 1000:
    print(b, end = " ", flush = True)
    a, b = b, a + b
print()

# 10 - Functions
def function(n = 1):
    print(n)

function(10)
#Funktion return immer None per default
x = function()
print(x)

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True
n1 = 5
n2 = 6 
if isprime(n1):
    print("{} is prime".format(n))
else:
    print("{} is not prime".format(n))

def list_prime():
    for n in range(100):
        if isprime(n):
            #end=" " = statt mit \n mit _ print beenden
            #flush = True = wie flush() in c/c++
            print(n, end=" ", flush = True)
    print()

list_prime()

# 11 - Objects
class Duck:
    sound = "Quaaaack!"
    walking = "Waling"
    #ersten Parameter kann man nennen wie man will, ist aber immer Referenz auf Objekt der Klasse (also this) !! self ist aber etabliert
    def quack(self):
        print("Quack!")
    def quack2(self):
        print(self.sound)
    
    def walk(self):
        print("Walk")

    def walk2(this):
        print(this.walking)

donald = Duck()
donald.quack()
donald.walk()
donald.quack2()
donald.walk2()