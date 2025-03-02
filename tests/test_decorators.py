import pytest
from src.decorators import log


@pytest.mark.parametrize("expected_start, expected_end",
                         [("Начало работы функции my_func\n\n", "my_func OK\n\n")])
def test_log_console_ok(capsys: pytest.CaptureFixture[str], expected_start: str, expected_end: str) -> None:
    """Проверка работы декоратора при выводе данных в консоль. Работает верно"""
    @log()
    def my_func(x: int, y: int) -> int:
        return x + y

    my_func(1, 2)

    captured = capsys.readouterr()
    assert expected_start in captured.out
    assert expected_end in captured.out


@pytest.mark.parametrize("expected_start, expected_end",
                         [("Начало работы функции my_func\n\n", "my_func error: TypeError Inputs: (1, '2'), {}\n\n")])
def test_log_console_error(capsys: pytest.CaptureFixture[str], expected_start: str, expected_end: str) -> None:
    """Проверка работы декоратора при выводе данных в консоль. Ошибка"""
    @log()
    def my_func(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        my_func(1, "2")  # type: ignore

    captured = capsys.readouterr()
    assert expected_start in captured.out
    assert expected_end in captured.out


@pytest.mark.parametrize("expected_start, expected_end",
                         [("Начало работы функции my_func\n", "my_func OK\n")])
def test_log_file_ok(capsys: pytest.CaptureFixture[str], expected_start: str, expected_end: str) -> None:
    """Проверка работы декоратора при выводе данных в файл. Работает верно"""
    @log(filename="mylog.txt")
    def my_func(x: int, y: int) -> int:
        return x + y

    my_func(1, 2)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        aii_str = file.readlines()
        start_message = aii_str[0]
        end_message = aii_str[-1]
    assert start_message == expected_start
    assert end_message == expected_end


@pytest.mark.parametrize("expected_start, expected_end",
                         [("Начало работы функции my_func\n", "my_func error: TypeError Inputs: (1, '2'), {}\n")])
def test_log_file_error(capsys: pytest.CaptureFixture[str], expected_start: str, expected_end: str) -> None:
    """Проверка работы декоратора при выводе данных в файл. Ошибка"""
    @log(filename="mylog.txt")
    def my_func(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        my_func(1, "2")  # type: ignore

    with open("mylog.txt", "r", encoding="utf-8") as file:
        aii_str = file.readlines()
        start_message = aii_str[0]
        end_message = aii_str[-1]
    assert start_message == expected_start
    assert end_message == expected_end
