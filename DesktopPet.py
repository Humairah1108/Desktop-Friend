import tkinter as tk
from PIL import Image, ImageTk

# Initialize main window
root = tk.Tk()
root.title("Moving Desktop Pet")
root.geometry("200x200")
root.overrideredirect(True)  # Remove window borders
root.attributes("-topmost", True)  # Keep on top

# Set transparent background
root.config(bg="white")  # Set background color (must match the transparency color)
root.wm_attributes("-transparentcolor", "white")  # Make "white" transparent

# List of animation frames
frame_files = [r"sprite/mushrooms/Mushroom_Run_1.png", r"C:\Users\ASUS\Desktop\DesktopPet\sprite\mushrooms\Mushroom_Run_2.png", r"C:\Users\ASUS\Desktop\DesktopPet\sprite\mushrooms\Mushroom_Run_3.png"]
  # Replace with your frames
frames = [
    ImageTk.PhotoImage(
        Image.open(f).resize((100, 100), Image.Resampling.LANCZOS)
    ) for f in frame_files
]

# Create label to display the pet
label = tk.Label(root, bg="white")  # Use same background color as transparency
label.pack()

# Animation index
frame_index = 0

# Pet's position and speed
x, y = 100, 100  # Initial position
dx, dy = 5, 0    # Speed (move rightwards initially)

# Function to animate the pet
def animate():
    global frame_index
    label.config(image=frames[frame_index])  # Update to the next frame
    frame_index = (frame_index + 1) % len(frames)  # Cycle frames
    root.after(100, animate)  # Adjust timing for smooth animation

# Function to move the pet
def move():
    global x, y, dx, dy
    # Update position
    x += dx
    y += dy

    # Boundary conditions (prevent pet from moving off-screen)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if x < 0 or x > screen_width - 100:  # Reverse direction on horizontal bounds
        dx *= -1
    if y < 0 or y > screen_height - 100:  # Reverse direction on vertical bounds
        dy *= -1

    # Apply new position
    root.geometry(f"+{x}+{y}")
    root.after(50, move)  # Adjust timing for smooth movement

# Dragging functionality
def on_drag(event):
    global x, y, dx, dy
    x, y = root.winfo_pointerxy()  # Update position to mouse pointer
    root.geometry(f"+{x}+{y}")
    dx, dy = 0, 0  # Stop movement when dragged

label.bind("<B1-Motion>", on_drag)

# Start animation and movement
animate()
move()

# Run the application
root.mainloop()
