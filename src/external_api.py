import os

import requests
from dotenv import load_dotenv


def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    """Конвертация валюты с помощью внешнего API"""
    load_dotenv()
    apikey = os.getenv('API_KEY')
    headers = {"apikey": apikey}

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    # Отправка GET-запроса к API
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    if response.status_code == 200:
        result_dict = response.json()
        result = result_dict["result"]
        return float(result)
    raise ValueError("Failed to get currency rate")


# if __name__ == "__main__":
#     print(convert_currency("USD", "RUB", 100.00))
