# Prints the text, DOESN'T move to next line...
## print("How old are you?", end=' ')
# ...Meaning the user types an input here right next to the previous print.
# The input function, I am guessing, takes in a use input. Here, it defines the variable.
age = input("How old are you?:")
# Same as before; prints text, doesn't move to next line.
##print("How tall are you? (in cm)", end=' ')
# As before, variable is defined by the user input
height = input("How tall are you? (in cm): ")
# Prints text and keeps it on line
##print("How much do you weigh? (in kg)", end= ' ')
# Weight variable is defined by user input
weight = input("How much do you weight? (in kg) ")

# Spits out the text along with {age}, {height} and {weight} in respective places.
print(f"So, you're {age} years old, {height} cm tall and weigh {weight} kg.")

hobby = input("What do you do in your spare time? ")

music = input("What is your favourite genre of music? ")

print(f"So, you like to do {hobby} in your spare time. That's cool!")
print(f"Yuck! I hate {music}! It sounds terrible!")

x = int(input("Give me the first numbner:"))
y = int(input("Give me the second number:"))

z = x + y

print(f"{x} plus {y} equals {z}!")