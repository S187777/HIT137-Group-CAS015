import os
import csv
from collections import Counter

def process_csv_files():
    Path = os.getcwd()  # Get current working directory
    filelist = os.listdir(Path)  # List all files in the directory
    word_list = []

    # Process each CSV file in the directory
    for i in filelist:
        if i.endswith(".csv"):
            with open(os.path.join(Path, i), mode='r') as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    for item in lines:
                        if len(item) >= 10:  # Assuming large text is at least 10 characters
                            cleaned_words = clean_text(item)
                            word_list.extend(cleaned_words)
    
    # Use Counter for efficient counting
    count_dict = Counter(word_list)

    # Extract top 30 most common words
    top_30_words = count_dict.most_common(30)

    # Write to output CSV file
    with open('outputfile.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerows(top_30_words)

def clean_text(text):
    words = []
    for x in text:
        if x.isalpha() or x == " ":
            words.append(x.lower() if x.isalpha() else " ")
    cleaned_text = "".join(words)
    return cleaned_text.split()

# Execute the function
process_csv_files()

