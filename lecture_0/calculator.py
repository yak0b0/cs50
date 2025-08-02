# nesting, function in a function
x = float(input("What's x? "))
y = float(input("What's y? "))

# int() function to turn str to int
# float() function to turn str to float
# round() function to round a number

z = round(x+y)
d = round(x / y, 2)  # 2 as the number of digits we are rounding to
d_no_round = x/y
print(f"{z:,}")
print(d)
print(f"{d_no_round:.2f}")  # f string aproach to rounding


def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))


def square(number):
    return number * number


main()
