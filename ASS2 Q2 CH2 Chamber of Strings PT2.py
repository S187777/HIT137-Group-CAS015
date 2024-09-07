"""
You are required to create a program that showcases the required output for the following question:
Many newspapers publish a cryptogram each day, for instance:
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