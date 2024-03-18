import pytest
from unittest.mock import Mock
from game import Game


class TestPlay:
    def test_displays_welcome_message(self):
        game = Game(player_1=Mock(), player_2=Mock(), display=Mock())
        game.play()
        game.display.assert_any_call(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )


class TestPlayRound:
    def test_displays_round_start_message(self):
        game = Game(player_1=Mock(), player_2=Mock(), display=Mock())
        game.play_round()
        game.display.assert_any_call(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip

    def test_calls_roll_die_on_players(self):
        game = Game(player_1=Mock(), player_2=Mock(), display=Mock())
        game.play_round()
        assert all(p.roll_die.called for p in (game.player_1, game.player_2))
