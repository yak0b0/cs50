import sys
import os.path
from PIL import Image
from PIL import ImageOps


def main():
    img_in, img_out = check_command()
    give_tshirt_to_file(img_in, img_out)


def check_command():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    image_input = sys.argv[1]
    image_output = sys.argv[2]

    if correct_extension(image_input, image_output) == False:
        sys.exit("Invalid input")

    try:
        with open(f"{image_input}") as file:
            pass
    except FileNotFoundError:
        sys.exit("File not found bozo")

    return image_input, image_output


def correct_extension(file_name1, file_name2):
    ready_name1 = str(file_name1).lower()
    ready_name2 = str(file_name2).lower()
    root1, ext1 = os.path.splitext(ready_name1)
    root2, ext2 = os.path.splitext(ready_name2)
    if ext2 != ext1:
        return False
    list_of_ext = ['.jpg', '.jpeg', '.png']
    for extension in list_of_ext:
        if extension == ext1:
            return True
    return False


def give_tshirt_to_file(file_root, output_file):
    image = Image.open(f"{file_root}")
    image = ImageOps.fit(image, size=(
        600, 600), bleed=0.0, centering=(0.5, 0.5))
    shirt = Image.open("set_6/shirt/shirt.png")
    image.paste(shirt, (0, 0), mask=shirt)
    image.save(f"{output_file}")


if __name__ == "__main__":
    main()
