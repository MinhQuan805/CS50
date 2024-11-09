import json
import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    amount = float(sys.argv[1])
    if amount < 0:
        sys.exit("Number is not a positive number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    rate_USD = o["bpi"]["USD"]["rate"]
    clean_rate_USD = rate_USD.replace(',', '')
    result = amount * float(clean_rate_USD)
    print(f"${result:,.4f}")
except (ValueError, requests.RequestException):
    sys.exit("Command-line argument is not a number")
