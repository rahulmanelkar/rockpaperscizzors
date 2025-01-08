from src.mvp import *
import pytest

@pytest.mark.parametrize("test_input,expected", [("R", str), ("P", str), ("S", str)])
def test_functionality(test_input, expected):
    assert type(game(test_input)) == expected