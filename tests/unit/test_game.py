import pytest
from unittest.mock import Mock, patch
from game import Game


@pytest.fixture
def game():
    return Game(
        player_1=Mock(), player_2=Mock(), round_=Mock(), display=Mock()
    )


class TestPlay:

    def test_displays_welcome_message(self, game):
        game.player_1.counter = 0
        game.play()
        game.display.assert_any_call(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def test_displays_end_of_game_message(self, game):
        game.player_1.counter = 0
        game.play()
        game.display.assert_called_with(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
            'And the winner is...\n'
            'Player 1!\n'
            '\n'
        )

    def test_calls_play_round_until_game_over(self, game):
        with patch.object(
            game, '_game_over', side_effect=[False, False, True]
        ):
            game.play()
            assert game.round.play.call_count == 2

    @pytest.mark.parametrize('winner,loser', [('player_1', 'player_2')])
    def test_update_counter_methods_called_if_not_a_tie(
        self, game, winner, loser
    ):
        game.round.winner = getattr(game, winner)
        game.round.loser = getattr(game, loser)
        with patch.object(game, '_game_over', side_effect=[False, True]):
            game.play()
            assert (
                getattr(game, winner).decrement_counter.called
                and getattr(game, loser).increment_counter.called
            )


class TestGameOver:

    def test_returns_true_when_any_player_counter_is_zero(self, game):
        game.player_1.counter = 0
        assert game._game_over() is True

    def test_returns_false_when_neither_player_counter_is_zero(self, game):
        assert game.player_1.counter != 0 and game.player_2.counter != 0
        assert game._game_over() is False
