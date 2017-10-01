# This defines what types_of_people means (which is 10 in this case)
types_of_people = 10
# The important part here is the f before the quotation marks. This seems to tell the interpreter to continue interpreting variables like {types_of_people}, rather than typing the variable name verbatim.
# This is also a place that stores a string inside a string
x = f"There are {types_of_people} types of people."

# This defines the variable binary
binary = "binary"
# This defines do_not
do_not = "don't"
# This tells the interpreter not to ignore formatiing even between these quotation marks, then prints the text with the variable name replaced with the variable itself.
# This is also a place that stores a string inside a string
y = f"Those who know {binary} and those who {do_not}."

# This tells the interpreter to print everything inside the variable x
print(x)
# This prints everything in the variable y.
print(y)

# This prints the text with variables replaced as before
# This is also a place that stores a string inside a string
print(f"I said: {x}")
# This prints the text with variables replaced
# This is also a place that stores a string inside a string
print(f"I also said: '{y}'")

# This defines the variable "hilarious" as False
hilarious = False

# This defines the variable joke_evaluation as the text. Note there is no at the beginning, nor is there any text between the curly brackets... 
joke_evaluation = "Isn't that joke so funny?! {}"

# ...This is because format is declared here instead, with the contents of hilarious replacing the previous curly brackets.
# This is also a place that stores a string inside a string
print(joke_evaluation.format(hilarious))

# This is another attempt at a poor joke, defining the variable "w" with the text shown
w = "This is the left side of..."
# As above, but declaring the variable e
e = "a string with a right side"

# This prints the contents of variables w and e beside each other, with no space.
# The reason it does this is because, on strings, + literally places together string_a and string_b
# If a number was defined as a string with str("11"), and other was also defined as str("11")... And they were added together... It would give "1111"
print(w + e)