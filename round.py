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
                self.ui.display_roll_prompt()
            player.roll_die()

        self.ui.display_player_die_values(self.players)

        highest_rolling_players = [
            p
            for p in self.players
            if all(p.die.value >= q.die.value for q in self.players)
        ]

        if len(highest_rolling_players) == 1:
            self._winner = highest_rolling_players[0]
            self._is_tie = False
        else:
            self._winner = None
            self._is_tie = True

        self.ui.display_round_result(winner=self.winner, is_tie=self.is_tie)
        self.ui.display_player_counters(self.players)
