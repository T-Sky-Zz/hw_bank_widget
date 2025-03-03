from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import convert_currency


@patch('requests.get')
def test_convert_currency_usd_success(mock_get: Any) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1.00}
    assert convert_currency("USD", "RUB", 100.00) == 1.00


@patch('requests.get')
def test_convert_currency_failed_request(mock_get: Any) -> None:
    mock_get.return_value.status_code = 500
    with pytest.raises(ValueError, match="Failed to get currency rate"):
        convert_currency("USD", "RUB", 100.00)
