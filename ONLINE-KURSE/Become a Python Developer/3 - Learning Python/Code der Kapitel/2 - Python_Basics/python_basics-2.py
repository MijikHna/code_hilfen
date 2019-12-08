#2 - Variables and expressions

#Variable deklarieren + initialisieren
f=0
print(f)

#Variable redeklarieren
f="abc"
print(f)

#Fehler: Variablen verschiedener Typen können nicht kombiniert
print("This is a string " + str(123) )

#Globale vs. lokale Variablen <- wie bei C/C++
def someFunktion():
    #sagen, dass f globale Variable ist:
    global f
    
    f="def"
    print(f)

someFunktion()
print(f)

#man kann deklarierte Variablen im laufendem Programm löschen
del f
#print(f)

#3 - Python functions:

#einfache Funktionsdefinition
def func1():
    print("I am a function")

#Funktion mit Param
def func2(arg1, arg2):
    print(arg1, " ", arg2)

#Funktion mit return:
def cube(x):
    return x*x*x

#Funktion mit default-Argumenten
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#Funktion mit variablen Parameterliste:
def multi_add(*args):
    result=0
    for x in args:
        result = result + x
    return result

#Aufrufe:
func1()
print(func1()) #gibt None aus, da Funktion kein return hat
print(func1) #gibt Adresse der Funktion

func2(10,20)
print(func2(10,20))
print(func2)

print(cube(3))
print(cube)

print ( power(2) )
print( power(2,3) )
#in Python kann man beim Aufruf die Parameter in belibiger Reihenfolge aufrufen:
print( power(x=3, num=2) )

print(multi_add(4,5,10,4))

# 4 - Conditional structuren:
x, y = 1000, 1000
if (x < y):
    st = "x is less then y"
elif (x == y):
    st = "x is the same as y"
else:
    st = "x is greater then y"
print (st)

# in Python gibt es kein switch-case

#Conditional statement = if-else in einer Zeile
st="x is less then y " if (x < y) else "x is greater than or the same as y"
print(st)

#5 - Loops:
x=0
while (x < 5):
    print(x)
    x = x + 1
#for fnktioiert etwas anders:
# range startet bei 5 und endet wenn x<10
for x in range(5, 10):
    print(x)

#for als Loop über Collection:
days=["Mon", "Tue", "Wed", "Thu", "Fri" ]
for d in days:
    print(d)

# continuer + break
x=5
for x in range (5, 10):
    if (x == 7):
        #break
        continue
    print(x)

#enumerate() benutzen: enumerate() return Index und Werte des Var[Index]
for i,d in enumerate(days):
    print(i,d)

#6 - Classes:

#
class myClass(): 
    # self = referenziert zum Objekt selbst ~ this-> in C++
    def method1(self): 
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)

#Vererbung
class anotherClass(myClass): 
    # self = referenziert zum Objekt selbst ~ this-> in C++
    def method1(self): 
        #hier die Funktion der Oberklasse aufrufen + braucht als Param self
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2 ")

c = myClass()
c.method1()
c.method2("mein String")

c2=anotherClass()
c2.method1()
c2.method2("mein String")