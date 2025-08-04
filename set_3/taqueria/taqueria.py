def burrito():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    try:
        item = input("Item: ")
    except EOFError:
        print("\n")
        exit()
# we are also going to have to strip().title() the txt, because the user might be tapped in the head
# so we are going to try to find the item in the keys in the dict
# using a loop
# except KeyError


burrito()
