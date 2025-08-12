def main():
    txt = input("Fraction: ")
    percentage = convert(txt)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split(sep="/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError()
    if x > y or x < 0 or y < 0:
        raise ValueError()
    division = x/y
    perc = round(division, 2) * 100
    return int(perc)


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
