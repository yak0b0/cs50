students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for person in sorted(gryffindors, key=lambda s: s["name"]):
    print(person["name"])


students_2 = ["Hermione", 'Harry', "Ron"]

gryffindors_2 = [{"name": student, "house": "Gryffindor"}
                 for student in students_2]

print(gryffindors_2)

gryffindors_3 = {student: "Gryffindor" for student in students_2}

print(gryffindors_3)

for i in range(len(students_2)):
    print(i+1, students_2[i])


# ENUMERATRE

print("Now we will use the enumerate function")
print()

for i, student in enumerate(students_2, start=1):
    print(i, student)
