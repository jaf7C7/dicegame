import pytest
from unittest.mock import Mock
from round import Round


@pytest.fixture
def round_():
    p1 = Mock(die=Mock(value=0))
    p2 = Mock(die=Mock(value=0))
    return Round(players=[p1, p2], ui=Mock())


class TestAttributes:

    @pytest.mark.parametrize('attr', (('winner', 'loser', 'is_tie')))
    def test_winner_loser_and_is_tie_attributes_are_protected(self, attr):
        round_ = Round(players=[Mock(), Mock()])
        with pytest.raises(AttributeError):
            setattr(round_, attr, 'Cheater!')

    @pytest.mark.parametrize('players', [([], [Mock()])])
    def test_players_are_required_attributes(self, players):
        with pytest.raises(AttributeError) as err:
            round_ = Round(players=players)
            assert err.msg == 'Two or more players are required to play'


class TestPlay:

    def test_displays_round_number_at_start_of_round(self, round_):
        round_.play()
        assert round_.ui.display_round_welcome.called

    def test_round_number_is_incremented_each_time_play_is_called(
        self, round_
    ):
        assert round_.number == 0
        round_.play()
        assert round_.number == 1
        round_.play()
        assert round_.number == 2

    def test_calls_roll_die_on_players(self, round_):
        round_.play()
        assert all(p.roll_die.called for p in round_.players)

    def test_requires_input_from_human_player_to_roll(self, round_):
        round_.play()
        round_.players[0].is_cpu = False
        round_.players[1].is_cpu = True
        round_.play()
        assert round_.ui.display_roll_prompt.called

    def test_displays_results_of_each_die_roll(self, round_):
        round_.play()
        round_.play()
        round_.ui.display_player_die_values.assert_called_with(round_.players)

    def test_correct_attributes_set_if_tie(self, round_):
        round_.play()
        assert round_.winner is None
        assert round_.loser is None
        assert round_.is_tie is True

    @pytest.mark.parametrize(
        'p1_die,p2_die,winner,is_tie', ((2, 1, 0, False), (1, 2, 1, False))
    )
    def test_correct_attributes_set_if_not_tie(
        self,
        round_,
        p1_die,
        p2_die,
        winner,
        is_tie,
    ):
        round_.players[0].die.value = p1_die
        round_.players[1].die.value = p2_die
        round_.play()
        assert round_.winner is round_.players[winner]
        assert round_.is_tie is is_tie

    def test_displays_results_and_counters_if_not_tie(self, round_):
        round_.players[0].die.value = 2
        round_.players[1].die.value = 1
        round_.number = 1
        round_.play()
        round_.ui.display_round_result.assert_called_with(
            winner=round_.players[0], is_tie=False
        )
        round_.ui.display_player_counters.assert_called_with(round_.players)

    def test_displays_results_and_counters_if_tie(self, round_):
        round_.players[0].die.value = 1
        round_.players[1].die.value = 1
        round_.number = 1
        round_.play()
        round_.ui.display_round_result.assert_called_with(
            winner=None, is_tie=True
        )
        round_.ui.display_player_counters.assert_called_with(round_.players)
