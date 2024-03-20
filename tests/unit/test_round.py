from unittest.mock import Mock
from round import Round


class TestPlay:
    def test_displays_incrementing_round_numbers(self):
        round_ = Round(display=Mock())
        round_.play_round()
        round_.display.assert_any_call(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip
