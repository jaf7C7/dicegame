import pytest
from unittest.mock import Mock, patch
from game import Game


@pytest.fixture
def game():
    game = Game(round_class=Mock, ui=Mock(), player_class=Mock)
    return game


class TestPlayers:

    def test_fails_if_has_less_than_two_players(self, game):
        game.add_player()
        with pytest.raises(AttributeError):
            game.play()

    def test_add_player_increases_number_of_players(self, game):
        game.add_player()
        assert len(game.players) == 1

    def test_add_player_sets_player_number(self, game):
        game.add_player()
        assert game.players[0].number == 1

    def test_add_player_can_add_cpu_player(self, game):
        game.add_player(is_cpu=True)
        assert game.players[0].is_cpu is True


class TestPlay:

    @pytest.fixture
    def game(self, game):
        game.add_player()
        game.add_player()
        return game

    def test_displays_welcome_message(self, game):
        game.game_over = lambda: True
        game.play()
        assert game.ui.display_game_welcome.called

    def test_displays_game_over_message(self, game):
        game.game_over = lambda: True
        game.play()
        assert game.ui.display_game_over.called

    def test_displays_game_results_message(self, game):
        game.game_over = lambda: True
        game.play()
        assert game.ui.display_winner.called

    def test_calls_play_round_until_game_over(self, game):
        round_ = Mock(play=Mock())
        game.round_class = lambda: round_
        game.game_over = Mock(side_effect=[False, False, True])
        game.play()
        assert round_.play.call_count == 2

    @pytest.mark.parametrize('winner,loser', [(0, 1), (1, 0)])
    def test_update_counter_methods_called_if_not_a_tie(
        self, game, winner, loser
    ):
        round_ = Mock(
            winner=game.players[winner],
            loser=game.players[loser],
            is_tie=False,
        )
        game.round_class = Mock(return_value=round_)
        game.game_over = Mock(side_effect=[False, True])
        game.play()
        assert (
            round_.winner.decrement_counter.called
            and round_.loser.increment_counter.called
        )

    def test_update_counter_methods_not_called_if_tie(self, game):
        round_ = Mock(winner=None, loser=None, is_tie=True)
        game.round_class = Mock(return_value=round_)
        game.game_over = Mock(side_effect=[False, True])
        game.play()
        assert not (
            game.players[0].increment_counter.called
            and game.players[0].decrement_counter.called
            and game.players[1].increment_counter.called
            and game.players[1].decrement_counter.called
        )

    def test_displays_player_counters(self, game):
        round_ = Mock(is_tie=False)
        game.round_class = Mock(return_value=round_)
        game.game_over = Mock(side_effect=[False, True])
        game.play()
        game.ui.display_player_counters.assert_called_with(game.players)


class TestGameOver:

    @pytest.fixture
    def game(self, game):
        game.add_player()
        game.add_player()
        return game

    @pytest.mark.parametrize('p1_counter,p2_counter', ((0, 1), (1, 0)))
    def test_returns_true_when_any_player_counter_is_zero(
        self, game, p1_counter, p2_counter
    ):
        game.players[0].counter = p1_counter
        game.players[1].counter = p2_counter
        assert game.game_over() is True

    def test_returns_false_when_neither_player_counter_is_zero(self, game):
        game.players[0].counter = 1
        game.players[1].counter = 2
        assert game.game_over() is False
