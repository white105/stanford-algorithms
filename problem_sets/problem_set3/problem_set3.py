#problem 1
f = open("QuickSort.txt","r")
integer_array = []

for line in f:
    integer_array.append(int(line.strip()))

def quickSort(unsorted_array, left, right):
    if left >= right:
        return
    else:
        counter += len(unsorted_array) - 1
        partition_val = partition(unsorted_array, left, right)
        quickSort(unsorted_array, left, partition_val - 1)
        quickSort(unsorted_array, partition_val + 1, right)


def partition(unsorted_array, left, right):

    pivotvalue = unsorted_array[left] #first element of array

    i = left + 1
    j = right

    while (j >= i):

        temp = unsorted_array[i]
        unsorted_array[i] = unsorted_array[j]
        unsorted_array[j] = temp

        while i <= j and unsorted_array[i] <= pivotvalue:
            i += 1

        while j >= i and unsorted_array[j] >= pivotvalue:
            j -= 1

    temp = unsorted_array[left]
    unsorted_array[left] = unsorted_array[j]
    unsorted_array[j] = temp


    return j


quickSort(integer_array, 0, len(integer_array) - 1)

#print('integer array sorted', integer_array)


#problem 2



#problem 3
