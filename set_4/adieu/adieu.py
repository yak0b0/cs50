#   while True:
#        try:
#            item_unready = input()
#            item = item_unready.strip().upper()
#            in_list = False
#            for items in list:
#                if item == items["name"]:
#                    in_list = True
#                    items["count"] = items["count"] + 1
#            if in_list == False:
#                list.append({"count": 1, "name": f"{item.upper()}"})
#        except EOFError:
#            break
#    # had to use ai to understand this part

import inflect


def main():
    p = inflect.engine()
    list_of_names = []
    while True:
        try:
            name = input("Name: ")
            list_of_names.append(name)
        except EOFError:
            print()
            break
    formatted_list = p.join(list_of_names)
    print(f"Adieu, adieu, to", formatted_list)


main()
