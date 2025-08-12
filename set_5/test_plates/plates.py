def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if plate_length(s) and first_two_letters(s) and check_if_alphanumeric(s) and check_numbers(s):
        return True
    else:
        return False


def plate_length(ss):
    if len(ss) < 2 or 6 < len(ss):
        return False
    else:
        return True


def first_two_letters(sss):
    if (sss[0].isalpha() and sss[1].isalpha()):
        return True
    else:
        return False


def check_if_alphanumeric(ssss):
    if not ssss.isalnum():
        return False
    else:
        return True


# got stuck on this function, had to use AI to help out however I now understand how it works
def check_numbers(sssss):
    number = False
    for i in range(len(sssss)):
        character = sssss[i]
        is_digit = False
        if character.isnumeric():
            is_digit = True
        if is_digit:
            if not number and character == '0':
                return False
            number = True  # this helps the computer know that one number has been found
        elif number:  # then this part helps us eliminate cases where we have numbers and then letters
            is_letter = False
            if character.isalpha():
                is_letter = True
            if is_letter:
                return False
    return True


if __name__ == "__main__":
    main()
