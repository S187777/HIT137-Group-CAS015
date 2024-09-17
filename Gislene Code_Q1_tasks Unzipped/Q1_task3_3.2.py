import os
import csv
from collections import Counter
from transformers import AutoTokenizer

# Step 1: Debug - print the current working directory
print("Current Working Directory:", os.getcwd())

# Step 2: Debug - list all files in the current directory
print("Files in the directory:", os.listdir())

# Load the BioBERT tokenizer (using for biomedical texts)
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Use the correct path for the text file
file_path = 'extracted_texts.txt'  # Update path as needed based on file location

# Open and read the text file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Make sure 'extracted_texts.txt' is located in the correct directory.")

# Tokenize the text using the Hugging Face tokenizer
tokens = tokenizer.tokenize(text)

# Count the tokens and get the top 30 most common tokens
token_counts = Counter(tokens)
top_30_tokens = token_counts.most_common(30)

# Write the top 30 tokens and their counts to a CSV file
with open('top_30_tokens.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Token', 'Count'])  # Write header
    writer.writerows(top_30_tokens)      # Write token counts

