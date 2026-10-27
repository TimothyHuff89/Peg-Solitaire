import tkinter as tk
from tkinter import messagebox
from board import EnglishBoard, DiamondBoard, HexagonBoard
from move import Move

window = tk.Tk()

BOARD_X = 25
BOARD_Y = 50
BOARD_WIDTH = 650
BOARD_HEIGHT = 400

# Create a text label
label = tk.Label(window, text="Peg Solitaire")
label.pack()

# Create a box using lines
canvas = tk.Canvas(window, width=700, height=500)
canvas.pack()

canvas.create_line(25, 50, 675, 50)
canvas.create_line(25, 50, 25, 450)
canvas.create_line(675, 50, 675, 450)
canvas.create_line(25, 450, 675, 450)

#create EnglishBoard
board = EnglishBoard(7)
board.create_board()

def draw_board():
    #removes previously drawn circles
    canvas.delete("pegs")

    #distance between board positions
    #if diamond change the spacing to help for better play
    if isinstance(board, DiamondBoard):
        spacing = min(
            BOARD_WIDTH / (board.size * 2**0.5),
            BOARD_HEIGHT / (board.size * 2**0.5)
        )
    else:
        spacing = min(BOARD_WIDTH / board.size, BOARD_HEIGHT / board.size)

    #makes each circle 70% of spacing for gaps between cirlces
    diameter = spacing * 0.7

    #centers board inside of playing area
    start_x = BOARD_X + (BOARD_WIDTH - spacing * board.size) / 2
    start_y = BOARD_Y + (BOARD_HEIGHT - spacing * board.size) / 2

    for row in range(board.size):
        for col in range(board.size):
            if board.grid[row][col] != -1:
                if isinstance(board, DiamondBoard):
                    center_x = BOARD_X + BOARD_WIDTH / 2
                    center_y = BOARD_Y + BOARD_HEIGHT / 2

                    rotated_x = (col - row) * spacing / 2**0.5
                    rotated_y = (col + row - (board.size - 1)) * spacing / 2**0.5

                    x = center_x + rotated_x - diameter / 2
                    y = center_y + rotated_y - diameter / 2

                else:
                    x = start_x + col * spacing
                    y = start_y + row * spacing

                if board.grid[row][col] == 1:
                    color = "blue"
                else:
                    color = "white"

                canvas.create_oval(
                    x, y,
                    x + diameter, y + diameter,
                    outline="black",
                    fill=color,
                    tags="pegs"
                )

move = Move(board)
selected_peg = None
game_over = False

def handle_click(event):
    global selected_peg, game_over

    if game_over:
        return

    #handle the mouse click area for the diamond board
    if isinstance(board, DiamondBoard):
        # Use the same spacing as draw_board()
        spacing = min(
            BOARD_WIDTH / (board.size * 2**0.5),
            BOARD_HEIGHT / (board.size * 2**0.5)
        )

        diameter = spacing * 0.7

        center_x = BOARD_X + BOARD_WIDTH / 2
        center_y = BOARD_Y + BOARD_HEIGHT / 2

        # Mouse position relative to the board's center
        dx = event.x - center_x
        dy = event.y - center_y

        # Convert rotated screen coordinates back to grid coordinates
        col = round(
            (dx + dy) / (spacing * 2**0.5)
            + (board.size - 1) / 2
        )

        row = round(
            (dy - dx) / (spacing * 2**0.5)
            + (board.size - 1) / 2
        )

        # Check that the click is close to the center of a peg
        peg_x = center_x + (col - row) * spacing / 2**0.5
        peg_y = center_y + (col + row - (board.size - 1)) * spacing / 2**0.5

        if (event.x - peg_x)**2 + (event.y - peg_y)**2 > (diameter / 2)**2:
            return

    else:
        # Existing click detection for English and Hexagon boards
        spacing = min(BOARD_WIDTH / board.size, BOARD_HEIGHT / board.size)

        start_x = BOARD_X + (BOARD_WIDTH - spacing * board.size) / 2
        start_y = BOARD_Y + (BOARD_HEIGHT - spacing * board.size) / 2

        col = int((event.x - start_x) // spacing)
        row = int((event.y - start_y) // spacing)
        
        # Ignore clicks outside the board
        if not (0 <= row < board.size and 0 <= col < board.size):
            return

    if selected_peg is None:
        # First click must select a peg
        if board.grid[row][col] == 1:
            selected_peg = (row, col)
            print("Selected peg:", selected_peg)
    else:
        # Second click selects the destination
        start_row, start_col = selected_peg

        if move.execute_move(start_row, start_col, row, col):
            print("Valid move!")
            draw_board()

            if board.check_win():
                game_over = True
                messagebox.showinfo("You Win!", "Congratulations! You won!")
            elif move.check_loss():
                game_over = True
                messagebox.showinfo("Game Over", "No valid moves remaining!")

        else:
            print("Invalid move!")

        #resets the selected_peg to allow for new peg
        selected_peg = None


canvas.bind("<Button-1>", handle_click)
draw_board()

board_type = tk.StringVar(value="English")

board_menu = tk.OptionMenu(
    window,
    board_type,
    "English",
    "Diamond",
    "Hexagon"
)
board_menu.pack()

board_size = tk.IntVar(value=7)

size_menu = tk.OptionMenu(
    window,
    board_size,
    7,
    11,
    13
)
size_menu.pack()

def new_game():
    global board, move, selected_peg, game_over

    #reset game over when new game is created
    game_over = False

    selected_type = board_type.get()
    selected_size = board_size.get()

    if selected_type == "English":
        board = EnglishBoard(selected_size)
    elif selected_type == "Diamond":
        board = DiamondBoard(selected_size)
    else:
        board = HexagonBoard(selected_size)

    board.create_board()
    move = Move(board)
    selected_peg = None

    draw_board()

new_game_button = tk.Button(window, text="New Game", command=new_game)
new_game_button.pack()

window.mainloop()