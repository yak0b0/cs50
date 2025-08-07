import sys
# try:
#    print("Hello, my name is", sys.argv[1], sys.argv[2])
# except IndexError:
#    first_name = input("First name: ")
#    last_name = input("Last name: ")
#    print(f"Hello, my name is {first_name} {last_name}")


# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")


for arg in sys.argv[1:-1]:  # slicing a list
    print("Hello, my name is", arg)
