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
print(total)

key = total     # The total value is the shift key for the next part.
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

global_variable = 100
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}
numbers = 0
def process_numbers():
    global global_variable
    # Why assign this global variable here?
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers


########################################################################        This Is Where We Need To Check From
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
""
result = process_numbers(numbers=my_set)
""
## The function process_numbers() does not expect an argument (numbers=my_set)
### A set will not return two items with the same value.
## ??? Do we need to replace the numbers list with the my_set ???

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