# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python



def find_nb(m):
	total = 1
	x = 2
	while total < m:
		total += x ** 3
		x += 1
	if total == m:
		return x - 1
	return -1
