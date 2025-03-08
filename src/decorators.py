from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def log_message(message: str) -> Any:
        if not filename:
            print(message)
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(message)

    def my_decorator(func: Callable) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_message = f"Начало работы функции {func.__name__}\n"
                log_message(start_message)
                result = func(*args, **kwargs)
                message = f"{func.__name__} OK\n"
                log_message(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__} Inputs: {args}, {kwargs}\n"
                log_message(message)
                raise e

        return wrapper

    return my_decorator


# @log(filename="mylog.txt")
# def my_function(x, y) -> Any:
#     """Функция суммирует 2 числа"""
#     return x + y

# my_function(1, 2)
# (my_function(1, "2"))
