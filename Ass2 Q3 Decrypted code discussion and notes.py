## Error Prone Code:

global_variable = 100
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}
numbers = 0

def process_numbers(): # requires a argument to be called could be list or set 
    global global_variable  # Why would you need to assign this global variable here?
    local_variable = 5 # length of set ??
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} #sets can't have double up
""
result = process_numbers(numbers=my_set)
""
## The function process_numbers() does not expect an argument (numbers=my_set)
### A set will not return two items with the same value.
## ??? Do we need to replace the numbers list with the my_set ??? 

# to remove double ups we could use this code my_set = list(set(my_set))

def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable

modify_dict()
## The function modify_dict() does not expect an argument.
## (5)  ==> remove argument to call function.

def update_global():
    global global_variable
    global_variable += 10
# This funtcion is never called, and so the global variable is never updated.
update_global()

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

#You made a change

###### I'll start here just in case I need to come back to the starting point; I get lost easily here ###########


##Encryption Recap:
 #The encrypt(text, key) function is a Caesar cipher that shifts each letter by a set number (the key). 
#To decrypt, we reverse this shift.

#Additional Info: I found more details about ROT13 and Caesar ciphers on Wikipedia. 
#The explanation there clarified how ROT13 is just a Caesar cipher with a 13-place shift.
#Noticed some variables like tybony_inenvoyr, zl_qvpg, noticed how functions and loops are being used

#question 3 appears to use some form of simple encryption (like ROT13)
#The text looks like it uses ROT13 (a 13-place shift), so we suspect the key is 13.

#Conclusion: Our hypothesis is that the key for decryption is 13. 🎯 Let's use this to crack the code! 🔓🕵️‍♂️

### WHy are we hypothesising? The Assessment Question TELLS us how it is decrypted, and also GIVES us the key??

## We just need a function that undoes the encryption by shifting each character back using the key value.

### YES, this is part of the previous Question?

# Decrypt the code using the key
key = 13
decrypted_code = decrypt(encrypted_code, key)
print("Decrypted Code:")
print(decrypted_code)


##Fixing the Decrypted Code:


##Error 1: process_numbers() Function

##Issue: The process_numbers() function doesn’t have parameters, 
##but it’s called with numbers=my_set. 
#Fix: Change the function to take a numbers parameter and remove the assignment of the local numbers.

#Working out and fixing this part of the code - 

def process_numbers(numbers):      # This def function and the code below is asking to remove all the odd numbers from within the list or set when call for. 
                            
    local_variable = 0
    local_variable += len(numbers) #adding this enables no limit on the lenght

    #local_variable = 5      # this is old code!!!  while loop only "iterates" through the set and then stops.
    #numbers = [1, 2, 3, 4, 5]       # the set or list to remove even numbers from

    while local_variable > 0:       # Start number is (5)

        if local_variable % 2 == 0:     # seeing if number is even and can be divided by 2
            numbers.remove(local_variable)      #if the number is even it will remove it from the list.

        local_variable -= 1     # next iteration, start number minus 1, will count-down while loop so not in an infinite loop
                                # lenght of set to iterate through?

    print(numbers) # no print function was in the old code!! this prints before the return is actioned. 

    return numbers      #  returns the number back to the list after removing even numbers

numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} #sets can't have double up of numbers 

result = process_numbers(numbers)        #  so this line removes (numbers = ) then shows new results


##Error 2: Calling modify_dict() with Arguments

#Issue: modify_dict() is defined without parameters but is called with (5).
#Correction: Remove the argument 5 from the function call.
modify_dict()  # Removed argument '5' as the function does not accept any parameters

##Error 3: Modifying Loop Variable Inside for Loop

#ssue: Inside the for loop, v is incremented with v += 1, which doesn't affect the loop.
#Correction: Remove v += 1 to prevent confusion.

#Corrected Code:
for v in range(5):
    print(v)
    # v += 1  # Removed this line as it doesn't affect the loop variable in 'range()'

##Error 4: Not Calling update_global() Function

#Issue: The function update_global() is defined but never called.
#Correction: Add a call to update_global() to update the global_variable.

#corrected code:
update_global()  # Added call to update the global variable

##Error 5: Incorrect Condition Check in if Statement

#Issue: The condition if 5 not in my_dict: is checking for the integer 5 in the dictionary keys, which are strings.
#Correction: Adjust the condition to check if 'key5' is in my_dict.

if 'key5' not in my_dict:
    print("Key 'key5' not found in the dictionary!")

#or if we need to check if the value 5 is in the dictionary values:
if 5 not in my_dict.values():
    print("Value 5 not found in the dictionary!")


##Error 6: Potential Modification of my_set

#Issue: my_set is modified inside process_numbers(), which might not be intended.
#Correction: If my_set should remain unchanged, pass a copy of it.

result = process_numbers(numbers=my_set.copy())  # Pass a copy to avoid modifying the original set

##the Corrected and Commented Code

# Decryption function
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key  # Subtract the key to reverse encryption
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around if below 'a'
                elif shifted > ord('z'):
                    shifted -= 26  # Wrap around if above 'z'
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around if below 'A'
                elif shifted > ord('Z'):
                    shifted -= 26  # Wrap around if above 'Z'
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Keep non-alphabetic characters unchanged
    return decrypted_text

# Encrypted code (as provided)
encrypted_code = """
tybony_inenvoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cbeprff_ahzoref():
    tybony tybony_inenvoyr
    ybpny_inenvoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inenvoyr > 0:
        vs ybpny_inenvoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inenvoyr)
        ybpny_inenvoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cbeprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inenvoyr = 10
    zl
"""

#### Where is the rest of it?