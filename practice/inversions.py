
#divide and conquer algorithm that emulates merge sort
def countInversions(unsorted_array):
    if (len(unsorted_array) == 0 or len(unsorted_array) == 1):
        return 0
    else:

        midpoint = len(unsorted_array) // 2
        left_half = unsorted_array[:midpoint]
        right_half = unsorted_array[midpoint:]

        countInversions(left_half)
        countInversions(right_half)

        i = 0
        j = 0
        k = 0
        inversion_count = 0

        while (i < len(left_half) and j < len(right_half)):
            if(left_half[i] < right_half[j]):
                unsorted_array[k] = left_half[i]
                i += 1
            else:
                unsorted_array[k] = right_half[j]
                j += 1
                #only increment inversion count when right_half[j] < left_half[i]
                inversion_count += len(left_half) - i
            k += 1

        while (i < len(left_half)):
            unsorted_array[k] = left_half[i]
            i += 1
            k += 1

        while (j < len(right_half)):
            unsorted_array[k] = right_half[j]
            j += 1
            k += 1

        return inversion_count


unsorted_array = [1, 3, 5, 2, 4, 6]
inversion_count = countInversions(unsorted_array)
print(inversion_count)
