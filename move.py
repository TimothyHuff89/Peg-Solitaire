from board import EnglishBoard, HexagonBoard


class Move():
    def __init__(self, board):
        self.board = board

    def validate_move(self, start_row, start_col, end_row, end_col) -> bool:

        mid_row_index = (start_row + end_row) // 2
        mid_col_index = (start_col + end_col) // 2
        row_diff = end_row - start_row
        col_diff = end_col - start_col

        #boundary check to assist with win/loss detection
        if start_row < 0 or start_row >= self.board.size:
            return False

        if start_col < 0 or start_col >= self.board.size:
            return False

        if end_row < 0 or end_row >= self.board.size:
            return False

        if end_col < 0 or end_col >= self.board.size:
            return False

        #check for valid piece to move
        if self.board.grid[start_row][start_col] != 1:
            return False

        #check to ensure that the destination is empty
        if self.board.grid[end_row][end_col] != 0:
            return False

        #if moving row ensure there is a piece to jump
        if abs(row_diff) == 2 and abs(col_diff) == 0:
            
            if self.board.grid[mid_row_index][start_col] != 1:
                return False

        #if moving col ensure there is a piece to jump
        elif abs(col_diff) == 2 and abs(row_diff) == 0:

            if self.board.grid[start_row][mid_col_index] != 1:
                return False
            
        #check if valid diagonal piece to jump
        elif abs(row_diff) == 2 and abs(col_diff) == 2:

            #restrict diagonal movement for Hexagon board
            if isinstance(self.board, HexagonBoard):
                return False

            #restrict diagonal movement for English board
            if isinstance(self.board, EnglishBoard):
                return False
            
            if self.board.grid[mid_row_index][mid_col_index] != 1:
                return False

        else:
            return False

        return True

    def execute_move(self, start_row, start_col, end_row, end_col) -> bool:
        if self.validate_move(start_row, start_col, end_row, end_col):
            mid_row_index = (start_row + end_row) // 2
            mid_col_index = (start_col + end_col) // 2

            self.board.grid[start_row][start_col] = 0
            self.board.grid[end_row][end_col] = 1
            self.board.grid[mid_row_index][mid_col_index] = 0

            return True
        else:
            return False

    def check_loss(self) -> bool:

        if self.board.check_win():
            return False

        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.grid[i][j] == 1:
                    if self.validate_move(i, j, i + 2, j + 2):
                        return False
                    elif self.validate_move(i, j, i + 2, j - 2):
                        return False
                    elif self.validate_move(i, j, i - 2, j + 2):
                        return False
                    elif self.validate_move(i, j, i - 2, j - 2):
                        return False
                    elif self.validate_move(i, j, i + 2, j):
                        return False
                    elif self.validate_move(i, j, i - 2, j):
                        return False
                    elif self.validate_move(i, j, i, j + 2):
                        return False
                    elif self.validate_move(i, j, i, j - 2):
                        return False

        return True
