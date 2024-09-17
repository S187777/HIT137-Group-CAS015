"""
Question 2
Here's an adventurous story intertwined with Python programming questions that involve 
nested 'for' loops, conditional statements, string manipulations, and more.

The Quest for the Hidden Treasure:
Deep within the mystical lands of Pythoria lay the fabled Temple of Codes, 
rumored to house a treasure of knowledge guarded by enigmatic puzzles. 
The path is challenging, and only those who can do the coding will unravel the final word, 
leading to the treasure.

Chapter 1: The Gatekeeper
The above algorithm generates a number (n). 
You should use this number to change the pixels (r,g,b) in the provided image (Chapter1.png) 
by adding the original pixel values (r,g,b) with the generated number (Example: (r+n, g+n, b+n)).
Generate a new image with the converted pixels (upload it as 'chapter1out.png').
Finally, add all the red (r) pixel values in the new_image and provide the sum as output to move to the next chapter.
"""


# Part 1: The above Algorithm (unchanged).

import time

current_time = int(time.time())
generated_number = (current_time & 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

#print(generated_number)        # Print after the next parts using formated string output instead, looks nicer.


# Part 2: Use this number to change the pixels...

from PIL import Image

img = Image.open("chapter1.jpg")        # Open the image.

img_width, img_height = img.size        # Determine the size of the image.

total_red_pixels = 0        # Create a variable to tally the red pixel count.

pixel_map = img.load()      # This loads a variable that allows access to the pixels in the image.

# Let the Generated Number from above = n.
n = generated_number

# We use a for loop to iterate through each pixel in the x,y coordinates (range as determined by the image size).
for x in range(0, img_width):
    for y in range(0, img_height):
        r, g, b = img.getpixel((x, y))
        # The maximum value for each Red, Green, and Blue value is 255.
        if r + n > 255:
            r -= n
        elif g + n > 255:
            g -= n
        elif b + n > 255:
            b-=n
        # I'm SURE there is a more pythonic way to do the above, without redefining a new var using max and mins.
# Part 3.1, Generate a new image...
        pixel_map[x, y] = (r + n, g + n, b + n)     # Using the pixel access, re-assign values to r, g, b.
# Part 4.1, add red pixel values...  
        total_red_pixels += (r+n)     # Count the red pixels.

# Part 3.2, and upload.
img.save('chapter1out.png')     # Self explanatory...

print(f"The Generated number from the above code is:\n {generated_number}")

# Part 4.1, and display sum as output.
print(f"The total sum of red pixel values in the new image is:\n {total_red_pixels}")

img.show()      # Shows the new output image.


"""
Chapter 2: The Chamber of Strings
Pt1.
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

def separate_string(string):        # Define a function to accomodate various string input.
	if len(string) < 16:		# Determine length is long enough.
		print("The string is not long enough. Try again.")

	# Initialise empty lists.	
	split_string = []
	digit_list = []		
	letter_list = []
	upper_case = []
	even_numbers = []
	upper_case_ord = []
	even_numbers_ord = []
	
	
	for x in string:
		split_string.append(x)		# Assign substrings from initial string to a list.
		for y in x:			# For all characters in substring.
			if y.isalpha():			# If that character is a letter.
				if y.isupper():
					upper_case_ord.append(ord(y))		# Convert upper-case letters.
					upper_case.append(y)
					letter_list.append(y)
				else:
					letter_list.append(y)
			elif y.isdigit():			# If that character is a number.
				z=int(y)			# We need to do this because y is a string, and if y.isdigit() = true, then it still may call an exception.
                        			# i.e. y=2^2 is a digit, but not an integer (4 is an integer).
				if z % 2 == 0:
					even_numbers_ord.append(ord(y))			# Convert even numbers.
					even_numbers.append(y)
					digit_list.append(y)
				else:
					digit_list.append(y)
			else:
				pass		# For any other type of character, ignore and move on.
	print("The letters in the long string are: \n", f"{letter_list}")
	print("The upper-case letters in the long string are: \n", f"{upper_case}")
	print("The ASCII decimal values for the upper-case letters in the long string are: \n", f"{upper_case_ord}")

	print("The numbers in the long string are: \n", f"{digit_list}")
	print("The even numbers in the long string are: \n", f"{even_numbers}")
	print("The ASCII decimal values for the upper-case letters in the long string are: \n", f"{even_numbers_ord}")

string = "56aAww1984sktr235270aYmn145ss785fsq31D0"

separate_string(string)

"""
Output:
The letters in the long string are: 
 ['a', 'A', 'w', 'w', 's', 'k', 't', 'r', 'a', 'Y', 'm', 'n', 's', 's', 'f', 's', 'q', 'D']
The upper-case letters in the long string are: 
 ['A', 'Y', 'D']
The ASCII decimal values for the upper-case letters in the long string are: 
 [65, 89, 68]
The numbers in the long string are: 
 ['5', '6', '1', '9', '8', '4', '2', '3', '5', '2', '7', '0', '1', '4', '5', '7', '8', '5', '3', '1', '0']
The even numbers in the long string are: 
 ['6', '8', '4', '2', '2', '0', '4', '8', '0']
The ASCII decimal values for the upper-case letters in the long string are: 
 [54, 56, 52, 50, 50, 48, 52, 56, 48]
"""

"""
Pt2.
You are required to create a program that showcases the required output for the following question:
Many newspapers publish a cryptogram each day, for instance:

VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
"""

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key       # For a value, say 'i', ord('i') = 105 + 13 = 128
            # The cryptogram is only capitals, so we can ignore lowercase cases
            if shifted < ord('A'):      # If the shifted value is less than the lower range (A-Z)
                shifted -= ord('A') - ord('Z') - 1
            elif shifted > ord('Z'):        # If the shifted value is more than the upper range (A-Z)
                shifted += ord('A') - ord('Z') + 1
            decrypted_text += chr(shifted)      ## add that character to the new string and continue
        else:
            decrypted_text += char      ## else add that character to the new string and continue
    print(decrypted_text)

key = ord("V")-ord("I")

### A little trial and error, but single letters in a sentence are normally either a or i,
###	and two letter words are similar.

encrypted = """
VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
"""

text = encrypted
decrypt(text, key)

"""
OUTPUT:
IM SELFISH IMPATIENT AND A LITTLE INSECURE I MISTAKES I AM OUT OF CONTROL
ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS
HELLDONT DESERVE ME AT MY BEST MARILYN MONROE
"""