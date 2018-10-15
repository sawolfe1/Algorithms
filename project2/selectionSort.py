

def selectionSort(a):

    length = len(a)
    for i in range(length-1):
        mini = i
        for j in range(i+1, length):
            if (a[j] < a[mini]):
                mini = j

        if (mini != i):
            bigger = a[i]
            a[i] = a[mini]
            a[mini] = bigger

    return(a)


selectionSort([9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980])
