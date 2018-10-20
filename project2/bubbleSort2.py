# Bubble Sort with swaps counting

def bubbleSort2(a):
    length = len(a)
    i=0
    swapcount = 1
    while i < length and swapcount > 0:
    	swaps=0
    	for j in range(length-1, i, -1):
    		if a[j] < a[j-1]:
    			bigger = a[j-1]
    			a[j-1] = a[j]
    			a[j] = bigger
    			swaps += 1
    	i+=1
    	swapcount = swaps
    print(i)
    return(a)

bubbleSort2([9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980])
