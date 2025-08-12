import csv
import numpy as np
from PIL import Image


def main():
    with open("lecture_6/views.csv", "r") as views, open("lecture_6/analysis.csv", "w", newline="") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(
            analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = calculate_brightness(
                f"lecture_6/{row['id']}.jpeg")
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return round(brightness, 2)


main()

#        for row in reader:
#            brightness = calculate_brightness(f"lecture_6/{row['id']}.jpeg")
#            writer.writerow(
#                {
#                    "id": row["id"],
#                    "english_title": row["english_title"],
#                    "japanese_title": row["japanese_title"],
#                    "brightness": (round(brightness, 2))
#                }
#            )
