# https://www.codewars.com/kata/57591ef494aba64d14000526
#  5 Kyu
j = [0, 0]
a = [1, 1]


def ja(n):
	for i in range(len(j), n):
		j.append(i - a[j[i - 1]])
		a.append(i - j[a[i - 1]])


def john(n):
	ja(n)
	return j[:n]


def ann(n):
	ja(n)
	return a[:n]


def sum_john(n):
	ja(n)
	return sum(j[:n])


def sum_ann(n):
	ja(n)
	return sum(a[:n])