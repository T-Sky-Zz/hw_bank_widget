from typing import Dict, Iterator, Union


def filter_by_currency(transactions_list: list[dict], currency: str) -> Iterator:
    """Функция должна возвращать итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной (например, USD)"""

    if not transactions_list:
        return "Список транзакций пуст"
    if not list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions_list)):
        return "Транзакция не найдена"
    for item_list in filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions_list):
        yield item_list


def transaction_descriptions(transactions_list):
    """ генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""

    if not transactions_list:
        return "Список транзакций пуст"
    for item_list in transactions_list:
        for item in item_list:
            if item == "description":
                # print(item_list["description"])
                yield item_list["description"]



if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    # ============
    # usd_transactions = filter_by_currency(transactions, "sdf")  # StopIteration: Транзакция не найдена
    # usd_transactions = filter_by_currency([], "USD")  # StopIteration: Список транзакций пуст
    # usd_transactions = filter_by_currency(transactions, "USD")
    #
    # for _ in range(2):
    #     print(next(usd_transactions))
    # ============

    # descriptions = transaction_descriptions(transactions)
    # for _ in range(5):
    #     print(next(descriptions))

# >>> Перевод организации
#     Перевод со счета на счет
#     Перевод со счета на счет
#     Перевод с карты на карту
#     Перевод организации
# ============


def card_number_generator(start: int, stop: int) -> str:
    """ генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""

    for number in range(start, stop + 1):
        card_number = "0" * (16 - len(str(number))) + str(number)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


if __name__ == "__main__":
    for card_number in card_number_generator(17, 21):
        print(card_number)

# 0000 0000 0000 0017
# 0000 0000 0000 0018
# 0000 0000 0000 0019
# 0000 0000 0000 0020
# 0000 0000 0000 0021
