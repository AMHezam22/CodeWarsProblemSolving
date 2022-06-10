#  https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084/train/python
#  4 Kuy

# Problem Instruction:
#   The task is simply stated. Given an integer n (3 < n < 109),
#   find the length of the smallest list of perfect squares which add up to n.
#   Come up with the best algorithm you can; you'll need it!

# Problem Solution:
#   You can write an algorithm that solves the problem,
#   but it won't be completely accurate only if you followed a mathematical formula.
#   Which is Lagrange’s Four Square Theorem. https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
#   however, I wrote down my algorithm and then the solution by the Theorem.


# in my algorithm solution I used -Before I raed about it ^_____^- :
#  - Overlapping Sub-problem- Dynamic Programming:
# 		 Which  solves a given complex problem by breaking it into sub-problems. "recursion function"
#  - Memoization (Top Down):
# 		 Which looks into a lookup table before computing solutions.

d = {0: 0, 4: 2, 3: 3, 2: 2, 1: 1}


def sum_of_squares_AMHezam_algorithm(n):
	# Memoization Using d dictionary
	if n in d:
		return d[n]
	# In case n itself is a perfect square
	if (n ** .5).is_integer():
		d[n] = 1
		return d[n]
	# In case n = a**2 + a**2
	if ((n // 2) ** .5).is_integer():
		d[n] = 2 + n % 2
		return d[n]
	# In case n = a**2 + a**2 + a**2
	if ((n // 3) ** .5).is_integer():
		d[n] = 3 + n % 3
		return d[n]
	# In case: n = a**2 + b**2 + c**2 Make a self-call
	# x is the square root of n, Why int ?
	# to know the max square smaller than n, x**2 >=n
	x = int(n ** .5)
	ans = n
	for i in range(4):
		r = n - ((x - i) ** 2)
		if r in d:
			return d[r] + 1
		t = sum_of_squares_AMHezam_algorithm(r) + 1
		if t < 4:
			return t
		ans = min(t, ans)
	d[n] = ans
	return ans


# Theorem algorithm solution. for more details:
#  https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/
def sum_of_squares(n: int):
	if (n ** .5).is_integer():
		return 1
	
	for x in range(1, int(n ** .5)):
		if ((n - (x ** 2))**.5).is_integer():
			return 2
	while n % 4 == 0:
		n //= 4
	if n % 8 == 7:
		return 4
	
	return 3

print(sum_of_squares(12))