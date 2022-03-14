# https://www.codewars.com/kata/55688b4e725f41d1e9000065/solutions/python
# Done, using Recursion Function

def even_fib(m, fib=None):
	if fib is None:
		fib = [0, 1]
	if fib[-1] + fib[-2] >= m:
		return 0
	fib.append(fib[-1] + fib[-2])
	return (fib[-1] if fib[-1] % 2 == 0 else 0) + even_fib(m, fib)
