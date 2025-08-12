def main():
    txt_input = input("Input: ")
    txt_changed = shorten(txt_input)
    print("Output:", txt_changed)


def shorten(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
