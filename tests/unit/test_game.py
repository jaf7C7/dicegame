import pytest
from unittest.mock import Mock, patch
from game import Game


@pytest.fixture
def game():
    game = Game(round_=Mock(), ui=Mock())
    game.add_player(Mock())
    game.add_player(Mock())
    return game


class TestPlayers:

    def test_fails_if_has_less_than_two_players(self):
        game = Game(round_=Mock(), ui=Mock())
        game.add_player(Mock())
        with pytest.raises(AttributeError):
            game.play()

    def test_add_player_increases_number_of_players(self):
        game = Game(round_=Mock(), ui=Mock())
        assert len(game.players) == 0
        game.add_player(Mock())
        assert len(game.players) == 1

    def test_add_player_sets_player_number(self):
        game = Game(round_=Mock(), ui=Mock())
        assert len(game.players) == 0
        player = Mock(number=None)
        game.add_player(player)
        assert player.number == 1

    def test_add_player_can_add_cpu_player(self):
        game = Game(round_=Mock(), ui=Mock())
        assert len(game.players) == 0
        game.add_player(Mock(), is_cpu=True)
        assert game.players[0].is_cpu is True


class TestPlay:

    def test_displays_welcome_message(self, game):
        game.players[0].counter = 0
        game.play()
        assert game.ui.display_game_welcome.called

    def test_displays_game_over_message(self, game):
        game.players[0].counter = 0
        game.play()
        assert game.ui.display_game_over.called

    def test_displays_game_results_message(self, game):
        game.players[0].counter = 0
        game.play()
        assert game.ui.display_winner.called

    def test_calls_play_round_until_game_over(self, game):
        with patch.object(game, 'game_over', side_effect=[False, False, True]):
            game.play()
            assert game.round.play.call_count == 2

    @pytest.mark.parametrize('winner,loser', [(0, 1), (1, 0)])
    def test_update_counter_methods_called_if_not_a_tie(
        self, game, winner, loser
    ):
        game.round.winner = game.players[winner]
        game.round.loser = game.players[loser]
        game.round.is_tie = False
        with patch.object(game, 'game_over', side_effect=[False, True]):
            game.play()
            assert (
                game.round.winner.decrement_counter.called
                and game.round.loser.increment_counter.called
            )

    def test_update_counter_methods_not_called_if_tie(self, game):
        game.round.winner = None
        game.round.loser = None
        game.round.is_tie = True
        with patch.object(game, 'game_over', side_effect=[False, True]):
            game.play()
            assert not (
                game.players[0].increment_counter.called
                and game.players[0].decrement_counter.called
                and game.players[1].increment_counter.called
                and game.players[1].decrement_counter.called
            )

    def test_displays_player_counters(self, game):
        game.round.is_tie = False
        with patch.object(game, 'game_over', side_effect=[False, True]):
            game.play()
            game.ui.display_player_counters.assert_called_with(game.players)


class TestGameOver:

    def test_returns_true_when_any_player_counter_is_zero(self, game):
        game.add_player(Mock())
        game.players[2].counter = 0
        assert game.game_over() is True

    def test_returns_false_when_neither_player_counter_is_zero(self, game):
        assert all(p.counter != 0 for p in game.players)
        assert game.game_over() is False
