import pytest
from unittest.mock import Mock, patch
from game import Game


@pytest.fixture
def game():
    game = Game(round_class=Mock(), ui=Mock(), player_class=Mock)
    return game


class TestAddPlayer:

    def test_increases_number_of_players(self, game):
        game.add_player()
        assert len(game.players) == 1

    def test_sets_player_number(self, game):
        game.add_player()
        assert game.players[0].number == 1

    def test_can_add_cpu_player(self, game):
        game.add_player(is_cpu=True)
        assert game.players[0].is_cpu is True


class TestPlay:

    @pytest.fixture
    def game(self, game):
        game.add_player()
        game.add_player()
        game.game_over = Mock(side_effect=[False, True])  # Only play 1 round.
        return game

    @pytest.fixture
    def round_(self, game):
        return game.round_class()

    @pytest.mark.parametrize('players', ([], [object]))
    def test_fails_if_has_less_than_two_players(self, game, players):
        game.players = players
        with pytest.raises(AttributeError):
            game.play()

    def test_displays_welcome_message(self, game):
        game.play()
        assert game.ui.display_game_welcome.called

    def test_displays_game_over_message(self, game):
        game.play()
        assert game.ui.display_game_over.called

    def test_displays_game_results_message(self, game):
        game.play()
        assert game.ui.display_winner.called

    def test_calls_play_round_until_game_over(self, game, round_):
        game.play()
        assert round_.play.call_count == 1

    @pytest.mark.parametrize('winner,loser', ((0, 1), (1, 0)))
    def test_update_counter_methods_called_if_not_a_tie(
        self, game, round_, winner, loser
    ):
        round_.configure_mock(
            winner=game.players[winner],
            loser=game.players[loser],
            is_tie=False,
        )
        game.play()
        assert (
            game.players[winner].decrement_counter.called
            and game.players[loser].increment_counter.called
        )

    def test_update_counter_methods_not_called_if_tie(self, game, round_):
        round_.configure.mock(winner=None, loser=None, is_tie=True)
        game.play()
        assert not all(
            p.increment_counter.called or p.decrement_counter.called
            for p in game.players
        )

    def test_displays_player_counters_after_each_round(self, game):
        game.play()
        game.ui.display_player_counters.assert_called_with(game.players)


class TestGameOver:

    @pytest.fixture
    def game(self, game):
        game.add_player()
        game.add_player()
        return game

    @pytest.mark.parametrize(
        'p1_counter,p2_counter,game_over',
        ((0, 1, True), (1, 0, True), (1, 1, False)),
    )
    def test_returns_true_if_any_player_counter_is_zero_else_false(
        self, game, p1_counter, p2_counter, game_over
    ):
        game.players[0].counter = p1_counter
        game.players[1].counter = p2_counter
        assert game.game_over() is game_over
