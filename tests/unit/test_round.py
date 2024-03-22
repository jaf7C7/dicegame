import pytest
from unittest.mock import Mock
from round import Round


@pytest.fixture
def round_():
    return Round(
        player_1=Mock(is_cpu=False, die=Mock(value=1)),
        player_2=Mock(is_cpu=True, die=Mock(value=2)),
        display=Mock(),
        input_=Mock(),
        number=1,
    )


class TestPlayers:

    def test_has_two_players(self, round_):
        round_ = Round(player_1=Mock(), player_2=Mock())
        assert hasattr(round_, 'player_1') and hasattr(round_, 'player_2')


class TestPlay:

    def test_displays_correct_round_number(self):
        round_ = Round(
            player_1=Mock(die=Mock(value=0)),
            player_2=Mock(die=Mock(value=0)),
            display=Mock(),
        )
        round_.number = 2
        round_.play()
        round_.display.assert_any_call(
            'Round 2:\n'
            '--------\n'
        )  # fmt: skip

    def test_players_are_required_attributes(self):
        with pytest.raises(TypeError):
            round_ = Round()

    def test_calls_roll_die_on_players(self):
        round_ = Round(
            player_1=Mock(die=Mock(value=0)),
            player_2=Mock(die=Mock(value=0)),
        )
        round_.play()
        assert (
            round_.player_1.roll_die.called and round_.player_2.roll_die.called
        )

    def test_requires_input_from_human_player_to_roll(self):
        round_ = Round(
            player_1=Mock(die=Mock(value=0), is_cpu=False),
            player_2=Mock(die=Mock(value=0), is_cpu=True),
            input_=Mock(),
        )
        round_.play()
        round_.input_.assert_called_once_with(
            'Player 1: Press any key to roll your die... '
        )

    def test_displays_results_of_each_die_roll(self):
        round_ = Round(
            player_1=Mock(),
            player_2=Mock(),
            display=Mock(),
        )
        round_.player_1.die.value = 1
        round_.player_2.die.value = 2
        round_.play()
        round_.display.assert_any_call(
            '\n'
            f'Player 1 rolled: 1\n'
            f'Player 2 rolled: 2\n'
        )  # fmt: skip

    @pytest.mark.parametrize(
        'p1_die,p2_die,p1_method,p2_method',
        (
            ('1', '2', 'increment_counter', 'decrement_counter'),
            ('2', '1', 'decrement_counter', 'increment_counter'),
        ),
    )
    def test_calls_update_counter_methods_on_players_if_not_a_tie(
        self, p1_die, p2_die, p1_method, p2_method
    ):
        round_ = Round(
            player_1=Mock(),
            player_2=Mock(),
        )
        round_.player_1.die.value = p1_die
        round_.player_2.die.value = p2_die
        round_.play()
        assert (
            getattr(round_.player_1, p1_method).called
            and getattr(round_.player_2, p2_method).called
        )

    def test_update_counter_methods_not_called_if_round_tied(self):
        round_ = Round(
            player_1=Mock(),
            player_2=Mock(),
        )
        round_.player_1.die.value = 1
        round_.player_2.die.value = 1
        round_.play()
        assert not (
            round_.player_1.increment_counter.called
            and round_.player_1.decrement_counter.called
            and round_.player_2.increment_counter.called
            and round_.player_2.decrement_counter.called
        )

    def test_correct_attributes_set_if_tie(self):
        round_ = Round(
            player_1=Mock(),
            player_2=Mock(),
        )
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
        p1_die,
        p2_die,
        p1_result,
        p2_result,
        is_tie,
    ):
        round_ = Round(
            player_1=Mock(),
            player_2=Mock(),
        )
        round_.player_1.die.value = p1_die
        round_.player_2.die.value = p2_die
        round_.play()
        assert getattr(round_, p1_result) is round_.player_1
        assert getattr(round_, p2_result) is round_.player_2
        assert round_.is_tie is is_tie

    def test_displays_results_and_counters(self):
        round_ = Round(
            player_1=Mock(die=Mock(value=0)),
            player_2=Mock(die=Mock(value=0)),
            display=Mock(),
        )
        round_.number = 1
        round_.winner = round_.player_1
        round_.loser = round_.player_2
        round_.player_1.counter = 1
        round_.player_2.counter = 2
        round_.play()
        round_.display.assert_any_call(
            '*************************\n'
            f'Round 1: WINNER: Player 1\n'
            '*************************\n'
            '\n'
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: 1\n'
            f'Player 2: 2\n'
            '\n'
        )
