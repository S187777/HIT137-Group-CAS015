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
            column = dataframe['TEXT', 'entites','SHORT-TEXT']  # Column Names from CSV1, CSV2, CSV3, and CSV4.
            for data in column.tolist():
                csv_data += ' ' + data

    if not csv_data:           # This baiscally asks if the csv_data is empyty, then True. 
        raise FileNotFoundError

except FileNotFoundError:
    print("Error: No *.csv files are found in this directory.\n Please check the filepath.")

cleaned_text = re.sub(r'[^\w\s]', '', csv_data)     # The Regular Expression Module .sub() replaces a matching string with an output.
                                                    # In this case, we want any punctuation to be replaced with ''.
text_list = cleaned_text.split()

with open('Ass2Q1Pt1-Extracted_Text.txt', 'w') as text_file:
    text_file.write(' '.join(text_list))
text_file.close()

# This just takes the data in the columns described, and puts it in a text file.


# To check if the text is a word:

try:
    with open('words.txt', 'r') as English:     # Here we use the file from GitHub to check if English words.
        valid_words = set(English.read().split())       # By creating a set, the check takes less time?? Forum consensus.
    
    if not os.path.isfile('words.txt'):
        raise FileNotFoundError("Error: words.txt file not found")
    
    with open('Ass2Q1Pt1-Extracted_Text.txt', 'r') as text_file:
        extracted_text = text_file.read()

    if not os.path.isfile('Ass2Q1Pt1-Extracted_Text.txt'):
       raise FileNotFoundError("Error: Ass2Q1Pt1-Extracted_Text.txt file not found")
    
except FileNotFoundError:
    print("Error: A file you tried to open is not found.")

english_words = []
extracted_list = extracted_text.split()

for cleaned_data in extracted_list:
    if cleaned_data.lower() in valid_words:
        english_words.append(cleaned_data)

# This takes all the cleaned data string, adds it to a list after splitting.
# This then compares the string portions with the set of english words.

with open('Ass2Q1Pt1-Extracted_Words.txt', 'w') as text_file:
    text_file.write(' '.join(english_words))
text_file.close()

# This writes the list of words from the CSV files into a text document.

