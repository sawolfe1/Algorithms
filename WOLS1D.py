

# non-recursive
def fib(num):
    d = [[0], [1]]
    for i in range(1, num):
        sum = sumTwoArrays(d[i - 1], d[i])
        d.append(sum)
    return d[num]


def sumTwoArrays(arr1, arr2):
    # fill arr1 with 0s on the left if its smaller than arr2
    if len(arr1) < len(arr2):
        arr1 = [0]*(len(arr2)-len(arr1)) + arr1

    carry = 0
    li = []
    for i in range(len(arr2)-1, -1, -1):
        placeholder = (arr1[i] + arr2[i] + carry) % 10
        carry = (arr1[i] + arr2[i] + carry)//10
        li = [int(placeholder)] + li
    if carry > 0:
        li = [int(carry)] + li
    return li


def findNLengthFibonacci(num):
    result = 0
    d = [[0], [1]]
    i = 0
    while result < num:
        i += 1
        sum = sumTwoArrays(d[0], d[1])
        d = [d[1], sum]
        result = len(sum)

    print(i)
    return d[0]
