import csv

name = input("What is your name? ")
home = input("Where is your home? ")

with open("lecture_6/students2.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
