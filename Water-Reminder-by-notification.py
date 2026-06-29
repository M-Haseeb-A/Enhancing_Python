# This program will remind you after one hour by showing popup

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

def show_popup():
    messagebox.showinfo("Reminder", "It's time to drink water!")
    root.after(3600*1000,show_popup) 

root.after(3600*1000, show_popup)

root.mainloop()