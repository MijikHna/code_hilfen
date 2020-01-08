# 1 - Basic data structures
#Strukturen:
x = [1, 2, 3, 4, 5] #Array in Python = List ist muteble
x = (1, 2, 3, 4, 5) #wie List aber imuteble
x = {"a": 1, "b": 2, "c": 3} #Dictionary, in aderen Sprachen = Hash-Array
x = {1, 2, 3, 4, 5} # Set

# 2 - Lists and tuples
def print_list(o):
    for i in o:
        print(i, end=" ", flush=True)
#List => mit Index einzelene Elemente errechbar
game = ["Rock", "Paper", "Scissors", "Test1", "Test 2", "Test 3"]
print_list(game)
print()
print_list(game[0])
print()
print_list(game[1:3]) # mit Slices/Range erreichen
print()
i=game.index("Paper")
print(i)
game.append("Computer")
game.insert(2, "Computer1")
game.remove("Rock")
removedValue = game.pop()
game.pop(2)
del game[2]
del game[1:2]
print(game)
print_list(", ".join(game) )
#Tupel = wie List nur immuteble = können nicht verändert werden, d.h kein pop, kein append, kein insert
print()
game = ("Rock", "Paper", "Scissors", "Test1", "Test 2", "Test 3")
print_list(game)
print()

# 3 - Dictionaries
def print_dict(o):
    for x in o:
        print("{}: {}".format(x, o[x]))

animals = {"kitten": "meow", "puppy": "ruff", "lion": "grrr", "giraffe": "i am a giraffe", "drageon": "rawr"}
print_dict(animals)

#ist leichter zu lesen
animals2 = dict(kitten = "meow", puppy = "ruff", lion = "grrr", giraffe = "i am a giraffe", drageon = "rawr")
print_dict(animals2)
for k, v in animals2.items(): #k ) key, v = value
    print("{}: {}".format(k, v))
for k in animals2.keys():
    print(i)
for v in animals2.values():
    print(v)
print(animals2["lion"])
animals2["lion"] = "i am a lion"
animals2["monkey"] = "haha"
print_dict(animals2)
print("lion" in animals2)
# 4 - Sets
# = Liste, die keine doppelten Einträge enhalten darf
def print_set(o):
    print('{', end="")
    for x in o:
        print(x, end="")
    print('}')
a = set("We're gonna need a bigger boat")
b = set("I'm sorry, Dave, I'm afraid")
print_set(a)
print_set(b)
print_set(a) # immer in unterschiedlicher Reihenfolge
print_set(sorted(a))

print_set(a - b) #Elemente in a ohne Elemente in b
print_set(a | b) #In a oder b
print_set(a ^ b) #nur in a oder b
print_set(a & b) #in a und in b

# 5 - List comprehension
#Technik um Listen,Sets, Dictionarys usw. aus listen zu erstellen
def print_seq(o):
    for x in o:
        print(x, end=" ")
    print()
seq = range(10)
print_seq(seq)

#List comprehensions
seq2 = [x * 2 for x in seq]
print_seq(seq2)
seq2 = [x for x in seq if x % 3 != 0]
print_seq(seq2)
seq2 = [(x, x**2) for x in seq] # Tupel aus seq
print_seq(seq2)
from math import pi
seq2 = [round(pi, i) for i in seq]
print_seq(seq2)
#Dictionaray aus seq erstellen
seq2 = {x: x**2 for x in seq}
seq2 = {x for x in "superduper" if x not in "pd"}

# 6 - Mixed structures
dlevel = 0
def disp(o):
    global dlevel

    dlevel += 1
    if isinstance(o, list):
        print_list(o)
    elif isinstance(o, range):
        print_list(o)
    elif isinstance(o, tuple):
        print_list(o)
    elif isinstance(o, set):
        print_set(o)
    elif isinstance(o, dict):
        print_dict(o)
    elif o is None:
        print("None")
    else:
        print(repr(o), end="", flush=True)
r = range(11)
l = [1, "two", None, "four"]
t = ("one", "two", None, "four")
s = set("It's a bird, Test")
d = dict(one = r, two = l, thre = s)
mixed = [ l, r, s, d, t ]
disp(mixed)
