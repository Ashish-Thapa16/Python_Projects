
import requests

currencies = ["USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "NZD", "SEK", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "ZAR", "BRL", "MYR", "THB", "PHP", "IDR", "AED", "SAR", "EGP", "ILS", "PLN", "DKK", "HUF", "CZK", "CLP", "COP", "PEN", "MAD", "LKR", "VND", "KWD", "BHD", "OMR", "QAR", "KZT", "RSD", "HRK", "RON", "BGN", "MKD", "LTL", "LVL", "EEK", "ISK", "ALL", "MDL", "MNT", "TWD", "KRW", "BAM", "GEL", "KGS", "UZS"]

def get_exchangeRate(user_base_currency, user_target_currency) :
    url = f"https://api.exchangerate-api.com/v4/latest/{user_base_currency}"
    response = requests.get(url)

    if response.status_code == 200 :
        data = response.json()
        rates = data.get("rates", {})

        if user_target_currency in rates :
            return rates[user_target_currency]
        else :
            print(f"Error: {user_target_currency} not found in rates")

    else :
        print(f"Error: {response.status_code}")
    return None


user_base_currency = input(f"Enter your currency from {currencies}: ").upper()
user_amount = int(input("Enter your amount: "))
user_target_currency = input("Enter the currency you want your amount to be converted: ").upper()


def convertor(user_amount, user_base_currency, user_target_currency) :
    rate = get_exchangeRate(user_base_currency, user_target_currency)
    if rate:
        return rate
    else:
        return None

result = convertor(user_amount, user_base_currency, user_target_currency)
print(result)


    


