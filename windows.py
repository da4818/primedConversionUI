import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Entry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk
import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS
from function_programs.skimage_image_analysis import get_files
from function_programs.image_analysis import *
from function_programs.files import *
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
        #, frame.after(4000, analysisPage(frame, "sample.png"))
        startButton = Button(self, text="Start Excitation", command=lambda: (display_LED_message(self, frame))) #Closes the current page and calls the next page to appear within the same frame
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
        startButton = Button(pcFrame, text="Start Photo Conversion", command=lambda: (startButton.forget(), analysisPage(pcFrame,"sample.png")))
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
    def __init__(self, frame, filename):
        super().__init__()
        self.master.title("Image Analysis")
        d = 25
        img, img1 = export_images(filename)
        fig = plt.figure(constrained_layout=True)
        spec = fig.add_gridspec(2, 2)
        a = fig.add_subplot(spec[0, 0])
        a.imshow(img)
        a.axis('off')
        a.set_title("Normalised")
        b = fig.add_subplot(spec[0, 1])
        b.imshow(img1)
        b.axis('off')
        b.set_title("Masked")
        c = fig.add_subplot(spec[1, 0:2])
        self.show_graph(c, fig, 25, filename)
        canvas = FigureCanvasTkAgg(fig, frame)

        plot_widget = canvas.get_tk_widget()
        plot_widget.pack(side="top", fill="both", expand=False, padx=5, pady=5)
        number = tk.StringVar()
        peak_criteria_entry = Entry(frame, textvariable=number, width=2)
        peak_criteria_entry.pack(side="left", fill="both", expand=True)
        adjust_peak = Button(frame, text='Adjust peak detection', command=lambda: (self.submit(number, c, fig, d)))
        adjust_peak.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        max_peak = Button(frame, text='Get highest value')
        max_peak.pack(side="top", fill="both", expand=True, padx=5, pady=5)





    def show_graph(self, c, fig, distance, filename):
        thresholds, colours = get_thresholds()
        hist, bin_edges = generate_histogram(filename)
        c.plot(bin_edges[0:-1], hist)

        for t, col in zip(thresholds, colours):
            c.axvline(x=t, color=col, label='line at x = {}'.format(t))

        x, y = obtain_peaks(20, distance, hist, bin_edges)
        c.plot(x, y, 'x')
        c.set_xlabel('Greyscale value')
        c.set_ylabel('Number of pixels')
        c.set_title("Graph")
        fig.canvas.draw()
        print("Highest greyscale value:",x[-1])


    def submit(self, number, c, fig, d):
        if only_numbers(number.get()):
            d = int(number.get()) #the smaller the number, the more peaks or detected
            print(d)
            c.cla()
            self.show_graph(c, fig, d, "sample.png")
        else:
            print("Invalid entry, try again")


def only_numbers(char):
    return char.isdigit()
def message(self, frame, label):
    label['text'] = "LED off..."
    frame.after(1000, remove_message, self, label, frame)
def remove_message(self, label, frame):
    label.forget()
    analysisPage(frame, "sample.png")
def display_LED_message(self, frame):
    label = Label(frame, text="LED on...", bg='gray92')
    label.pack()
    frame.after(1000, message, self, frame, label)


if __name__ == "__main__":
    startPage()
    root.mainloop()
