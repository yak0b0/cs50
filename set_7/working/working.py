import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    shimy = r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.search(shimy, s)

    if not match:
        raise ValueError("Invalid input")

    start_hour = int(match.group(1))
    if match.group(2):
        start_min = match.group(2)
    else:
        start_min = "00"
    start_period = match.group(3).upper()
    end_hour = int(match.group(4))
    if match.group(5):
        end_min = match.group(5)
    else:
        end_min = "00"
    end_period = match.group(6).upper()
    start_time_24 = convert_to_24(start_hour, start_period)
    end_time_24 = convert_to_24(end_hour, end_period)
    return f"{start_time_24:02d}:{start_min} to {end_time_24:02d}:{end_min}"


def convert_to_24(hr, am_or_pm):
    hr = int(hr)
    if am_or_pm.upper() == "AM":
        if hr == 12:
            hr = 0
    else:
        if hr != 12:
            hr += 12
    return hr


if __name__ == "__main__":
    main()
