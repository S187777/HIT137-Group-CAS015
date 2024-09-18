try:
    import csv
    import os

    import pandas as panda
    import re

    from collections import Counter
    from transformers import AutoTokenizer
    import spacy
except ImportError:
    print("One or more libraries have not been imported.")

"""
First we open and Read all CSV files in filepath(folder).
By using Gislene's PANDA DataFrames method, 
    we can use DataFrames to import the data as a column,
    using the csv column names to differentiate the data we want.
    Then we can convert the column of data in the dataframe into a list of data,
    using *.tolist()
Extract the list contents into a string.
We can write that string into a text file, and voila.
We can then save that file (Task 1 complete.)
"""

try:
    csv_data = ""

    for file in os.listdir():       # os.listdir(arg = path):, if path is left out, then default is Current Working Directory.
                                    # If required, insert the filepath here.
        if file.endswith('.csv'):
            dataframe = panda.read_csv(file)
            column = dataframe['TEXT','entites','SHORT-TEXT']  # Column Names in CSV files.
            for data in column.tolist():
                csv_data += ' ' + data

    if not csv_data:           # This baiscally asks if the csv_data is empyty, then True. 
        raise FileNotFoundError

except FileNotFoundError:
    print("Error: No *.csv files are found in this directory.\n Please check the filepath again.")

cleaned_text = re.sub(r'[^\w\s]', '', csv_data)     # The Regular Expression Module .sub() replaces a matching string with an output.
                                                    # In this case, we want any punctuation to be replaced with ''.
text_list = cleaned_text.split()

with open('Ass2Q1Pt1-Extracted_Text.txt', 'w') as text_file:
    text_file.write(' '.join(text_list))
text_file.close()

# This just takes the data in the columns described, and puts it in a text file.

# To check if the text is a word:

try:
    with open('words.txt', 'r') as English:     # Here we use the file from GitHub to check if English words. this list has a comparable list to compare our list to a global source. 
        valid_words = set(English.read().split())       # By creating a set, the check takes less time?? Forum consensus.
    
    if not os.path.isfile('words.txt'):
        raise FileNotFoundError("Error: words.txt file not found")
   
except FileNotFoundError:
    print("Error: A file you tried to open is not found.")

english_words = []

for cleaned_data in text_list:
    if cleaned_data.lower() in valid_words:
        english_words.append(cleaned_data)

with open('Ass2Q1Pt1-Extracted_Words_Text.txt', 'w') as extracted_data:
    extracted_data.write(' '.join(english_words))


# Here we start Part 2, counting the most common words.

# Using Counter to count the 30 most common words. 

most_common_words = Counter(english_words).most_common(30) # Counting the top 30 words

with open('Ass2Q1Pt2-Counter-30-Most-Common.csv', 'w') as csvfile:  # Open a new CSV file 

    writer = csv.writer(csvfile)  
    writer.writerow(['Word', 'Count'])  # Write a new header title with 'WORD' and 'COUNT'
    
for word, count in most_common_words:  # Loop through the list
    writer.writerow([word, count])  # Write the word and its count to the CSV file

print(most_common_words)  # Print the words and its count to the screen


# Using Tokeniser to count the 30 most common tokens.

the_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")        

list_tokens = the_tokenizer.tokenize(' '.join(text_list))

most_common_tokens = Counter(list_tokens).most_common(30)

with open('Ass2Q1Pt2-Tokens-30_Most_Common.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Tokens', 'Number of Occurances'])
    for token, count in most_common_tokens:
        writer.writerow([token, count])

print(most_common_tokens)


