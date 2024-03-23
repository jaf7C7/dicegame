import pytest
from unittest.mock import Mock
from display import Display


@pytest.fixture
def display():
    return Display(display=Mock())


class TestDisplay:

    def test_game_welcome(self, display):
        display.game_welcome()
        display.display.assert_called_with(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )
