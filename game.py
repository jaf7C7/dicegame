from round import Round
from player import Player


class PlayerError(Exception):
    pass


class Game:
    """A game to be played by two players over a number of rounds"""

    def __init__(
        self,
        display=print,
        round_=None,
    ):
        self.players = []
        self.display = display
        self.round = round_
        self.winner = None

    def play(self):
        self.display.display_game_welcome()

        while not self.game_over():
            self.round.play()
            if not self.round.is_tie:
                self.round.winner.decrement_counter()
                self.round.loser.increment_counter()

        self.display.display_game_over()
        self.display.display_game_results()

    def add_player(self, player):
        player.number = len(self.players) + 1
        self.players.append(player)

    def game_over(self):
        if len(self.players) < 2:
            raise PlayerError('Two players are required to play.')
        self.winner = None
        for p in self.players:
            if p.counter == 0:
                self.winner = p
        return self.winner is not None
