# 1 - Aritmetical operators
x = 5
y = 3
z = x + y
w1 = x / y # wird float
w2 = x // y # wird ganze Zahl
print(z," ", w1, " ",w2 )
# 2 - Bitwise operators
# & | ^ << >>
print("")
x = 0x0a
y = 0x02
z = x & y
print("(hex) x is {:02x}, y is {:02x}, z is {:02x}".format(x,y,z)) # 02 = Zwei Stellen + erste 0
print("(hex) x is {:08b}, y is {:08b}, z is {:08b}".format(x,y,z))

x = 0x0a
y = 0x05
z = x | y
print("(hex) x is {:02x}, y is {:02x}, z is {:02x}".format(x,y,z)) # 02 = Zwei Stellen + erste 0
print("(hex) x is {:08b}, y is {:08b}, z is {:08b}".format(x,y,z))

x = 0x0a
y = 0x0f
#y = ox05
z = x ^ y
print("(hex) x is {:02x}, y is {:02x}, z is {:02x}".format(x,y,z)) # 02 = Zwei Stellen + erste 0
print("(hex) x is {:08b}, y is {:08b}, z is {:08b}".format(x,y,z))

x = 0x0a
y = 0x01
#y = ox05
z = x << y
print("(hex) x is {:02x}, y is {:02x}, z is {:02x}".format(x,y,z)) # 02 = Zwei Stellen + erste 0
print("(hex) x is {:08b}, y is {:08b}, z is {:08b}".format(x,y,z))

# 3 - Comparison operators
# < > <= >= == !=
x = 42
y = 73
if x < y:
#if x == y:
    print("comparison is true")
else:
    print("comparison is false")

# 4 - Boolean operators
# and, or, not, in, not in (Value (not) in set) is, is not ((not) same object)
a = True
b = False
x = ("bear", "bunny", "tree")
y = "bear"
if a and b:
    print("comparison is true")
else:
    print("comparison is false")

if not b:
    print("comparison is true")
else:
    print("comparison is false")

if y in x:
    print("comparison is true")
else:
    print("comparison is false")

if "tree" in x:
    print("comparison is true")
else:
    print("comparison is false")

if "tree" is x:
    print("comparison is true")
else:
    print("comparison is false")

if y is x[0]:
    print("comparison is true")
else:
    print("comparison is false")
print(id(y), "<- y; x-> ", id(x[0]))

# 5 - Operators precedence