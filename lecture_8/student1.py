class Student:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod  # without having a student object in my universe already
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    print(Student.get())


if __name__ == "__main__":
    main()


# inheritance, other classes can inherit methods etc.
