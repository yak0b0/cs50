from pyfiglet import Figlet
import random
import sys


def main():
    try:
        figlet = Figlet()
        list_of_fonts = figlet.getFonts()
        if check_command() == False:
            raise SystemError
        if len(sys.argv) == 1:
            font = random.choice(list_of_fonts)
        else:
            if font_checker(sys.argv[2]) == False:
                raise SystemError
            if (sys.argv[1] == '-f') or (sys.argv[1] == '--font'):
                font = sys.argv[2]
            else:
                raise SystemError
        user_txt = input("Input:")
        font_berker(font, user_txt)
    except SystemError:
        sys.exit("Invalid usage")


def check_command():
    if (len(sys.argv) == 1) or (len(sys.argv) == 3):
        return True
    else:
        return False


def font_berker(font_output, text):
    giglet = Figlet()
    giglet.setFont(font=font_output)
    print(giglet.renderText(text))


def font_checker(font_name):
    biglet = Figlet()
    list_of_fonts2 = biglet.getFonts()
    name_appears = 0
    for name in list_of_fonts2:
        if name == font_name:
            name_appears = 1
    if name_appears == 1:
        return True
    else:
        return False


main()
