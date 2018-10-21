

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
