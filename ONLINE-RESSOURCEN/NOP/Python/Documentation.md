### Sphinx Doku - DocString
* Syntex `""" ... """`
* steht am Anfang des Moduls, Klasse, Funktion usw. Nur so wird von Python Interpreter als Docstring erkannt und mit `__doc__` und `help()` angezeigt.
#### Best Practises:
1. alle Module, Klassen, Methoden (auch Konstruktor `__init__()`) sollten eigenen Docstring haben
2. beginnen mit Großbuchstaben
3. Einzeilige Docstring beschreiben Methode als Befehl nicht was sie macht.
4. Mehrzeilige Docstrings.
```py
"""Returns longitude and latitude of first suggested location in the Netherlands from Postcode API.
  
  :param auth_key: authorization key for Postcode API
  :type auth_key: str
  :param city: textual input for city names to match in Postcode API
  :type city: str
  
  :rtype: (str, str), str, str
  :return: (longitude, latitude), Postcode API status code, Postcode API error message
```
* weitere DocString Formate: `Google Format`, `NumPy Format`.
#### Sphynx Syntax:
* `:param` и `:type`: значение параметра и тип его переменной;
* `:return` и `:rtype`: возвращаемое значение и его тип;
* `:raises`: описывает любые ошибки, которые возникают в коде;
* `:seealso`: информация для дальнейшего чтения;
* `:notes`: добавление заметки;
* `:warning`: добавление предупреждения.
```py
"""SUMMARY

:param VARNAME:VARBESCHREIBUNG
:type VARNAME: VARTYP

:raises ERRORTYPE: ERRORBESCHREIBUNG

:rtype: RETURNTYPE
:return: RETURNBESCHREIBUNG

"""