
"""Implement an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which,
 when dragged around the canvas, sets all of the rectangles it is in contact with to white."""

import tkinter as tk

# Define constants for canvas size, cell size, and eraser size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 40

# Function to erase cells in contact with the eraser
def erase_cells(event):
    # Calculate the eraser bounds based on mouse position
    left_x = event.x
    top_y = event.y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find all objects within the eraser bounds
    overlapping_objects = canvas.find_enclosed(left_x, top_y, right_x, bottom_y)
    for obj in overlapping_objects:
        # Set overlapping cells to white to simulate erasing
        canvas.itemconfig(obj, fill='white')

# Initialize the tkinter window
root = tk.Tk()
root.title("Canvas Eraser Example")

# Create the canvas widget
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Calculate the number of rows and columns based on cell size
num_rows = CANVAS_HEIGHT // CELL_SIZE
num_cols = CANVAS_WIDTH // CELL_SIZE

# Create a grid of blue cells
for row in range(num_rows):
    for col in range(num_cols):
        left_x = col * CELL_SIZE
        top_y = row * CELL_SIZE
        right_x = left_x + CELL_SIZE
        bottom_y = top_y + CELL_SIZE
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue', outline='black')

# Bind the mouse drag event to the erase function
canvas.bind('<B1-Motion>', erase_cells)

# Run the tkinter event loop
root.mainloop()
