#problem 1
f = open("QuickSort.txt","r")
integer_array = []

for line in f:
    integer_array.append(int(line.strip()))

###Help from https://github.com/meclark256/Coursera/blob/master/QuickSort.py

#problem 1 - count comparisons with pivot as first element

first_element_counter = 0

def quickSortFirstElement(arr, left, right):
    global first_element_counter
    if (left >= right):
        return

    pivot = partitionFirstElement(arr, left, right)
    first_element_counter += right - left - 1
    quickSortFirstElement(arr, left, pivot)
    quickSortFirstElement(arr, pivot + 1, right)

def partitionFirstElement(arr, left, right):
    pivot = arr[left]
    i = left + 1

    for j in range(left + 1, right):
        if (arr[j] < pivot):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    left = arr[left]
    arr[left] = arr[i - 1]
    arr[i - 1] = left
    return i - 1

#A method for partition around the first element of the array
def partition_first(array, leftend, rightend):
    pivot = array[leftend]
    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1

ans = quickSortFirstElement(integer_array[:10], 0, len(integer_array[:10]))
print(ans)
