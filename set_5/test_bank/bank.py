def main():
    greeting = input("Greeting: ")
    if value(greeting) == 0:
        print("$0")
    elif value(greeting) == 20:
        print("$20")
    else:
        print("$100")


def value(greeting):
    string_ready = greeting.lower().strip()
    if string_ready.startswith("hello"):
        return 0
    elif string_ready.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
