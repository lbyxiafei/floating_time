import tkinter as tk
import time
import pygetwindow as gw

from pygetwindow import PyGetWindowException


class TimeWindow:
    def __init__(self):
        self.cw = gw.getActiveWindow()  # Get current active window

        self.window = tk.Tk()
        self.window.overrideredirect(True)  # Remove title bar and buttons
        self.window.attributes("-topmost", 1)  # Make the window stay on top
        self.window.attributes("-alpha", 0.8)  # Set the -alpha value to 0.6

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

        self.label = tk.Label(self.window, font=("Arial", 36, "bold"), fg="white", bg="black")
        self.label.pack(fill=tk.BOTH, expand=True)

        self.update_time()
        self.window.after(10000, self.close_window)

    def _change_focus_back(self):
        try:
            self.cw.activate()
        except PyGetWindowException as ex:
            print(ex)

    def update_time(self):
        self._change_focus_back()
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.window.update_idletasks()
        self.window.after(1000, self.update_time)

    def show(self):
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()
