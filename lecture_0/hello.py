# print function, it prints an argument,
# that the user has to give (input to a function)

# input function, returns the value that the user gives,
# so we can add a variable that will store that value
name = input("What is your name? ")
print("Hello,", name, end='\n')
print("Hello, " + name)
print(f"Hello {name}")  # f string - formatted string
print("Hello", name, sep=", ")
# bug is a mistake in a program
# variable is a container for some value in a program

# parameters, what the function can take
# arguments, what the function is taking
# positional argument follows keyword argument

# how to print double quotes
print("hello, \"friend\"")  # escape character

# string methods :)
name = name.strip()  # remove whitespace from str
print(f"Hello {name}")
name = name.capitalize()  # capitalize user's name
print(f"Hello {name}")
name = name.title()
print(f"Hello {name}")  # title method
name = name.strip().title()  # chaining methods together
print(f"Hello {name}")
first, last = name.split(" ")  # spliting str into two strings
print(f"Hello, {last}")
