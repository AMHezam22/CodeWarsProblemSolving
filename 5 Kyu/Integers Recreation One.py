# https://www.codewars.com/kata/55aa075506463dac6600010d/solutions/python
#  Kyu 5

def get_divisors(n):
	for i in range(1, int(n / 2) + 1):
		if n % i == 0:
			yield i
	yield n


def list_squared(m, n):
	ans = []
	for x in range(m,n):
		total = sum(x**2 for x in list(get_divisors(x)))
		if (total**.5).is_integer():
			ans.append([x,total])
	return ans



