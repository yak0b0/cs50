class Student:
    ...  # .. a validplacerholder
    # classes come with certain methods - functions that you can define :)

    def __init__(just_created, name, house):  # instance method - dunder method?
        # house with = None, becomes optional
        just_created.name = name
        just_created.house = house  # we call just_created - SELF okay bro '_+)
        # just_created.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house  # why do we add the _?

    # def charm(self):
    #    match self.patronus:
    #        case "Stag":
    #            return "🦌"
    #        case "Dog":
    #            return "🐶"
    #        case "Otter":
    #            return "🦦"
    #        case _:
    #            return "🧙‍♂️"


def main():
    student = get_student()
    # you can still access tuples like lists
    # if student[0] == "Padma":
    # ' tuple' object does not support item assignment
    #    student[1] = "Ravenclaw"
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"
    # variables named name/house (instance variable)
    # print(f"{student.name}, from {student.house}")
    # print("Expecto Patonum!")
    # print(student.charm())
    # student.house = "Humber Four, Privet Drive" testing getter/setter functions
    # :) - it is meant to be private, but it is a honor system student._house = "Number Four, Privet Drive"
    print(student)


def get_student():
    # here we are creating an object, we are using the blueprint to build a object (instance)
    # storing atributes in it
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    # passing in arguments to the Class funciton?!
    # treating class as a funciton # CONSTRUCTOR CALL
    return Student(name, house)


# () - will return a tuple
# tuple is a data structure in python
# it is a collection of values
# it is inmutable - you can't change the values
# classes are blueprints for data
# they allow you to create your own objects and data
# anytime you use a program you create an object
# they are mutable but, you can make them immutable
# properties, is an attribute with even more defence mechanicsms
# @property
# decorators, functions that modify the properties of other functions?
if __name__ == "__main__":
    main()
