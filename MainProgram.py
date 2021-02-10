import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Frame, Button

import PIL
from PIL import Image
from PIL.ImageTk import PhotoImage

from image_analysis import get_file
from arduino import arduino_connection
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
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)

        redButton = Button(frame, text="Red Excitation", command=lambda: (self.destroy(), colourExcitationPage("red")))
        redButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)
        greenButton = Button(frame, text="Green Excitation",
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

        startButton = Button(self, text="Start Excitation", command=lambda: (display_LED_message(frame), arduino_connection(colour))) #Closes the current page and calls the next page to appear within the same frame
        startButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        stopButton = Button(self, text="Stop") #Closes the current page and calls the next page to appear within the same frame
        stopButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        backButton = Button(self, text="Back", command=lambda: (self.destroy(), excitationPage()))
        backButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)


def message(frame, label):
    label['text'] = "Stopping LED..."
    frame.after(2000, remove_message, label)
def remove_message(label):
    label.forget()


def display_LED_message(frame):
    label = Label(frame, text="Starting LED...", bg='gray92')
    label.pack()
    '''
    As the label is in a white box - this is to match the window
    Here the function to turn the light on/off will coded - 
    for now there is a delay that simulate the time taken to perform the excitation
    '''

    frame.after(2000, message, frame, label)

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
        #photo = PIL.Image.open("example3.png")
        #photo.show()
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

# opens file explorer at program path, useful to choose images to analyze or to load previously analyzed data
def get_file(filetype="img"):
    # default is image file loader bc it'll be used in more windows than data loader
    if filetype == "img":
        # function returns directory path for chosen file(s) as tuple
        filename = filedialog.askopenfilenames(initialdir='C:\IdeaProjects\primedConversionUI', title="Select a file",
                                               filetype=(
                                                   ("png files", "*.png"),
                                                   ("jpg files", "*.jpg"),
                                                   ("tif files", "*.tif"),
                                               ))
        # random example code opening one or more images
        if len(filename) > 1:
            for image in filename:
                photo = PIL.Image.open(image)
                photo.show()
        elif len(filename) == 1:
            photo = PIL.Image.open(filename[0])
            photo.show()
    # will add specific filetype instead of pdf for data when we know what we're saving it as
    else:
        filename = filedialog.askopenfilename(initialdir='C:\IdeaProjects\primedConversionUI', title="Select a file",
                                              filetype=(("All files", "*.pdf"), ("all files", "*.*")))


if __name__ == "__main__":
    startPage()
    root.mainloop()
