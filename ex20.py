# Imports feature argv from module sys
from sys import argv

# defines this script name and input_file as two arguments
script, input_file = argv

# defines function print_all, defines argument f from given argument
def print_all(file):
    # reads file f and prints result to end of file
    print(file.read())

# defines function rewind, with argument defined as f
def rewind(file):
    # seeks back to beginning of file (like a tape)
    file.seek(0)

# defines function print_a_line, expecting 2 args and naming them line_count and f
def print_a_line(line_count, file):
    # prints the number in line_count, and reads the next line of f
    # readline works by scanning for the next (hidden?) \n in the file
    print(line_count, file.readline())

# defines variable current_file as the file object of input_file
current_file = open(input_file)

# prints this text
print("\nFirst let's print the whole file:\n")

# calls print_all function on current_file (prints contents of f)
print_all(current_file)

# prints text
print("\nNow let's rewind, kind of like a tape.\n")

# calls rewind function on current_file (rewinds to beginning of f)
rewind(current_file)

# prints text
print("let's print three lines:\n")

# defines variable current line as 1
current_line = 1
# calls print_a_line function, passing current_line and current_file variables as arguments
print_a_line(current_line, current_file)

# defines variable as current_line plus 1
current_line += 1
# calls function, passing these two variables as arguments
print_a_line(current_line, current_file)

# definesd variable as current_line plus 1
current_line += 1
# calls function, passing these two variables as arguments
print_a_line(current_line, current_file)