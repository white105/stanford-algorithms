#problem 1
f = open("QuickSort.txt","r")
integer_array = []

for line in f:
    integer_array.append(int(line.strip()))

def quickSort(a, n):
    if (n == 1):
        return

    pivot = a[0]
    index = partition(a, pivot)
    quickSort(a, 0, index - 1)
    quickSort(a, index, len(a) - 1)


#single scan of array
def partition(a, pivot):

    i = 1
    seenGreaterThan = False

    for(j in range(1, right))
        if(a[j] < pivot && seenGreaterThan):
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            i += 1
        if(a[j] > pivot):
            seenGreaterThan = True

    #final swap
    temp = a[i - 1]
    a[i - 1] = pivot
    a[left] = temp


test_case_1 = integer_array[:10]
test_case_2 = integer_array[:100]
quickSort(test_case_1, 0, len(test_case_1) - 1)



#problem 2



#problem 3
