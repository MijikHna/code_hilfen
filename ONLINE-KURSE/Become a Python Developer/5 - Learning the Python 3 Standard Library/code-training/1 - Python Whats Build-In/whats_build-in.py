#Vorwort:
#Std-Library = Built-In-Funktionen und Built-In-Module (in Python); ist auf jeder Mashine verfügbar
#Std-Library = Built-In => kommt mit Compiler/Interpreter vs. External Library = muss extra heruntergeladen werden.

#1 - Logical Operators and, or ,not
isRaining = True
isSunny = False

#and
if isRaining and isSunny:
    print("We migth see a rainbow")
#or
if isRaining or isSunny:
    print("It might be rainy or sunny")

#not
if not isRaining: #wie ! in C/C++
    print("It muss be raining")

print()
ages = [12, 18, 39, 87, 7, 2]
for age in ages:
    isAdult = age > 17
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult")
    else:
        print("Your are " + str(age) + " an adult")

print()
#2 - Comparison Operator
#<- return boolean (True, False)
#Bsp: 5 > 90, 5 == 5, 10 <= 10
print(10 < 75)  #<- True oder False wird ausgegeben
print(75 < 10)

if (10 < 75):
    print("The bigger number is bigger")

kitten = 10
tigger = 75
if kitten < tigger:
    print("The kitten weights less than the tiger")

mouse = 1
if mouse < kitten and mouse < tigger:
    print("The mouse weight the latest")

print(False > True)  # Ausgabe ist False -> False = 0, True = 1

print("Jennifer" > "Jenny")  #Ausgabe ist False da lexikografisch verglichen

print('a' <= 'b')

print()
#3 - Calculation length
firstName = "Taylor"
print(len(firstName))
lastName = "Swift"
print(len(lastName))
firstName.__len__()  #<- len() funktioniert, das String die Funktion __len__() hat

print()
ages = [0, 11, 43, 12, 10]
print(len(ages))
ages.__len__()

print()
i = 0
for i in range(0, len(ages)):
    print(ages[i])

print()
print(len(["Bob", "Mary", "Sam"]))

#Also len() funtioniert für jedes Iterirbares Objekt

candyCollection = {"Bob": 10, "Mary": 7}
print(len(candyCollection))

print()
#4 - Range and list
#range(x) => von 0 bis x
numberedContestants = range(30)  # von 0 bis 30 -> letzte Zahl ist 29

#list(x) = x ist Tupel, list returns Inhalt von diesem Tupel
print(list(numberedContestants))  # x ist 30-Tupel => Ausgabe 0...29
for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here")

print()
luckyWinners = range(7, 30, 5)  # von 7 bis 29 in 5-er Schritten
print(list(luckyWinners))


print()
#5 - Min and Max
playeOneScore = 10
playerTwoScore = 4
print(min(playeOneScore, playerTwoScore))  # min(param...) = gibt min aus des Arrays
print(min(10, 15, -19, 43, 90))
print(min("Kathryn", "Katie"))  #funktioniert auch mit Strings
print(min("Angela", "Bob"))
print(max(playeOneScore, playerTwoScore))
playThreeScore = 19
print(max(playerTwoScore, playeOneScore, playThreeScore))
print(max(10, 15, -19, 43, 90))


print()
#6 - Rounding, absolute Value and exponents

#rounding <- Output ist Int, normal gerundet <- bzw. hängt von Pythonversion
myGPA = 3.6
print(round(myGPA))
amountOfSalt = 1.4
print(round(amountOfSalt))

apple = -1.2
print(round(apple))
goole = -1,6
print(goole)

#print()
#abs() = Betrag
distanceAway = -13
print(abs(distanceAway))
lengthOfRootInGround = -2.5
print(abs(lengthOfRootInGround))

print()
#x hoch y = pow(x,y) -> Bsp: 3 hoch 2 = 9 => pow(3,2)
chanceOfTail = 0.5
inARowTails = 3
print(pow(chanceOfTail, inARowTails))

chanceOfOne = 1/6
inARowOne = 2
print(pow(chanceOfOne, inARowOne))

print()
#7 - Sorted function
#sorted(x) -> x ist iterables Objekt (List, Tuple, String, Dict) -> Output = sortiertes Objekt
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

print()
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))
# => sorted() mit Optionen
print(sorted(["Sue", "jerry", "linda"], key=str.upper))  #Param ist key
print(sorted(pointsInaGame, reverse=True))  #Param ist reverse <- = sortiert in andere Richtung

print()
leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
print(sorted(leaderBoard, reverse=True))  #sortiert nur Keys
print(leaderBoard.get(432))

students = [("Alice", "B", 12), ("eliza", "A", 16), ("Tae", "C", 15)]  #liste von Tupels
print(sorted(students, key=lambda student: student[0]))  # man sortiert nach key; key ist 0-ter Tupel der Tupels in der Liste
print(sorted(students, key=lambda student: student[1]))


print()
#8 - Type functions

#type(x) = returnt den Typ des Param
r = range(0, 30)
print(type(r))

print(type(10))
print(type("Test"))
print(type('a'))

#isinstance(x,y) = x = Variable, y=Klassenname -> Returnt True/False
class Car:
    pass

class Truck(Car):
    pass

c = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))  #return False, type() schauet nicht nach der Vererbung
print(isinstance(c, Car))  #isinstance() schauet nach der Vererbung
print(isinstance(t, Car))

if isinstance(r, range):  #da ja True oder False return => so kann man checken, ob ein Objekt bestimmte Eigenschaften, die die Basisklasse hat beinhaltet
    print(list(r))

