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
        self.display(
            f'Round {self.number}:\n'
            '--------\n'
        )  # fmt: skip
        for player in (self.player_1, self.player_2):
            if player.is_cpu is False:
                self.input_('Player 1: Press any key to roll your die... ')
            player.roll_die()
        self.display(
            '\n'
            f'Player 1 rolled: {self.player_1.die.value}\n'
            f'Player 2 rolled: {self.player_2.die.value}\n'
        )
        if self.player_1.die.value > self.player_2.die.value:
            self._winner = self.player_1
            self._loser = self.player_2
        elif self.player_1.die.value < self.player_2.die.value:
            self._winner = self.player_2
            self._loser = self.player_1
        else:
            self._is_tie = True

        if self.winner == self.player_1:
            result = 'WINNER: Player 1'
        elif self.winner == self.player_2:
            result = 'WINNER: Player 2'
        elif self.is_tie:
            result = "It's a Tie!"

        self.display(
            '*************************\n'
            f'Round 1: {result}\n'
            '*************************\n'
            '\n'
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: 1\n'
            f'Player 2: 2\n'
            '\n'
        )
