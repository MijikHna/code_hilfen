from functools import partial
import pickle
import json
import re
satz = "the quick brown fox jumps over the lazy dog"
worte = satz.split()
wort_laenge = []
for wort in worte:
    if wort != "the":
        wort_laenge.append(len(worte))
print(worte)
print(wort_laenge)

pattern = re.compile(r"\[(on|off)\]")
print(re.search(pattern, "Mono: Playback 65 [75%] [on]"))
print(re.search(pattern, "Nada...:("))

mySet = set("my name is Eric and Eric is my name".split())
print(mySet)

set1 = set(["Jake", "John", "Eric"])
print(set1)
set2 = set(["Jake", "John"])
# Welche Elemente der Beiden Set übereinstimmen. Wird neues Set dabei erzeugt.
print(set1.intersection(set2))
# Welche Elemente nur in einem der Sets vorkommen.
print(set1.symmetric_difference(set2))
# Welche Elemente nur in einem der Sets vorkommen.
print(set1.difference(set2))
print(set1.union(set2))  # Vereinigung der beiden Sets

salaries = '{"Alfred" : 300, "Jane" : 400 }'
decoded_salaries = json.loads(salaries)
print(decoded_salaries)

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# print(json.load(json_string))
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))


def funkt1(x, y):
    return x*y


dbl = partial(funkt1, 2)
print(dbl(4))


def funkt1(param1):
    # Nested Funktion
    def funkt2():
        print(param1)
        # Aufruf der Nested Funktion
    funkt2()


# Aufruf der Funktion
print(funkt1("Test"))


def funkt1(param1):
    # Nested Funktion
    def funkt2():
        nonlocal param1
        param1 = 3
        print(param1)
        # Aufruf der Nested Funktion
    funkt2()
    print(param1)


def funkt1(param1):
    # Nested Funktion
    def funkt2():
        print(param1)
    # Aufruf der Nested Funktion
    return funkt2


# Aufruf der Funktion
funktaufruf = funkt1(10)
funktaufruf()


@decorator
def funkt1(param):
    return param


def funkt1(param):
    return param


funkt1 = decorator(funkt1)
