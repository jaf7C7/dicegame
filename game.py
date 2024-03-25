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
        self.player_1.number = 1
        self.player_2 = player_2
        self.player_2.number = 2
        self.display = display
        self.round = round_
        self.winner = None

    def play(self):
        self.display.display_game_welcome()

        while not self._game_over():
            self.round.play()
            if not self.round.is_tie:
                self.round.winner.decrement_counter()
                self.round.loser.increment_counter()

        self.display.display_game_over()
        self.display.display_game_results()

    def _game_over(self):
        if self.player_1.counter == 0:
            self.winner = 'Player 1'
        elif self.player_2.counter == 0:
            self.winner = 'Player 2'
        else:
            self.winner = None

        return self.winner is not None
