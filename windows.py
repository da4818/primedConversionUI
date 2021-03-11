import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Entry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS

from gpiozero import DigitalOutputDevice
from function_programs.raspigpio import raspi_turnon, raspi_turnoff
from function_programs.image_analysis import *
from function_programs.files import *
from function_programs.camera import *
from OldFiles.skimage_image_analysis import get_files
root = Tk()
root.title("Primed Conversion Testing Stage")
root.geometry("700x600")
'''
CODE FUNCTIONALITY:
Buttons are displayed in order of 
('Home',) 'Photo Conversion','Primed Conversion', 'Load Previous Data'
Photo conversion/Primed conversion pages will essentially perform the same code, except for the LED control
On photo conversion page:
- The user can then choose to capture images for the green or red channel
- On green channel, the user can take an initial phot --> this will be saved as the pre photoconversion photo for the green channel
- When if the user is satisfied, they can then then start green excitation and capture an image
* Need to perform normalisation for green channel
The user should then go to the red channel option (where photo conversion will occur)
- Similar to the green channel, they can take an initial photo
- They can then undergo photo conversion, red excitation and capture an image
- This will then normalise the red channel images and display the data
'''

#START PAGE
class startPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        #Displays 3 menu options: Photoconversion, PRimed Conversion and previous data
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), excitationPage("pc")))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), excitationPage("pr")))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#EXCITATION PAGE
class excitationPage(Frame):
    def __init__(self, method):
        super().__init__()
        if method == "pc":
            title = "Photo Conversion"
        elif method == "pr":
            title = "Primed Conversion"
        self.master.title("Regular Excitation: " + title)
        exFrame = Frame(self, relief=RAISED, borderwidth=1)
        exFrame.pack(fill="both", expand=True)

        redButton = Button(exFrame, text="Red Excitation", command=lambda: (self.destroy(), colourExcitationPage("red_excitation", method)))
        redButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)
        greenButton = Button(exFrame, text="Green Excitation",command=lambda: (self.destroy(), colourExcitationPage("green_excitation", method)))
        greenButton.pack(side="top", fill="both", expand=True, padx=5, pady=10)

        self.pack(fill="both", expand=True)

        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        '''
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), photoPage())) #Closes the current page and calls the next page to appear within the same frame
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), primedPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)'''
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#EXCITATION PAGE
class colourExcitationPage(Frame):
    def __init__(self, colour, method):
        super().__init__()
        if colour == 'red_excitation':
            print('Red Excitation')
            self.master.title("Red Excitation - " + str(method))

        elif colour == 'green_excitation':
            print('Green Excitation')
            self.master.title("Green Excitation - " + str(method))


        frame = Frame(self, relief="raised", borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        f = files(colour, method)
        c = camera(f, gpio)

        cameraButton = Button(self, text="Take initial photo", command=lambda: c.take_photo("pre"))
        cameraButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        '''This code will be used to undergo LED excitation - I've removed it as I don't have the rasp pi connected and will return an error
        startButton = Button(self, text="Start Excitation", command=lambda: (raspi_connection(colour),display_LED_message(self, frame), c.take_photo("post")))
        '''

        startButton = Button(self, text="Start Excitation", command=lambda: (display_LED_message(self, colour, frame), c.take_photo("post")))
        startButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        backButton = Button(self, text="Back", command=lambda: (self.destroy(), excitationPage(method)))
        backButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        # self.destroy() Closes the current page and calls the next page to appear within the same frame

#PREVIOUS DATA PAGE
class dataPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Previous Data")
        dataFrame = Frame(self, relief=RAISED, borderwidth=1)
        dataFrame.pack(fill="both", expand=True)
        f = files("green_excitation", "pc") #Here the type of excitation and method isn't really important - it's just to access the files
        #Obtain a directory of previous raw images - currently separates
        previous, IDs, methods = f.get_raw_images()
        print(previous)
        print(IDs)
        print(methods)
        if len(previous) == 0:
            l = Label(dataFrame, text="No previous data")
            l.pack(fill="both", expand=True)

        elif len(previous) > 0:
            prev_data_list = []
            for names in previous:
                prev_data_list.append(names)

            canvas = tk.Canvas(dataFrame, width=300, height=500, bg='gray92')
            canvas.pack(fill="both", expand=True, pady=5)

            #Previous images displayed in a grid format - .grid() can only be in frames that also use only .grid()
            col_num = 4 #Set to 4 columns
            for i,(num, method, filename) in enumerate(zip(IDs, methods, prev_data_list)):
                r = int(i/col_num) #Calculates row number
                c = i % col_num #Calculates column number
                photo = PIL.Image.open(filename).resize((150, 150), ANTIALIAS)
                render = ImageTk.PhotoImage(photo)
                img = Label(canvas, text=str(method) + " Test " + str(num), image=render, compound="bottom")
                img.image = render
                img.grid(row=r, column=c, padx=5, pady=5)

        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), excitationPage("Photo Conversion")))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), excitationPage("Primed Conversion")))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#DATA ANALYSIS PAGE
class analysisPage(Frame):
    def __init__(self, frame, colour):
        super().__init__()
        self.master.title("Image Analysis")
        d = 25
        #img, img1 = export_images(filename)
        f = files(colour, "pc")
        img, img1, masked_path = f.export_files()
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
        self.show_graph(c, fig, 25, masked_path)
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

def message(self, frame, label, colour):
    label['text'] = "LED off..."
    frame.after(1000, remove_message, self, label, frame, colour)

def remove_message(self, label, frame, colour):
    label.forget()
    #self.destroy()
    analysisPage(frame, colour)

def display_LED_message(self, colour, frame):
    label = Label(frame, text="LED on...", bg='gray92')
    label.pack()
    frame.after(1000, message, self, frame, label, colour)

# raspberry pi GPIO class, needed in main program to ensure that the pins stay in correct voltage at all times, even when exiting external
# modules that alter their state
class raspi:
    def __init__(self):
        # initializing output pins and setting them LOW to ensure transistor gates are all closed on startup, thus all LEDs start off
        # leds are each a tuple with identifying name at index 0 and digitaloutputdevice object at index 1
        self.leds = [None]*4
        self.leds[0] = ("UV", DigitalOutputDevice(17,initial_value=0))
        self.leds[1] = ("green_excitation", DigitalOutputDevice(27,initial_value=0))
        self.leds[2] = ("red_priming", DigitalOutputDevice(22,initial_value=0))
        self.leds[3] = ("red_excitation", DigitalOutputDevice(23,initial_value=0))
    # had to put here to have leds as global variables, since they need to be at specific constant outputs at all times
# Could instead initialize led list in global space at start of code
gpio = raspi()


if __name__ == "__main__":
    startPage()
    root.mainloop()
