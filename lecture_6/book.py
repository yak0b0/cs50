def main():
    with open("lecture_6/alice.txt", "r", encoding='utf-8') as f:
        contents = f.readlines()

    chapter1 = contents[52:270]
    with open("lecture_6/chapter1.txt", "w", encoding="utf-8") as f:
        f.writelines(chapter1)


main()
