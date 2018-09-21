import timeit
from matplotlib import pyplot as plt

functions = """
def rFib(num):  # recursive
    
    if num < 2:
        return num
    else:
        sum = 0
        sum = rFib(num - 2) + rFib(num - 1)
    return sum
    
def fib(num):  # non-recursive

    if num < 2:
        return num
    else:
        f = [0, 1]
        for i in range(1, num):
            sum = f[i - 1] + f[i]
            f.append(sum)
    return f[num]
"""


def compare(num):
    iterative = timeit.timeit(stmt=f"fib({num})", setup=functions, number=100)

    recursive = timeit.timeit(stmt=f"rFib({num})", setup=functions, number=100)

    percentDiff = (abs(recursive-iterative)/((recursive+iterative)/2))*100

    if iterative < recursive:
        return f"Iterative is faster with {percentDiff}% difference"
    if recursive < iterative:
        return f"Recursive is faster with {percentDiff}% difference"
    else:
        return "They are equivalent!"


In[11]: compare(1)
Out[11]: 'They are equivalent!'

In[12]: compare(5)
Out[12]: 'Iterative is faster with 60.58479532263219% difference'

In[13]: compare(10)
Out[13]: 'Iterative is faster with 171.7528373266598% difference'

In[14]: compare(15)
Out[14]: 'Iterative is faster with 196.1669209560672% difference'

In[15]: compare(20)
Out[15]: 'Iterative is faster with 199.55081711651985% difference'

In[16]: compare(25)
Out[16]: 'Iterative is faster with 199.94979780649024% difference'
