from src.mvp import *
import pytest

def test_functionality():
    assert type(game('R')) == str