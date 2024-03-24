import pytest
from unittest.mock import Mock
from round import Round


@pytest.fixture
def round_():
    round_ = Round(
        player_1=Mock(), player_2=Mock(), display=Mock(), input_=Mock()
    )
    round_.player_1.die.value = 0
    round_.player_2.die.value = 0
    return round_


class TestAttributes:

    @pytest.mark.parametrize('attr', (('winner', 'loser', 'is_tie')))
    def test_winner_loser_and_is_tie_attributes_are_protected(
        self, round_, attr
    ):
        with pytest.raises(AttributeError):
            setattr(round_, attr, 'Cheater!')

    def test_has_two_players(self, round_):
        assert hasattr(round_, 'player_1') and hasattr(round_, 'player_2')

    def test_players_are_required_attributes(self):
        with pytest.raises(TypeError):
            round_ = Round()


class TestPlay:

    def test_displays_round_number_at_start_of_round(self, round_):
        round_.play()
        assert round_.display.display_round_welcome.called

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
        assert (
            round_.player_1.roll_die.called and round_.player_2.roll_die.called
        )

    def test_requires_input_from_human_player_to_roll(self, round_):
        round_.player_1.is_cpu = False
        round_.player_2.is_cpu = True
        round_.play()
        assert round_.display.prompt_player_roll.called

    def test_displays_results_of_each_die_roll(self, round_):
        round_.player_1.die.value = 1
        round_.player_2.die.value = 2
        round_.play()
        round_.display.display_player_die_values.assert_called_with(
            p1_die=1, p2_die=2
        )

    def test_correct_attributes_set_if_tie(self, round_):
        round_.player_1.die.value = 1
        round_.player_2.die.value = 1
        round_.play()
        assert round_.winner is None
        assert round_.loser is None
        assert round_.is_tie is True

    @pytest.mark.parametrize(
        'p1_die,p2_die,p1_result,p2_result,is_tie',
        (
            (2, 1, 'winner', 'loser', False),
            (1, 2, 'loser', 'winner', False),
        ),
    )
    def test_correct_attributes_set_if_not_tie(
        self,
        round_,
        p1_die,
        p2_die,
        p1_result,
        p2_result,
        is_tie,
    ):
        round_.player_1.die.value = p1_die
        round_.player_2.die.value = p2_die
        round_.play()
        assert getattr(round_, p1_result) is round_.player_1
        assert getattr(round_, p2_result) is round_.player_2
        assert round_.is_tie is is_tie

    def test_displays_results_and_counters_if_not_tie(self, round_):
        round_.number = 1
        round_.player_1.die.value = 6
        round_.player_2.die.value = 1
        round_.player_1.counter = 1
        round_.player_2.counter = 2
        round_.play()
        round_.display.display_round_result.assert_called_with(
            winner=round_.player_1, is_tie=False
        )
        round_.display.display_player_counters.assert_called_with(
            p1_counter=1, p2_counter=2
        )

    def test_displays_results_and_counters_if_tie(self, round_):
        round_.number = 1
        round_.player_1.die.value = 1
        round_.player_2.die.value = 1
        round_.player_1.counter = 1
        round_.player_2.counter = 2
        round_.play()
        round_.display.display_round_result.assert_called_with(
            winner=None, is_tie=True
        )
        round_.display.display_player_counters.assert_called_with(
            p1_counter=1, p2_counter=2
        )
