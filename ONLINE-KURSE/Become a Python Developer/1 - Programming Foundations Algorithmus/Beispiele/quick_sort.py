list1=[20, 8, 19, 56, 23, 87, 41, 49, 6, 53]

def quickSort(dataset, first, last):
    if first < last:
        pivotIdx=partition(dataset, first, last)

        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(datavalue, first, last):
    pivotvalue=datavalue[first]

    lower = first+1
    upper = last

    done = False
    while not done:
        # TODO weiterer Kommentar
        while lower <=upper and datavalue[lower] <= pivotvalue:
            lower +=1
        while datavalue[upper] >= pivotvalue and upper >= lower:
            upper -=1
        if upper < lower:  
            done = True
        else:
            temp=datavalue[lower]
            datavalue[lower]=datavalue[upper]
            datavalue[upper]=temp

    temp=datavalue[first]
    datavalue[first]=datavalue[upper]
    datavalue[upper]=temp


    return upper


print("Unsortier: ", list1)
quickSort(list1, 0, len(list1)-1)
print("Sortiert: ", list1)
print("0: ", list1[0])