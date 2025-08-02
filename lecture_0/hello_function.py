def main():
    name = input("What's your name? ")
    hello(name)
    hello()


def hello(to="world"):  # the name of my paramater "to"
    print(f"Hello, {to}")


main()  # kinda like in c++
