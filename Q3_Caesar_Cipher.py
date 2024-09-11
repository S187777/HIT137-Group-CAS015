def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Assuming we now know the key, replace `key` with the value (you'll determine the key)'I mean the person running the code 
#need to figure out what key was used to encrypt the code in the first place.

key = 13  # Example key, this could vary 
encrypted_text = """tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}
qrs cebprff_ahzoref():
    tybony_tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

juvyr ybpny_inevnoyr > 0:
    vs ybpny_inevnoyr % 2 == 0:
        ahzoref.erzbir(ybpny_inevnoyr)
    ybpny_inevnoyr -= 1

erghea ahzoref
"""

# Decrypt the text using the key
decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)
