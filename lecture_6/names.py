name = input("What is your name? ")


with open("lecture_6/names.txt", "a") as file:
    file.write(f"{name}\n")
