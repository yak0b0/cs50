import random


def main():
    difficulty = get_level()
    count = 1
    score = 0
    while count <= 10:
        if equation(difficulty):
            score += 1
        count += 1
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1:
                return 1
            elif level == 2:
                return 2
            elif level == 3:
                return 3
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def equation(diff):
    x = generate_integer(diff)
    y = generate_integer(diff)
    result = x + y
    counting_try = 0
    while counting_try <= 2:
        try:
            user_ans = input(f"{x} + {y} = ")
            if int(user_ans) == result:
                return True
            else:
                raise ValueError
        except ValueError:
            print("EEE")
            counting_try += 1
    print(x, "+", y, "=", result)
    return False


if __name__ == "__main__":
    main()
