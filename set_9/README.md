# Currency converter

#### Video Demo:

<https://www.youtube.com/watch?v=VYTyEjRje64>

#### Description:

I created this program because I really liked using an API during the set_4 `bitcoin.py` excercise. It is a simple currency converter that uses real-time exchange rates from **ExchangeRate-API**. (*Well maybe not that real-time since the free plan only allows daily updates ;P*)

The program checks if the user entered input is a valid **ISO 4217** code using a set of ~160 curriencies fetched from the API

It then retrieves a conversion rate for a currency pair ("USD", "PLN") via the ExchangeRate-API

It then gives the user the choice to exit the program or continue with a specified amount.

My program tightly handles Errors, not allowing the user to mess up anywhere.

##### Description of functions

- `get_valid_currencies()`: Fetches a set of valid currency codes from the API

- `is_currency_valid(currency, currency_set)`: Validates a currency against the set, raising a ValueError for invalid codes. Handles case-insensitive inputs (e.g., "usd" is valid)

- `convertion_from_to(currency_from, currency_to)`: Retrieves the conversion rate for a currency pair from the API

- `convert_amount_by_rate(amount, rate)`: Converts an amount using the rate, raising a ValueError for negative or non-numeric inputs

- `main()`: Manages user input, validation, rate display, and amount conversion, with a loop to handle the conversion decision

##### Testing

The project includes pytest tests to ensure functionality:

- Empty currency input (raises a ValueError)

- Invalid currency code (raises a ValueError)

- Valid currency code (returns True)

- Case-insensitive input (e.g., "gbp" vs. "GBP")

- Invalid amount inputs (negative or non-numeric, raises a ValueError)
