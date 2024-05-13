from Computer import Computer
from Game import Game
from Player import Player


class Controller:
    def __init__(self, depth):
        self.player = Player("B")
        if depth == 2:
            depth = 3
        elif depth == 3:
            depth = 5
        self.computer = Computer("W", depth)
        self.game = Game(self.computer, self.player, depth)

    def print_scores(self):
        scores = self.game.get_scores()
        self.computer.score = scores[0]
        self.player.score = scores[1]
        print("Player score: ", self.player.get_score())
        print("Computer score: ", self.computer.get_score())

    def game_finished(self):
        if self.game.game_finished():
            self.declare_winner()
            return True
        return False

    def print_board(self):
        self.game.print_board()

    def declare_winner(self):
        winner = self.game.find_winner()
        if winner == 1:
            print("White is the winner!")
        elif winner == -1:
            print("Black is the winner!")
        else:
            print("It's a tie!")
        self.print_scores()

    def make_move(self, row, col, color):
        if not self.game.make_move(row, col, color):
            print("This move is not valid")
            return False
        return True

    def get_valid_moves(self, color):
        return self.game.valid_moves(color)

    def computer_move(self):
        return self.game.computer_best_move()
