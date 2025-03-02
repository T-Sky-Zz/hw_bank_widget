import json
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import create_list_from_j_file


@patch('builtins.open')
@patch('json.load')
def test_create_list_from_j_file_correct(mock_load: Any, mock_open_file: Any) -> None:
    """Тестирует функцию при корректных исходных данных в JSON-файле"""
    mock_open_file.new = mock_open()
    json_list = [{'ind': 159}, {'ind': 741}]
    mock_load.return_value = json_list
    result = create_list_from_j_file("")
    assert result == json_list


@patch('builtins.open')
@patch('json.load')
def test_create_list_from_j_file_json_decode_error(mock_load: Any, mock_open_file: Any) -> None:
    """Тестирует функцию при ошибке данных в JSON-файле"""
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError('Error', '', 1)
    result = create_list_from_j_file("")
    assert result == []


@patch('builtins.open')
def test_create_list_from_j_file_type_error(mock_open_file: Any) -> None:
    """Тестирует функцию при ошибке типа данных в JSON-файле"""
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = TypeError
    result = create_list_from_j_file("")
    assert result == []


@patch('builtins.open')
def test_create_list_from_j_file_file_not_found(mock_open_file: Any) -> None:
    """Тестирует функцию при отсутствии JSON-файла"""
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = FileNotFoundError
    result = create_list_from_j_file("")
    assert result == []
