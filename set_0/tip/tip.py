def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_d = str(d.removeprefix("$"))
    return float(new_d)


def percent_to_float(p):
    new_p = str(p.removesuffix("%"))
    return float(new_p) * 0.01


main()
