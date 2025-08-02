def main():
    text = input()
    text_with_emoji = convert(text)
    print(text_with_emoji)


def convert(txt):
    txt_emoji = txt.replace(":)", "🙂").replace(":(", "🙁")
    return txt_emoji


main()
