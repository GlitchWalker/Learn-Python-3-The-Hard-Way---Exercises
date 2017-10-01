# Prints the text in the brackets
print("Mary had a little lamb.")
# Prints the text in brackets; snow is inserted between the {} using format
print("She took it to a {}.".format('wedding'))
# Prints the text
print("Every time it made a noise.")
# Prints a full-stop 10 times
print("." * 10) # what'd that do?

# Defines end1 to end12
end1 = "S"
end2 = "h"
end3 = "e"
end4 = "k"
end5 = "i"
end6 = "c"
end7 = "d"
end8 = "t"
end10 = "s"
end11 = "f"
end12 = "u"
end13 = "n"
end14 = "g"
end15 = "a"
end16 = "."
end17 = " "

# removing the comma causes a syntax error, as end=' ' is an expression
# these two print each end variable one after another
# the end=' ' prints a space
print(end1 + end2 + end3 + end17 + end4 + end5 + end6 + end4 + end3 + end7, end=" ")
print(end5 + end8 + end10 + end17 + end11 + end12 + end6 + end4 + end5 + end13 + end14 + end17 + end2 + end3 + end15 + end7 + end17 + end5 + end13 + end16)