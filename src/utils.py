import json
# import os
from typing import Any


def create_list_from_j_file(path: str) -> Any :
    """функцию, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)
            print(type(data))
            return data
    except json.JSONDecodeError:
        return []
    except TypeError:
        return []
    except FileNotFoundError:
        return []


# if __name__ == "__main__":
#     path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#     print(create_list_from_j_file(path))
