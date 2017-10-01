#  This imports the class argv from module sys
from sys import argv

# This defines script and user_name variables from prior command line arguments
script, user_name, password = argv
# This defines the variable "prompt"
prompt = '> '

# This prints the variables inline with text because of f
print(f"Hi {user_name}, I'm the {script} script.")
# This just prints the test
print(f"Your password is {password}.")
print("I'd like to ask you a few questions.")
# The f means it prints the variable for user_name inline with text
# print(f"Do you like me {user_name}?")
likes = input(f"Do you like me {user_name}?\n" + prompt)
# This prompts the user for an input with text from "promp", 
# then defines variable "likes" with it
lives = input(f"Where do you live {user_name}?\n" + prompt)

computer = input("What kind of computer do you have?\n" + prompt)

# This prints the text and inline variables
# print(f"Where do you live {user_name}?")
# This again prompts for input with "prompt" variable, then puts the result in "lives" 
# lives = input(prompt)

# This prints the text
# print("What kind of computer do you have?")

# Prompts user for input with prompt variable, then puts result in "computer"
# computer = input(prompt)

# Three quotation marks means multi-line print
# f Means format variables between {} inline with text
# That prints the likes, lives and computer variables respectively.
# The f is combined before the commas, same as before.
# Only, being  a multi-line string, the f also works multi-line.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")