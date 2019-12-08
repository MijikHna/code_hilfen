list1=[6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset)>1:
        mid=len(dataset) //2
        lefarr=dataset[:mid]
        rightarr=dataset[mid:]

        mergesort(lefarr)
        mergesort(rightarr)
        
        i=0 #left
        j=0 #right
        k=0 #whole

        while i<len(lefarr) and j<len(rightarr):
            if lefarr[i]<rightarr[j]:
                dataset[k]=lefarr[i]
                i+=1
            else:
                dataset[k]=rightarr[j]
                j +=1
            k += 1

        while i < len(lefarr):
            dataset[k]=lefarr[i]
            i+=1
        
        while j < len(rightarr):
            dataset[k]=rightarr[j]
            j+=1

print("Unsortier: ", list1)
mergesort(list1)
print("Sortiert: ", list1)