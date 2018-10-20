

def insertionSort(a):
    length = len(a)
    i = 1
    while i < length:
        j = i
        while j > 0 and a[j-1] > a[j]:
            bigger = a[j-1]
            a[j-1] = a[j]
            a[j] = bigger
            j = j-1
        i += 1
    return a


insertionSort([9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980])
