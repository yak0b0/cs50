class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


# super() is a way of accessing a classes parent class
# .__init__ is reffering to that classes initalization method?
# wizard is taking care of the names :D


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Snape", "Defense Against the Dark Arts")

# operator overloading
# + does not have to equal addition, for example concatination
