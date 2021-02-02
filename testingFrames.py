import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Style

#Function to display the desired frame
#def show_frame(frame):
    #frame.tkraise()

root = Tk()
root.title("Primed Conversion Testing Stage")
root.geometry("650x600")


#START PAGE
class startPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion")
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load previous data")
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#EXCITATION PAGE
class excitationPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Regular Excitation")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion")
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load previous data")
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#PRIMED CONVERSION PAGE
class primedPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Primed Conversion")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion")
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load previous data")
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

if __name__ == "__main__":
    startPage()
    root.mainloop()
root.mainloop()