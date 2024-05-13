from Game import Game
from Player import Player


class Computer(Player):

    def __init__(self, color, depth):
        super().__init__(color)
        self.depth = depth

    def update_score(self, score):
        super().update_score(score)

    def get_color(self):
        return super().get_color()

    def get_score(self):
        return super().get_score()

    def get_depth(self):
        return self.depth
