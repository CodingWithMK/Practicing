import requests

API_KEY = 'Enter your API key here.'
BASE_URL = "Enter your request url here."

CURRENCIES = ["EUR", "TRY", "USD", "CAD", "AUD"]

def convert_currencies(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print("Invalid currency. Try again!")
        return None
    
while True:
    
    base = input("Enter base currency (q for quit): ").upper()

    if base == 'Q':
        break
    
    data = convert_currencies(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
