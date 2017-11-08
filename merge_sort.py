def mergeSort(unsorted_array):

    if (len(unsorted_array) > 1):
        midpoint = len(unsorted_array) // 2
        left_half = unsorted_array[:midpoint]
        right_half = unsorted_array[midpoint:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0

        #both left and right halves still need to be sorted
        while ((i < len(left_half)) and (j < len(right_half))):
            if (left_half[i] < right_half[j]):
                unsorted_array[k] = left_half[i]
                i += 1
            else:
                unsorted_array[k] = right_half[j]
                j += 1

            k += 1

        #all of the elements in the right half have been sorted
        while(i < len(left_half)):
            unsorted_array[k] = left_half[i]
            i += 1
            k += 1

        #all of the elements in the left half have been sorted
        while(j < len(right_half)):
            unsorted_array[k] = right_half[j]
            j += 1
            k += 1

        return unsorted_array

def merge_sort(unsorted_array):

    if(len(unsorted_array) == 0 or len(unsorted_array) == 1):
        return unsorted_array
    else:
        midpoint = len(unsorted_array) // 2
        left_half = unsorted_array[:midpoint]
        right_half = unsorted_array[midpoint:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0

        for k in range(0, len(unsorted_array)):
            if (i < len(left_half) and j < len(right_half)):
                if (left_half[i] < right_half[j]):
                    unsorted_array[k] = left_half[i]
                    i += 1
                else:
                    unsorted_array[k] = right_half[j]
                    j += 1
            else:
                if (i < len(left_half)):
                    unsorted_array[k] = left_half[i]
                    i += 1

                if (j < len(right_half)):
                    unsorted_array[k] = right_half[j]
                    j += 1

        return unsorted_array


unsorted_array = [4, 3, 5, 2, 1, 7, 8, 6]
#unsorted_array = [2, 1]
print('unsorted array :', unsorted_array)
sorted_array = merge_sort(unsorted_array)
print('sorted array :', sorted_array)
