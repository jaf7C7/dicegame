class Round:

    def __init__(
        self, player_1, player_2, number=1, display=print, input_=input
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.number = number
        self.display = display
        self.input_ = input_

    def play(self):
        self.display(
            f'Round {self.number}:\n'
            '--------\n'
        )  # fmt: skip
        for player in (self.player_1, self.player_2):
            if player.is_cpu is False:
                self.input_('Player 1: Press any key to roll your die... ')
            player.roll_die()
