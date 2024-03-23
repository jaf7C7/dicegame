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

    def test_game_over(self, display):
        display.game_over()
        display.display.assert_called_with(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def test_game_results(self, display):
        display.game_results(winner='Player 1')
        display.display.assert_called_with(
            'And the winner is...\n'
            'Player 1!\n'
            '\n'
        )  # fmt: skip
