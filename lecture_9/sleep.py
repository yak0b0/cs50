# GENERATORS


def main():
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * (i+1)


if __name__ == "__main__":
    main()
