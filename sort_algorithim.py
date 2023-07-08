
array = [5, 2, 8, 12, 1,0,62,-33,11]
array2 =['ball', 'dog','car', 'apple', 'bike', 'bicycle','ape']

# Selection Sort
def selectionSort(myArray):
    n = len(myArray)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if myArray[j] < myArray[position]:
                position = j
        # swapping with the least number
        temp = myArray[i]
        myArray[i] = myArray[position]
        myArray[position] = temp
    return myArray

print((selectionSort(array)))
print((selectionSort(array2)))


# Insertion Sort

def insertionSort(myArray):
    arrayLength = len(myArray)
    for i in range(1, arrayLength):
        # Assumes the first index is sorted
        temp = myArray[i]
        position = i
        while position > 0 and myArray[position - 1] > temp:
            myArray[position] = myArray[position - 1]
            position = position - 1
        myArray[position] = temp
    return myArray

print(insertionSort(array))
print(insertionSort(array2))
