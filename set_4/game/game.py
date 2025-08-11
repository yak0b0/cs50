import random


def main():
    level_bg = level_get()
    game(level_bg)


def level_get():
    while True:
        try:
            level_input = input("Level: ")
            if int(level_input) <= 0:
                raise ValueError
            break
        except ValueError:
            continue
    return int(level_input)


def game(level):
    rand_numb = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError
            if guess > rand_numb:
                print("Too large!")
            elif guess < rand_numb:
                print("Too small!")
            if guess == rand_numb:
                print("Just right!")
                exit()
        except ValueError:
            continue


main()
