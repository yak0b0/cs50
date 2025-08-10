import emoji


def main():
    string_input = input("Input: ")
    emoji_fun(string_input)


def emoji_fun(txt):
    try:
        emoji_txt = emoji.emojize(f"{txt}", language='alias')
    except ValueError:
        print("Error")
    print("Output:", emoji_txt)


main()
