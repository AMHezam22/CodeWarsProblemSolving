# https://www.codewars.com/kata/54d81488b981293527000c8f
# 5 Kyu


# Task description:
# Given a list of integers and a single sum value, return the first two values (parse from the left
# please) in order of appearance that add up to form the sum.

def sum_pairs(numbers, s):
	sets = set()
	for x in range(len(numbers)):
		current_int = numbers[x]
		if s - current_int in sets:
			return [s - current_int, current_int]
		else:
			sets.add(current_int)
