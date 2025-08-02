def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    if is_even_2(x):
        print("Even")
    else:
        print("Odd")
    if is_even_3(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_even_2(n):
    return True if n % 2 == 0 else False


def is_even_3(n):
    return n % 2 == 0


main()
