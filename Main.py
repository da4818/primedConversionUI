import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Primed Conversion Testing Stage')
window.geometry("400x400")
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=1, column=i, padx=5, pady=5)
    label = tk.Label(master=frame, text=f"Row {i}")
    label.pack(padx=5, pady=5)
window.mainloop()
