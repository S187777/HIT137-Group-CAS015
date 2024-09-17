import spacy
import scispacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from collections import Counter

# Load SpaCy models for disease and drug detection
spacy_model = spacy.load("en_ner_bc5cdr_md")  # Load the SciSpacy NER model

# Load BioBERT for comparison
biobert_model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
biobert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
biobert_ner_pipeline = pipeline("ner", model=biobert_model, tokenizer=biobert_tokenizer)

# Helper function to split the text into chunks of a specified size
def split_text_into_chunks(text, max_length=50000):  # Set max_length appropriate for SpaCy
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Read the text file
with open('extracted_texts.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Step 1: Extract entities using SpaCy
# Split text into smaller chunks
spacy_text_chunks = split_text_into_chunks(text)

# Process each chunk in SpaCy and collect entities
spacy_entities_filtered = []
for chunk in spacy_text_chunks:
    spacy_entities = spacy_model(chunk).ents
    spacy_entities_filtered.extend([ent for ent in spacy_entities if ent.label_ in ["DISEASE", "CHEMICAL"]])

# Step 2: Extract entities using BioBERT
# Split the text into chunks of 512 tokens for BioBERT
text_chunks = split_text_into_chunks(text, max_length=512)
biobert_entities_filtered = []

# Note:
#  The entities extracted using BioBERT are filtered to only include specific types ('B-DISEASE' and 'B-CHEMICAL').
#  Modify this list if we need to filter for other entity types.
#  Using Counter to find the 10 most common entities from both SpaCy and BioBERT.
#This helps to identify differences in the types of entities each model detects.
#   Adjust 'most_common(10)' if we want to compare a different number of entities.

# Process each chunk for BioBERT and collect entities
for chunk_text in text_chunks:
    biobert_entities = biobert_ner_pipeline(chunk_text)
    biobert_entities_filtered.extend([(entity['word'], entity['entity']) for entity in biobert_entities if entity['entity'] in ['B-DISEASE', 'B-CHEMICAL']])  # Change as needed

# Step 3: Count and compare entities
# Most common entities in SpaCy
spacy_common = Counter([ent.label_ for ent in spacy_entities_filtered]).most_common(10)
# Most common entities in BioBERT
biobert_common = Counter([ent[1] for ent in biobert_entities_filtered]).most_common(10)

# Step 4: Print the comparison of most commom entities
print("\nSpaCy Most Common Entities:")
for entity, count in spacy_common:
    print(f"{entity}: {count}")

print("\nBioBERT Most Common Entities:")
for entity, count in biobert_common:
    print(f"{entity}: {count}")





