class Board:
    def __init__(self, size):
        self.size = size
        self.grid = []

    def create_board(self):
        self.grid = []

        for i in range(self.size):
            row = []

            for j in range(self.size):
                row.append(-1)

            self.grid.append(row)

    def check_win(self) -> bool:

        count = 0

        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 1:
                    count += 1

        if count == 1:
            return True
        else:
            return False
                    

class EnglishBoard(Board):
    def create_board(self):
        super().create_board()

        #English board initialization
        center = self.size // 2
        arm_width = self.size // 4
        lower = center - arm_width
        upper = center + arm_width

        for i in range(self.size):
            for j in range(self.size):
                if lower <= i <= upper:
                    self.grid[i][j] = 1
                elif lower <= j <= upper:
                    self.grid[i][j] = 1

        self.grid[center][center] = 0

class DiamondBoard(Board):
    def create_board(self):
        super().create_board()

        #Diamond board initialization
        center = self.size // 2

        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = 1

        self.grid[center][center] = 0

class HexagonBoard(Board):
    def create_board(self):
        super().create_board()

        #Hexagon board initialization
        center = self.size // 2
        arm_width = self.size // 4
        lower = center - arm_width
        upper = center + arm_width

        for i in range(self.size):
            for j in range(self.size):
                if lower <= i <= upper:
                    self.grid[i][j] = 1
                elif lower <= j <= upper:
                    self.grid[i][j] = 1
                elif i < lower and j < lower:
                    if i + j >= lower:
                        self.grid[i][j] = 1
                elif i < lower and j > upper:
                    if j - i <= upper:
                        self.grid[i][j] = 1
                elif i > upper and j < lower:
                    if i - j <= upper:
                        self.grid[i][j] = 1
                elif i > upper and j > upper:
                    if i + j <= upper + self.size - 1:
                        self.grid[i][j] = 1


        self.grid[center][center] = 0

