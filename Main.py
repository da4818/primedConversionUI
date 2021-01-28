import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title('Home')
window.geometry("400x400")

def display_primed_conversion():
    window.title('Primed Conversion Testing Stage')

def display_photo_conversion():
    window.title('Photo Conversion Testing Stage')

def display_excitation():
    window.title('Excitation Testing Stage')


b1 = Button(window, text="Regular Excitation", command=display_excitation)
b2 = Button(window, text="Photo Conversion", command=display_photo_conversion)
b3 = Button(window, text="Primed Conversion", command=display_primed_conversion)

#b1.grid(row=0, column=0)
#b2.grid(row=1, column=1)
#b3.grid(row=1, column=2)

window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)
window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)
frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame.grid(row=1, column=0, padx=5, pady=5)
b1.grid(row=2, column=0)
frame.grid(row=1, column=1, padx=5, pady=5)
b2.grid(row=2, column=1)
frame.grid(row=1, column=3, padx=5, pady=5)
b3.grid(row=2, column=2)

window.mainloop()
