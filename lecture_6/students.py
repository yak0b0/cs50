import csv
"""
with open("lecture_6/students.csv") as file:
    for line in file:
        row = line.rstrip().split(sep=",")
        print(f"{row[0]} is in {row[1]}")


print()
print("^^^ This is one way")
print()

with open("lecture_6/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(sep=",")
        print(f"{name} is in {house}")

print()
print("^^^ This is one way")
print()


students = []

with open("lecture_6/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

print()
print("^^^ This is one way")
print()

students = []

with open("lecture_6/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


print()
print("^^^ This is one way")
print()
"""
students = []

with open("lecture_6/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


def get_name(student):
    return student["name"]


def get_home(student):
    return student["home"]


# the get_name() function gives us the key on which to sort by
# lambda functions
for student in sorted(students, key=lambda x: x["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")
