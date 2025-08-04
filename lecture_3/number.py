# ValueError, and using try/except

def main():
    y = get_int("What's y? ")
    print(f"y is {y}")
    x = get_int_2()
    print(f"x is {x}")
    x = get_int_3()
    print(f"x is {x}")


def get_int(text):
    while True:
        try:
            x = int(input(f"{text} "))
        except ValueError:
            print("x is not an integer")
        else:
            return x  # will also break out of a loop


def get_int_2():
    while True:
        try:
            return float(input("What is x? "))
        except ValueError:
            print("x is not an float")


def get_int_3():
    while True:
        try:
            return float(input("What is x? "))
        except ValueError:
            pass


main()
