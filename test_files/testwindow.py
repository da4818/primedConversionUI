
import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS

root = Tk()
root.title("Testing Stage")
root.geometry("650x600")

from function_programs.save_create_files import *
canvas = tk.Canvas(root, width = 300, height = 500)
canvas.pack(fill="both", expand=True, pady=5)

images, names = save_analysis_images("green", "pc")

for i,j in zip(images, names):
    photo = PIL.Image.open(i).resize((150, 150), ANTIALIAS)
    render = ImageTk.PhotoImage(photo)
    img = Label(canvas, text=j, image=render, compound="bottom")
    img.image = render
    img.pack(side="left", anchor=NW, fill="none", expand=True, padx=5, pady=5)

root.mainloop()

