import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button

from PIL import Image
from PIL.ImageTk import PhotoImage

from image_analysis import get_file

root = Tk()
root.title("Primed Conversion Testing Stage")
root.geometry("650x600")

#Buttons are displayed in order of 'Home', 'Regular Excitation', 'Photo Conversion', 'Primed Conversion', 'Load Previous Data'

#START PAGE
class startPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage()))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#EXCITATION PAGE
class excitationPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Regular Excitation")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        redButton = Button(self, text="Red Excitation")
        redButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)
        greenButton = Button(self, text="Green Excitation")
        greenButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)

        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage())) #Closes the current page and calls the next page to appear within the same frame
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data",command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#PRIMED CONVERSION PAGE
class primedPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Primed Conversion")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)

        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage()))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

class photoPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Photo Conversion")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load previous data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

class dataPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Previous Data")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame, width = 500, height = 400)
        canvas.pack(pady=20)
        image = Image.open("example3.png") # This function returns the name of the png file to be imported
        image = image.resize((476, 378), Image.ANTIALIAS)
        img = PhotoImage(image)
        canvas.create_image(12, 11, anchor=tk.NW, image=img)#(500-476)/2=12, (400-378)/2=11

        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage()))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

if __name__ == "__main__":
    startPage()
    root.mainloop()
root.mainloop()