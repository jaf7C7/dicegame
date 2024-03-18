import pytest
from unittest.mock import Mock
from game import Game


@pytest.fixture
def game():
    return Game(
        player_1=Mock(counter=10), player_2=Mock(counter=10), display=Mock()
    )


class TestPlay:
    def test_displays_welcome_message(self, game):
        game.play()
        game.display.assert_any_call(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )


class TestPlayRound:
    def test_displays_round_start_message(self, game):
        game.play_round()
        game.display.assert_any_call(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip

    def test_calls_roll_die_on_players(self, game):
        game.play_round()
        assert all(p.roll_die.called for p in (game.player_1, game.player_2))

    def test_displays_values_of_counters(self, game):
        game.play_round()
        game.display.assert_any_call(
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: {game.player_1.counter}\n'
            f'Player 2: {game.player_2.counter}\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        )


class TestGameOver:
    def test_returns_true_when_any_player_counter_is_zero(self, game):
        game.player_1.counter = 0
        assert game.game_over() is True

    def test_returns_false_when_neither_player_counter_is_zero(self, game):
        assert game.player_1.counter != 0 and game.player_2.counter != 0
        assert game.game_over() is False
