def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты в формате XXXX XX** **** XXXX"""
    if len(card_number) != 16:
        raise ValueError("Введено неверное количество символов номера карты")
    if type(card_number) is not str:
        raise TypeError("Введен неверный тип данных")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(card_number: str) -> str:
    """Функция маскирует номер счета в формате **XXXX"""
    if len(card_number) != 20:
        raise ValueError("Введено неверное количество символов номера счета")
    if type(card_number) is not str:
        raise TypeError("Введен неверный тип данных")
    return f"**{card_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
