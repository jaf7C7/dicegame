class Display:

    def __init__(self, display):
        self.display = display

    def display_game_welcome(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def display_game_over(self):
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def display_game_results(self, winner):
        self.display(
            'And the winner is...\n'
            f'{winner}!\n'
            '\n'
        )  # fmt: skip

    def display_round_welcome(self, round_number):
        self.display(
            f'Round {round_number}:\n'
            '--------\n'
        )  # fmt: skip

    def display_player_die_values(self, p1_die, p2_die):
        self.display(
            '\n'
            f'Player 1 rolled: {p1_die}\n'
            f'Player 2 rolled: {p2_die}\n'
        )  # fmt: skip

    def display_round_result(self):
        self.display(
            '*************************\n'
            'Round 1: WINNER: Player 1\n'
            '*************************\n'
            '\n'
        )

    def display_player_counters(self, p1_counter, p2_counter):
        self.display(
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: {p1_counter}\n'
            f'Player 2: {p2_counter}\n'
            '\n'
        )
