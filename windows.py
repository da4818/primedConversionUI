import tkinter as tk
from tkinter import *
from tkinter import Frame, Button
import matplotlib.pyplot as plt
from tkinter import font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS
from function_programs.camera import *
from function_programs.image_profile import *

root = Tk()
root.title("Primed Conversion Testing Stage")
root.geometry("700x600")

#START PAGE
f = Files() #global file variable (to have continual access to files)
class startPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1, bg='gray92')
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        #Displays 3 menu options: Photo Conversion, Primed Conversion and Previous Data
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), methodPage("pc")))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), methodPage("pr")))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#METHOD PAGE - this page is for primed conversion or photo conversion, depending on the value passed through
class methodPage(Frame):
    def __init__(self, method):
        super().__init__()
        if method == "pc":
            title = "Photo Conversion"
        elif method == "pr":
            title = "Primed Conversion"
        self.master.title(title)
        '''Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)'''
        optionsFrame = Frame(self, relief=RAISED, borderwidth=1, bg='gray92')
        optionsFrame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)


        #Button options
        helv36 = tkFont.Font(size=20, weight=tkFont.BOLD)
        Grid.grid_columnconfigure(optionsFrame, 0, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 0, weight=1)
        gblankButton = Button(optionsFrame, text="Take a Blank Photo (Green Channel)", font=helv36, command=lambda: (blank_camera("green_excitation", method)))
        gblankButton.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 0, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 1, weight=1)
        greenButton = Button(optionsFrame, text="Green Excitation", font=helv36, command=lambda: (self.destroy(), excitationPage("green_excitation", method)))
        greenButton.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 0, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 2, weight=1)
        gcameraButton = Button(optionsFrame, text="Take Green Channel Photo", font=helv36, command=lambda: (fluo_camera("green_excitation", method)))
        gcameraButton.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 0, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 3, weight=1)
        methodButton = Button(optionsFrame, text="Undergo " + title, font=helv36, command=lambda: (self.destroy(), excitationPage(method, method)))
        methodButton.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 0, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 4, weight=1)
        normaliseButton = Button(optionsFrame, text="Normalise (green channel)", font=helv36, command=lambda: (modify_images("green_excitation", method)))
        normaliseButton.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 1, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 0, weight=1)
        rblankButton = Button(optionsFrame, text="Take a Blank Photo (Red Channel)", font=helv36, command=lambda: (blank_camera("red_excitation", method)))
        rblankButton.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 1, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 1, weight=1)
        redButton = Button(optionsFrame, text="Red Excitation", font=helv36, command=lambda: (self.destroy(), excitationPage("red_excitation", method)))
        redButton.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 1, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 2, weight=1)
        rcameraButton = Button(optionsFrame, text="Take Red Channel Photo", font=helv36, command=lambda: (fluo_camera("red_excitation", method)))
        rcameraButton.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 1, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 3, weight=1)
        normaliseButton = Button(optionsFrame, text="Normalise (red channel)", font=helv36, command=lambda: (modify_images("red_excitation", method)))
        normaliseButton.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        Grid.grid_columnconfigure(optionsFrame, 1, weight=1)
        Grid.grid_rowconfigure(optionsFrame, 4, weight=1)
        analysisButton = Button(optionsFrame, text="View Image Analysis", font=helv36, command=lambda: self.analyse_images())
        analysisButton.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

        self.pack(fill="both", expand=True)
        #Main menu options
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), dataPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def analyse_images(self):
        if f.curr_filename is None:
            print("No current normalised images. Please ensure a normalised image is saved.")
        else:
            self.destroy()
            analysisPage()

def blank_camera(colour, method):
    if colour == "both":
        g = Files("green_excitation", method)
        r = Files("red_excitation", method)
        c = Camera(g)
        c.take_photo("pre")
        c = Camera(r)
        c.take_photo("pre")
    else:
        global f
        f = Files(colour, method) #prepare filenames for specifc channel
        c = Camera(f)
        c.take_photo("pre")

def fluo_camera(colour, method):
    if colour == "both":
        g = Files("green_excitation", method)
        r = Files("red_excitation", method)
        c = Camera(g)
        c.take_photo("post")
        c = Camera(r)
        c.take_photo("post")
    else:
        global f
        f = Files(colour, method)
        c = Camera(f)
        c.take_photo("post")

def modify_images(colour, method):
    global f
    f = Files(colour, method)
    c = Camera(f)
    c.check_recent_photos()

#EXCITATION PAGE
class excitationPage(Frame):
    def __init__(self, colour, method):
        super().__init__()
        if method == "pc":
            title = "Photo Conversion"
        elif method == "pr":
            title = "Primed Conversion"
        self.master.title("Regular Excitation: " + title)
        exFrame = Frame(self, relief=RAISED, borderwidth=1)
        exFrame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        self.after(0, self.display_LED_message, colour, exFrame, method)

    def display_LED_message(self, colour, frame, method):
        if colour == 'green_excitation':
            description = "Green Excitation: "
        elif colour == 'red_excitation':
            description = "Red Excitation: "
        elif colour == 'pc':
            description = "Photo Conversion: "
        elif colour == 'pr':
            description = "Primed Conversion: "
        #Will lead to raspi LED functions

        label = Label(frame, text=description+"LED on...", bg='gray92')
        label.grid(row=4, column=4)
        frame.after(1000, self.message, frame, label, method)

    def message(self, frame, label, method):
        label['text'] = "LED off..."
        frame.after(1000, self.remove_message, label, method)

    def remove_message(self, label, method):
        label.grid_forget()
        self.destroy()
        methodPage(method)

