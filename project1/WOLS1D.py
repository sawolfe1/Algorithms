
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
    output = "".join(str(x) for x in d[0])
    return f"F({i}): {output}"


findNLengthFibonacci(100)
'F(475): 831082459908702935293955784701120993704369028200651613859972830080739980541065544674812034151699525'
