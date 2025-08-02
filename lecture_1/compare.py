x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:  # slow
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


if x > y or y > x:  # faster
    print("x is not equal to y")
else:
    print("x is equal to y")


if x != y:  # the fastest
    print("x is not equal to y")
else:
    print("x is equal to y")
