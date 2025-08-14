import re

locations = {"+1": "United States and Canada",
             "+62": "Indonesia",
             "+505": "Nicaragua",
             "+48": "Poland"}


def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{3,4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    capture = match.group("country_code")
    print(f"Your number is from {locations[capture]}")
    if match:
        print(f"Valid")
    else:
        print("Invalid.")


main()
