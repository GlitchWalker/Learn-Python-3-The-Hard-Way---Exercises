## this one is like your scripts with argv
# Ths defines a function with a potentially unlimited amount of arguments called args
def print_two(*args):
    #This defines the two args as variables arg1 and arg2 (in effect, putting them both
    # In parenthesis above)
    arg1, arg2 = args
    # This prints out text/variables as we are used to
    print(f"arg1: {arg1}, arg2: {arg2}")

## ok, that *args is actually pointless, we can just do this
# This time the args are defined directly inside the parenthesis
def print_two_again(arg1, arg2):
    # Again, this prints out the strings/variables
    print(f"arg1: {arg1}, arg2: {arg2}")

## This just takes one argument
# This accepts just one argument "arg1", which creates a variable
def print_one(arg1):
    #This prints string/variable
    print(f"arg1: {arg1}")

## This one takes no arguments
# It's a function without any arguments
def print_none():
    # This prints out the string
    print("I got nothin'.")

first_name = input("What is your first name?> ")
second_name = input("What is your second name?\n> ")

race_place = input("What is the preferred ranking you'd want in a race?\n> ")

# Calls the function and provides it two arguments 
print_two(first_name, second_name)
# This also calls the function and provides the two arguments
print_two_again(first_name, second_name)
# This passes just one argument, which is what the function is expecting
print_one(race_place)
# This passes no arguments; again, as the function is expecting
print_none()

