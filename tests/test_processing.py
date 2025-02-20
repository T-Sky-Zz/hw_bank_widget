import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions_input_list() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_executed() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions_canceled() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_executed(transactions_input_list: list[dict], transactions_executed: list[dict]) -> None:
    assert filter_by_state(transactions_input_list, "EXECUTED") == transactions_executed


def test_filter_by_state_empty(transactions_input_list: list[dict], transactions_executed: list[dict]) -> None:
    assert filter_by_state(transactions_input_list) == transactions_executed


def test_filter_by_state_canceled(transactions_input_list: list[dict], transactions_canceled: list[dict]) -> None:
    assert filter_by_state(transactions_input_list, "CANCELED") == transactions_canceled


def test_filter_by_state_incorrect() -> None:

    with pytest.raises(TypeError):
        filter_by_state("zdfgbsfy")  # type: ignore
    with pytest.raises(TypeError):
        filter_by_state([""])  # type: ignore
    with pytest.raises(TypeError):
        filter_by_state()  # type: ignore


@pytest.fixture
def sort_by_descending() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_increasing() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_by_descending(transactions_input_list: list[dict], sort_by_descending: list[dict]) -> None:
    assert sort_by_date(transactions_input_list, "True") == sort_by_descending


def test_sort_by_date_empty(transactions_input_list: list[dict], sort_by_descending: list[dict]) -> None:
    assert sort_by_date(transactions_input_list) == sort_by_descending


def test_sort_by_date_by_increasing(transactions_input_list: list[dict], sort_by_increasing: list[dict]) -> None:
    assert sort_by_date(transactions_input_list, "False") == sort_by_increasing
