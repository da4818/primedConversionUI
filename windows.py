import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Entry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk
from generate_plots import choose_y
from matplotlib.figure import Figure


import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS
from skimage_image_analysis import get_files

from function_programs.analysis_data import *
root = Tk()
root.title("Primed Conversion Testing Stage")
root.geometry("650x600")
'''
Buttons are displayed in order of 
'Home','Regular Excitation','Photo Conversion','Primed Conversion', 'Load Previous Data'
'''

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
        exFrame = Frame(self, relief=RAISED, borderwidth=1)
        exFrame.pack(fill="both", expand=True)

        redButton = Button(exFrame, text="Red Excitation", command=lambda: (self.destroy(), colourExcitationPage("red")))
        redButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)
        greenButton = Button(exFrame, text="Green Excitation",
                             command=lambda: (self.destroy(), colourExcitationPage('green')))
        greenButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)

        self.pack(fill="both", expand=True)

        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage())) #Closes the current page and calls the next page to appear within the same frame
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

'''
The red and green excitation will perform similar commands, 
but will vary in terms of the title name and the type of light to turn on and off
Here, a validation check is used to confirm whether red or green excitation occurs - 
appropriate functions will be added accordingly
'''
class colourExcitationPage(Frame):
    def __init__(self, colour):
        super().__init__()
        if colour == 'red':
            print('Red light')
            self.master.title("Excitation - Red LED")
        elif colour == 'green':
            print('Green light')
            self.master.title("Excitation - Green LED")

        frame = Frame(self, relief="raised", borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        startButton = Button(self, text="Start Excitation", command=lambda: (display_LED_message(frame), frame.after(4000, analysisPage(1, frame)))) #Closes the current page and calls the next page to appear within the same frame
        startButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        stopButton = Button(self, text="Stop")
        stopButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        backButton = Button(self, text="Back", command=lambda: (self.destroy(), excitationPage()))
        backButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        #Closes the current page and calls the next page to appear within the same frame





#PRIMED CONVERSION PAGE
class primedPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Primed Conversion")
        prFrame = Frame(self, relief=RAISED, borderwidth=1)
        prFrame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        startButton = Button(prFrame, text="Start Primed Conversion")
        startButton.pack(fill="both", expand=True, padx=5, pady=5)
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
        pcFrame = Frame(self, relief=RAISED, borderwidth=1)
        pcFrame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        startButton = Button(pcFrame, text="Start Photo Conversion", command=lambda: (startButton.forget(), analysisPage(2, pcFrame)))
        startButton.pack(fill="both", expand=True, padx=5, pady=5)

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
        dataFrame = Frame(self, relief=RAISED, borderwidth=1)
        dataFrame.pack(fill="both", expand=True)

        imageinfo = get_files()
        canvas = tk.Canvas(dataFrame, width = 300, height = 500, bg='gray92')
        canvas.pack(fill="both", expand=True, pady=5)
        for i in range(len(imageinfo)):
            photo = PIL.Image.open(os.path.join(imageinfo[i].path, imageinfo[i].name)).resize((150, 150), ANTIALIAS)
            render = ImageTk.PhotoImage(photo)
            img = Label(canvas, text="Test "+str(i+1), image=render, compound="bottom")
            img.image = render
            img.pack(side="left", anchor=NW, fill="none", expand=True, padx=5, pady=5)

        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        excitationButton = Button(self, text="Regular Excitation", command=lambda: (self.destroy(), excitationPage()))
        excitationButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage()))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

class analysisPage(Frame):
    def __init__(self,val, frame):
        super().__init__()
        self.master.title("Image Analysis")
        #self.pack(fill="both", expand=True)
        show_label(val, frame)

def show_label(val, frame):
    x = [1,2,3]
    y, is_valid = choose_y(val)
    print(y)
    if (is_valid == False):
        print("Invalid number")
    fig = plt.figure(1)
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Test')
    canvas = FigureCanvasTkAgg(fig, frame)
    fig.canvas.draw()
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    test = Button(frame, text='Adjust peak detection')
    test.pack(side="left", fill="both", expand=True, padx=5, pady=5)

def only_numbers(char):
    return char.isdigit()

def message(frame, label):
    label['text'] = "LED off..."
    frame.after(1000, remove_message, label)
def remove_message(label):
    label.forget()
def display_LED_message(frame):
    label = Label(frame, text="LED on...", bg='gray92')
    label.pack()
    frame.after(1000, message, frame, label)

if __name__ == "__main__":
    startPage()
    root.mainloop()
