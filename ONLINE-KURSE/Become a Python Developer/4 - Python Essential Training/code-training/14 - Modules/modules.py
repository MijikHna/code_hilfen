# 1 - Using standard modules

#System-Spezifische Parameter + Funktionen
import sys

v = sys.version
p = sys.platform
print("Pyhton version {}.{}.{}".format(*v))
print(p)

#Betriebssystem Funktionen
import os

v1 = os.name
v2 = os.getenv("PATH")
v3 = os.getcwd() # Current Working Direktroy
v4 = os.urandom(34) #24 Bytes Randomzahl
v5 = os.urandom(35).hex()

import random

x = random.randint(1, 1000) # Int zwishcen 1 und 1000

print(x)

x1 = list(range(25))
#braucht eine Liste als param
random.shuffle(x1)
print(x)

import datetime

now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.microsecond)


# 2 - Creating a modules
print("\n # - 2")

import saytime
st = saytime.saytime()
print("\nnumbers test")
list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20)
for l in list:
    st.number(l)
    print(l, st.numwords)

print("\ntime test:")
list = ()


