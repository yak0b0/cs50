count = 3
while count != 0:
    print("meow")
    count = count - 1


count = 0
while count < 3:
    print("bark")
    count = count + 1


for _ in range(3):  # remember that indexes are from 0, so here 0,1,2 (not 3)
    print("bubble")

print("meow\n"*3, end='')


while True:
    number = int(input("What's n? "))
    if number > 0:
        break


for _ in range(number):
    print("Prrrr")


def main():
    el_primo = get_number()
    meow(el_primo)


def meow(n):
    for _ in range(n):
        print("Meowwwww!")


def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n


main()
