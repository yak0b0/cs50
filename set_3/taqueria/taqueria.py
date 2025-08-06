def burrito():
    dicti = {
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
        count = 0.00
        while True:
            item = input("Item: ")
            changed_item = item.strip().lower().title()
            for item in dicti:
                if changed_item == item:
                    count = float(count) + float(dicti[item])
                    print(f"Total: ${count:.2f}")
    except EOFError:
        print("")
        exit()


burrito()
