"""
Task 1:
First we open and Read all CSV files in filepath(folder).
By using Gislene's PANDA DataFrames method, 
    we can use DataFrames to import the data as a column,
    using the csv column names to differentiate the data we want.
    Then we can convert the column of data in the dataframe into a list of data,
    using *.tolist()
Extract the list contents into a string.
We can write that string into a text file, and voila.
We can then save that file (Task 1 complete.)

I then found an online "english word list" on github, with instructions on how to use it.
I believe before we do any futher works, we should compare all strings
    with this list, and ensure we only have text and words to work with.
So we open that "english word list" file and import the contents into a set.

Next, we import and clean up the contents of our task 1 text file, 
    and compare the two, adding only "words" to a new list.

After that, we can create a new text file, and save the list.

We can then move on to the next part, using Counter to count the 30 most common words.
We write the 30 most common words into a new CSV file.
    We can print the output here to Sanity check everything is working correctly.

Importing the tokenizer, we can count the 30 most common tokens,
    Here we can choose the 'OG' file or new filtered words.
We write that output to a new CSV file.
    We can print the output here again to Sanity check everything is working correctly.

We then Use NLPs to extract the Disease and Drug words into new list,
    This is where the 'filtered' words should imporve our results.
Write the output from each Model to a new CSV file.

Open using Panda, dataframes, and write to lists.
Count the length of the lists and compare.
Using Counter again get the most common words in each file,
    print them to a new list. (30? 50? not specified)
Compare the most common words.
Write a new list with output lists, and if in list, append list.
    This should give us a returned list with only unique words.
Write this lists and unique words list to csv.

Write a small comparison about the different models.
    """