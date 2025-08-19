import random


class Hat:

    houses = ["Gryffindor",
              "Hufflepuff",
              "Ravenclaw",
              "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# we are not initializing anything, we are just calling the classes method
Hat.sort("Harry")

# when should you use a class?
# when you are representing a real world entity
# :) :D :L
# class methods, if you are using it once i think?
