class Round:

    def __init__(
        self, player_1, player_2, number=1, display=print, input_=input
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.number = number
        self.display = display
        self.input_ = input_
        self.winner = None
        self.loser = None
        self.is_tie = False

    def play(self):
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
            self.winner = self.player_1
            self.loser = self.player_2
            self.player_1.decrement_counter()
            self.player_2.increment_counter()
        elif self.player_1.die.value < self.player_2.die.value:
            self.winner = self.player_2
            self.loser = self.player_1
            self.player_2.decrement_counter()
            self.player_1.increment_counter()
        else:
            self.is_tie = True
