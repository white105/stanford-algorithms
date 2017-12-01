#problem 1
f = open("QuickSort.txt","r")
integer_array = []

for line in f:
    integer_array.append(int(line.strip()))

#problem 1 - count comparisons with pivot as first element

first_element_counter = 0

def quickSortFirstElement(arr, l, r):
    global first_element_counter
    if (l >= r):
        return

    first_element_counter += r - l - 1

    pivot = partitionFirstElement(arr, l, r)
    quickSortFirstElement(arr, l, pivot)
    quickSortFirstElement(arr, pivot + 1, r)

def partitionFirstElement(arr, l, r):
    pivot = arr[l]
    i = l + 1

    for j in range(l + 1, r):
        if (arr[j] < pivot):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    #final swap
    temp = arr[l]
    arr[l] = arr[i - 1]
    arr[i - 1] = temp
    return i - 1


#problem 2 - count comparisons with pivot as last element

last_element_counter = 0

def quickSortLastElement(arr, l, r):
    global last_element_counter
    if (l >= r):
        return

    last_element_counter += r - l - 1

    pivot = partitionLastElement(arr, l, r)
    quickSortLastElement(arr, l, pivot)
    quickSortLastElement(arr, pivot + 1, r)

def partitionLastElement(arr, l, r):

    #pivot as last element
    pivot = arr[r - 1]

    arr[r - 1] = arr[l]
    arr[l] = pivot

    i = l + 1

    for j in range(l + 1, r):
        if (arr[j] < pivot):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    #final swap
    temp = arr[l]
    arr[l] = arr[i - 1]
    arr[i - 1] = temp
    return i - 1

#problem 2 - count comparisons with pivot as last element

median_element_counter = 0

def quickSortMedianElement(arr, l, r):
    global median_element_counter
    if (l >= r):
        return

    median_element_counter += r - l - 1

    pivot = partition_median(arr, l, r)
    quickSortMedianElement(arr, l, pivot)
    quickSortMedianElement(arr, pivot + 1, r)


###Help from https://github.com/meclark256/Coursera/blob/master/QuickSort.py for median element

#A method to calculate the median of three numbers using two comparisons
def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c

#A method to partition around the median
def partition_median(array, leftend, rightend):
    left = array[leftend]
    right = array[rightend-1]
    length = rightend - leftend
    if length % 2 == 0:
        middle = array[leftend + length//2 - 1]
    else:
        middle = array[leftend + length//2]



    pivot = median(left, right, middle)

    pivotindex = array.index(pivot) #only works if all values in array unique

    array[pivotindex] = array[leftend]
    array[leftend] = pivot

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

quickSortFirstElement(integer_array[:10], 0, 10)
print('Number of comparisons when pivot is chosen as first element:', first_element_counter)

quickSortLastElement(integer_array[:10], 0, 10)
print('Number of comparisons when pivot is chosen as last element:', last_element_counter)

quickSortMedianElement(integer_array[:10], 0, 10)
print('Number of comparisons when pivot is chosen as median element:', median_element_counter)
