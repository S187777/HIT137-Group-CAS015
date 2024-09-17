import csv
from collections import Counter
import re

# Step 1: Here we can read the extracted text file
with open('extracted_texts.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Here we can preprocess the text and count word occurrences
# Remove any special characters and make all words lowercase
words = re.findall(r'\b\w+\b', text.lower())

# Step 3: Here we use Counter to find the most common words
word_counts = Counter(words)

# Step 4: Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Step 5: Write the top 30 words and their counts to a CSV file
with open('top_30_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_30_words)






