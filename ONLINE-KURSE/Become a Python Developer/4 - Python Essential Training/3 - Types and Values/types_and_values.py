# 1- Overview:

#Python is dynamic-typing Sprache = Wert bestimmt den Variablentyp
x = 7
x = "7.0"
x = True
x = None
print("x is {}".format(x))
print(type(x))

# 2 - The string type

#mit ''' bzw. """" = mehrzeilige Strings
x = '''

seven 

'''

x = "seven '{1:<05}'  '{0:>5}'".capitalize().upper().format(10, 20)

print("x is {}".format(x))
print(type(x))

# 3 - Numeric types
x = 7 * 3
x = 7 * 3.0
x = 7 / 3
x = 7 // 3 # Teilen ohne Rest
x = 7 % 3
print("x is {}".format(x))
print(type(x))

#Alles importieren
from decimal import * 
a = Decimal('.10')
b = Decimal('.3')
x = a + a + a - b
print("x is {}".format(x))
print(type(x))

# 4 - the bool type

x = True
x = 5 > 7
print("x is {}".format(x))
print(type(x))

x = None
#True: !=0, "text"
#False: ==0 "" None
if x:
    print("True")
else:
    print("False")


# 5 - Sequence type
# list, tupel, dictionary

#list
x = [1, 2, 3, 4, 5]
x[2] = 42
for i in x:
    print("i is {}".format(i))

print()
#tupel:
# statt [] ()
# + kann nicht mehr geändert werden
x = (1, 2, 3, 4, 5)
for i in x:
    print("i is {}".format(i))

print()
#range
#kann nicht verändert werden
x = range(5)
x = range(5,10)
x = range(5, 50, 10)
for i in x:
    print("i is {}".format(i))

#list mit Hilfe von range
x = list(range(5,10))
for i in x:
    print("i is {}".format(i))

#dictionary
x = {"one" : 1, "zwei": 2, "drei": 3}
x["drei"] = 45
#so nur keys ausgegeben
for i in x:
    print("i is {}".format(i))
for k, v in x.items():
    print("key:{}, value {}".format(k, v))

# 6 - type() and id()
x = (1,2,3,4,5,6)
x = (1,"two",3.0,[4, "four"],5)
y = [1,"two",3.0,[4, "four"],5]
print("x is {}".format(x))
print(type(x))
print(type(x[1]))
#id = return Identifier of Object
print(id(x))
print(id(y))

if x[0] is y[0]:
    print("yes")
else:
    print("no")

if isinstance(x, tuple):
    print("tuple")
elif isinstance(y, list):
    print("list")
else:
    print("nothing")