from game import Game


class TestSaneDefaults:
    def test_has_one_human_one_computer_player(self):
        game = Game()
        assert game.player_1.is_cpu is False
        assert game.player_2.is_cpu is True

    def test_default_display_is_print(self):
        game = Game()
        assert game.display is print

    def test_both_players_have_rollable_die(self):
        game = Game()
        assert hasattr(game.player_1.die, 'roll')
        assert hasattr(game.player_1.die, 'roll')
