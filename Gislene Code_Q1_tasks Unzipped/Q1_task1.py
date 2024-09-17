import os
import pandas as pd

# Define the folder where the CSV files are stored (raw string to handle backslashes)
folder_path = r'C:\Users\Liany\Desktop\Ass2_HIT137\Code_Q1_tasks'

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Open a file to write the extracted text
with open('extracted_texts.txt', 'w', encoding='utf-8') as output_file:
    # Loop through each CSV file
    for csv_file in csv_files:
        # Read the CSV file
        csv_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(csv_path)

        # Check if the 'TEXT' column exists
        if 'TEXT' in df.columns:
            # Write the text column to the output file
            df['TEXT'].to_string(output_file, index=False)

        # Debug: Print the column names to help ensure the correct extraction
        print(f"Columns in {csv_file}: {df.columns}")

print("Extraction complete. Check the 'extracted_texts.txt' file.")


