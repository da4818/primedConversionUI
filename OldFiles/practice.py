
import tkinter as tk
from tkinter import *

from tkinter import Frame, Button
import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS
root = Tk()
root.geometry("700x600")

class startPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        self.canvas = Canvas(frame, bg = 'pink')
        self.canvas.pack(side = "right", fill = "both", expand = True)

        self.button_frame = Frame(self.canvas, bg = 'purple')
        self.canvas.pack(side = "left", fill = "both", expand = True)

        scrollbar = Scrollbar(self.canvas, orient = "vertical", bg="bisque", command = self.canvas.yview)
        scrollbar.pack(side = "right", fill = "y")

        self.canvas_frame = self.canvas.create_window((0,0), window=self.button_frame, anchor = "nw")

        self.canvas.config(yscrollcommand = scrollbar.set)

        self.button_frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind('<Configure>', self.frameWidth)

        rows = 10
        columns = 3
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            #Grid.grid_rowconfigure(buttonFrame, i, weight=1)
            for j in range(0, columns):
                Grid.grid_columnconfigure(self.button_frame, j, weight=1)
                buttons[i][j] = tk.Button(self.button_frame, height=10, width=10, text=((columns*i)+j+1))
                buttons[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        h = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        h.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def frameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    startPage()
    root.mainloop()