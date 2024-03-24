import pytest
from unittest.mock import Mock
from display import Display


@pytest.fixture
def display():
    return Display(display=Mock())


class TestDisplay:

    def test_display_game_welcome(self, display):
        display.display_game_welcome()
        display.display.assert_called_with(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def test_display_game_over(self, display):
        display.display_game_over()
        display.display.assert_called_with(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def test_display_game_results(self, display):
        display.display_game_results(winner='Player 1')
        display.display.assert_called_with(
            'And the winner is...\n'
            'Player 1!\n'
            '\n'
        )  # fmt: skip

    def test_display_round_welcome(self, display):
        display.display_round_welcome(round_number=1)
        display.display.assert_called_with(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip

    def test_display_player_die_values(self, display):
        display.display_player_die_values(p1_die=1, p2_die=2)
        display.display.assert_called_with(
            '\n'
            f'Player 1 rolled: 1\n'
            f'Player 2 rolled: 2\n'
        )  # fmt: skip

    def test_display_round_result(self, display):
        display.display_round_result()
        display.display.assert_called_with(
            '*************************\n'
            'Round 1: WINNER: Player 1\n'
            '*************************\n'
            '\n'
        )

    def test_display_player_counters(self, display):
        display.display_player_counters(p1_counter=1, p2_counter=2)
        display.display.assert_called_with(
            '~~~~ Player counters: ~~~~\n' 'Player 1: 1\n' 'Player 2: 2\n' '\n'
        )