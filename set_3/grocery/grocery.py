def grocer():
    list = []
    while True:
        try:
            item_unready = input()
            item = item_unready.strip().upper()
            in_list = False
            for items in list:
                if item == items["name"]:
                    in_list = True
                    items["count"] = items["count"] + 1
            if in_list == False:
                list.append({"count": 1, "name": f"{item.upper()}"})
        except EOFError:
            break
    # had to use ai to understand this part
    sorted_list = sorted(list, key=get_name)
    for stuff in sorted_list:
        print(stuff["count"], stuff["name"])


def get_name(item):
    return item["name"]


grocer()
