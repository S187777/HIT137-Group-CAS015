# This code uses CWD (current working directory) to open a described folder, 
# 	and then opens and reads each CSV file, ignores any data <10 characters,
# 	determines if it is Alphabetical, and writes a lower-case of the data into 
# 	a "csv compiled text" txt file. 
# 	It also takes every punctuation symbol in "string" and replaces that with a space,
# 	and writes everything else as a "".
#	As it finishes each cell, it uses NLP to inspect the cells contents to pick out 
# 	the words related to the library we use.
# *** We need to add all the NLP words into a new list[str], and counter the occurences of the words.
# 	The code then does the same for the next CSV file.
# After compiling the text file, the code then takes every string, and compiles that into a list[str]
# 	ignores every string less <3 characters, and counts the occurance of that string in the list,
# 	and compiles that string and count into a dictionary.
# The dictionary is then sorted using max to determine the max value(count) and its key(string)
# 	for the 30 highest values (30 most common strings), and those 30 are added to a new dictionary.
# The new dictionary is then written into a new CSV file.

## Still to use the ‘Auto Tokenizer’ function in the ‘Transformers’ library, 
# 	write a ‘function’ to count unique tokens in the text (.txt) and give the ‘Top 30’ words.
## Still to extract the ‘diseases’, and ‘drugs’ entities in the ‘.txt file’ separately 
# 	using ‘en_core_sci_sm’/’en_ner_bc5cdr_md’ and biobert. 
## Still to compare the differences between the two models 
# 	(Example: Total entities detected by both of them, what’s the difference, 
# 	 check for most common words, and check the difference.)

import os
import csv
#import scispacy
import spacy

nlp = spacy.load("en_core_sci_sm")

def add_all_words_to_text():

	f = open("CSV_compiled.txt",'w')
	f.write("")
	f.close()
	
	# I thought CWD would be a good choice here because VS Code usually likes to draw most 
	# 	of its information and save to the same folder by default, so we can just add our CSV files
	# 	to that folder and then we dont need to go importing file paths.

	Path = os.getcwd()		#get current working directory ==> where is python interpreter accessing from.
	filelist = os.listdir(Path)		#create string of path directory

	for i in filelist:
		if i.endswith(".csv"):
			with open(Path + "\\" + i, mode ='r') as file:

				f = open("CSV_compiled.txt",'a')
				csvFile = csv.reader(file)
				sentence = ""
				for lines in csvFile:
					for item in lines:
						if len(item)<10:
							pass
						else:
							for x in item:
								if x.isalpha():
									lower_x = x.lower()
									f.write(lower_x)
									sentence += lower_x
								elif x == " " or x == "-" or x == "_" or x == "\n":
									f.write(" ")
									sentence += " "
								else:
									f.write("")
							line = nlp(sentence)
							#print(list(line.ents))
							f.write(" ")
				f.close()

add_all_words_to_text()

word_string = str()

with open("CSV_compiled.txt",'r') as f:
	for i in f:
		word_string += " " + i

complete_list = word_string.split()

print(len(complete_list))

#temporarilly blanked out to test the above.
"""

# New dictionary to add key/value of (word/word count).
count_dict = {}

for x in complete_list:
	if len(x) < 3:
		pass
	else:
		count = complete_list.count(x)
		count_dict[x] = count

		
# New dictionary to add the 30 highest (word/word count) as they loop.
max_dict = {}
tally = 0

while tally < 30:
	max_value_key = max(zip(count_dict.values(), count_dict.keys()))[1]
	max_dict[max_value_key] = count_dict[max_value_key]
	del count_dict[max_value_key]
	tally += 1

# Write the 30 highest dictionary to a CSV file.
with open('outputfile.csv','w') as f:
    w = csv.writer(f)
    w.writerows(max_dict.items())
"""