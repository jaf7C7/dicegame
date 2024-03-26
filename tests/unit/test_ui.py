import pytest
from unittest.mock import Mock
from ui import UI


@pytest.fixture
def ui():
    return UI(display=Mock())


@pytest.fixture
def players():
    p1 = Mock(__str__=Mock(return_value='Player 1'))
    p2 = Mock(__str__=Mock(return_value='Player 2'))
    return [p1, p2]


class TestDisplay:

    def test_game_welcome(self, ui):
        ui.display_game_welcome()
        ui.display.assert_called_with(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def test_game_over(self, ui):
        ui.display_game_over()
        ui.display.assert_called_with(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def test_winner(self, ui):
        ui.display_winner(winner='Player 1')
        ui.display.assert_called_with(
            'And the winner is...\n' 'Player 1!\n' '\n'
        )

    def test_round_welcome(self, ui):
        ui.display_round_welcome(round_number=1)
        ui.display.assert_called_with('Round 1:\n' '--------\n')

    def test_player_die_values(self, ui, players):
        players[0].die.value = 1
        players[1].die.value = 2
        ui.display_player_die_values(players)
        ui.display.assert_any_call(f'Player 1 rolled: 1\n')
        ui.display.assert_any_call(f'Player 2 rolled: 2\n')

    @pytest.mark.parametrize(
        'winner,is_tie,message',
        [('Player 1', False, 'WINNER: Player 1'), (None, True, "It's a Tie!")],
    )
    def test_round_result(self, ui, winner, is_tie, message):
        ui.display_round_result(winner=winner, is_tie=is_tie)
        ui.display.assert_called_with(
            '*************************\n'
            f'Round 1: {message}\n'
            '*************************\n'
            '\n'
        )

    def test_player_counters(self, ui, players):
        players[0].counter = 1
        players[1].counter = 2
        ui.display_player_counters(players)
        ui.display.assert_any_call('~~~~ Player counters: ~~~~\n')
        ui.display.assert_any_call('Player 1: 1\n')
        ui.display.assert_any_call('Player 2: 2\n')

    def test_roll_prompt(self, ui):
        p1 = Mock(__str__=Mock(return_value='Player 1'))
        ui.display_roll_prompt(player=p1)
        ui.display.assert_called_with(
            'Player 1: Press any key to roll your die... '
        )
