import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_regex = r"\bum\b"  # word boundary anchor
    list_of_um = re.findall(um_regex, s, re.IGNORECASE)
    counter = 0
    for ums in list_of_um:
        counter += 1
    return counter


if __name__ == "__main__":
    main()
