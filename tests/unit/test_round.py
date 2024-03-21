import pytest
from unittest.mock import Mock
from round import Round


class TestPlayers:

    def test_has_two_players(self):
        round_ = Round(player_1=Mock(), player_2=Mock())
        assert hasattr(round_, 'player_1') and hasattr(round_, 'player_2')


class TestPlay:

    def test_displays_correct_round_number(self):
        round_ = Round(
            player_1=Mock(), player_2=Mock(), display=Mock(), number=2
        )
        round_.play()
        round_.display.assert_any_call(
            'Round 2:\n'
            '--------\n'
        )  # fmt: skip

    def test_players_are_required_attributes(self):
        with pytest.raises(TypeError):
            round_ = Round()

    def test_calls_roll_die_on_players(self):
        round_ = Round(player_1=Mock(), player_2=Mock())
        round_.play()
        assert (
            round_.player_1.roll_die.called and round_.player_2.roll_die.called
        )

    def test_requires_input_from_human_player_to_roll(self):
        round_ = Round(
            player_1=Mock(is_cpu=False),
            player_2=Mock(is_cpu=True),
            input_=Mock(),
        )
        round_.play()
        round_.input_.assert_called_once_with(
            'Player 1: Press any key to roll your die... '
        )
