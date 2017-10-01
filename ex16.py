# Imports feature argv from package sys
from sys import argv

# Takes name of script it is running in as script and filename as the filename arg passed
script, filename = argv

# My own code to open the file passed as an argument
fileread = open(filename)

# Prints the text and {filename}
print(f"Here are the contents of {filename}:")
# Prints contents of file
print(fileread.read())

fileread.close()

# Prints the text and formatted variable
print(f"We're going to erase {filename}.")
# Prints the text
print("If you don't want to do that, hit CTRL-C (^C).")
# Prints the text
print("If you do want to do that, hit RETURN.")

# Prints ?
input("?")

#Print again
print("Opening the file...")
# Opens {filename} as path to file, in write ("w") mode
# Then passes the "file object" as the variable contents
# The "w" means we are opening the file so we can write to it
target = open(filename, 'w')

# Prints text
# print("Truncating the file. Goodbye!")
# Uses truncate (delete everything) on {target} (i.e. wipes contents of file object)
target.truncate()

#Prints text
print("Now, I'm going to ask you for three lines.")

# Prints text as prompt for imput, defines line1 with it
line1 = input("Line 1: ")
# Same as above, but to line2
line2 = input("Line 2: ")
# Input of this one goes to line 3.
line3 = input("Line 3: ")

# Prints this text
print("I'm going to write these to the file.")

# Writes line1 to file object defined in target
##target.write(line1)
# Writes a line break to file defined in target
##target.write("\n")
# Writes {line2} to {target} file
##target.write(line2)
# Writes line break to {target} file
##target.write("\n")
# Writes {line3} to {target} file
##target.write(line3)
# Writes line break to {target} file
##target.write("\n")

# Rewrite of previous code for lesson drill:

target.write(f"{line1}\n{line2}\n{line3}\n")


# Prints text
print("And finally, we close it.")
# Closes file object defined in {target}
target.close()

fileread = open(filename)
print(f"Here are the new contents of {filename}:")
print(fileread.read())
fileread.close()