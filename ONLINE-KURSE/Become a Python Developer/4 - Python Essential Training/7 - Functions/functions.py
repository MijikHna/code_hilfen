# 1 - Defining a function
#Vordeklarationen:
def main():
    kitten1()
    x = kitten2(5)
    print(x)
    x = kitten3()
    print(x)

    # 2 - Function arguments
    # nur die letzten Params können Defaluts-Values haben
    kitten2_1(1)

    #Call by Value
    x = 5
    print(id(x))
    kitten2_2(x)
    print("{} Meow.".format(x))

    #gleiche ID bei Zuweisung, nach Veränderung aber underschiedliche ID

    #int, double, char sind imutable
    #Objekte sind mutable = Call by Ref
    x = 5
    y = x
    print(id(x))
    print(id(y))
    y = 3
    print(id(y))

    #mutable Variable => automatisch Call by Ref
    xArray = [5]
    yArray = xArray
    yArray[0] = 3
    print(id(xArray))
    print(id(yArray))
    print(xArray[0])
    print(yArray[0])

    # 3 - Argument lists
    #Aufruf mit drei Parametern
    kitten3_1("one", "two", "three")
    test = ("one", "two", "three")
    #Aufruf mit 1 einem Parameter (=Objekt)
    kitten3_1(test)
    #Aufruf mit * = Arrayelemente als einzelne Parameter behandeln
    kitten3_1(*test) # als Ref aufrufen

    # 4 - Keywords arguments
    test = dict(Buffu = "meow", Zilla = "grr", Angel = "rawr")
    kitten4_1(Buffu = "meow", Zilla = "grr", Angel = "rawr")
    kitten4_1(**test)

    # 5 - Return values
    print( kitten5_1() )
    print( kitten5_2() )

    # 6 - Return values


    #7 Generators:
    for i in range(10):
        print(i, end=' ')
    print()

    for i in inclusive_range(10):
        print(i, end =' ')

    #8 - Decorators:
    x = f1
    x()

    x=f2
    f2()

    x = f21(f23)
    x()

    #aufrufen wie oben, aber mit der Wrapper-Aufruf-Kurzschreibweise
    @f21
    def f24():
        print("this ist F24")
    f24()

def kitten1():
    print("Meow.")

def kitten2(n):
    print("{} Meow".format(n))
# in Python return jede Funktion etwas, wenn kein return explizit => None wird return
def kitten3():
    return "Meow."

# 2 - Function arguments
#nur die letzten Params können Defaluts-Values haben
def kitten2_1(a, b = 1, c = 0):
    print("{} Meow.".format(c))

#globale + locale Params:
#Call By Value
def kitten2_2(a):
    print(id(a))
    a = 3
    #andrer ID = Speicheradresse
    print(id(a))
    print("{} Meow.".format(a))
# 3 - Argument lists
def kitten3_1(*varArg):
    if len(varArg):
        for s in varArg:
            print(s)
    else:
        print("Meow.")

# 4 - Keywords arguments
# <- = Arrays mit String als Index
# gute Paxis solche Argumente als kwargs zu nennen
def kitten4_1(**kwargs):
    if len(kwargs):
        for k in kwargs: # k = key
            print("Kitten {} says {}".format(k, kwargs[k]))

# 5 - Return values

def kitten5_1():
    print("Test")

def kitten5_2():
    print("Test")
    #return "returned"
    return [10, 20, 30]
# 6 - Return values

# 7 - Generators
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError("expected at least 1 argument, got {}".format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("expected at most 3 arguments, got {}".format(numargs))

    i = start
    #eigentliche Implementation des Generators
    while i <= stop:
        yield i # ist wie return nur für Generatoren = nach yeild geht wieder in die Funktion
        i += step
    print()

# 8 - Decorator
#spezielle Funktion, die Wrapper-Funktion zurückgibt
#in Python ist alles ein Objekt, auch eine Funktion
def f1():
    print("Decorator")

#etwas wirres:
def f2():
    #hier wird f3 definiert
    def f3():
        print("f3 in f2")
    return f3() # hiert wird f3 aufgerufen
#<- man kann hier f2 nicht aufrufen, da es nur innerhalb von f2 bekannt ist. f2 ist Wrapper von f3
def f21(f):
    def f22():
        print("bevor Funktion-Call")
        f()
        print("after Funtion-Call")
    return f22
def f23():
    print("F23")

#ALSO Decorator = einer Funktion, Funktion als Parameter übergeben




#main-Funktion:
#__name__ = hat namen des Moduls. -> Wenn diese Datei mit Import irgendwo eingebunden, dann wird diese Datei als Modul gelaufen. und Name des Moduls wird dann in __name__ gespeichert.
#Da aber hier diese Datei nicht einbebunden wird, sondern als main(-Modul) gelaufen wird =>
# __main__ = sagt: Das ist kein Modul, dass ist main-Executable
if __name__ == "__main__":
    main()
