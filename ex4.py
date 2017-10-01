# This sets cars to 100
cars = 100
# This sets the space in a car to 4
space_in_a_car = 4
# This sets the drivers to 30
drivers = 30
# This sets the passengers to 90
passengers = 90
# This sets cars_not_driven to the answer to number in variable cars minus number in variable drivers
cars_not_driven = cars - drivers
# This sets cars_driven equal to the number set in variable drivers
cars_driven = drivers
# This sets carpool_capacity to the number set in cars_driven multiplied by the number set in space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# This sets average_passengers_per_car to the answer to number set in passengers divided by the number set in cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

## Exercise 4 task:
## This first line means it is going to display the last line(s) of code which caused the failure
# Traceback (most recent call last):
## This second line explains that it was in the file ex4.py, on line 8, in the default module
#   File "ex4.py", line 8, in <module>
## This next line displays the actual line that failed (i.e. line 8)
#       average_passengers_per_car = car_pool_capacity / passenger
## This line explains what the problem was, that the variable was not defined.
# NameError: name 'car_pool_capacity' is not defined
## Looking at the original code, the variable is actually 'carpool_capacity'...
## He made a typo and accidentally added another underscore between 'carpool'!
## I also made a typo and forgot a line!