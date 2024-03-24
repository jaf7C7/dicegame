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

    def test_round_welcome(self, display):
        display.round_welcome()
        display.display.assert_called_with(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip

    def test_player_die_values(self, display):
        display.player_die_values()
        display.display.assert_called_with(
            '\n'
            f'Player 1 rolled: 1\n'
            f'Player 2 rolled: 2\n'
        )  # fmt: skip

    def test_round_results(self, display):
        display.round_results()
        display.display.assert_called_with(
            '*************************\n'
            'Round 1: WINNER: Player 1\n'
            '*************************\n'
            '\n'
            '~~~~ Player counters: ~~~~\n'
            'Player 1: 1\n'
            'Player 2: 2\n'
            '\n'
        )
