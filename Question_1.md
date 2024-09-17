Hi team, I was think for question 1 we step up the code like this

Create an empty list to store the text 

Loop through all the files in the specified folder:

Use a loop to go through all files in the folder 

Use an if condition to check if the file ends with something


Append the text from the CSV file into the created empty list.

Create another list to keep track of the files that have been processed.

######  #####  ######  ######  ######   #######  ######  ######  #########   ###### ###### ######
Notes down here:
First Step or Start point<<>>
 
Create an empty list, text_list, to store the text from the .csv files.
Create another list, processed_files, to track the files that have been processed.

Next
Loop Through Files<<>>

Use a for loop to go through every file in the specified folder.
But with a condition: Check if the file ends with .csv. This ensures we only process CSV files.

Next
Processing and Appending<<>>
For each .csv file found, append its text into the text_list.
Add the file name to processed_files to ensure that we know what has been processed.

Note:
Add error handling: If the file cannot be read, log the error and continue processing.
Add logging to provide feedback on which files have been processed.
Consider optimising for large datasets by processing files in chunks (especially in the case of large .csv files).

Code:


# List to store text from CSV files
text_list = []

# List to track processed files
processed_files = []


# Loop through all the files in the specified folder
for file in folder:
    # Only process CSV files
    if file.endswith('.csv'):
        try:
           # Read the file and append the content to text_list
            text_list.append(read_file(file))
            
            # Add the file to the processed files list
            processed_files.append(file)


## TODO: Add full logging implementation below here> back later.


## Just a note here I've mentioned about doing logging but haven’t shown how.>>>>Back here later tp finish it
import logging
logging.basicConfig(filename='process.log', level=logging.INFO)

# Inside the loop, log the processed files
logging.info(f"Processed file: {file}")
