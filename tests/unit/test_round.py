from unittest.mock import Mock
from round import Round


class TestPlay:
    def test_displays_correct_round_number(self):
        round_ = Round(display=Mock(), number=2)
        round_.play_round()
        round_.display.assert_any_call(
            'Round 2:\n'
            '--------\n'
        )  # fmt: skip
