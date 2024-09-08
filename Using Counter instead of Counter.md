Using Counter instead of Counter

From Gislene:

Instead of manually counting each word by looping through the list, You can use a built-in Python tool called Counter.
In finding the top 30 words you were manually finding the most common words one by one, 
which was slowing things down. I swapped that out for the function in Counter that directly gives the top 30 most common words. This way, we get the same result with less code and effort.
 
I added a little function to clean up the text before counnting the words. 
This makes sure everything is lowercase and removes any unwanted characters like hyphens or underscores.
 
To help you more, you can definitely find information about these commands on the official Python website.
 
 
Functions Python Docs here:
https://docs.python.org/3/library/functions.html
 
Python Standard Library
 https://docs.python.org/3/library/index.html
 
 
The Counter class is part of the collections module of the Python Standard Library.
 
 
Here is the Os :  https://docs.python.org/3/library/os.html
 
 
String methods like isalpha() (checking if characters are alphabetic) and lower() 
(converting strings to lowercase) are part of Python’s string handling here :  https://docs.python.org/3/library/stdtypes.html#string-methods