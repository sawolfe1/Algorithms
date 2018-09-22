# recursive
def rFib(num):
	sum = 0
	if num < 2:
		return num
	else:
		sum = rFib(num - 2) + rFib(num - 1)
	return sum
