# libraries are generally pieces of code that other people have written that you can use in your program

# or code that you have written before

# module is a library that has one or more functions written in it,

# the purpose of a library (or a module) is to encourage re=usability of code

# random library!

# from random import choice # if you are importing just one function

import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
