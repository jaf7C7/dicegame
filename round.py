class Round:

    def __init__(self, players=None, ui=None):
        if players is None:
            players = []
        self.players = players
        self.number = 0
        self.ui = ui
        self._winner = None
        self._loser = None
        self._is_tie = False

    @property
    def winner(self):
        return self._winner

    @property
    def loser(self):
        return self._loser

    @property
    def is_tie(self):
        return self._is_tie

    def play(self):
        if len(self.players) < 2:
            raise AttributeError('Two or more players are required to play.')
        self.number += 1
        self.ui.display_round_welcome(round_number=self.number)

        for player in self.players:
            if player.is_cpu is False:
                self.ui.get_user_input()
            player.roll_die()

        self.ui.display_player_die_values(self.players)

        if self.players[0].die.value > self.players[1].die.value:
            self._winner = self.players[0]
            self._loser = self.players[1]
        elif self.players[0].die.value < self.players[1].die.value:
            self._winner = self.players[1]
            self._loser = self.players[0]
        else:
            self._is_tie = True

        self.ui.display_round_result(winner=self.winner, is_tie=self.is_tie)
