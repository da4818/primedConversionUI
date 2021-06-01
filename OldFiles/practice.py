import tkinter as tk
from tkinter import *
from tkinter import Frame, Button
import PIL
from PIL import ImageTk
from PIL.Image import ANTIALIAS
from function_programs.files import *

root = Tk()
root.geometry("700x600")

class startPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        #Displays 3 menu options: Photoconversion, PRimed Conversion and previous data
        #photoButton = Button(self, text="Photo Conversion", command=lambda: (self.destroy(), excitationPage("pc")))
        b = Button(self, text="Options", command=lambda: (self.destroy(), buttonsPage()))
        b.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        i = Button(self, text="Images", command=lambda: (self.destroy(), imagePage()))
        i.pack(side="left", fill="both", expand=True, padx=5, pady=5)

class buttonsPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Options")

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

        h = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        h.pack(side="left", fill="both", expand=True, padx=5, pady=5)


class imagePage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Images")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)

        self.canvas = Canvas(frame, bg='gray92')
        self.canvas.pack(side="left", expand=True, fill="both")

        self.buttonFrame = Frame(self.canvas,bg='gray92')
        self.buttonFrame.configure(width=self.canvas.cget("width"))

        yscrollbar = Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        yscrollbar.pack(side="right", fill="y")
        self.canvasFrame = self.canvas.create_window((0,0), window=self.buttonFrame, anchor="nw")

        self.canvas.configure(yscrollcommand=yscrollbar.set)
        self.buttonFrame.bind('<Configure>', self.onFrameConfigure)
        self.canvas.bind('<Configure>', self.frameWidth)

        f = Files() #here f is not global as the current files are irrelevant
        prev_files, roots_list = f.get_prev_files()
        if prev_files == 0:
            emptyLabel = Label(self.canvas, text="No previous data", anchor="center",bg='gray92')
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
        h = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        h.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def obtain_filename(self, event):
        widget = event.widget
        out = widget.cget("text")
        filename = self.convert_to_filename(out)
        print("Opening " + out)
        global f
        p = f.get_analysis_path()
        f.curr_filepath = p + 'green/' + filename
        self.destroy()

    def frameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvasFrame, width = canvas_width)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    startPage()
    root.mainloop()
