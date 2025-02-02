def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED') и возвращает
    новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
    """

    return [transaction for transaction in transactions if transaction["state"] == state]


if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(transactions, state="EXECUTED"))


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание (reverse: bool = True)).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    if reverse:
        sorted_transactions = sorted(transactions, key=lambda transaction: transaction["date"], reverse=True)
    else:
        sorted_transactions = sorted(transactions, key=lambda transaction: transaction["date"])
    return sorted_transactions


if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(transactions))
