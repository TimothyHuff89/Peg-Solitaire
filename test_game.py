import unittest
from board import HexagonBoard, DiamondBoard, EnglishBoard
from move import Move

class TestBoard(unittest.TestCase):

    def test_all_board_types(self):
        for BoardType in [EnglishBoard, DiamondBoard, HexagonBoard]:
            board = BoardType(7)
            board.create_board()

            self.assertEqual(len(board.grid), 7)
            self.assertEqual(len(board.grid[0]), 7)
            self.assertEqual(board.grid[3][3], 0)

    def test_valid_horizontal_move(self):
        # Create and initialize a 7x7 English board
        board = EnglishBoard(7)
        board.create_board()

        # Set up a valid horizontal move
        board.grid[3][1] = 1  # Starting peg
        board.grid[3][2] = 1  # Peg to jump over
        board.grid[3][3] = 0  # Empty destination

        # Create a Move object
        move = Move(board)

        # Execute the move
        result = move.execute_move(3, 1, 3, 3)

        # Verify that the move was successful
        self.assertTrue(result)

        # Verify the board was updated correctly
        self.assertEqual(board.grid[3][1], 0)  # Starting position is empty
        self.assertEqual(board.grid[3][2], 0)  # Jumped peg was removed
        self.assertEqual(board.grid[3][3], 1)  # Destination contains the peg

    def test_valid_vertical_move(self):
        # Create and initialize a 7x7 English Board
        board = EnglishBoard(7)
        board.create_board()

        board.grid[1][3] = 1
        board.grid[2][3] = 1
        board.grid[3][3] = 0

        # Create a Move object
        move = Move(board)

        # Execute the move
        result = move.execute_move(1, 3, 3, 3)

        # Verify that the move was sucessful
        self.assertTrue(result)

        # Verify the board was updated
        self.assertEqual(board.grid[1][3], 0)
        self.assertEqual(board.grid[2][3], 0)
        self.assertEqual(board.grid[3][3], 1)


    def test_diagonal_move_rules(self):
        for BoardType in [DiamondBoard, EnglishBoard]:
            board = BoardType(7)
            board.create_board()

            # Construct a diagonal jump
            board.grid[1][1] = 1
            board.grid[2][2] = 1
            board.grid[3][3] = 0

            move = Move(board)
            result = move.execute_move(1, 1, 3, 3)

            if BoardType == DiamondBoard:
                self.assertTrue(result)
            else:
                self.assertFalse(result)

    def test_invalid_move(self):
        board = EnglishBoard(7)
        board.create_board()

        move = Move(board)

        # Save the board before attempting the move
        original_grid = [row.copy() for row in board.grid]

        # Attempt an invalid move (three spaces instead of two)
        result = move.execute_move(3, 0, 3, 3)

        # Verify the move was rejected
        self.assertFalse(result)

        # Verify the board was not changed
        self.assertEqual(board.grid, original_grid)

if __name__ == "__main__":
    unittest.main()