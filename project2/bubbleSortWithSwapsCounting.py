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
