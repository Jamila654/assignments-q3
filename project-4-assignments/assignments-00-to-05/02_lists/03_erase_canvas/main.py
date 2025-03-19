from tkinter import Tk, Canvas
import time

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse coordinates from the last known position
    mouse_x, mouse_y = canvas.coords(eraser)[:2]  # Use eraser's current position
    
    # Calculate eraser bounds
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find overlapping objects
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # Change color of overlapping objects (except the eraser) to white
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def main():
    # Create the Tkinter root window
    root = Tk()
    root.title("Erase Canvas")
    
    # Create the canvas
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
    canvas.pack()
    
    # Create the grid of blue squares
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
    
    # Variables to store click coordinates
    click_coords = [0, 0]
    
    # Wait for a click to create the eraser
    def on_click(event):
        click_coords[0] = event.x
        click_coords[1] = event.y
        root.unbind('<Button-1>')  # Stop listening after first click
    
    canvas.bind('<Button-1>', on_click)
    canvas.wait_variable(root)  # Wait for the click event (simulates wait_for_click)
    
    # Create the eraser at the click position
    eraser = canvas.create_rectangle(
        click_coords[0], 
        click_coords[1], 
        click_coords[0] + ERASER_SIZE, 
        click_coords[1] + ERASER_SIZE, 
        fill='pink'
    )
    
    # Track mouse movement
    def move_eraser(event):
        # Move eraser to mouse position
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        # Erase overlapping objects
        erase_objects(canvas, eraser)
    
    # Bind mouse motion to move the eraser
    canvas.bind('<Motion>', move_eraser)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()