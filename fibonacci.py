import timeit
# non-recursive
def fib(num):
	f = [0, 1]
	for i in range(1, num):
		sum = f[i - 1] + f[i]
		f.append(sum)
	return f[num]

# recursive
def rFib(num):
	sum = 0
	if num < 2:
		return num
	else:
		sum = rFib(num - 2) + rFib(num - 1)
	return sum
	

code = """
def fib():
	num=10
	f = [0, 1]
	for i in range(1, num):
		sum = f[i - 1] + f[i]
		f.append(sum)
	return f[num]
	"""

rec = """
def rFib(num):
	sum = 0
	if num < 2:
		return num
	else:
		sum = rFib(num - 2) + rFib(num - 1)
	return sum
	"""
	
t = timeit.Timer(rec)
