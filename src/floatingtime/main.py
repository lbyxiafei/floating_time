import tkinter as tk

def close_window():
    window.destroy()

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

# Create a label widget
label = tk.Label(window, text='Floating Window')
label.pack(pady=20)

# Schedule the window to close after 5 seconds
window.after(5000, close_window)

# Start the main loop
window.mainloop()
