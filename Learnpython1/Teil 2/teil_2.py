import pandas as pd
import numpy as np

array1 = [1, 3, 4, 5]
array2 = [4, 5, 6, 9]

np_array1 = np.array(array1)
np_array2 = np.array(array2)

print(type(np_array1))

calc_np_array = np_array1 / np_array2 ** 2
print(calc_np_array)

print(calc_np_array > 0.1)
print(calc_np_array[calc_np_array > 0.1])


dict = {"country": ["Brazil", "Russia", "India"], "capital": [
    "Brazilia", "Moscow", "New Dehli"], "area": [8.515, 17.10, 3.286]}

brics = pd.DataFrame(dict)
print(brics)

####
brics.index = ["BR", "RU", "IN"]
print(brics)
