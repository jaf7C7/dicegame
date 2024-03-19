class Game:
    def __init__(self, player_1, player_2, display):
        self.player_1 = player_1
        self.player_2 = player_2
        self.display = display

    def play(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
        )

    def play_round(self):
        self.display(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip

        self.player_1.roll_die()
        self.player_2.roll_die()

        self.display(
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: {self.player_1.counter}\n'
            f'Player 2: {self.player_2.counter}\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        )

        if self.player_1.die.value == self.player_2.die.value:
            result = "It's a Tie!"
        elif self.player_1.die.value > self.player_2.die.value:
            result = 'WINNER: Player 1'
        else:
            result = 'WINNER: Player 2'

        self.display(
            '*************************\n'
            f'Round 1: {result}\n'
            '*************************\n'
        )

    def game_over(self):
        return self.player_1.counter == 0 or self.player_2.counter == 0
