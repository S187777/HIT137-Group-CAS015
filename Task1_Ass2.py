# This code uses panda to look for all csv files in a described folder,
# Then opens and reads each CSV file, writes the data in either "text" or "short-text" columns
#  from that file into an "extracted texts" txt file, and then does the same for the next CSV file. 
# And then returns an output indicating an exception or completeness.


import os
import pandas as pd

# Define the folder where the CSV files are stored # Hi Team, just update below here your folder path
folder_path = 'C:/Users/  '

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Open a file to write the extracted text
with open('extracted_texts.txt', 'w', encoding='utf-8') as output_file:
    # Loop through each CSV file
    for csv_file in csv_files:
        # Read the CSV file
        csv_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(csv_path)
        
        # Print the column names to help debug
        print(f"Columns in {csv_file}: {df.columns}")
        
        # Check if 'SHORT-TEXT' or 'TEXT' column exists in the CSV
        if 'SHORT-TEXT' in df.columns:
            # Extract the 'SHORT-TEXT' column and write to the output file
            for text in df['SHORT-TEXT']:
                output_file.write(str(text) + '\n')
        elif 'TEXT' in df.columns:
            # Extract the 'TEXT' column and write to the output file
            for text in df['TEXT']:
                output_file.write(str(text) + '\n')
        else:
            print(f"Neither 'SHORT-TEXT' nor 'TEXT' column found in {csv_file}")

print("Extraction is complete. Please check the 'extracted_texts.txt' file.")

