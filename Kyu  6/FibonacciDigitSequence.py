# https://www.codewars.com/kata/5bc555bb62a4cec849000047/train/python
# 6 Kyu - level

# Problem Instructions:
# You are given three non negative integers a, b and n, and making an infinite sequence just like fibonacci sequence,
# use the following rules:
#
# step 1: use ab as the initial sequence.
# step 2: calculate the sum of the last two digits of the sequence, and append it to the end of sequence.
# repeat step 2 until you have enough digits

# Your task is to complete the function which returns the nth digit (0-based) of the sequence.

# Solution: the Problem is easy to solve in easy cases. you can just use loops till find the n-th digit. but in worst
# cases, loop isn't enough special when ind is bigger than 10**9. however, if you try to write a code to see all
# possible sequences you will notice that there are two patterns and one special.


def find(a, b, ind):
	if a == 0 and b == 0:  # special case one
		return 0
	if ind == 0:  # special case two from the instruction
		return a
	elif ind == 1:  # special case three from the instruction
		return b
	ans = [a, b]
	r = ind
	while ind > 1:
		a, b = ans[-2], ans[-1]
		temp = a + b
		if a == 1 and b == 1:  # pattern one
			return (1, 1, 2, 3, 5, 8, 1, 3, 4, 7)[ind % 10]
		if a == 4 and b == 5:  # patter two
			return (4, 5, 9, 1)[ind % 4]
		if temp <= 9:
			ind -= 1
			ans.append(temp)
			continue
		ind -= 2
		ans.extend(map(int, str(temp)))
	if ind == 0:
		return ans[-2]
	return ans[-1]
