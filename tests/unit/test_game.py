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
