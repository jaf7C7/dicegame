from round import Round
from player import Player


class Game:
    """A two player dice game.

    The game is played over several successive rounds. The winner of
    each round has their counter decremented, and the loser has their
    counter incremented. If the round is a tie no action is taken.

    The game is over when either player's counter reaches zero. This
    player is declared the winner.
    """

    def __init__(self, ui=None, round_class=None, player_class=None):
        self.players = []
        self.ui = ui
        self.round_class = round_class
        self.winner = None
        self.player_class = player_class

    def play(self):
        """Start playing the game."""
        if len(self.players) < 2:
            raise AttributeError('Two or more players are required to play.')

        self.ui.display_game_welcome()

        while not self.game_over():
            round_ = self.round_class()
            round_.play()
            if not round_.is_tie:
                round_.winner.decrement_counter()
                round_.loser.increment_counter()
            self.ui.display_player_counters(self.players)

        self.ui.display_game_over()
        self.ui.display_winner(self.winner)

    def add_player(self, is_cpu=False):
        """Add a new player to the game."""
        player = self.player_class(number=len(self.players) + 1, is_cpu=is_cpu)
        self.players.append(player)

    def game_over(self):
        """Determine if the game is over."""
        for p in self.players:
            if p.counter == 0:
                self.winner = p
        return self.winner is not None
