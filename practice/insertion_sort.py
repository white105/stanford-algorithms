def insertionSort(unsorted_array):
    for i in range(0, len(unsorted_array)):
        if (i > 0 and unsorted_array[i - 1] > unsorted_array[i]):
            
            unsorted_array[i] = unsorted_array[i - 1]
        else:
            return unsorted_array





unsorted_array = [4, 3, 5, 2, 1, 7, 8, 6]
#unsorted_array = [2, 1]
print('unsorted array :', unsorted_array)
sorted_array = insertionSort(unsorted_array)
print('sorted array :', sorted_array)
