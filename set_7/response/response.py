import validator_collection


def main():
    email_by_user = input("What's your email address? ")
    is_email = validator_collection.is_email(email_by_user)
    if is_email:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
