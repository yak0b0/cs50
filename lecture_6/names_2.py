with open("lecture_6/names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

print()
print("^^^ This is one way")
print()

with open("lecture_6/names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())  # canot sort like this

print()
print("^^^ This is one way")
print()

# sorting
names = []

with open("lecture_6/names.txt") as file1:
    for line in file1:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

print()
print("^^^ This is one way")
print()

with open("lecture_6/names.txt") as file2:
    for line in sorted(file2, reverse=True):
        print("Hi,", line.rstrip())
