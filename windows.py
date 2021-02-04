import tkinter as tk
from tkinter import ttk, Label, Button, PhotoImage, filedialog
import PIL
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage

#Displa_excitation and Display_photo_conversion are now in another file.
from excitation import display_excitation
from photoconversion import display_photo_conversion
from image_analysis import send_message, get_file # We can use this to use functions from other python scripts
# Setting up the initial window

window = tk.Tk()
window.title('Home')
window.geometry("800x600")

def display_primed_conversion():
    pr_window = tk.Toplevel() # Widget that is daughter window of the parent
    pr_window.title('Primed Conversion Testing Stage')
    pr_window.geometry("600x600")
    canvas = tk.Canvas(pr_window, width = 500, height = 400)
    canvas.pack()
    image = Image.open(get_file(3)) # This function returns the name of the png file to be imported
    image = image.resize((476, 378), Image.ANTIALIAS)
    img = PhotoImage(image)
    canvas.create_image(12, 11, anchor=tk.NW, image=img) #(500-476)/2=12, (400-378)/2=11
    pr_window.mainloop()
#output = Label(pr_window, text=send_message())
#output.place(x=100, y=100)
# When Primed Conversion button is pressed, it will display "Example code" to the window as a label








# opens file explorer at program path, useful to choose images to analyze or to load previously analyzed data
def get_file(filetype="img"):
    # default is image file loader bc it'll be used in more windows than data loader
    if filetype == "img":
        # function returns directory path for chosen file(s) as tuple
        filename = filedialog.askopenfilenames(initialdir='C:\IdeaProjects\primedConversionUI',title="Select a file",
                                                     filetype=(
                                                         ("png files", "*.png"),
                                                         ("jpg files", "*.jpg"),
                                                         ("tif files", "*.tif"),
                                                     ))
        # random example code opening one or more images
        if len(filename)>1:
            for image in filename:
                photo = PIL.Image.open(image)
                photo.show()
        elif len(filename)==1:
            photo = PIL.Image.open(filename[0])
            photo.show()
    # will add specific filetype instead of pdf for data when we know what we're saving it as
    else:
        filename = filedialog.askopenfilename(initialdir='C:\IdeaProjects\primedConversionUI', title="Select a file",
                                              filetype=(("All files", "*.pdf"), ("all files", "*.*")))



b1 = Button(window, text="Regular Excitation", command=display_excitation)
b2 = Button(window, text="Photo Conversion", command=display_photo_conversion)
b3 = Button(window, text="Primed Conversion", command=display_primed_conversion)
b4 = Button(window, text="Load previous data", command=lambda: get_file("data"))


#Small text to introduce the user interface
Hello = Label(window, text="\n Welcome to the user interface of our imaging platform. \n Click on 'Regular Excita"
                           "tion' to analyse the fluorescence properties of the samples. \nTo see if the samples are "
                           "photoconvertible, click on Photoconversion."
                           "\nTo determine if the samples are primed convertible, click on 'Primed Conversion'.")

# This produces a grid structure so we can add the buttons in a grid format
window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)
window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)
frame = tk.Frame(
    master = window,
    relief = tk.RAISED,
    borderwidth = 1
)
frame.grid(row=1, column=0, padx=5, pady=5)
b1.grid(row=2, column=0)
frame.grid(row=1, column=1, padx=5, pady=5)
b2.grid(row=2, column=1)
frame.grid(row=1, column=3, padx=5, pady=5)
b3.grid(row=2, column=2)
frame.grid(row=1, column=2, padx=5, pady=5)
b4.grid(row=3, column=1)

Hello.grid(row=0, column=1)


window.mainloop()
