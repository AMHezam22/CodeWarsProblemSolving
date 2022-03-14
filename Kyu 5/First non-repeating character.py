# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
#  5 level - Kyu


# In this kata we make a function -first_non_repeating_letter- takes a String and return the first NON-Repeating letter
# with consider letter case. More info visit the link.


# to solve the kata first we make a variable hold the string but in lower or upper case to compare it with for loop
# and make the loop with the origin string to save the letter case and then count the letter.
# if the letter didn't repeated, the function will return the letter with it's case because we pick it from the origin
# string. else return empty string for not find NON-Repeating letter.

def first_non_repeating_letter(string: str):
	s = string.lower()
	for letter in string:
		count = s.count(letter.lower())
		if count == 1:
			return letter
	return ""
