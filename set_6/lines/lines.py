import sys


def main():
    check_command()
    count_lines()


def check_command():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        txt = sys.argv[1]
        if not txt.endswith(".py"):
            sys.exit("Not a python file")
    try:
        bongo = open(f"{txt}")
        bongo.close()
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines():
    file_location = sys.argv[1]
    with open(f"{file_location}", "r") as file:
        contents = file.readlines()
    count = 0
    for line in contents:
        clean_line = line.lstrip()
        if (clean_line) and (not clean_line.startswith("#")):
            count += 1
    print(f"Amount of lines = {count}")


if __name__ == "__main__":
    main()
