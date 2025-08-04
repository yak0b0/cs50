def main():
    gas_tank_amount = fraction()
    print(gas_tank_amount)


def fraction():
    while True:
        try:
            txt = input("Fraction: ")
            x, y = txt.split(sep="/")
            x, y = int(x), int(y)
            if x > y or x < 0 or y < 0:
                raise ValueError()
            division = x/y
            perc = round(division, 2) * 100
            if 99 <= perc <= 100:
                return "F"
            elif 0 <= perc <= 1 or (x == 0 and y != 0):
                return "E"
            else:
                return (str(int(perc)) + "%")
        except (ValueError, ZeroDivisionError):
            continue


main()
