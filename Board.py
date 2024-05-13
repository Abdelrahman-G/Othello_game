class Board:
    def __init__(self):
        self.board = [["_" for _ in range(8)] for _ in range(8)]
        self.board[3][3] = "W"
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[4][4] = "W"

    def update_board(self, row, col, color):
        self.board[row][col] = color

    def get_board(self):
        return self.board
