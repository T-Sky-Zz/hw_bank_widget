import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions_empty_list() -> list[dict]:
    return []


@pytest.fixture
def transactions_input_list() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency_correct(transactions_input_list: list[dict]) -> None:
    """Тестирует ф-цию filter_by_currency на корректное выполнение"""
    generator = filter_by_currency(transactions_input_list, "USD")
    # try:
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    # except StopIteration:
    #     assert "No more transactions"


def test_filter_by_currency_incorrect(transactions_empty_list: list[dict]) -> None:
    """Тестирует ф-цию filter_by_currency на ввод пустого списка"""
    with pytest.raises(ValueError):
        generator = filter_by_currency(transactions_empty_list, "USD")
        next(generator)  # Транзакция не найдена


def test_filter_by_currency_incorrect_curr(transactions_input_list: list[dict]) -> None:
    """Тестирует ф-цию filter_by_currency на ввод валюты не входящей в список"""
    with pytest.raises(ValueError):
        generator = filter_by_currency(transactions_input_list, "EUR")
        next(generator)  # Транзакция не найдена


def test_transaction_descriptions(transactions_input_list: list[dict]) -> None:
    """Тестирует ф-цию transaction_descriptions на корректное выполнение"""
    generator = transaction_descriptions(transactions_input_list)
    # try:
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    # except StopIteration:
    #     assert "No more transactions"


def test_card_number_generator_range() -> None:
    """Тестирует ф-цию card_number_generator на корректное выполнение"""
    generator = card_number_generator(1, 3)
    # try:
    assert next(generator) == "0000 0000 0000 0001"  # type: ignore
    assert next(generator) == "0000 0000 0000 0002"  # type: ignore
    assert next(generator) == "0000 0000 0000 0003"  # type: ignore
    # except StopIteration:
    #     assert "No more transactions"


def test_card_number_generator_error() -> None:
    """Тестирует ф-цию card_number_generator на ввод данных, вызывающих ошибку"""
    with pytest.raises(ValueError):
        generator_start = card_number_generator(3, 1)
        next(generator_start)  # type: ignore
    with pytest.raises(ValueError):
        generator_zero = card_number_generator(0, 5)
        next(generator_zero)  # type: ignore
    with pytest.raises(ValueError):
        generator_stop = card_number_generator(2, 1234567890123456789)
        next(generator_stop)  # type: ignore
    with pytest.raises(TypeError):
        generator_type = card_number_generator(1, "5")  # type: ignore
        next(generator_type)  # type: ignore
