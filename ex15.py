# This imports feature argv from package sys
from sys import argv


# This takes its own file name and whatever argument is passed
# To "script" and "filename" respectively
script, filename = argv

# This opens the (hopefully) stream of the filename defined in {filename}
# And passes the result as "txt"
txt = open(filename)

# Prints text with variable formatted inline
print(f"Here's your file {filename}:")
## This is my own addition, this shows what txt without read command prints
## As just "open(filename)" Actually just creates and returns a description
## Of itself. Like describing a DVD itself rather than putting it in a computer
## And reading the data from it.
print(txt)
# This prints the contents of file opened in txt variable as a string
print(txt.read())
# This closes any "open" files. Which is important if we are finished with them.
txt = txt.close
# This is so I can check it has closed the file
print(txt)

# Prints text to user
print("Type the filename again:")
# Prompts input from user, prints "> " and puts results of input in file_again
file_again = input ("> ")

# Opens file_again as file, and txt_again is defined by result
txt_again = open(file_again)

# Prints contents of file opened in txt_again as a string
print(txt_again.read())
txt_again = txt_again.close
# This is so I can check the file has closed
print(txt_again)

# Commands are also called functions and methods!
# It's better to let the user pass the arguments themselves,
# As they have access to auto-complete with tab. Also it stops you
# Getting halfway through the code only to find it doesn't work.