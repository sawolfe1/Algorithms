import math


def mergeSort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L, R = [], []
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+j])

    L.append(math.inf)
    R.append(math.inf)
    x, y = 0, 0
    for k in range(p, r):
        if L[x] <= R[y]:
            A[k] = L[x]
            x += 1
        else:
            A[k] = R[y]
            y += 1


A = [9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980]
mergeSort(A, 0, len(A))
