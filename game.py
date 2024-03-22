from round import Round
from player import Player


class Game:
    """A game to be played by two players over a number of rounds"""

    def __init__(
        self,
        player_1=Player(),
        player_2=Player(is_cpu=True),
        display=print,
        round_=None,
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.display = display
        if round_ is None:
            round_ = Round(
                self.player_1,
                self.player_2,
                display=self.display,
                input_=input,
            )
        self.round = round_
        self.game_winner = None

    def play(self):
        self._display_game_welcome_message()

        while not self._game_over():
            self.round.play()

        self._display_game_over_message()

    def _game_over(self):
        self._set_game_winner()
        return self.game_winner is not None

    def _set_game_winner(self):
        if self.player_1.counter == 0:
            self.game_winner = 'Player 1'
        elif self.player_2.counter == 0:
            self.game_winner = 'Player 2'
        else:
            self.game_winner = None

    def _display_game_welcome_message(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def _display_game_over_message(self):
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
            'And the winner is...\n'
            f'{self.game_winner}!\n'
            '\n'
        )
