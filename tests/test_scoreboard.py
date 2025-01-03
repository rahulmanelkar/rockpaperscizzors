import pytest
from src.scoreboard import Scoreboard

def test_scoreboard_init():
    score = Scoreboard()
    assert score.points == {}
