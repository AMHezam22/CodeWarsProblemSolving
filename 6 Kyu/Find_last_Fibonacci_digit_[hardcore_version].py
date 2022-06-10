# https://www.codewars.com/kata/56b7771481290cc283000f28
# 6 Kyu

# In this kata have to find the last digit in Fibonacci sequences.
# We noticed thad the last digit of Fibonacci Sequences repeated every 60 numbers. So, the first step to solve this
# kata is by make a list that hold the repeated digit and then return modulus 60.

# the list that will hold the digits
f = [0] * 60


# Function will made this digits
def fibo_digits(digit_list):
	# 0th and 1th in fibonacci sequences are 1 and 0.
	digit_list[0] = 0
	digit_list[1] = 1

	for i in range(2, len(digit_list)):
		digit_list[i] = (digit_list[i - 1] + digit_list[i - 2]) % 10
	return digit_list


# Solution starts:

# f will be :
fibo_list = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7,
	8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6,
	9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]


# Now we can find the last digit by finding nth modulus 60
def last_fib_digit(n):
	return fibo_list[n % 60]
