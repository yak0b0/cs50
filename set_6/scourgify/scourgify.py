import sys
import csv


def main():
    check_command()
    convert()


def check_command():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        txt_input = sys.argv[1]
        txt_output = sys.argv[2]
        if (not txt_input.endswith(".csv")) or (not txt_output.endswith(".csv")):
            sys.exit("Not a CSV file")
    try:
        bongo = open(f"{txt_input}")
        bongo.close()
    except FileNotFoundError:
        sys.exit(f"Could not read {txt_input}")


def convert():
    txt_input = sys.argv[1]
    txt_output = sys.argv[2]
    names = []
    homes = []
    with open(f"{txt_input}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row["name"])
            homes.append(row["house"])

    with open(f"{txt_output}", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        # so here we needed to find a way to make houses iterable, because i messed up opsie daisy
        for i in range(len(names)):
            name = names[i]
            home = homes[i]
            part_of_name = name.split(",")
            if len(part_of_name) == 2:
                last_name = (part_of_name[0].strip())
                first_name = (part_of_name[1].strip())
            writer.writerow(
                {"first": first_name, "last": last_name, "house": home})


if __name__ == "__main__":
    main()
