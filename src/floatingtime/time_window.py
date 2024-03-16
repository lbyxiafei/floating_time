import tkinter as tk
import time


class TimeWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.overrideredirect(True)  # Remove title bar and buttons
        self.window.attributes("-topmost", 1)  # Make the window stay on top
        self.window.attributes("-alpha", 0.6)  # Set the -alpha value to 0.6

        # Calculate the screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        # Set the window size and position (top-right corner)
        self.window_width = 200
        self.window_height = 100
        self.x_pos = self.screen_width - self.window_width
        self.y_pos = 0
        self.window.geometry(
            f"{self.window_width}x{self.window_height}+{self.x_pos}+{self.y_pos}"
        )
        # Create a label widget with the current time
        self.label = tk.Label(self.window, font=("Arial", 24), fg="white", bg="black")
        self.label.pack(fill=tk.BOTH, expand=True)

        self.update_time()  # Update the time initially and schedule updates every second
        self.window.after(10000, self.close_window)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
        self.label.config(text=current_time)
        self.window.update_idletasks()  # Update the window without taking focus

        # Schedule the update_time method every second
        self.window.after(1000, self.update_time)

    def show(self):
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()
