import sys
import requests
import json


def main():
    number_of_btc = check_command()
    get_btc_price(number_of_btc)


def check_command():
    try:
        if len(sys.argv) != 2:
            raise SystemError
        if float(sys.argv[1]):
            number = float(sys.argv[1])
        return number
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except SystemError:
        sys.exit("Missing command-line argument")


def get_btc_price(btc_amount):
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=MY_API_KEY :)"
        )
        response_json = response.json()
        btc_price_usd = response_json['data']['priceUsd']
        final_price = float(btc_price_usd) * btc_amount
        print(f"${final_price:,.4f}")
    except requests.RequestException:
        sys.exit("Request Errir")


main()
