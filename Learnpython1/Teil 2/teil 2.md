#### Numpy Array

Alternative zu List. Sie sind schneller, möglich Kalkulationen innerhalb des Arrays

```python
import numpy as np # numpy importieren, eventuell noch pip3 install numpy ausführen.

array1 = [1, 3, ,4 ,5]
array2 = [4, 5, 6, 9]

np_array1 = np.array(array1)
np_array2 = np.array(array2)

print(type(np_array))

calc_np_array = np_array1 / np_array2 ** 2
print(calc_np_array)
```
Ausgabe:
```
<class 'numpy.ndarray'>
[0.0625     0.12       0.11111111 0.0617284 ]
```


##### Untermenge
Ganzes Array auf bestimmte Merkmale überprüfen
```python
print(calc_np_array > 0.1)
print(calc_np_array[calc_np_array > 0.1])
```
Ausgabe:
```
[False  True  True False]
[0.12       0.11111111]
```

#### Panda
basiert auf Numpy-Arrays. Hauptstruktur ist DataFrame. DataFrame erlaubt tabellenförmige Daten.

```python
import pandas as pd

dict = {"country" : ["Brazil", "Russia", "India"], "capital" : ["Brazilia", "Moscow", "New Dehli"],"area" : [8.515, 17.10, 3.286]}

brics = pd.DataFrame(dict)
print(brics)
```
Ausgabe:
```
     area    capital country
0   8.515   Brazilia  Brazil
1  17.100     Moscow  Russia
2   3.286  New Dehli   India
```


```python
# Indexierung ändern: (siehe bieden Ausgaben)
brics.index = ["BR", "RU", "IN"]
print(brics)
```

Ausgabe:
```
      area    capital country
BR   8.515   Brazilia  Brazil
RU  17.100     Moscow  Russia
IN   3.286  New Dehli   India
```

Panda-Array(-Tabelle) aus CSV-Datei füllen.
```python
cars = pd.read_csv("cars.csv")
print(cars)
```
