import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Entry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk
from matplotlib.figure import Figure


import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS

from arduino import arduino_connection
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

        startButton = Button(self, text="Start Excitation", command=lambda: (display_LED_message(frame), arduino_connection(colour),display_analysis())) #Closes the current page and calls the next page to appear within the same frame
        startButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        stopButton = Button(self, text="Stop", command=lambda: display_analysis())
        stopButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        backButton = Button(self, text="Back", command=lambda: (self.destroy(), excitationPage()))
        backButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        #Closes the current page and calls the next page to appear within the same frame

        def display_analysis():
            self.master.title("Image analysis")
            img, img1 = export_images("sample.png")
            fileTitle= Label(frame, text = 'Sample.png')
            fileTitle.pack()
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(221)
            a.imshow(img)
            a.axis('off')
            b = f.add_subplot(222)
            b.imshow(img1)
            b.axis('off')

            c = f.add_subplot(212) #Take the 3rd and 4rd subplot as one
            display_graphs(f,c,25)

        def plot_peaks(graph, canvas, distance, hist, bin_edges):
            x, y = obtain_peaks(20,distance,hist,bin_edges)
            graph.plot(x,y,'x')
            canvas.draw()

        def display_graphs(f,c,default):
            thresholds, colours = get_thresholds()
            hist, bin_edges = histogram("tagCFP.png")
            c.plot(bin_edges[0:-1], hist)
            for t, col in zip(thresholds, colours):
                c.axvline(x=t, color=col, label='line at x = {}'.format(t))

            x, y = obtain_peaks(20,default,hist,bin_edges)
            c.plot(x,y,'x')
            c.legend()
            c.set_xlabel('Greyscale value')
            c.set_ylabel('Number of pixels')
            canvas = FigureCanvasTkAgg(f, frame)
            #plot_peaks(c, canvas, default, hist, bin_edges)
            canvas.draw()

            canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
            canvas._tkcanvas.pack(side="top", fill="both", expand=True)
            number=tk.StringVar()
            dLabel= Label(frame, text = 'Adjust distance criteria:', font=('calibre', 15, 'normal'))
            #dLabel.insert(0, 'Default: 25')
            dLabel.pack(side="left", fill="both", expand=True)
            distance = tk.Entry(frame, width=5, textvariable=number, font=('calibre', 10, 'normal'))
            distance.pack(side="left", fill="both", expand=True)
            out = Button(frame, text="Add peaks", command=lambda: (submit(c, canvas)))
            out.pack(side="left", fill="both", expand=True)
            confirm = Button(frame, text="Show highest brightness", command=lambda: display_brightness())
            confirm.pack(side="left", fill="both", expand=True)
            def display_brightness():
                print("Highest greyscale value:",x[x.size-1])
            def submit(graph, canvas):
                if (only_numbers(number.get())):
                    d = int(number.get()) #the smaller the number, the more peaks or detected
                    print(d)
                    plot_peaks(graph,canvas,d, hist, bin_edges)
                    #display_graphs(f,c,d,True)

                else:
                    print("Invalid entry, try again")



def only_numbers(char):
    return char.isdigit()

def message(frame, label):
    label['text'] = "Stopping LED..."
    frame.after(2000, remove_message, label)
def remove_message(label):
    label.forget()
def display_LED_message(frame):
    label = Label(frame, text="Starting LED...", bg='gray92')
    label.pack()
    '''
    As the label is in a white box - this is to match the window colour
    Here the function to turn the light on/off will coded - 
    for now there is a delay that simulate the time taken to perform the excitation
    '''
    frame.after(2000, message, frame, label)

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
        startButton = Button(pcFrame, text="Start Photo Conversion")
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

        '''#photo = PIL.Image.open(os.path.join('/Users/debbie/BioEng/year 3/Group project/Primed_Conversion_efficiency_Images_test/Test File/4/','pr-mEosFP new_pr-mEosFP_new_after4_1_ch00.tif'))
        photo = PIL.Image.open(os.path.join(imageinfo.paths[0],imageinfo.names[0])).resize((150, 150), ANTIALIAS)
        render = ImageTk.PhotoImage(photo)
        img = Label(canvas, image=render)
        img.image = render
        photo1 = PIL.Image.open(os.path.join(imageinfo.paths[2],imageinfo.names[2])).resize((150, 150), ANTIALIAS)
        render1 = ImageTk.PhotoImage(photo1)
        img1 = Label(canvas, image=render1)
        img1.image = render1
        img.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        img1.pack(side="left", fill="both", expand=True, padx=5, pady=5)'''
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


'''# opens file explorer at program path, useful to choose images to analyze or to load previously analyzed data
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
                                              filetype=(("All files", "*.pdf"), ("all files", "*.*")))'''


if __name__ == "__main__":
    startPage()
    root.mainloop()
