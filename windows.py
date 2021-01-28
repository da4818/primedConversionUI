import tkinter as tk
from tkinter import *
from image_analysis import sendMessage # We can use this to use functions from other python scripts

# Setting up the initial window
window = tk.Tk()
window.title('Home')
window.geometry("600x600")

def display_primed_conversion():
    pr_window = tk.Tk()
    pr_window.title('Primed Conversion Testing Stage')
    pr_window.geometry("600x600")
    output = Label(pr_window, text=sendMessage())
    output.place(x=100, y=100)
# When Primed Conversion button is pressed, it will display "Example code" to the window as a label

def display_photo_conversion():
    pc_window = tk.Tk()
    pc_window.title('Photo Conversion Testing Stage')
    pc_window.geometry("600x600")

def display_excitation():
    e_window = tk.Tk()
    e_window.title('Excitation Testing Stage')
    e_window.geometry("600x600")

b1 = Button(window, text="Regular Excitation", command=display_excitation)
b2 = Button(window, text="Photo Conversion", command=display_photo_conversion)
b3 = Button(window, text="Primed Conversion", command=display_primed_conversion)

#b1.grid(row=0, column=0)
#b2.grid(row=1, column=1)
#b3.grid(row=1, column=2)

# This produces a grid structure so we can add the buttons in a grid format
window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)
window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)
frame = tk.Frame(
    master = window,
    relief = tk.RAISED,
    borderwidth = 1
)
frame.grid(row=1, column=0, padx=5, pady=5)
b1.grid(row=2, column=0)
frame.grid(row=1, column=1, padx=5, pady=5)
b2.grid(row=2, column=1)
frame.grid(row=1, column=3, padx=5, pady=5)
b3.grid(row=2, column=2)

window.mainloop()
