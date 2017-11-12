#runs in O(2n) or O(n)
def secondLargest(unsorted_array):
    if(len(unsorted_array) == 1):
        return 0
    else:
        largest = unsorted_array[0]
        for i in range(0, len(unsorted_array)):
            if (unsorted_array[i] > largest):
                largest = unsorted_array[i]

        secondLargest = unsorted_array[0]
        for j in range(0, len(unsorted_array)):
            if (unsorted_array[j] > secondLargest and unsorted_array[j] != largest):
                secondLargest = unsorted_array[j]

        return secondLargest

unsorted_array = [1, 5, 3, 19, 2, 13, 12, 8]
second_largest = secondLargest(unsorted_array)
print(second_largest)
