
# Bubble Sort without swaps counting


def bubbleSort(a):
    length = len(a)
    for i in range(length):
        for j in range(length-1, i, -1):
            if a[j] < a[j-1]:
                bigger = a[j-1]
                a[j-1] = a[j]
                a[j] = bigger
    return(a)


bubbleSort([9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980])
