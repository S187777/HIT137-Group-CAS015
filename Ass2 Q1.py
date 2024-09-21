import csv
import os
import pandas as panda
import re
from collections import Counter
from transformers import AutoTokenizer, AutoModelForTokenClassification
import spacy
import scispacy

"""try:
    csv_data = []
    column_heading = ["TEXT", "entites", "SHORT-TEXT"]
    for file in os.listdir():       # os.listdir(arg = path):, if path is left out, then default is Current Working Directory.
                                    # If required, insert the filepath here.
        if file.endswith(".csv"):
            dataframe = panda.read_csv(file)
            # Break the file(s) into portions of file that gets iterated.
            # Instead of trying to iterate through the entire file.
            for portion in panda.read_csv(file, chunksize = 10000):
            # Check for column names in CSV files.
                for heading in column_heading:
                    if heading in portion.columns:
                        csv_text = portion[heading]
                        for data in csv_text:
                            csv_data.append(data)
                        break
    if not csv_data:           # This baiscally asks if the csv_data is empyty, then True. 
        raise FileNotFoundError

except FileNotFoundError:
    print("Error: No *.csv files are found in this directory.\n Please check the filepath again.")

# Creating a pattern to check against.

pattern = re.compile(r"[\d\W\s]")       # \d = is string contains digits (not a word) 
                                        # \W = if string does not contain ("a-Z, 0-9, or _")
                                        # \s = if string contains " "

cleaned_text = pattern.sub(" ", " ".join(csv_data))     # The Regular Expression Module .sub() replaces a matching string with an output.
                                                    # In this case, we want any punctuation, " ", or digit to be replaced with " ".
text_list = cleaned_text.split()"""

text_list = []
with open("Ass2Q1Pt1-Extracted_Text.txt", "r") as text_file:
    text_list = text_file.read().split()
"""
with open("Ass2Q1Pt1-Extracted_Text.txt", "w") as text_file:
    text_file.write(" ".join(text_list))
text_file.close()
"""
"""
# This just takes the data in the columns described, and puts it in a text file.
"""
"""
# To check if the text is a word:
valid_words = set()

try:
    with open("words.txt", "r") as English:     # Here we use the file from GitHub to check if English words. this list has a comparable list to compare our list to a global source. 
        valid_words = set(English.read().split())       # By creating a set, the check takes less time?? Forum consensus.
    
    if not os.path.isfile("words.txt"):
        raise FileNotFoundError("Error: words.txt file not found")
   
except FileNotFoundError:
    print("Error: A file you tried to open is not found.")


english_words = []

for clean_data in text_list:
    if clean_data.lower() in valid_words:
        english_words.append(clean_data)        # We are just comparing the strings in text_list with the strings in valid_words.

with open("Ass2Q1Pt1-Extracted_Words.txt", "w") as extracted_words:
    extracted_words.write(" ".join(english_words))
"""
"""
# Here we start Part 2, counting the most common words.

most_common_words = Counter(text_list).most_common(30) # Using Counter to count the 30 most common words. 

with open("Ass2Q1Pt2-Counter-30-Most-Common.csv", "w") as csvfile:  # Open a new CSV file.

    writer = csv.writer(csvfile)  
    writer.writerow(["Word", "Count"])  # Write a new header title with 'Word' and 'Count'.
    
    for word, count in most_common_words:  # Loop through the list.
        writer.writerow([word, count])  # Write the word and its count to the CSV file.

print(most_common_words)  # Print the words and their count to the screen.
"""

# Using Tokeniser to count the 30 most common tokens.

the_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")        

list_tokens = the_tokenizer.tokenize(" ".join(text_list))

most_common_tokens = Counter(list_tokens).most_common(30)

with open("Ass2Q1Pt2-Tokens-30_Most_Common.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Tokens", "Number of Occurances"])
    for token, count in most_common_tokens:
        writer.writerow([token, count])

print(most_common_tokens)   # Print the tokens and their count to the screen.

# Here we go with Part 3, using NLP models to extract the 'diseases' and 'drugs' entities.

# First we tokenise the text. Here we are using the English words list we created before, hopefully the output will be more accurate.
"""
bert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")        
bert_model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")

bert_tokens = bert_tokenizer.tokenize(" ".join(text_list))      # To change this to the english words, substitute text_list for english_words.

nlp_core_sci = spacy.load("en_core_sci_sm")     # Loading the Spacy model.
nlp_ner_bc5cdr = spacy.load("en_ner_bc5cdr_md")     # Loading the other Spacy model.

# Create a few empty sets.
spacy_en_core_set = set()
spacy_en_ner_set = set()
biobert_set = set()

for i in range(0, len(bert_tokens), 10000):     # The NLP models can't deal with large string sizes.
    chunk = bert_tokens[i:i+10000]

    for doc in nlp_core_sci.pipe(chunk):
        for entity in doc.ents:
            if entity.label_ in ["DISEASE", "DRUG"]:
                spacy_en_core_set.add(entity.text)

    for doc in nlp_ner_bc5cdr.pipe(chunk):
        for entity in doc.ents:
            if entity.label_ in ["DISEASE", "DRUG"]:
                spacy_en_ner_set.add(entity.text)
   
    inputs = bert_tokenizer(chunk, return_tensors="pt", padding=True, truncation=True)
    outputs = bert_model(**inputs).logits
    predictions = outputs.argmax(dim=-1).tolist()

    for tokens, pred in zip(chunk, predictions):
        for token, label in zip(tokens.split(), pred):
            if label == 1:
                biobert_set.add(token)

combined_entities = list(spacy_en_core_set) + list(spacy_en_ner_set) + list(biobert_set)

most_common_entities = []

for entity, count in Counter(combined_entities).most_common(30):
    most_common_entities.append(entity)

unique_entities = set(combined_entities)

df = panda.DataFrame({
    "spacy_en_core": [",\n".join(spacy_en_core_set)],
    "spacy_en_ner_set": [",\n".join(spacy_en_ner_set)],
    "biobert_set": [",\n".join(biobert_set)],
    "most_common_entities": [",\n".join(most_common_entities)],
    "unique_entities": [",\n".join(unique_entities)]
})

df.to_csv("Ass2Q1Pt3-Using-NLPs-for-NER.csv")       # Use DF to write to CSV file.

print("The number of entities from the model 'en_core_sci_sm' is:", len(spacy_en_core_set))
print("The number of entities from the model 'en_ner_bc5cdr_md' is:", len(spacy_en_ner_set))
print("The number of entities from the model 'biobert':", len(biobert_set))
"""