#DATA ANALYSIS PAGE§
class analysisPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Image Analysis")
        fig = plt.figure(constrained_layout=True)
        spec = fig.add_gridspec(3, 2) #Creates 3 x 2 grid (1st row for images, 2nd & 3rd row for brightness profiles)
        #Generate equivalent sample images' filepath (e.g. paths for green and red pc test ID 2)
        green_path, red_path = get_equiv_file(f.curr_filepath)
        #Obtain green channel and red channel values
        green_norm_img, green_brightness_profile, green_y_coords = generate_brightness_profile(green_path)
        red_norm_img, red_brightness_profile, red_y_coords = generate_brightness_profile(red_path)

        #Display normalised green and red channel images together
        a = fig.add_subplot(spec[0, 0])
        a.imshow(green_norm_img)
        #a.axis('off')
        a.set_title("Normalised (Green Channel)")
        b = fig.add_subplot(spec[0, 1])
        b.imshow(red_norm_img)
        #b.axis('off')
        b.set_title("Normalised (Red Channel)")

        #Plotting green values together
        c = fig.add_subplot(spec[1, 0:2])
        greens = ('#E0FFD4', '#7BC45E', '#337A1D', '#0B2902')
        greens = ('#7BC45E', '#0B2902')
        for profile, y, col in zip(green_brightness_profile, green_y_coords, greens):
            c.plot(profile, color=col, label='line at y={}'.format(y))
        c.set_xlabel('Pixel location')
        c.set_ylabel('Brightness')
        c.set_title("Brightness profile")
        c.legend(loc="lower right")

        #Plotting red values together
        #for p in red_brightness_profile:
        #    c.plot(p)
        ##c.plot(red_brightness_profile[:], color="red")
        d = fig.add_subplot(spec[2, 0:2])
        reds = ('#FFD4D4', '#FF0000', '#8F0A0C', '#781214')
        reds = ( '#FF0000', '#781214')
        for profile, y, col in zip(red_brightness_profile, red_y_coords, reds):
            d.plot(profile, color=col, label='line at y ={}'.format(y))
        d.set_xlabel('Pixel location')
        d.set_ylabel('Brightness')
        d.legend(loc="lower right")

        fig.canvas.draw()
        canvas = FigureCanvasTkAgg(fig, self)
        plot_widget = canvas.get_tk_widget()
        plot_widget.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), methodPage("pc")))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), methodPage("pr")))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#PREVIOUS DATA PAGE
class dataPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Previous Data")
        dataFrame = Frame(self, relief=RAISED, borderwidth=1)
        dataFrame.pack(fill="both", expand=True)
        self.canvas = Canvas(dataFrame, bg='gray92')
        self.canvas.pack(side="left", expand=True, fill="both")

        self.buttonFrame = Frame(self.canvas,bg='gray92')
        self.buttonFrame.configure(width=self.canvas.cget("width"))

        yscrollbar = Scrollbar(dataFrame, orient="vertical", command=self.canvas.yview)
        yscrollbar.pack(side="right", fill="y")
        self.canvasFrame = self.canvas.create_window((0,0), window=self.buttonFrame, anchor="nw")

        self.canvas.configure(yscrollcommand=yscrollbar.set)
        self.buttonFrame.bind('<Configure>', self.onFrameConfigure)
        self.canvas.bind('<Configure>', self.frameWidth)


        f = Files() #here f is not global as the current files are irrelevant
        prev_files, roots_list = f.get_prev_files()
        if prev_files == 0:
            emptyLabel = Label(self.canvas, text="No previous data")
            emptyLabel.pack(fill="both", expand=True)
        else:
            previous, IDs, methods = f.get_raw_images(prev_files, roots_list)
            if len(previous) > 0:
                prev_data_list = []
                for names in previous:
                    prev_data_list.append(names)

                #Previous images displayed in a grid format - .grid() can only be in frames that also use only .grid()
                col_num = 4 #Set to 4 columns
                for i, (num, method, filename) in enumerate(zip(IDs, methods, prev_data_list)):
                    r = int(i/col_num) #Calculates row number
                    c = i % col_num #Calculates column number
                    photo = PIL.Image.open(filename).resize((150, 150), ANTIALIAS)
                    render = ImageTk.PhotoImage(photo)
                    img = Label(self.buttonFrame, text=str(method) + " Test " + str(num), image=render, compound="bottom")
                    img.image = render
                    img.bind("<Button>", self.obtain_filename)
                    img.grid(row=r, column=c, padx=5, pady=5)

        self.pack(fill="both", expand=True)
        home = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        home.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), methodPage("pc")))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion", command=lambda: (self.destroy(), methodPage("pr")))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def frameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvasFrame, width = canvas_width)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def obtain_filename(self, event):
        widget = event.widget
        out = widget.cget("text")
        filename = self.convert_to_filename(out)
        print("Opening " + out)
        p = f.get_analysis_path()
        f.curr_filepath = p + 'green/' + filename
        self.destroy()
        analysisPage()

    def convert_to_filename(self, text):
        #Finds the numbers in the name -> must be converted into list format,
        # but as there is only 1 number in the list, we take the first (0th) element
        ID = list(re.findall(r'\d+', text))[0]
        if "Photo Conversion" in text:
            file_method = "pc"
        elif "Primed Conversion" in text:
            file_method = "pr"
        return "norm_" + file_method + "_green_" + ID + ".png"


# raspberry pi GPIO class, needed in main program to ensure that the pins stay in correct voltage at all times,
# even when exiting external
# modules that alter their state


'''class raspi:
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
gpio = raspi()'''


if __name__ == "__main__":
    startPage()
    root.mainloop()
