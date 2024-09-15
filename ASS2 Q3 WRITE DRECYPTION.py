encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xr11' 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr, = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir (ybpny_inevnoyr)
        ybpny inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref (ahzoref=zl_frg)

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

vs z1_frg vf abg Abar naq zl_qvpg['xr14']== 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va z1_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr),
cevag(zl_qvpg)
cevag(zl_frg)
"""

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
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

key = 13
text = encrypted_code

decrypt(text,key)
