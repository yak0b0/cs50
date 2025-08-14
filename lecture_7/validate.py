# what is a regex? regular expression
# it is just a pattern, used to validate data
# some basic regex
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string or just before the newline at the end of a string
# [] set of characters
# [^] complementing the set
# \d decimal digit
# \D not a decimal digit
# \s whitespace char
# \S not a whitespace char
# \w word char - as well as numbers and the underscore
# \ W not a word char
# A | B either A or B
# (...) a group
# (?:...) non-capturing version
import re

email = input("What is your email? ").strip()  # .lower()

# r".+@.+\.{1}.+" - mine
# r".+@.+\.edu" - dmalans first attempt
# r - to tell format that this is a RAAAAW string
# r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$" - second :)
# r"^\w+@\w+\.edu$" - third
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):  # flags
    print("Valid")  # ^^ we could use * instead of ?
else:
    print("Invalid")
# flags in module re
# re.IGNORECASE - ignorecase , case insensitive
# re.MULTILINE - multilans
# re.DOTALL - idk really

# re.match(pattern, string, flags=0) # matches from the begining
# re.fullmatch(pattern, string, flags=0) # matches from both sides
