def main():
    unconverted_time = input("What time is it? ")
    converted_time = convert(unconverted_time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    if 12 <= converted_time <= 13:
        print("lunch time")
    if 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours) + (1/60*int(minutes)))


if __name__ == "__main__":
    main()
