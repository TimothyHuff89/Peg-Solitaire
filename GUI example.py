import tkinter as tk

window = tk.Tk()

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

# Create a checkbox to help player
show_moves = tk.BooleanVar()

checkbox = tk.Checkbutton(window, text="Show Possible Moves", variable=show_moves)
checkbox.pack()

# Starting difficulty will be normal using radio buttons to toggle
difficulty = tk.StringVar(value="normal")
normal_radio = tk.Radiobutton(window, text="Normal", variable=difficulty, value="normal")
normal_radio.pack()
challenge_radio = tk.Radiobutton(window, text="Challenge", variable=difficulty, value="challenge")
challenge_radio.pack()

window.mainloop()