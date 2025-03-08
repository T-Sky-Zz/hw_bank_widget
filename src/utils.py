import json
import logging
import os
from typing import Any

from src.external_api import convert_currency

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def create_list_from_j_file(path: str) -> Any:
    """функцию, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        logger.info(f"Поиск JSON-файла по заданному пути: {path}")
        with open(path, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)
            logger.info(f"Функция возвращает список словарей с данными о финансовых транзакциях \n{data}")
            return data
    except json.JSONDecodeError:
        logger.error("Ошибка: Файл пуст")
        return []
    except TypeError:
        logger.error("Ошибка: Файл содержит не список")
        return []
    except FileNotFoundError:
        logger.error("Ошибка: Файл не найден")
        return []


# if __name__ == "__main__":
#     path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#     print(create_list_from_j_file(path))


def get_conversion_amount(transaction: dict) -> float:
    """Функция, принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""
    logger.info("Определение валюты транзакции")
    amount = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    logger.info(f"Валюта: {currency_code}")
    if currency_code == "RUB":
        logger.info(f"Сумма транзакции: {amount} руб.")
        return float(amount)
    elif currency_code in ["USD", "EUR"]:
        result = convert_currency(currency_code, "RUB", amount)
        logger.info(f"Сумма транзакции конвертированная: {amount} руб.")
        return round(result, 2)
    else:
        logger.error("Ошибка: иная валюта транзакции")
        return 0.00


# if __name__ == "__main__":
#     transaction_rub = {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     }
# print(get_conversion_amount(transaction_rub))
#
# transaction_usd = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#         "amount": "8221.37",
#         "currency": {
#             "name": "USD",
#             "code": "USD"
#         }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
# }
# print(get_conversion_amount(transaction_usd))
#
# transaction_cny = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#         "amount": "2182.37",
#         "currency": {
#             "name": "CNY",
#             "code": "CNY"
#         }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
# }
# print(get_conversion_amount(transaction_cny))
