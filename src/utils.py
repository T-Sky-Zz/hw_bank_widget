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
            for operation in data:
                operation_amount = operation.pop("operationAmount") if operation.get("operationAmount", {}) else {}
                operation["amount"] = operation_amount.get("amount")
                operation["currency_name"] = operation_amount.get("currency", {}).get("name")
                operation["currency_code"] = operation_amount.get("currency", {}).get("code")
            logger.info(f"Файл прочитан, функция возвращает список словарей с данными о транзакциях \n{data}")
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
    amount = float(transaction["amount"]) if transaction.get("amount") else 0.00
    currency_code = transaction.get("currency_code")
    logger.info(f"Валюта: {currency_code}")
    if currency_code == "RUB":
        logger.info(f"Сумма транзакции: {amount} руб.")
        return amount
    elif currency_code in ["USD", "EUR"]:
        result = convert_currency(currency_code, "RUB", amount)
        logger.info(f"Сумма транзакции конвертированная: {amount} руб.")
        return round(result, 2)
    else:
        logger.error("Ошибка: иная валюта транзакции")
        return 0.00


# if __name__ == "__main__":
#     path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#     create_list = create_list_from_j_file(path)
# #     print(create_list)
# #     print("ПОЛУЧАЕМ СУММУ ТРАНЗАКЦИИ")
#     conversion_amount = get_conversion_amount(create_list[-1])
#     print(conversion_amount)
#     print(type(conversion_amount))
