from board import EnglishBoard, DiamondBoard, HexagonBoard
from move import Move


# Test 1: Create boards
print("=== Test 1: Board Creation ===")

for BoardType in [EnglishBoard, DiamondBoard, HexagonBoard]:
    board = BoardType(7)
    board.create_board()

    print(f"\n{BoardType.__name__}")
    for row in board.grid:
        print(row)


# Test 2: Valid move
print("\n=== Test 2: Valid Move ===")

board = EnglishBoard(7)
board.create_board()

move = Move(board)

result = move.execute_move(3, 1, 3, 3)

print("Move successful:", result)
print("Starting position:", board.grid[3][1])
print("Jumped position:", board.grid[3][2])
print("Destination:", board.grid[3][3])


# Test 3: Invalid move
print("\n=== Test 3: Invalid Move ===")

board = EnglishBoard(7)
board.create_board()

move = Move(board)

result = move.execute_move(3, 0, 3, 3)

print("Move successful:", result)


# Test 4: Winning condition
print("\n=== Test 4: Winning Condition ===")

board = EnglishBoard(7)
board.create_board()

for i in range(board.size):
    for j in range(board.size):
        if board.grid[i][j] == 1:
            board.grid[i][j] = 0

board.grid[3][3] = 1

print("Win detected:", board.check_win())


# Test 5: Losing condition
print("\n=== Test 5: Losing Condition ===")

board = EnglishBoard(7)
board.create_board()

for i in range(board.size):
    for j in range(board.size):
        if board.grid[i][j] == 1:
            board.grid[i][j] = 0

board.grid[3][2] = 1
board.grid[3][4] = 1

move = Move(board)

print("Loss detected:", move.check_loss())