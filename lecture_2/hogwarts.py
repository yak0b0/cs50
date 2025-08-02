students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

print(students[0], students[1], students[2])

print(students[0])
print(students[1])
print(students[2])

count = 1
for student in students:
    print(count, ". ", student, sep="")
    count = count + 1


for i in range(len(students)):
    print(i + 1, students[i])


# dictionaries - allow you to associate a key with a values


students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin", }


print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


for student in students:  # only seeing the keys :)
    print(student)


for student in students:  # keys + values
    print(student, "-", students[student])


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" - ")
