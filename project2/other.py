"""
Source: https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
"""


def merge(a, b):
    """ Function to merge two arrays """
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
    """ Function to sort an array using merge sort algorithm """
    if len(A) < 2:
        return A
    else:
        middle = int(len(A)/2)
        a = mergeSort(A[:middle])
        b = mergeSort(A[middle:])
        return merge(a, b)


A = [9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980]
mergeSort(A)
