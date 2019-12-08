# 1 - Handling exceptions
# x = int("string")  <- ValueError
#Bei Fehler -> Fehler steht ganz unten
#+ geht von Unten nach oben

import sys

try:
    #x = int("string")
    x = 5/0
#man kann mehrere Exceptions -> hier Except hintereinander schreiben
except ValueError:
    print("caught ValueError")
except ZeroDivisionError:
    print("caught ZeroDivisionError")
#alle anderen Error fangen
except:
    print("unknown Error")
    print(sys.exc.info())
else:
    print("alles OK")

# 2 - Reporting errors
print("\n # - 2 \n")
class inclusiveRange:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            # eigene Exception Werfen
            raise TypeError("Expected at least 1 arg")
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            #eigene Exception Werfen
            raise TypeError("Drei Argumenten erwartet")

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

try:
    for n in inclusiveRange(5, 25, 5, 10):
        print(n, end=' ')
#Exception abfangen
except TypeError as e:
    print("Range Error, {}".format(e))
print()
