import requests
import sys

# this function allows us to get a set of valid codes, which we will use later on in is_currency_valid()


def get_valid_currencies():
    try:
        response = requests.get(
            "https://v6.exchangerate-api.com/v6/MYAPI/codes"
        )
        response_json = response.json()
        list_of_codes = response_json["supported_codes"]
        set_of_codes = set()
        for code_pair in list_of_codes:
            set_of_codes.add(code_pair[0])
        return set_of_codes
    except requests.RequestException:
        sys.exit("Request Error")


# okay so grok advised to me to add a second parameter, to this function, since i was just thinking about adding the set as a global variable
def is_currency_valid(currency, currency_set):
    currency_valid = currency.upper().strip()
    if currency_valid not in currency_set:
        raise ValueError
    else:
        return True

# exchangerate api allows to easily get the converation rate in a forex pair


def convertion_from_to(currency_from, currency_to):
    try:
        response = requests.get(
            f"https://v6.exchangerate-api.com/v6/MYAPI/pair/{currency_from}/{currency_to}"
        )
        response_json = response.json()
        convertion_rate = response_json["conversion_rate"]
        return convertion_rate
    except requests.RequestException:
        sys.exit("Request Error")  # handling request errors

# this function calculates an amount of currency times the rate of that currenct, while checking for Errors


def convert_amount_by_rate(amount, rate):
    amount = float(amount)
    if amount < 0:
        raise ValueError
    return (amount * rate)


def main():
    valid_codes = get_valid_currencies()
    print("--- Welcome to the currency converter program ---")

    try:
        input_currency = input("Input base currency: ").upper().strip()
        is_currency_valid(input_currency, valid_codes)
        convert_currency = input(
            "Input currency to convert to: ").upper().strip()
        is_currency_valid(convert_currency, valid_codes)
    except ValueError:
        sys.exit(
            f"What you provided is not a valid ISO 4217 alpha code for a currency")

    rate = convertion_from_to(input_currency, convert_currency)
    print(
        f"1 {input_currency} is {rate} {convert_currency}")

    decision = "not_decided"
    while decision != "Y" and decision != "N":
        decision = input(
            f"Would you like to convert a certain amount of {input_currency} to {convert_currency}? Y/N: ").upper()
        if decision != "Y" and decision != "N":
            print("Invalid option, choose again")

    if decision == "N":
        sys.exit("Thank you for using the currency converter program")

    else:
        amount = input("Amount: ").strip()
        try:
            converted = convert_amount_by_rate(amount, rate)
        except ValueError:
            sys.exit("Invalid Amount")
        print(f"{amount} {input_currency} = {converted:.3f} {convert_currency}")
        sys.exit("Thank you for using the currency converter program")


if __name__ == "__main__":
    main()
