#I have put this function in another file to make the reading easier.


import tkinter as tk
from tkinter import ttk, Label, Button, PhotoImage, filedialog

import PIL
from PIL import Image, ImageTk




def display_excitation():
    e_window = tk.Toplevel()
    e_window.title('Excitation Testing Stage')
    e_window.geometry("600x600")
    e_window.columnconfigure(0, weight=1, minsize=75)
    e_window.columnconfigure(1, weight=1, minsize=75)
    e_window.rowconfigure(0, weight=1, minsize=50)
    e_window.rowconfigure(1, weight=1, minsize=75)
    e_window.rowconfigure(2, weight=1, minsize=50)
    button_red = Button(e_window, text="Red Excitation", foreground="Red")
    button_green = Button(e_window, text="Green Excitation", foreground="Green")
    e_frame = tk.Frame(
        master = e_window,
        relief = tk.RAISED,
        borderwidth = 1
    )
    e_frame.grid(row=0, column=0, padx=5, pady=5)
    button_red.grid(row=1, column=0)
    e_frame.grid(row=0, column=1, padx=5, pady=5)
    button_green.grid(row=1, column=1)
    #Small text to explain the use of each button.
    Text_Green = Label(e_window, text=" Click on 'Green Excitation' \n  to excite the samples \n with the 488nm LED ")
    Text_Red = Label(e_window, text=" Click on 'Red Excitation'\n to excite the samples\n with the 540nm LED ")
    Text_Green.grid(row=0, column=1)
    Text_Red.grid(row=0, column=0)
    e_window.mainloop()