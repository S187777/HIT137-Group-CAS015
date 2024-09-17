#   First Step:
    # Fix code to get key.

total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i- j
counter = 0
while counter < 5:
    if total < 13:
        total += 1
    
    elif total > 13:
        total -= 1
    
    else:
        counter += 2
print(total)   # Issue Found!! was not able to print the key

key = total     # The total value is the shift key for the next part. #Make key = total
## key = 13


#   Second Step:
    # Understand how the code was encrypted.
"""
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():      ## Only if a character is a letter.
            shifted = ord (char) + key
            if char.islower():
                if shifted > ord('z'):  # if the key is positive, and shifted value goes past the boundary of lowercase ord('z')
                    shifted -= 26   # reduce the shifted value by 26 == ord('a') - ord('z') + 1
                elif shifted < ord('a'):    # if the key is negative, and shifted value goes past the boundary of lowercase ord('a')
                    shifted +=26    # increase the shifted value by 26 == ord('a') - ord('z') + 1
            elif char.isupper():
                if shifted > ord('Z'):  # if the key is positive, and shifted value goes past the boundary of uppercase ord('Z')
                    shifted -= 26   # reduce the shifted value by 26 == ord('A') - ord('Z') + 1
                elif shifted < ord('A'):    # if the key is negative, and shifted value goes past the boundary of uppercase ord('A')
                    shifted += 26   # increase the shifted value by 26 == ord('A') - ord('Z') + 1
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

key = ?????

encrypted_code = encrypt(original_code, key)

print(encrypted_code)
"""


#   Third Step:
    # Write a decryption based on the above.

"""
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():      #   ONLY if the character is a letter
            shifted = ord(char) - key       #for a value, say 'i', ord('i') = 105 + 13 = 128
            if char.islower():      # lowercase case
                if shifted < ord('a'):      # if the shifted value is more than.
                    shifted -= ord('a') - ord('z') - 1
                elif shifted > ord('z'):
                    shifted += ord('a') - ord('z') + 1
            elif char.isupper():        # uppercase case
                if shifted < ord('A'):      # if the shifted value is more than.
                    shifted -= ord('A') - ord('Z') - 1
                elif shifted > ord('Z'):
                    shifted += ord('A') - ord('Z') + 1
            decrypted_text += chr(shifted)      ## add that character to the new string and continue
        else:
            decrypted_text += char      ## else add that character to the new string and continue
    print(decrypted_text)

"""


#   Fourth Step:
    # Decrypt the code.

encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted -= ord('a') - ord('z') - 1
                elif shifted > ord('z'):
                    shifted += ord('a') - ord('z') + 1
            elif char.isupper():
                if shifted < ord('A'):
                    shifted -= ord('A') - ord('Z') - 1
                elif shifted > ord('Z'):
                    shifted += ord('A') - ord('Z') + 1
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    print(decrypted_text)

decrypt(encrypted_code, key)

"""
OUTPUT:

global_variable = 100
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable

modify_dict(5)

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
"""


#   Fifth Step:
    # Assess decrypted code to fix any mistakes.


global_variable = 100       # Define a variable "global_variable"

my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}        # Define a dictionary


"""
def process_numbers():         # Define a function with no argument.
    global global_variable          # Use global to modify a local variable inside a function.
    local_variable = 5          # Assign a local variable
    numbers = [1, 2, 3, 4, 5]       # Assign another local Variable

    while local_variable > 0:           # While loop to remove even numbers from a list or set.
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers      # Return output.

The intent of this function seems to be to remove any even numbers from a list (or set).
    If so, then the function requires an argument, i.e. a list, or a set.
The global_variable is assigned global, but not modified in this function.
    So we can remove it.
The numbers list is a variable local to this function.
    So we can make it global or move it outside of the function.
The *.remove() function removes the first occurance of an element in a list.
    Do we need to add a check for multiple numbers in list??
The *.remove() function will raise a ValueError if the value is not in the list.
    Do we need to add an error exception case?
    If so:
    expcept 
The variable local_variable is 5, but is this to ensure the while loop iterates through the whole list?
    If so, then we need to make local_variable = len(list).
The return function returns a new list with the values removed.

The cleaned up code would then read:
"""

def process_numbers(numbers):
    local_variable = len(numbers)

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    print(numbers)
    return numbers

numbers = [1, 2, 3, 4, 5]

process_numbers(numbers)

# Output: [1, 3, 5]


my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}         
# A set of integers including duplicates.
# Duplicates will be ignored when the set is called.

"""
result = process_numbers(numbers=my_set)

Calling the function above and assigning the returned list to a variable.
The original function did not require any arguments, but that has changed.
The argument 'numbers = my_set' indicates the code is intended to iterate through the set.
    We can just remove 'numbers =', or '= my_set'.
"""
# Clean code:
result = process_numbers(numbers)

# If we wanted to run this function on the my_set set:

numbers = my_set
result = process_numbers(numbers)


"""
def modify_dict():          # A function to add a value (10) to the key 'ke14'.
                            # This function does not expect an argument.
    local_variable = 10
    my_dict['ke14'] = local_variable

modify_dict(5)

The intent of this function seems to be to add a value, or a key/value pair to a dictionary.
    If the intent is to add a key/value pair, then we will require two arguments in the function.
    i.e. modify_dict(key, value):
This would then oblige us to change the code to this:
"""
def modify_dict(key, value):
    local_variable = value
    my_dict[key] = local_variable

modify_dict('ke14', 5)

"""
Otherwise, if the intent is to just add the value 10 to the key 'ke14', 
We would remove all arguments in the function, and the call.

We could then change the code to this:
"""
def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable

modify_dict()


"""
def update_global():
    global global_variable
    global_variable += 10

This funtion appears to call the global variable 'global_variable' assigned at the begining of this decrypted code,
Then proceeds to add 10 to the variable.
The function is never called, however.

If the intent is to update global_variable with a value, we can add an argument, and call the function.

"""
def update_global(value):
    global global_variable
    global_variable += value
update_global(10)

"""
Else, If the intent is to just change the global_variable by 10, every time it is called,
we can simply call it by using:

def update_global():
    global global_variable
    global_variable += 10
update_global()

However, this seems a very large piece of code for a limited use.
"""


"""
for i in range(5):
    print(i)
    i += 1

Discussion:
If the intent was to just print 0,1,2,3,4,
Then we could delete i +=1.

Else, if the intent was to print 1,2,3,4,5,
Then we could move i += 1 to before the print function.
That would look like this:
"""
for i in range(5):
    i += 1
    print(i)
    

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")
# my_set is not none, and key ke14 does have value 10, so True.


"""
if 5 not in my_dict:
    print("5 not found in the dictionary!")

If the intent of this code is determine if key '5' is not in the my_dict dictionary,
Then the code requires no change, except to add quotation marks to 5, i.e. '5' 
This then checks for the string '5', not an integer.

Else, if the intent of this code is determine if key or value '5' is not in the my_dict dictionary,
We could change it to:
"""
if '5' not in my_dict and '5' not in my_dict.values():
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)