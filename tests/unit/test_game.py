import pytest
from unittest.mock import Mock, patch
from game import Game


@pytest.fixture
def game():
    return Game(
        player_1=Mock(is_cpu=False, counter=10, die=Mock(value=0)),
        player_2=Mock(is_cpu=True, counter=10, die=Mock(value=0)),
        display=Mock(),
    )


class TestPlay:
    def test_displays_welcome_message(self, game):
        with patch.object(game, 'game_over', side_effect=[True]):
            game.play()
            game.display.assert_any_call(
                '=========================\n'
                'Welcome To The Dice Game!\n'
                '=========================\n'
            )

    def test_displays_end_of_game_message(self, game):
        with patch.object(game, 'game_over', side_effect=[True]):
            game.play()
            game.display.assert_called_with(
                '===================\n'
                '**** GAME OVER ****\n'
                '===================\n'
                '\n'
                'And the winner is...\n'
                f'{game.winner}!\n'
                '\n'
            )

    def test_calls_play_round_until_game_over(self, game):
        with (
            patch.object(game, 'game_over', side_effect=[False, False, True]),
            patch.object(game, 'play_round') as fake_play_round,
        ):
            game.play()
            assert fake_play_round.call_count == 2


class TestPlayRound:
    def test_displays_incrementing_round_numbers(self, game):
        with patch('game.input', return_value=''):
            game.play_round()
            game.display.assert_any_call(
                'Round 1:\n'
                '--------\n'
            )  # fmt: skip

            game.play_round()
            game.display.assert_any_call(
                'Round 2:\n'
                '--------\n'
            )  # fmt: skip

    def test_requires_input_from_human_player_to_roll(self, game):
        with patch('game.input', return_value='') as fake_input:
            game.play_round()
            fake_input.assert_called_once_with(
                'Press any key to roll your die... '
            )

    def test_calls_roll_die_on_players(self, game):
        with patch('game.input', return_value='') as fake_input:
            game.play_round()
        assert all(p.roll_die.called for p in (game.player_1, game.player_2))

    def test_displays_results_of_each_die_roll(self, game):
        with patch('game.input', return_value=''):
            game.play_round()
            game.display.assert_any_call(
                '\n'
                f'Player 1 rolled: {game.player_1.die.value}\n'
                f'Player 2 rolled: {game.player_2.die.value}\n'
                '\n'
            )

    def test_calls_update_counter_methods_on_players(self, game):
        with patch('game.input', return_value=''):
            game.player_1.die.value = 6
            game.player_2.die.value = 1
            game.play_round()
            game.player_1.decrement_counter.assert_called()
            game.player_2.increment_counter.assert_called()

    def test_update_counter_methods_not_called_if_round_tied(self, game):
        with patch('game.input', return_value=''):
            game.player_1.die.value = 1
            game.player_2.die.value = 1
            game.play_round()
            game.player_1.decrement_counter.assert_not_called()
            game.player_1.increment_counter.assert_not_called()
            game.player_2.decrement_counter.assert_not_called()
            game.player_2.increment_counter.assert_not_called()

    @pytest.mark.parametrize(
        'p1_die,p2_die,result',
        [
            ('6', '1', 'WINNER: Player 1'),
            ('1', '6', 'WINNER: Player 2'),
            ('1', '1', "It's a Tie!"),
        ],
    )
    def test_displays_results_and_counters(self, game, p1_die, p2_die, result):
        with patch('game.input', return_value=''):
            game.player_1.die.value = p1_die
            game.player_2.die.value = p2_die
            game.play_round()
            game.display.assert_any_call(
                '*************************\n'
                f'Round 1: {result}\n'
                '*************************\n'
                '\n'
                '~~~~ Player counters: ~~~~\n'
                f'Player 1: {game.player_1.counter}\n'
                f'Player 2: {game.player_2.counter}\n'
                '\n'
            )


class TestGameOver:
    def test_returns_true_when_any_player_counter_is_zero(self, game):
        game.player_1.counter = 0
        assert game.game_over() is True

    def test_returns_false_when_neither_player_counter_is_zero(self, game):
        assert game.player_1.counter != 0 and game.player_2.counter != 0
        assert game.game_over() is False
