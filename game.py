from player import Player


class Game:
    def __init__(
        self, player_1=Player(), player_2=Player(is_cpu=True), display=print
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.display = display
        self.round_number = 0
        self.winner = None

    def play(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

        while not self.game_over():
            self.play_round()

        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
            'And the winner is...\n'
            f'{self.winner}!\n'
            '\n'
        )

    def play_round(self):
        self.round_number += 1

        self.display(
            f'Round {self.round_number}:\n'
            '--------\n'
        )  # fmt: skip

        for player in (self.player_1, self.player_2):
            if not player.is_cpu:
                input('Press any key to roll your die... ')
            player.roll_die()

        self.display(
            '\n'
            f'Player 1 rolled: {self.player_1.die.value}\n'
            f'Player 2 rolled: {self.player_2.die.value}\n'
            '\n'
        )

        if self.player_1.die.value == self.player_2.die.value:
            result = "It's a Tie!"
        elif self.player_1.die.value > self.player_2.die.value:
            result = 'WINNER: Player 1'
            self.player_1.decrement_counter()
            self.player_2.increment_counter()
        else:
            result = 'WINNER: Player 2'
            self.player_2.decrement_counter()
            self.player_1.increment_counter()

        self.display(
            '*************************\n'
            f'Round {self.round_number}: {result}\n'
            '*************************\n'
            '\n'
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: {self.player_1.counter}\n'
            f'Player 2: {self.player_2.counter}\n'
            '\n'
        )

    def game_over(self):
        if self.player_1.counter == 0:
            self.winner = self.player_1
        elif self.player_2.counter == 0:
            self.winner = self.player_2

        return self.winner is not None
