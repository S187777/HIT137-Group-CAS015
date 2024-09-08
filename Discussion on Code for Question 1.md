Discussion on Code for Question 1

Discussion involving Thuseethan regarding NLP and reasons for including inside the iterations.
"
I showed him some code in class, and asked for advice regarding using the NLP etc on such huge files, 
and getting errors because the sheer number of "words" to comb through was huge.
My computer set a limit of 1,000,000 "words", and the smallest csv file contained at least 
1.5 or 1.6 million strings ("words") after I extracted and removed any punctuations.
The larger files are way (way, way, way) larger, so to solve that small problem, 
(I figured out the solution before he got back to me) I used the NLP inside the iteration.
Then it only needs to read and process each segment.
"

Discussion about process for writting code
From Gislene:
"
Hi Rhett, 
 
I checked out your code for task 1 last night, and it’s doing things more in detail. I also have added my code to task 1 in the git hub repository.
 
 In my code I'm just pulling text from specific columns ('SHORT-TEXT' or 'TEXT') in each CSV file and writing that into a text file (extracted_texts.txt). I'm using Pandas, which makes it simple to work with CSVs when you're focusing on certain columns.
 
In your code, you're processing the whole CSV file, grabbing every bit of text, converting everything to lowercase, and cleaning it up by skipping symbols. Then, you’re counting the most frequent words and saving the top 30 into a CSV (outputfile.csv). So, you’re doing a lot more with word counting and stuff like that.
 
Basically, my code is more about quickly extracting specific columns, while yours is doing more detailed word analysis across the whole file.
"
