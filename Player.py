class Player:

    def __init__(self, color):
        self.color = color
        self.score = 0

    def update_score(self, score):
        self.score = score

    def get_color(self):
        return self.color

    def get_score(self):
        return self.score
