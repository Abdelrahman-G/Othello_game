from Board import Board


class Game:
    def __init__(self, computer, player, depth):
        self.board = Board()
        self.computer = computer
        self.depth = depth
        self.player = player

    def game_finished(self):
        for row in range(8):
            for col in range(8):
                if self.board.board[row][col] == "_":
                    return False
        return True

    def print_board(self):
        for row in range(8):
            print(self.board.board[row])

    def get_scores(self):
        w = sum(row.count("W") for row in self.board.board)
        b = sum(row.count("B") for row in self.board.board)
        self.computer.score = w
        self.player.score = b
        return [w, b]

    def update_board(self, row, col, color):
        self.board.update_board(row, col, color)

    def find_winner(self):
        w = sum(row.count("W") for row in self.board.board)
        b = sum(row.count("B") for row in self.board.board)
        return 1 if w > b else (-1 if b > w else 0)

    def valid_moves(self, color):
        if self.game_finished():
            return []
        moves = set()
        for row in range(8):
            for col in range(8):
                if self.board.board[row][col] == "_":
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            r, c = row + dr, col + dc
                            found_opponent = False
                            while 0 <= r < 8 and 0 <= c < 8:
                                if self.board.board[r][c] == "_":
                                    break
                                if self.board.board[r][c] == color:
                                    if found_opponent:
                                        moves.add((row, col))
                                    break
                                found_opponent = True
                                r += dr
                                c += dc
        return list(moves)

    def make_move(self, row, col, color):
        if (row, col) in self.valid_moves(color):
            self.update_board(row, col, color)
            self.flip_tiles(row, col, color)
            return True
        return False

    def flip_tiles(self, row, col, color):
        flipped_tiles = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                found_opponent = False
                to_flip = []
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board.board[r][c] == "_":
                        break
                    if self.board.board[r][c] == color:
                        if found_opponent:
                            for flip_row, flip_col in to_flip:
                                flipped_tiles.append((flip_row, flip_col))
                                self.update_board(flip_row, flip_col, color)
                        break
                    found_opponent = True
                    to_flip.append((r, c))
                    r += dr
                    c += dc

        return flipped_tiles

    def computer_best_move(self):
        valid_moves_list = self.valid_moves("W")
        move = self.find_best_move(valid_moves_list)
        if move is None:
            return False
        self.update_board(move[0], move[1], "W")
        self.flip_tiles(move[0], move[1], "W")
        self.get_scores()
        return True

    def minimax(self, max_min, alpha, beta, depth):
        if self.game_finished():
            if self.find_winner() == 1:
                return 10000 - depth
            elif self.find_winner() == -1:
                return -10000 + depth
        if depth >= self.depth:
            print("return from depth")
            scores = self.get_scores()
            return scores[0] - scores[1]

        if max_min:
            current_valid_moves = self.valid_moves("W")
            mx_score = -100000
            for move in current_valid_moves:
                self.update_board(move[0], move[1], "W")
                tiles = self.flip_tiles(move[0], move[1], "W")
                mx_score = max(mx_score, self.minimax(False, alpha, beta, depth + 1))
                self.update_board(move[0], move[1], "_")
                for row, col in tiles:
                    self.update_board(row, col, "B")
                alpha = max(alpha, mx_score)
                if alpha >= beta:
                    break
            return mx_score
        else:
            current_valid_moves = self.valid_moves("B")
            mn_score = 10000
            for move in current_valid_moves:
                self.update_board(move[0], move[1], "B")
                tiles = self.flip_tiles(move[0], move[1], "B")
                mn_score = min(mn_score, self.minimax(True, alpha, beta, depth + 1))
                self.update_board(move[0], move[1], "_")
                for row, col in tiles:
                    self.update_board(row, col, "W")

                beta = min(beta, mn_score)
                if alpha >= beta:
                    break
            return mn_score

    def find_best_move(self, possible_moves):
        best_move = None
        alpha = -10000
        beta = 10000
        for move in possible_moves:
            self.update_board(move[0], move[1], "W")
            tiles = self.flip_tiles(move[0], move[1], "W")
            score = self.minimax(False, alpha, beta, 0)
            self.update_board(move[0], move[1], "_")
            for row, col in tiles:
                self.update_board(row, col, "B")
            if score > alpha:
                alpha = score
                best_move = move

        return best_move
