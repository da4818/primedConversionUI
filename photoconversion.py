#I have put this function in another file to make the reading easier.
import tkinter as tk
from tkinter import ttk, Label, Button, PhotoImage, filedialog
import PIL
from PIL import Image, ImageTk
from image_analysis import send_message, get_file # We can use this to use functions from other python scripts
# Setting up the initial window


def display_photo_conversion():
    pc_window = tk.Toplevel()
    pc_window.title('Photo Conversion Testing Stage')
    pc_window.geometry("800x600")
    text_pc=Label(pc_window, text="To photoconvert the samples, a 405nm LED is used."
                                  "\n Click on the following button to start the experiment.").pack()
    b_pc = Button(pc_window, text="Start Photo Conversion").pack()
    pc_window.mainloop()