f = open("IntegerArray.txt","r")
integer_array = []

for line in f:
    integer_array.append(int(line.strip()))

#divide and conquer algorithm that emulates merge sort
def countInversions(unsorted_array):
    if (len(unsorted_array) == 0 or len(unsorted_array) == 1):
        return 0
    else:

        midpoint = len(unsorted_array) // 2
        left_half = unsorted_array[:midpoint]
        right_half = unsorted_array[midpoint:]

        x = countInversions(left_half)
        y = countInversions(right_half)

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

        return inversion_count + x + y

test_case_1 = [1, 3, 5, 2, 4, 6]
test_case_2 = [1, 5, 3, 2, 4]
test_count_1 = countInversions(test_case_1)
test_count_2 = countInversions(test_case_2)

final_answer = countInversions(integer_array)
print(final_answer)
