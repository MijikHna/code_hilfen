import sys
import time

__version__ = '1.2.0'

class numwords():
    #Dokumentations-Kommentare
    '''

        return a number as words
        e.g, 42 becomes "forty-two

    '''

    _words = {
        "ones": ("oh", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"),
        "tens": ("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"),
        "ten": ("eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"),
        "quarters": ("o\'clock", "qurter", "half"),
        "range": {"hundred": "hundred"},
        "misc": {"munus": "minus"}
    }

    _oor = "OOR" #Out of range

    def __init__(self, n):
        self._number = n
    def numwords(self, num = None):
        n = self._number if num is None else num
        s = ""
        if n < 0:
            s += self._words["misc"]["minus"] + " "
            n = abs(n)
        if n < 10:
            s += self._words["ones"][n]
        elif n < 20:
            s += self._words["teens"][n - 10]
        elif n < 100:
            m = n % 10
            t = n // 10
            s += self._words["tens"][t]
            if m:
                s += "-" + numwords(m).numwords()
        elif n < 100:
            m = n % 100
            t = n // 100
            s += self._words["ones"][t] + " " + self._words["range"]["hundred"]
            if m:
                s += " " + numwords(m).numwords()
        else:
            s += self._oor

        return s

    def number(self, n = None):
        "setter/getter"
        if n is not None:
            self._number = n
        return str(self._number)

#abgeleitet Klasse
class saytime(numwords):
    '''
    
    return the time (from two parameters as words
    e.g., fourteen til noon, quarter past one, etc
    '''

    _specials = {
        "noon": "noon",
        "midnight": "midnight",
        "til": "til"
        "past": "past"
    }

    def __init__(self, h = None, m = None):
        self.time(h, m)

    def time(self, h = None, m = None):
        if h is not None:
            self._hour = abs(int(h))
        if m is not None:
            self._min = abs(int(m))
        return (h, m)

    def time_t(self, t = None):
        if t is None:
            t = time.localtime()
        self._hour = t.tm_hour
        self._hour = t.tm_min

    def words(self):
        h = self._hour
        m = self._min

        if h > 23:
            return self._oor
        if m > 59:
            self._oor

        sign = self._specials["past"]
        if self._min > 30:
            sign = self._specials["til"]
            h += 1
            m = 60 - m
        if h > 23:
            h -= 24
        elif h > 12:
            h -= 12

        if h is 0:
            hword = self._specials["midnight"]
        elif h is 12:
            hword = self.numwords(h)

        if m is 0:
            if h is (0, 12):
                return hword
            else:
                return "{} {}".format(self.numwords(), self._words["quarters"][m])
        if m % 15 is 0:
            return "{} {}".format(self._words["quarters"][m // 15], sign, hword)

