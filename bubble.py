def bubblesort(array):
    n=len(array)-1
    while n>=1:
        i=0
        while i<n:
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
            i=i+1
        n=n-1
array1=[8,7,5,6,4,4,3,2]
bubblesort(array1)
print(array1)
