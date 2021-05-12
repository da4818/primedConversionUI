import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame, Button, Entry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2Tk
import skimage.io
from image_profile import *
import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS

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

        analysisButton = Button(self, text="Load Previous Data", command=lambda: (self.destroy(), analysisPage()))
        analysisButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#DATA ANALYSIS PAGE
class analysisPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Image Analysis")
        self.filename="pre_pr_red1.png"

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        fig = plt.figure(constrained_layout=True)
        spec = fig.add_gridspec(2, 2)

        norm_img, brightness_profile, pixel_locations = generate_brightness_profile(self.filename)
        a = fig.add_subplot(spec[0, 0])
        a.imshow(norm_img)
        a.axis('off')
        a.set_title("Normalised")
        c = fig.add_subplot(spec[1, 0:2])
        c.plot(brightness_profile[:,2])
        c.set_xlabel('Pixel location')
        c.set_ylabel('Brightness')
        c.set_title("Brightness profile")
        fig.canvas.draw()

        canvas = FigureCanvasTkAgg(fig, frame)

        plot_widget = canvas.get_tk_widget()
        plot_widget.pack(side="top", fill="both", expand=True, padx=5, pady=5)

if __name__ == "__main__":
    startPage()
    root.mainloop()
