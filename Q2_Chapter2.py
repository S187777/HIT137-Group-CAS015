# Input string (example from the task)
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Step 1: Here we separate the string into numbers and letters
numbers = ''.join([char for char in s if char.isdigit()])  # Extract digits
letters = ''.join([char for char in s if char.isalpha()])  # Extract letters

print(f"Number string: {numbers}")
print(f"Letter string: {letters}")

# Step 2: Here we convert even numbers to ASCII code
even_numbers = [int(char) for char in numbers if int(char) % 2 == 0]
ascii_even_numbers = [ord(str(num)) for num in even_numbers]

print(f"Even numbers: {even_numbers}")
print(f"ASCII codes of even numbers: {ascii_even_numbers}")

# Step 3: Here we convert uppercase letters to ASCII code
uppercase_letters = [char for char in letters if char.isupper()]
ascii_uppercase_letters = [ord(char) for char in uppercase_letters]

print(f"Uppercase letters: {uppercase_letters}")
print(f"ASCII codes of uppercase letters: {ascii_uppercase_letters}")
