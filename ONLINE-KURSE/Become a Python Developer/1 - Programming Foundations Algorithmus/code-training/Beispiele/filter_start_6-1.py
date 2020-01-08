items=["apple", "pear", "orange", "banana", "apple", "orange", "pear", "banana", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

# => wird Daten-typ Dictionaries verwendet

#TODO Hash-Tabele erstellen
filter=dict()

#TODO Array durchgehen und die Items der Hash-Tabele hinzufügen
for key in items:
    filter[key]=0

#TODO Paare erstellen
result=set(filter.keys())
print(result)