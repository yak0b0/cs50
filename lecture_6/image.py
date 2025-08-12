from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("lecture_6/fe.jpg") as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("lecture_6/fefe.jpg")


main()
