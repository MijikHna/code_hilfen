items=["apple", "pear", "orange", "banana", "apple", "orange", "pear", "banana", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

#TODO hach-Tabelle erstellen um Array-Elemente zu halten und sie zu zählen:
counter=dict()

#TODO über Elemente iterriereen und counter inkrementieren
for item in items: 
    if(item in counter.keys()):
        counter[item]+=1
    else:
        counter[item]=1

print(counter)