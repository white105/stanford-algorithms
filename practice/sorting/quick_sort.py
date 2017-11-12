def quickSort(unsorted_array, left, right):
    if left >= right:
        return
    else:
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


test_list = [54,26,93,17,77,31,44,55,20]
quickSort(test_list, 0, len(test_list) - 1)
print(test_list)
