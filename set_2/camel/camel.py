def main():
    text_camel = input("camelCase: ")
    text_snake = snake(text_camel)
    print("snake_case:", text_snake)


def snake(text_to_convert):
    copied_text = text_to_convert
    for letter in text_to_convert:
        if letter.isupper():
            lower_letter = letter.lower()
            copied_text = copied_text.replace(letter, f"_{lower_letter}")
    return copied_text


main()
