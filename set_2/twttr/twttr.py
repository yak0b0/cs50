def main():
    txt_input = input("Input: ")
    txt_changed = twtr_txt(txt_input)
    print("Output:", txt_changed)


def twtr_txt(txt_to_change):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for letter in txt_to_change:
        for vowel in vowels:
            if letter == vowel:
                txt_to_change = txt_to_change.replace(letter, "")
    return txt_to_change


main()
