## Defines function "cheese_and_crackers" as well as defining arguments it expects
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    ## Prints text with {cheese_count} inline
    print(f"You have {cheese_count} cheeses!")
    ## Prints text with {boxes_of_crackers} inline
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    ## Prints text
    print("Man that's enough for a party!")
    ## Prints text and does line break
    print("Get a blanket. \n")

def my_questions():

    global food_name
    global food_number
    global drink_name
    global drink_number
    global person
    global person_case

    food_name = "Pizza"
    food_number = 2
    drink_name = "Pepsi"
    drink_number = 4
    person = "I"
    person_case = "I am"


def questions():

    global food_name
    global food_number
    global drink_name
    global drink_number
    global person
    global person_case

    food_name = input("What is your favourite food?\n>")
    food_number = input(f"What is your ideal amount of {food_name}?\n>")
    drink_name = input("What is your favourite drink?\n>")
    drink_number = input(f"What is your ideal amount of {drink_name}?\n>")
    person = "You"
    person_case = "You are"

def blank():
    
    global food_name
    global food_number
    global drink_name
    global drink_number
    global person
    global person_case

    food_name = "food_name"
    food_number = "food_number"
    drink_name = "drink_name"
    drink_number = "drink_number"
    person = "person"
    person_case = "person_case"

def answers(*args):

    print("So...\n")
    arg1, arg2, arg3, arg4 = args

    print(f"{person} like {arg1}.")
    print(f"{person} prefer to have {arg2} number of {arg1}.")
    print(f"{person} like {arg3}.")
    print(f"{person} prefer to have {arg4} number of {arg3}.")
    print(f"{person_case} a fat fuck.")

def addition(*args):

    arg1, arg2 = args
    arg1 = int(arg1)
    arg2 = int(arg2)
    numbers_total = arg1 + arg2

    print(f"When you add the amounts together, {arg1} plus {arg2} equals {numbers_total}")

## Prints text
print("We can just give the function numbers directly:")
## Calls cheese_and_crackers() and provides two arguments; "20" and "30"
cheese_and_crackers(20, 30)

## Prints text
print("OR, we can use variables from our script:")
## Defines variable amount_of_cheese
amount_of_cheese = 10
## Defines variable amount_of_crackers
amount_of_crackers = 50

## Calls function, and passes variables "amount_of_cheese" and "amount_of_crackers"
## As arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

## Prints text
print("We can even do math inside too:")
## Calls function and does the math and passes results as each comma seperated argument
cheese_and_crackers(10 + 20, 5 + 6)

## Prints text
print("And we can combine the two, variable and math:")
## Calls the fuction
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Now we're going to talk about food. In my case,...")
my_questions()
answers(food_name, food_number, drink_name, drink_number)
print("...So, how about you?")

questions()
answers(food_name, food_number, drink_name, drink_number)
addition(food_number, drink_number)

print("\n\n")
print("The function uses this template...")
blank()
answers(food_name, food_number, drink_name, drink_number)

