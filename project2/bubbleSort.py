
# Bubble Sort without swaps counting


def bubbleSort(A):
    length = len(A)
    for i in range(length):
        for j in range(length-1, i, -1):
            if A[j] < A[j-1]:
                # swap
                A[j], A[j-1] = A[j-1], A[j]
    return(A)
