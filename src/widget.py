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
        else:
            raise ValueError("Введены неверные данные счета/карты")
    else:
        raise TypeError("Неверный тип данных")

# if __name__ == "__main__":
#     print(mask_account_card("Maestro 1596837868705199"))


def get_date(date: str) -> str:
    """Функция меняет формат даты на ДД.ММ.ГГГГ"""
    if type(date) is str:
        list_date = date.split("-")  # — возвращает список слов в строке

        if list_date[0].isdigit() and date[4] == "-" and date[7] == "-":
            return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
        else:
            raise ValueError("Введены неверные данные")
    else:
        raise TypeError

# if __name__ == "__main__":
#     print(get_date("2024-03-11T02:26:18.671407"))
