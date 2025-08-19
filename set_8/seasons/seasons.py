from datetime import date
import sys
import re
import inflect


def main():
    peepee = input("Date of Birth: ")
    piipii = get_date(peepee)
    days = get_amount_o_days(piipii)
    ready_txt = calculate_mins(days)
    print(ready_txt)


def get_date(pingo):
    try:
        year, month, day = pingo.split("-")
        user_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    except TypeError:
        sys.exit("Invalid date")
    return user_date


def get_amount_o_days(inpt_data):
    user_date = inpt_data
    current_date = date.today()
    difference = current_date - user_date
    regex = r"\d+(?= days)"
    days = int(re.search(regex, str(difference)).group())
    return days


def calculate_mins(days):
    p = inflect.engine()
    minutes = days*24*60
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
