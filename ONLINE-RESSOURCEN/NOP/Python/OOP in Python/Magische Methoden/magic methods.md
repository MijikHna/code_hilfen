Magische Methoden sind Methoden mit `__` am Anfang und `__` enden
#### Einführung
* `__init__` und `__new__` = `new`
* `__str__` = `str()`
* `__repr__` = `repr()`
* `__add__(self, op2)` = `+`-Operator überladen
* `__sub__(self, op2` = `+`-Operator überladen
* <- wenn man dann `obj1 + obj2` wird Python intern `obj1.__add__(op2)` aufrufen. Wenn es keine solche Methode gibt => Excpetion geworfen
#### Binäre Operatoren:
* `+` -	`object.__add__(self, other)`
* `-` - `object.__sub__(self, other)`
* `*` - `object.__mul__(self, other)`
* `//` -`object.__floordiv__(self, other)`
* `/` - `object.__truediv__(self, other)`
* `%` - `object.__mod__(self, other)`
* `**` - `object.__pow__(self, other[, modulo])`
* `<<` - `object.__lshift__(self, other)`
* `>>` - `object.__rshift__(self, other)`
* `&` - `object.__and__(self, other)`
* `^` - `object.__xor__(self, other)`
* `|` - `object.__or__(self, other)`
#### Erweiterte Zuweisungen:
`+=` - `object.__iadd__(self, other)`
`-=` - `object.__isub__(self, other)`
`*=` - `object.__imul__(self, other)`
`/=` - `object.__idiv__(self, other)`
`//=` -`object.__ifloordiv__(self, other)`
`%=` - `object.__imod__(self, other)`
`**=` -`object.__ipow__(self, other[, modulo])`
`<<=`	`object.__ilshift__(self, other)`
`>>=`	`object.__irshift__(self, other)`
`&=` - `object.__iand__(self, other)`
`^=` - `object.__ixor__(self, other)`
`|=` - `object.__ior__(self, other)`
#### Unäre Operatoren
`-` - `object.__neg__(self)`
`+` - `object.__pos__(self)`
`abs()` - `object.__abs__(self)`
`~`	- `object.__invert__(self)`
`complex()` - `object.__complex__(self)`
`int()`	- `object.__int__(self)`
`long()` - `object.__long__(self)`
`float()` - `object.__float__(self)`
`oct()` - `object.__oct__(self)`
`hex()` - `object.__hex__(self)`
#### Vergleichsoperatoren
`<` - `object.__lt__(self, other)`
`<=` - `object.__le__(self, other)`
`==` - `object.__eq__(self, other)`
`!=` - `object.__ne__(self, other)`
`>=` - `object.__ge__(self, other)`
`>`	- `object.__gt__(self, other)`

* Bsp siehe code/length