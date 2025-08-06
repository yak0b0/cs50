def main():
    my_function()


def my_function():
    while True:
        try:
            user_input = input("Date: ")
            if check_date_type(user_input) == 1:
                date_type_1(user_input)
                break
            elif check_date_type(user_input) == 2:
                date_type_2(user_input)
                break
        except ValueError:
            continue


def check_date_type(txt_by_user):
    try:
        month, day, year = txt_by_user.split(sep="/")
        return 1
    except ValueError:
        try:
            month_day, year = txt_by_user.split(sep=",")
            month_day, year = month_day.strip(), year.strip()
            month, day = month_day.split(sep=" ")
            return 2
        except ValueError:
            raise ValueError


def date_type_1(txt):
    try:
        month, day, year = txt.split(sep="/")
        day, month, year = int(day), int(month), int(year)
        if (day >= 31) or (day <= 1) or (month >= 12) or (month <= 1) or (year <= 0):
            raise ValueError()
        print(f"{year:04}-{month:02}-{day:02}")
    except ValueError:
        raise ValueError


def date_type_2(txt):
    try:
        month_day, year = txt.split(sep=",")
        month_day, year = month_day.strip(), year.strip()
        month, day = month_day.split(sep=" ")
        month = month.strip().lower().title()
        day, year = int(day), int(year)
        list_of_months = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12}
        if month in list_of_months:
            month = list_of_months[month]
        if (day >= 31) or (day <= 1) or (month >= 12) or (month <= 1) or (year <= 0):
            raise ValueError()
        print(f"{year:04}-{month:02}-{day:02}")
    except ValueError:
        raise ValueError


main()
