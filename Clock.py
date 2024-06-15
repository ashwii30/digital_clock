import tkinter as tk
import time

def update_time():
    # Get the current time in 12-hour format with AM/PM
    current_time = time.strftime("%I:%M:%S %p")
    # Update the time label
    time_label.config(text=current_time)
    # Schedule the update_time function to be called after 1000ms (1 second)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
time_label.pack()

update_time()

root.mainloop()
