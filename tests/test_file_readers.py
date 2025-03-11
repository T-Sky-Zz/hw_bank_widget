from typing import Any
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.file_readers import get_transactions_csv, get_transactions_excel


@pytest.fixture
def transactions_df() -> dict:
    sample_dict = {
        "id": [441945886.0, 4813301],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2019-08-26T10:50:58.294041", "2021-11-02T13:32:15Z"],
        "amount": ["31957.58", "15080"],
        "currency_name": ["руб.", "Euro"],
        "currency_code": ["RUB", "EUR"],
        "description": ["Перевод организации", "Перевод со счета на счет"],
        "from": ["Maestro 1596837868705199", "Счет 65547878890984510340"],
        "to": ["Счет 64686473678894779589", "Счет 91457207307678002163"],
    }
    return sample_dict


@pytest.fixture
def result_transactions_df() -> list:
    result_list = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "amount": "31957.58",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 4813301,
            "state": "EXECUTED",
            "date": "2021-11-02T13:32:15Z",
            "amount": "15080",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "description": "Перевод со счета на счет",
            "from": "Счет 65547878890984510340",
            "to": "Счет 91457207307678002163",
        },
    ]
    return result_list


def test_get_transactions_csv(transactions_df: dict, result_transactions_df: list) -> None:
    """Тестирует функцию при корректных исходных данных в CSV-файле"""
    mock_get = Mock(return_value=pd.DataFrame(transactions_df))
    pd.read_csv = mock_get
    assert get_transactions_csv("path") == result_transactions_df


# @patch("pandas.read_csv")
# def test_get_transactions_csv(mock_get: Any, transactions_df: dict, result_transactions_df: list) -> None:
#     mock_get.return_value = pd.DataFrame(transactions_df)
#     assert get_transactions_csv("path") == result_transactions_df


@patch("pandas.read_excel")
def test_get_transactions_excel(mock_get: Any, transactions_df: dict, result_transactions_df: list) -> None:
    """Тестирует функцию при корректных исходных данных в EXCEL-файле"""
    mock_get.return_value = pd.DataFrame(transactions_df)
    assert get_transactions_excel("path") == result_transactions_df
