# https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python
#  4 Kuy

# Problem Instruction:
#   Construct a function that, when given a string containing an expression in infix notation (3+2*5),
#   will return an identical expression in postfix notation (325*+). The operators used will be +, -, *, /, and ^ with
#   left-associativity of all operators but ^. The precedence of the operators (most important to least) are : 1)
#   parentheses, 2) exponentiation, 3) times/divide, 4) plus/minus. The operands will be single-digit integers between
#   0 and 9, inclusive. Parentheses may be included in the input, and are guaranteed to be in correct pairs.

# Problem Solution:
#   Using stack Database, for more information https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/

def check(d, stac):
	operator_order = {"^": 5, "*": 4, "/": 4, '+': 3, '-': 3}
	try:
		return operator_order[d] <= operator_order[stac]
	except KeyError:
		return False


def to_postfix(infix):
	stack = []
	postfix = ""
	for digit in infix:
		if digit.isalnum():
			postfix += digit
		elif digit == '(':
			stack.append(digit)
		elif digit == ')':
			while stack and stack[-1] != '(':
				postfix += stack.pop()
			stack.pop()
		else:
			while stack and check(digit, stack[-1]):
				if digit == '^' == stack[-1]:
					break
				postfix += stack.pop()
			stack.append(digit)
	postfix += "".join(stack[::-1])
	return postfix
