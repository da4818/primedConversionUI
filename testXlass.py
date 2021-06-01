import tkinter as tk
from tkinter import *
from tkinter import Frame, Button
import PIL
from PIL import ImageTk
from PIL.Image import ANTIALIAS
from OldFiles.practice import *
from function_programs.files import *

root = Tk()
root.geometry("700x600")

class startPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Start Page")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        #Displays 3 menu options: Photoconversion, PRimed Conversion and previous data
        #photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), excitationPage("pc")))
        b = Button(self, text="Options", command=lambda: (self.destroy(), buttonsPage()))
        b.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        i = Button(self, text="Images", command=lambda: (self.destroy(), imagePage()))
        i.pack(side="left", fill="both", expand=True, padx=5, pady=5)


if __name__ == "__main__":
    startPage()
    root.mainloop()