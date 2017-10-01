name = 'Glitch P. Walker'
age = 29 # not a lie
height = 74 # inches
weight = 250 # lbs
eyes = 'Blue/Green'
teeth = 'Whiteish'
hair = 'Brown'

# This line multiplies the height by 2.54 to give the height in cm
height_metric = height * 2.54
# This second line converts it from a float to an integer so it reads better)
height_metric = int(height_metric)

# This line multiplies the weight by 0.4 to give the weight in kg, and the second line does the same
weight_metric = weight * 0.45359237
weight_metric = int(weight_metric)

# This line divides the weight by 14 to give the number of stone 
weight_stone = weight / 14
# Stone isn't divided into decimal, but the leftover lb are displayed instead. This gets the stone integer
weight_stone = int(weight_stone)
# And this gets the remainder for the lb value
weight_stone_pounds = weight % 14

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"(That's {height_metric} cm.)")
print(f"He's {weight} pounds heavy.")
print(f"(That's {weight_metric} kg).")
print(f"(or {weight_stone} st {weight_stone_pounds} lb).")
print("Actually that's bloody heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# I tried using the round function in this, although it didn't work with the stone value as obviously it rounds it up!!
# So I changed it back to a int()