import pytest


from src.generators import log


def test_log_console_error(capsys):

    @log()
    def my_function(x, y):
        return x + y


    with pytest.raises(TypeError):
        my_function(1, "2")