import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "type_num, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card_correct(type_num: str, expected: str) -> None:
    assert mask_account_card(type_num) == expected


def test_get_mask_account_card_incorrect() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Maestro 123456")
    with pytest.raises(ValueError):
        mask_account_card("Счет 123456789012345678915687")
    with pytest.raises(ValueError):
        mask_account_card("Master Card")
    with pytest.raises(ValueError):
        mask_account_card("MasterCard")
    with pytest.raises(ValueError):
        mask_account_card("1234 56789012345678915687")
    with pytest.raises(TypeError):
        mask_account_card(123456789012345678915687)  # type: ignore
    with pytest.raises(ValueError):
        mask_account_card("")
    with pytest.raises(TypeError):
        mask_account_card()  # type: ignore


@pytest.mark.parametrize(
    "date, expected", [("2018-09-12T21:27:25.241689", "12.09.2018"), ("2019-07-03T18:35:29.512364", "03.07.2019")]
)
def test_get_date_correct(date: str, expected: str) -> None:
    assert get_date(date) == expected


def test_get_date_incorrect() -> None:
    with pytest.raises(ValueError):
        get_date("дата и время")
    with pytest.raises(TypeError):
        get_date(123456)  # type: ignore
