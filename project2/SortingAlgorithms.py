"""
Sorting algorithms for Project 2 for CS3130 UMSL
Scott Wolfe
"""
# a)


def selectionSort(a):

    length = len(a)
    for i in range(length-1):
        mini = i
        for j in range(i+1, length):
            if (a[j] < a[mini]):
                mini = j

        if (mini != i):
            # swap
            bigger = a[i]
            a[i] = a[mini]
            a[mini] = bigger

    return(a)

# b)


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

# c)

# Bubble Sort without swaps counting


def bubbleSort(A):
    length = len(A)
    for i in range(length):
        for j in range(length-1, i, -1):
            if A[j] < A[j-1]:
                # swap
                A[j], A[j-1] = A[j-1], A[j]
    return(A)


# Bubble Sort with swaps counting


def bubbleSortWithSwapsCounting(A):
    length = len(A)
    i = 0
    isSorted = False
    while i < length and not isSorted:
        isSorted = True
        for j in range(length-1, i, -1):
            if A[j] < A[j-1]:
                # swap
                A[j], A[j-1] = A[j-1], A[j]
                # Signal that a swap has taken place
                isSorted = False
        i += 1
    return(A)


# d)


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q, r)
    return(A)


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            # swap
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return(i+1)

# e)


"""
Source: https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
"""


def merge(a, b):
    # Function to merge two arrays
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def mergeSort(A):
    # Function to sort an array using merge sort algorithm
    if len(A) < 2:
        return A
    else:
        middle = int(len(A)/2)
        a = mergeSort(A[:middle])
        b = mergeSort(A[middle:])
        return merge(a, b)
