* mit `return [wert1, wert2, wert 3]` kann man mehrere Werte returnen
* Tupel:
    1. Tupel = ordered immutable Sequense `myTypel = ('str1', 1, 'str2')`
    2. `return 'str1', 1, 'str2'` - Tupel returnen. Es ist eigentlich `,` was den Tupel ausmacht. Kommas sind bei leeren Tupels und um Tupel deutlicher zu machen => geht auch so: `return ('str1', 1, 'str2')`
* List
    1. List = ordered mutable Sequence (also List kann verändert werden) `myList = ['str1', 'str2', 'str3']` oder `myList = [1, 2, 3]
    2. `myList = []; ... return myList;` oder `return [wert1, wert2, wert3]` - Liste returnen
* Dictionaries
    1. Dictionries = Key-Value Paare

        ```py
        myDict = {
            "one": "one",
            "two": "two",
            "three": "three",
        }
        ```

    2. Bsp:

        ```py
        def myFunc(param1, param2):
            toReturn = {}
            toReturn[param1] = param2
            return toReturn
        ```