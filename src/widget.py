# import masks
from masks import get_mask_card_number
from masks import get_mask_account


# def mask_account_card(type_and_number: str) -> str:
#     """Функция маскирует номер карты/счета"""
#     list_str = type_and_number.split(" ")  # — возвращает список слов в строке
#     number_account_card = int(list_str[-1])
#     if len(list_str[-1]) > 16:
#         list_str[-1] = masks.get_mask_account(number_account_card)
#     else:
#         list_str[-1] = masks.get_mask_card_number(number_account_card)
#     return " ".join(list_str)


def mask_account_card(type_and_number: str) -> str:
    """Функция маскирует номер карты/счета"""
    list_str = type_and_number.split(" ")  # — возвращает список слов в строке
    number_account_card = int(list_str[-1])
    if len(list_str[-1]) > 16:
        list_str[-1] = get_mask_account(number_account_card)
    else:
        list_str[-1] = get_mask_card_number(number_account_card)
    return " ".join(list_str)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
