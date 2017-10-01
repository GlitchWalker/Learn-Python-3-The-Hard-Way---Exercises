## defines function add with 2 arguments called a and b
def add(a, b):
    ## prints the text
    print(f"ADDING {a} + {b}")
    ## adds a + b, then replaces called function with result
    return a + b

## defines function subtract with two expected arguments
def subtract(a, b):
    ## prints text
    print(f"SUBTRACTING {a} - {b}")
    ## subtracts b from a then replaced called function with result
    return a - b

## defines function multiply with two expected arguments
def multiply(a, b):
    ## prints text
    print(f"MULTIPLYING {a} * {b}")
    ## multiplies a by b, then replaces called function with result
    return a * b

## defines function multiply with two expected arguments
def divide(a, b):
    ## prints text
    print(f"DIVIDING {a} / {b}")
    ## divides a by b, then replaces the called function with result
    return a / b

## prints text
print("Let's do something with just functions!")

## defines variable age as the result of called add function acting on these two arguments
age = add(30, 5)
## defines height as result of function subtract acting on arguments
height = subtract(78, 4)
## defines weight as the result of called multiply function acting on arguments
weight = multiply(90, 2)
## defines divide as the result of called divide function acting on arguments
iq = divide(100, 2)

## prints text with variables inline
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# a puzzle for the extra credit, type it in anyway.
## prints text
print("Here is a puzzle.")
## following I have provided a long-hand summary of this
what = add(age, subtract(height, multiply(weight, divide(iq, 4))))

print("That becomes: ", what, "Can you do it by hand?")

## beginning of my attempt to unravel above equation
what2 = divide(iq, 8)
what2 = multiply(weight, what2)
what2 = subtract(height, what2)
what2 = add(age, what2)


print("This is my attempt at creating", what2, "I hope it works")

what3 = float(input("Give me a number"))
what3 = subtract(what3, divide(what3, add(what3, subtract(what3, multiply(what3, what3)))))

print("This is my attempt at creating my own puzzle:", what3, "So there you go.")