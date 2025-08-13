import sys
import csv
from tabulate import tabulate


def main():
    check_command()
    bingo = check_table()
    print(tabulate(bingo, headers="keys", tablefmt="grid"))


def check_command():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        txt = sys.argv[1]
        if not txt.endswith(".csv"):
            sys.exit("Not a CSV file")
    try:
        bongo = open(f"{txt}")
        bongo.close()
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_table(fileng=sys.argv[1]):
    with open(f"{fileng}") as file:
        reader = csv.DictReader(file)
        pizza_table = []
        for row in reader:
            pizza_table.append(row)
        return (pizza_table)


if __name__ == "__main__":
    main()
