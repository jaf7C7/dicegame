import pytest
from unittest.mock import Mock
from game import Game


class TestPlay:
    def test_displays_welcome_message(self):
        game = Game(display=Mock())
        game.play()
        game.display.assert_any_call(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )


class TestPlayRound:
    def test_displays_round_start_message(self):
        game = Game(display=Mock())
        game.play_round()
        game.display.assert_any_call(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip
