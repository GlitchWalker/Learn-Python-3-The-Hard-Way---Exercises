# This defines "formatter" as four "spaces" onto which I can pass variables
formatter = "{} {} {} {}"

# This passes 1, 2, 3 and 4 as the four arguments to fill the spaces in formatter
# And prints it
print(formatter.format(1, 2, 3, 4))
# This passes one, two, three and four into the four spaces
# And prints it
print(formatter.format("one", "two", "three", "four"))
# This passes these boolean arguments (and prints it).
# As they are boolean, they do not need quotes.
# Putting quotes will still print it, but it will no longer be a boolean which may break stuff!
print(formatter.format(True, False, False, True))
# This passes itself i.e. "{} {} {} {}" four times and prints it
print(formatter.format(formatter, formatter, formatter, formatter))
# This passes these four arguments, and prints it
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))