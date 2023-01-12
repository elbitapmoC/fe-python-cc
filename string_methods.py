msg = "-------     hello woRLD!     -------------"
# Capitalizaton Methods
print(msg.capitalize())

# Upper case
print(msg.upper())

# Lower case
print(msg.lower())

# If you want more information on a method.
# Add it into ipython: first_name.upper?

# strip - returns a copy of the string w/ the leading and trailing characters removed.
# [] as a parameter, means it's optional
# default: removes white space
# secondary behavior: [-] as a parameter. All -'s would be taken out of the string.
print(msg.strip("- ").upper())

# lstrip - takes away leading(characters on the left) characters
# rstrip - takes away trailing(characters on the right) characters
