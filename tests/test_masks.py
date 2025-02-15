import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361"),
                                                   ("1234567890123456", "1234 56** **** 3456")
                                                   ])
def test_get_mask_card_number_correct(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_incorrect():

    with pytest.raises(ValueError):
        get_mask_card_number("123456")
    with pytest.raises(ValueError):
        get_mask_card_number("1234567890123456789")
    with pytest.raises(ValueError):
        get_mask_card_number("")


@pytest.mark.parametrize("acc_number, expected", [("73654108430135874305", "**4305"),
                                                  ("12345678901234567890", "**7890")
                                                  ])
def test_get_mask_account_correct(acc_number, expected):
    assert get_mask_account(acc_number) == expected


def test_get_mask_account_incorrect():

    with pytest.raises(ValueError):
        get_mask_account("700079")
    with pytest.raises(ValueError):
        get_mask_account("73654108430135874305136")
    with pytest.raises(ValueError):
        get_mask_account("")
