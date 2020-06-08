### 1 - Overview
#### 1 - Was ist Algorithmus
#### 2 - Verbreitete Algoritmen
+ Suchalgorithmen
+ Sortieralgorithmen
+ Computation Alg.
+ Collection Alg.
#### 3 -Algorithmen-Eigenschaften → Komplexität usw.
### 2 -Datenstrukturen:
#### 2 - Arrays
#### 3 - Linked Lists
+ Stack = Last In – First out → array
    + array1.append(wert)
    + deletet = array1.pop()
+ Quees = First In – First out → deque
    + from collections import deque
    + queue1=deque()
    + queue1.append(wert)
    + deletet = queue1.popleft()
#### 5 - Hash-Table = Dictionaries 
    + = Mappt Key zu Value
    + braucht eigentlich Hash-Funktion ← können Kolissionen entstehen.
    + hashtable1=dict{„key1“ : 1, „key2“ : „zwei})
    + hashtable2={}
    + hashtable2[„key1“]=1
    + hashtable2[„key2“]=“zwei“
    + hashtable2[„key2“]=2
    + for key, value in hashtable1.items():
        + do something z.B print(„Key: “, key, „ Value: „, value) 
### 4 - Sorting Data:
#### 1 - Overview of sorting:
1. es gibt eigentlich schon in Programmierensprachen imlementierte Sortier-funktionen
#### 2 - The bubble sort:
1. Performence: O(n²)
2. es gibt bessere Algorithmen
#### 3 - The merge sort:
1. Divide-and-conquer algorithm
2. = teilt Daten in Teile und setzt sie wieder zusammen
3. benutzt Rekursion
4. Performance O(n log(n))
5. → Schlüssel wie man zusammensetzt
    1. z.B zwei Teile:
        1. schauen auf ersten Elemente von beiden Teilen.
        2. Den kleineren der Beiden einsortieren + Index erhöhen.
        3. Dann wieder bei 1)
#### 4 - Implement the merge sort:
#### 5 - The quicksort
1.  teilt Daten in Teile und setzt sie wieder zusammen
2. benutzt Rekursion
3. ist etwas besser als Quicksort
4. arbeitet im Originalen Array
5. braucht Pivot Point:
    1. Pivot auswählen z.B index[0]
    2. Array Durchgehen
        1. wenn Pivot größer, dann nichts machen
        2. wenn Pivot kleiner => Pivot 
            1. ans Ende des Liste gehen, wenn der Pivot größer ist, dann letztes Element mit i tauschen, sonst die Liste nach unten gehen
            2. Wenn vorVorneIndex und vonHintenIndex sich überschneiden, => hier wird die Liste geteilt
            3. vonHintenIndex mit Pivot tauschen
            4. ← hier wird die Liste geteilt = linkt ist alles kleiner als Pivot, rechts ist alles größer als Pivot
            5. dann auf rechten und linken Teil quickSort anwenden
6. Implement the quicksort:
### 5 - Searching Data:
#### 1 - Unordered list search:
1. = key in der Liste suchen = Liste durchgehen
#### 2 - Ordered list search:
1. = Binary search
    1. (first+last)/2
    2. Wenn key großer => rechts weiter suchen
        1. (mid+last)/2
    3. Wenn key kleiner => links weiter suchen
        1. (first+mid)/2
    4. Wenn last/mid/first sind gleich => key nicht in der Liste
#### 3 - Determine if a list is sorted:
1. siehe is_sorted.py
### 6 - Other Algorithms:
#### 1 - Unique filtering with hash table:
1. = im Array doppelte Elemente rausnehmen
#### 2 - Value counting with hash table:
1. siehe valuecounter_start-6-2
#### 3 - Find max value recursively: