item1=[20, 8, 19, 56, 23, 87, 41, 49, 6, 53]
item2=[6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def is_sorted(dataset):
    
    #for i in range(0, len(dataset)-1):
    #    if (dataset[i] > dataset[i+1]):
    #        return False

    #return True

    #Python-Ding:
    return all(dataset[i] <= dataset[i+1] for i in range(len(dataset)-1))

print("Unortierte Liste: ", is_sorted(item1))
print ("Sortierte Liste: ", is_sorted(item2))