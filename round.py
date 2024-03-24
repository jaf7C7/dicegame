class Round:

    def __init__(self, player_1, player_2, display=print, input_=input):
        self.player_1 = player_1
        self.player_2 = player_2
        self.number = 0
        self.display = display
        self.input_ = input_
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
        self.number += 1
        self.display.display_round_welcome(round_number=self.number)

        for player in (self.player_1, self.player_2):
            if player.is_cpu is False:
                self.display.prompt_player_roll()
            player.roll_die()

        self.display.display_player_die_values(p1_die=1, p2_die=2)

        if self.player_1.die.value > self.player_2.die.value:
            self._winner = self.player_1
            self._loser = self.player_2
        elif self.player_1.die.value < self.player_2.die.value:
            self._winner = self.player_2
            self._loser = self.player_1
        else:
            self._is_tie = True

        self.display.display_round_result(
            winner=self.winner, is_tie=self.is_tie
        )
        self.display.display_player_counters(
            p1_counter=self.player_1.counter, p2_counter=self.player_2.counter
        )
