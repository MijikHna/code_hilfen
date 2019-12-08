items = [6,20,8,19,56,23,87,41,49,53]

def find_max(items):

    #TODO Abbruchbedingung = wenn letztes Element in der Liste => returne es
    if(len(items)==1):
        return items[0]

    #TODO im anderen Fall nimm das erste Element und rufe diese Funktion nochmal auf
    op1=items[0]
    print(op1)
    op2=find_max(items[1:])
    print(op2)
    #TODO Vergleich durchführen, wenn nur noch zwei Elemente
    if(op1>op2):
        return op1
    else:
        return op2


print(find_max(items))