class Display:

    def __init__(self, display):
        self.display = display

    def game_welcome(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def game_over(self):
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def game_results(self, winner):
        self.display(
            'And the winner is...\n'
            f'{winner}!\n'
            '\n'
        )  # fmt: skip
