# 1 - Conditional syntax

x = 5

if x == 0:
    print("0")
elif x < 2:
    print("1,2")
elif x < 4 :
    print("3,4")
else:
    print("5")

# 2 - Conditional operators
x=5
y=6


#logische Operatorn:
# and
if x and y:
    print("x und y")
else:
    print("x nicht und y") 

# or
if x and y:
    print("x oder y")
else:
    print("x nicht oder y") 

# not
if not x:
    print("not x")
else:
    print("nicht not x") 
#Idntity Operator

# is
if x is y:
    print("x ist y")
else:
    print("x ist nicht y")  

# is not
if x is not y:
    print("x ist nicht y")
else:
    print("x ist y")  

#Membership Operator:
# in
x2=[1,2]
if x in x2:
    print("x in x2")
else:
    print("x nicht in x2")   

# not in
if x not in x2:
    print("x nicht in x2")
else:
    print("x in x2")  


# 3 - Conditional assignment

hungry = True
#else muss sein
x = "Feed the bear now" if hungry else "Do not feed the bear"
print(x)