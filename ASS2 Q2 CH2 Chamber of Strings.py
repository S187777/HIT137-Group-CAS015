"""
Assume s is a string.
Write a program that separates a long string (at least length of 16)
that contains both numbers and letters (upper and lower case)
into two substrings of numbers and letters.
Convert the even numbers in "number substring"
and upper case letters in the "letter string"
into ASCII code decimal values.

Example Scenario:
String = "56aAww1984sktr235270aYmn145ss785fsq31D0"
Separate them: 561984235270145785310 (number string) and aAwwsktraYmnssfsqD (letter string)
Convert the even numbers in the number string to ASCII code decimal values:
6, 8, 4, 2, 2, 0, 4, 8, 0 (even numbers)
becomes 54, 56, 50, 50, 48, 52, 56, 48 (ASCII decimal values)

Convert the upper-case letters in the letter string to ASCII code decimal values:
A, Y, D (upper case letters)
becomes 65, 89, 68 (ASCII decimal values)
"""

def separate_string():
	string = "56aAww1984sktr235270aYmn145ss785fsq31D0"
	if len(string)<16:
		print("The string is not long enough. Try again.")
	digit_string = []
	letter_string = []
	split_string = []
	for x in string:
		split_string.append(x)
		for y in x:
			if y.isalpha():
				if y.isupper():
					letter_string.append(ord(y))
				else:
					letter_string.append(y)
			elif y.isdigit():
				z=int(y)
				if z % 2 == 0:
					digit_string.append(ord(y))
				else:
					digit_string.append(y)
			else:
				pass
	print(letter_string)
	print(digit_string)

separate_string()

"""
OUTPUT:

['a', 65, 'w', 'w', 's', 'k', 't', 'r', 'a', 89, 'm', 'n', 's', 's', 'f', 's', 'q', 68]
['5', 54, '1', '9', 56, 52, 50, '3', '5', 50, '7', 48, '1', 52, '5', '7', 56, '5', '3', '1', 48]
"""