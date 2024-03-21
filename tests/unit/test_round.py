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
