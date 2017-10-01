# Here's some new strange stuff, remember type it exactly

# This defines days as this string
days = "Mon Tue Wed Thu Fri Sat Sun"
# This defines months. Notice the \n... That causes a line break when it appears
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# This prints the text then string days. Notice they are in a line...
print("Here are the days:", days)
# ...Wheras this prints each day on its own line, thanks to each \n
print("Here are the months:", months)

# The triple quotation marks seem to allow the string to span multiple lines (WYSIWYG)
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like
Even 4 lines if we want, or 5, or 6
Really?
Lets see if it lets me go to six, shall we?
Or seven?
""")