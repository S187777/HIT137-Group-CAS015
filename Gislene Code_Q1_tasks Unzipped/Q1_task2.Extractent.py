import spacy

# Load the scispaCy models
nlp_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")

# File containing the combined text
input_file = 'combined_text.txt'

# Read the text file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Process the text using the biomedical NER model
doc_bc5cdr_md = nlp_bc5cdr_md(text)
print("\nEntities detected by en_ner_bc5cdr_md model:")

# Extract entities and print them
for entity in doc_bc5cdr_md.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
