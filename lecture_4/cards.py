import random

cards = ["jack", "queen", "king"]


def main():
    random.seed(1)
    print(random.sample(cards, k=2))  # without replacements
    print(random.choices(cards, k=2))  # with replacement
    print(random.choice(cards))  # one card
    # changing the weight
    print(random.choices(cards, k=2))  # weights=[60, 30, 10]


main()
