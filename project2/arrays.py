from random import randint

sortedArray100 = [i for i in range(100)]
sortedArray1000 = [i for i in range(1000)]
sortedArray10000 = [i for i in range(10000)]

randomArray100 = [randint(0, 100) for i in range(100)]
randomArray1000 = [randint(0, 1000) for i in range(1000)]
randomArray10000 = [randint(0, 10000) for i in range(10000)]

semiSortedArray100 = [i if i % 10 != 0 else i+10 for i in range(100)]
semiSortedArray1000 = [i if i % 10 != 0 else i+10 for i in range(1000)]
semiSortedArray10000 = [i if i % 10 != 0 else i+10 for i in range(10000)]
