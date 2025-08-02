def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if check_answer(answer):
        print("Yes")
    else:
        print("No")


def check_answer(user_answer):
    if user_answer.strip().lower() == "forty two" or user_answer.strip().lower() == "forty-two" or (user_answer).strip() == str(42):
        return True
    else:
        return False


main()
