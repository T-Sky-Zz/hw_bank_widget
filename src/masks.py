import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты в формате XXXX XX** **** XXXX"""
    logger.info(f"Количество введенных символов номера карты {card_number} должно быть равно 16")
    if len(card_number) != 16:
        logger.error("Введено неверное количество символов номера карты")
        raise ValueError("Введено неверное количество символов номера карты")

    logger.info(f"Номер карты выводится в формате: {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


# if __name__ == "__main__":
#     logger.info("Маскируем номер карты")
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_card_number("7000792289606361123"))


def get_mask_account(acc_number: str) -> str:
    """Функция маскирует номер счета в формате **XXXX"""
    logger.info(f"Количество введенных символов номера карты {acc_number} должно быть равно 20")

    if len(acc_number) != 20:
        logger.error("Введено неверное количество символов номера счета")
        raise ValueError("Введено неверное количество символов номера счета")

    logger.info(f"Номер счета выводится в формате: **{acc_number[-4:]}")
    return f"**{acc_number[-4:]}"


# if __name__ == "__main__":

#     logger.info("Маскируем номер счета")
#     print(get_mask_account("73654108430135874305"))
#     print(get_mask_account("73654108430135874305123"))
