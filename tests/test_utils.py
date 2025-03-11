import json
from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.utils import create_list_from_j_file, get_conversion_amount


@patch("builtins.open")
@patch("json.load")
def test_create_list_from_j_file_correct(mock_load: Any, mock_open_file: Any) -> None:
    """Тестирует функцию при корректных исходных данных в JSON-файле"""
    mock_open_file.new = mock_open()
    json_list = [{"ind": 159}, {"ind": 741}]
    mock_load.return_value = json_list
    result = create_list_from_j_file("")
    assert result == json_list


@patch("builtins.open")
@patch("json.load")
def test_create_list_from_j_file_json_decode_error(mock_load: Any, mock_open_file: Any) -> None:
    """Тестирует функцию при ошибке данных в JSON-файле"""
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError("Error", "", 1)
    result = create_list_from_j_file("")
    assert result == []


@patch("builtins.open")
def test_create_list_from_j_file_type_error(mock_open_file: Any) -> None:
    """Тестирует функцию при ошибке типа данных в JSON-файле"""
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = TypeError
    result = create_list_from_j_file("")
    assert result == []


@patch("builtins.open")
def test_create_list_from_j_file_file_not_found(mock_open_file: Any) -> None:
    """Тестирует функцию при отсутствии JSON-файла"""
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = FileNotFoundError
    result = create_list_from_j_file("")
    assert result == []


@pytest.fixture
def transaction_dict_rub() -> dict:
    return {"amount": "31957.58", "currency_name": "руб.", "currency_code": "RUB"}


def test_get_conversion_amount_rub(transaction_dict_rub: dict) -> None:
    """Тестируем функцию, если транзакция в рублях"""
    assert get_conversion_amount(transaction_dict_rub) == 31957.58


@pytest.mark.parametrize(
    "transaction_dict, expected",
    [
        ({"amount": "8221.37", "currency_name": "USD", "currency_code": "USD"}, 1.00),
        ({"amount": "7531.37", "currency_name": "EUR", "currency_code": "EUR"}, 1.00),
        ({"amount": "2182.37", "currency_name": "CNY", "currency_code": "CNY"}, 0.00),
    ],
)
@patch("src.utils.convert_currency")
def test_get_conversion_amount_not_rub(mock_convert_currency: Any, transaction_dict: dict, expected: float) -> None:
    """Тестируем функцию, если транзакция не в рублях"""
    mock_convert_currency.return_value = 1.00
    assert get_conversion_amount(transaction_dict) == expected
