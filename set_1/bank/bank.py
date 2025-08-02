def main():
    greeting = input("Greeting: ")
    if is_hello(greeting) == 2:
        print("$0")
    elif is_hello(greeting) == 1:
        print("$20")
    else:
        print("$100")


def is_hello(string):
    string_ready = string.lower().strip()
    if string_ready.startswith("hello"):
        return 2
    elif string_ready.startswith("h"):
        return 1
    else:
        return 0


main()
