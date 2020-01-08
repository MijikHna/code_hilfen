# 1 - Creating a class
class Duck:
    sound = "Quack"
    movement = "Walk"

    #erster Paramenter kann man nennen wie man will, ist immer THIS. Guter Still ist aber self
    def quack(this):
        print(this.sound)

    def move(this):
        print(this.movement)

donald = Duck()
donald.quack()
donald.move()
print(donald.sound)
# 2- Constructin an object
print("\n# - 2 \n")
class Animal1:
    def __init__(self, type, name, sound):
        #Variablen so initialisiert werden direkt privat
        #_ = privat
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound
class Animal2:
    def __init__(self, **kwargs):
        self._type = kwargs["type"]
        self._name = kwargs["name"]
        #mit Default-Value
        self._sound = kwargs["sound"] if "sound" in kwargs else "gav"

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal1):
        raise TypeError("print_animal(): requies as Animal")
    print("The {} is named '{}' and says '{}'".format(o.type(), o.name(), o.sound()))
a0 = Animal1("kitten", "fluffy", "rwar")
a1 = Animal2(type = "duck", name = "fluffy", sound = "rwar")
print(a0)
print_animal(Animal1("godzilla", "lala", "rwar"))

# 3- Class methods
print("\n # - 3 \n")
class Animal3:
    x = ["test1", "test2"]
    def __init__(self, **kwargs):
        #_ = private, aber mit obj_name._type ansprechbar
        self._type = kwargs["type"]
        self._name = kwargs["name"]
        #mit Default-Value
        self._sound = kwargs["sound"] if "sound" in kwargs else "gav"

    #Getter und Setter gleichzeitig
    def type(self, t = None):
        if t:
            self._type = t
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound
    #
    def __str__(self):
        return "The {} is named '{}' and says '{}'".format(self.type(), self.name(), self.sound())

a0 = Animal3(type = "kitten", name = "name")
a0.type("lala")
print(a0)

# 4 - Object data
print("\n # - 4 #\n" )
a0.x[1] = "lala"
print(a0.x)

# 5 - Inheritance
print("\n # - 5 \n")
class Aninmal4:
    def __init__(self, **kwargs):
        #_ = private, aber mit obj_name._type ansprechbar
        self._type = kwargs["type"]
        self._name = kwargs["name"]
        #mit Default-Value
        self._sound = kwargs["sound"] if "sound" in kwargs else "gav_animal4"
    def type(self, t = None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None
    def __str__(self):
        return "Type: {}, Name: {}, Sound: {}".format(self._type, self._name, self._sound)

#Ableitung
class Unteranimal(Aninmal4):
    def __init__(self, **kwargs):
        self._sound = "gav"
        if "sound" in kwargs:
            del kwargs["sound"]
        #Aufruf des Konstruktors der Basisklasse
        super().__init__(**kwargs)

a0 = Unteranimal(type = "Duck", name = "lala", sound = "test")
a1 = Unteranimal(type = "Duck", name = "lala")
print(a0)
print(a1)

# 6 - Iterators objects
print("\n # - 6 \n")
class inclusiveRange:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError("Expected at least 1 arg")
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

for n in inclusiveRange(25):
    print(n, end=' ')
print()

for n in inclusiveRange(5, 25, 5):
    print(n, end=' ')
print()