import os
import csv
#import scispacy
import spacy

nlp = spacy.load("en_core_sci_sm")

def add_all_words_to_text():

	f = open("CSV_compiled.txt",'w')
	f.write("")
	f.close()

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

"""
count_dict = {}

for x in complete_list:
	if len(x) < 3:
		pass
	else:
		count = complete_list.count(x)
		count_dict[x] = count

max_dict = {}
tally = 0

while tally < 30:
	max_value_key = max(zip(count_dict.values(), count_dict.keys()))[1]
	max_dict[max_value_key] = count_dict[max_value_key]
	del count_dict[max_value_key]
	tally += 1

with open('outputfile.csv','w') as f:
    w = csv.writer(f)
    w.writerows(max_dict.items())
"""