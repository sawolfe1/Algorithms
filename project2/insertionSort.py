

def insertionSort(a):
    length = len(a)
    i = 1
    while i < length:
        j = i
        while j > 0 and a[j-1] > a[j]:
            # swap
            bigger = a[j-1]
            a[j-1] = a[j]
            a[j] = bigger
            j = j-1
        i += 1
    return a
