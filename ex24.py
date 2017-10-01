## These three print the text
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

## This makes the contents of "poem" a multi-line string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

## Prints text
print("--------------")
## Prints the contents of variable "poem"
print(poem)
## Prints text
print("--------------")

## Performs equation and makes the result the contents of five
five = 10 - 2 + 3 - 6
## Prints text with in-line variable
print(f"This should be five: {five}")

## Starts a function/method definition; expecting 1 argument when called, names it "started"
def secret_formula(started):
    ## Defines local variable jelly_beans as the "started" variable multiplied by 500
    jelly_beans = started * 500
    ## Defines local variable jars as the "jelly_beans" variable divided by 1000
    jars = jelly_beans / 1000
    ## Defines local variable crates as "jars" divided by 100
    crates = jars / 100
    ## Replaces the function called in the code with 3 values from jelly_beans,
    ## jars and crates.
    return jelly_beans, jars, crates


## Defines variable "start_point" as 10000
start_point = 10000
## Defines beans, jars and crates as whatever is returned from
## the secret_formula function (with start_point passed as arg in that function)
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string

## prints text, with function .format acting on string passing arg start_point
## This has effect of replacing {} with the value of start_point
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
## This also formats any curly brackets, but this time the arguments (variable names)
## are delivered inline
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

## This (re)defines "start_point" as start_point divided by 10
start_point = start_point / 10

## Prints text
print("We can also do that this way:")
## defines variable formule by calling secret_formula passing start_point as argument
formula = secret_formula(start_point)
## Performs .format function on string, passing the multiple arguments of formula
## as each of the arguments to replace curly brackets with respectively.
print("We'd have {} beans, {} jars and {} crates.".format(*formula))