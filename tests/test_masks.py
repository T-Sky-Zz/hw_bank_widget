import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_correct():
    """Тест проверяет, маскируется ли номер карты в формате XXXX XX** **** XXXX"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_uncorrect():
    """Тест проверяет, правильность введения данных"""
    with pytest.raises(ValueError) as e_info:
        get_mask_card_number("700079228960636113249876")
        get_mask_card_number("")
        get_mask_card_number("700079")
    with pytest.raises(TypeError) as e_info:
        get_mask_card_number(7000792289606361)
        get_mask_card_number({7000792289606361})
        get_mask_card_number(["7000792289606361"])


def test_get_mask_account_correct():
    """Тест проверяет, маскируется ли номер счета в формате **XXXX"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_uncorrect():
    """Тест проверяет, правильность введения данных"""
    with pytest.raises(ValueError) as e_info:
        get_mask_card_number("700079")
        get_mask_card_number("700079228960636113249876")
        get_mask_card_number("")
    with pytest.raises(TypeError) as e_info:
        get_mask_card_number(700079228960636113249876)
        get_mask_card_number({700079228960636113249876})
        get_mask_card_number(["700079228960636113249876"])
