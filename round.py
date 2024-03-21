class Round:

    def __init__(self, player_1, player_2, number=1, display=print):
        self.player_1 = player_1
        self.player_2 = player_2
        self.number = number
        self.display = display

    def play_round(self):
        self.display(
            f'Round {self.number}:\n'
            '--------\n'
        )  # fmt: skip
