import pytest
from game import Game


class TestPlay:
    def display(self, message):
        self.messages.append(message)

    def test_displays_welcome_message(self, capsys):
        self.messages = []
        Game().play(display=self.display)
        assert (
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        ) in self.messages
