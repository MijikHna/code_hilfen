#1 - Trigonomentry, Ceiling, Floor and Constants

import math # module muss man importieren

math.ceil(10.10) #Methhoden und Variablen des Moduls benutzen mit math.

#Konstanten
print(math.pi)
print(math.e)

print(math.nan)  # Non a number
print(math.inf)  #unendlich
print(-math.inf)  #-unendlich

#trigonometrische Methoden:
obst_direction = math.cos(math.pi / 4)
print(obst_direction)
print(math.sin(math.pi /4))

#Ceiling and Floor:
cookies = 10.3
candy = 7
print(math.ceil(cookies))  #aufrunden
print(math.ceil(candy))

print(math.floor(cookies))
print(math.floor(candy))

print()
#2 - factorial, square root and GCD
import math

print(math.factorial(3))  #= 3! = 1*2*3
print(math.sqrt(9))

print()
#GCD = größter gemeinsamer Teiler:
print(math.gcd(52, 8))
print(math.gcd(8, 52))

print()
#Rad <-> Grad
print(math.radians(180))  #180 Grad nach rad => 3,14
print(math.degrees(3.14))  # pi nach Grad

#!!!! nicht alle Funktionen sind in math z.B pow(), abs() <- siehe #1

print()
#3 - Python random
import random

print(random.random())  #Zufallszahl von 0 bis 1 <- Kommanzahlen

decider = random.randrange(2)  #Zufallszahl von 0 bis 1
if decider == 0:
    print("HEADS")
else:
    print("TAILS")

print("You rolled " + str(random.randrange(1, 7)))  #Zufallszahl zwischen 1 bis 6 (7 ist exklusiv, 1 ist inklusiv

lotteryWinners = random.sample(range(100), 5)  #5 Zufallszahlen aus 0 bis 99 holen => returnt liste
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))  #Zufall aus einem Array

#Mischen
random.shuffle(possiblePets)
print(possiblePets)

print()
#4 - Calculating statics with Python
#Mittelwert, Median usw.
import statistics

agesData = [10, 13, 14, 12, 11, 10, 11, 15]
print(statistics.mean(agesData))
#print(statistics.mode(agesData))
print(statistics.median(agesData))
print(sorted(agesData))

#Varianz, Standardabweichug
print(statistics.variance(agesData))
print(math.sqrt(statistics.variance(agesData)))
print(statistics.stdev(agesData))



print()
#5 - Iterations with itertools: Infinite processes
import itertools

for x in itertools.count(50):  #von 50 bis unendlich zählen
    print(x)
    if x == 80:
        break
#oder
for x in itertools.count(50, 5):  #in 5-er Schritten
    print(x)
    if x == 80:
        break

x = 0
for c in itertools.cycle("RACECAR"):  #unendlich Loop, der durch Iterierbares Objekt läuft
    print(c)
    x = x + 1
    if x > 10:
        break

for a in itertools.repeat(True):  #unendlich einen Wert wiederholen
    print(a)
    x = x + 1
    if x > 20:
        break

print()
#6 - Iterations with itertools: Permutations and combinations (Permutation = Umsetzung/Vertauschung)
import itertools

election = {1: "Barb", 2: "Karen", 3: "Erin"}

for p in itertools.permutations(election):  #gibt alle möglichen Reihenfolgen von der Liste (hier Dict)
    print(p)

for p in itertools.permutations(election.values()):
    print(p)

print()
#Kombinationen
colorForPainting = ["Red", "Blue", "Purple", "Orange", "Yello"]
for c in itertools.combinations(colorForPainting, 2): #gibt alle Möglichen Kombinationen von 2 Elementen aus der Liste
    print(c)