class UI:
    """Handles user input and output."""

    def __init__(self, display, input_):
        self.display = display
        self.input_ = input_

    def display_game_welcome(self):
        """Welcomes the user to the game."""
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def display_game_over(self):
        """Displays the game over message to the user."""
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def display_winner(self, winner):
        """Displays the game's overall winner to the user."""
        self.display('And the winner is...\n' f'{winner}!\n' '\n')

    def display_round_welcome(self, round_number):
        """Notifies the user that a new round has started."""
        self.display(f'Round {round_number}:\n' '--------\n')

    def display_player_die_values(self, players):
        """Displays player die values to the user."""
        self.display('\n')
        for player in players:
            self.display(f'{player} rolled: {player.die.value}\n')

    def display_round_result(self, winner):
        """Displays the outcome of the last round to the user."""
        result = f'WINNER: {winner}' if winner is not None else "It's a Tie!"
        self.display(
            '*************************\n'
            f'Round 1: {result}\n'
            '*************************\n'
            '\n'
        )

    def display_player_counters(self, players):
        """Displays the player counter values to the user."""
        self.display('~~~~ Player counters: ~~~~\n')
        for player in players:
            self.display(f'{player}: {player.counter}\n')

    def get_user_input(self, player):
        """Prompts the user for their input to roll their die."""
        self.input_(f'{player}: Press any key to roll your die... ')
