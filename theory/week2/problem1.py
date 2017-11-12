def secondLargest(unsorted_array):
    if (len(unsorted_array) == 1):
        return 0
    else:
        midpoint = len(unsorted_array) // 2
        left_half = unsorted_array[:midpoint]
        right_half = unsorted_array[midpoint:]

        secondLargest(left_half)
        secondLargest(right_half)

        i = 0
        j = 0
        k = 0

        while(i < len(left_half) and j < len(right_half)):
            if(left_half[i] < right_half[j]):
                unsorted_array[k] = left_half[i]
                i += 1
            else:
                unsorted_array[k] = right_half[j]
                j += 1

            k += 1

        while(i < len(left_half)):
            unsorted_array[k] = left_half[i]
            i += 1
            k += 1

        while(j < len(right_half)):
            unsorted_array[k] = right_half[j]
            j += 1
            k += 1

        return unsorted_array[-2]





unsorted_array = [1, 5, 3, 19, 2, 13, 12, 8]
second_largest = secondLargest(unsorted_array)
print(second_largest)
