print("#")
print("#")
print("#")
print("")

for _ in range(3):
    print("#")

print("")


def main():
    print_column(3)
    print_column_1(3)
    print_row(4)
    print_square(3)
    print_square_1(4)


def print_column(height):
    for _ in range(height):
        print("#")


def print_column_1(height):
    print("#\n" * height, end="")


def print_row(width):
    print("?" * width)


def print_square(size):
    for i in range(size):  # for each row in square
        for j in range(size):  # for each brick in row
            print("X", end="")  # print brick
        print()


def print_square_1(size):
    for i in range(size):
        print_row(size)


main()
