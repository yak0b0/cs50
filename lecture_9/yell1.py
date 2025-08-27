def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)  # map :) like in R
    print(*uppercased)


if __name__ == "__main__":
    main()
