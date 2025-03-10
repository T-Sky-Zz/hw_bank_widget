from typing import Iterator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""

    filtered_transactions = list(filter(lambda x: x.get("currency_code", {}) == currency, transactions_list))
    if not filtered_transactions:
        raise ValueError("Транзакция не найдена")
    for item_list in filtered_transactions:
        yield item_list


def transaction_descriptions(transactions_list: list[dict]) -> Iterator:
    """Функция принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""

    for item_list in transactions_list:
        for item in item_list:
            if item == "description":
                # print(item_list["description"])
                yield item_list["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999"""

    if start >= stop or start == 0 or len(str(start)) > 16 or len(str(stop)) > 16:
        raise ValueError("Введен неверный диапазон")
    else:
        for number in range(start, stop + 1):
            card_number = "0" * (16 - len(str(number))) + str(number)
            yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


# if __name__ == "__main__":
#     for card_number in card_number_generator(0, 10):
#     # for card_number in card_number_generator(3, 10):
#
#         print(card_number)
