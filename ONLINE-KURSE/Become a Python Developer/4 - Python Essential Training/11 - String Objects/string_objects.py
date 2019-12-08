# 1 - Overview of string objects
#String sind Objekte
# Strin-Methoden,
print("TestString".upper())
print("TestString".swapcase())
print("TestString {}".format(4))
print('''Test

Str   ing {}'''.format(4))
s = "Test String {}"
print(s.format(4))

class myString(str):
    def __str__(self):
        return self[::-1]
s = myString("TestString")

# 2 - Common string methods
print("\n # - 2\n")
print("Test string".title())
print("TestString".casefold()) # auch für UNICODE

#Stirng ist imuteble = nicht veränderbar
s1 = "Hello World1"
s2 = "Hello World2".upper()
print(id(s1))
print(id(s2))

#Zwei Strings verbinden
print(s1 +' '+ s2)
print("TestString")

# 3 - Formatting strings
print("Test {xx} String{bb}".format(xx = 10, bb = 20))
print("Test {1} String{0}".format(10, 20))
print("Test {0:<5} String{1:+05}".format(10, 20))
print("Test {} String{:,}".format(10, 20000000))
print("Test {} String{:,}".format(10, 20000000).replace(",", "."))
# mit ...f kann man Nachkommastellen spezifizieren
print("Test {:f} String{}".format(10, 20))
#hexadezimal
print("Test {:x} String{}".format(10, 20))
#oktal
print("Test {:o} String{}".format(10, 20))
#binär
print("Test {:b} String{}".format(10, 20))
#print(f'Test String {10}')
x = 10
#print(F'Test String{x}')

# 4 - Splitting and Joining
s = "grosser String mit Leerzeilen"
print(s.split())
print(s.split('e'))
#Teilt String in Liste auf
l = s.split()
#Verbinden + statt _ :
s2 = ":".join(l)

