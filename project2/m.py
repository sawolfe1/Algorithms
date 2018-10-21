import math


def mergeSort(A):

    length = len(A)

    if length < 2:
        return(A)
    else:
        q = int(length/2)
        a = mergeSort(A[:q])
        b = mergeSort(A[q:])
        return merge(a, b)


def merge(a, b):
    c = []

    i, j = 0, 0
    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            c.append(a[0])
            a.remove(a[0])
            i += 1
        else:
            c.append(b[0])
            b.remove(b[0])
            j += 1


A = [9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980]
mergeSort(A)
