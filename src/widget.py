from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскирует номер карты/счета"""

    if type(type_and_number) is str:
        list_str = type_and_number.split(" ")
        number_account_card = list_str[-1]

        if list_str[-1].isdigit() and list_str[0].isalpha():

            if len(list_str[-1]) == 16:
                list_str[-1] = get_mask_card_number(number_account_card)
            elif len(list_str[-1]) == 20:
                list_str[-1] = get_mask_account(number_account_card)
            else:
                raise ValueError("Введены неверные данные номера счета/карты")
                # print("Введены неверные данные номера счета/карты")

            return " ".join(list_str)
        raise ValueError("Введены неверные данные счета/карты")
    raise TypeError("Неверный тип данных")


# if __name__ == "__main__":
#     print(mask_account_card("Maestro 1596837868705199"))


def get_date(input_date: str) -> str:
    """Функция меняет формат даты на ДД.ММ.ГГГГ"""
    if type(input_date) is str:
        if datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f"):
            output_date = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
            return output_date.strftime("%d.%m.%Y")
        raise ValueError("Неверный формат даты")
    raise TypeError


# if __name__ == "__main__":
#     print(get_date("2024-03:26:18.671407"))
