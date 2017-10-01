# \t appears to tab any text in the string to the right
tabby_cat = "\tI'm tabbed in.{}"
# This splits in the middle to a new line, where \n is located
persian_cat = "I\'m {}\non a line."
# This allows the backslash to be on its own
# I guess two slashes stops it confusing it if right next to letter n?
backslash_cat = "I\'m{} cat.".format("\\NYAN\\")

anti_swear = "STOP SWEARING"


# Multi-line string; also, uses \t to tab each line
fat_cat = '''\nI'll do a list:\n\t* Cat food\n\t* Fishies\n\t* Catnip\n\t* Grass\a'''

# These print each of the variables defined above
print(tabby_cat.format(" Mother-fucker\n"), anti_swear)
print(persian_cat.format(tabby_cat))
print(backslash_cat)
print(fat_cat)