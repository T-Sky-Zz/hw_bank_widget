def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты в формате XXXX XX** **** XXXX"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(card_number: str) -> str:
    """Функция маскирует номер счета в формате **XXXX"""
    return f"**{card_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
