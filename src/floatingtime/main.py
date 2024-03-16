import tkinter as tk
import time

def close_window():
    window.destroy()

def update_time():
    current_time = time.strftime('%H:%M:%S')  # Get current time in HH:MM:SS format
    label.config(text=current_time)
    window.after(1000, update_time)  # Update every second

# Create the main window without title bar and buttons
window = tk.Tk()
window.overrideredirect(True)  # Remove title bar and buttons
window.attributes('-topmost', 1)  # Make the window stay on top

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size and position (top-right corner)
window_width = 200
window_height = 100
x_pos = screen_width - window_width
y_pos = 0
window.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')

# Create a label widget with the current time
label = tk.Label(window, font=('Arial', 24), fg='white', bg='black')
label.pack(fill=tk.BOTH, expand=True)

# Update the time initially and schedule updates every second
update_time()

# Schedule the window to close after 5 seconds
window.after(5000, close_window)

# Start the main loop
window.mainloop()
