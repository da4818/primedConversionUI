import tkinter as tk
from tkinter import *

from tkinter.ttk import Frame, Button
import PIL
from PIL import Image, ImageTk
from PIL.Image import ANTIALIAS
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

class imagePage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Images")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame, width=300, height=500, bg='gray92')
        canvas.pack(fill="both", expand=True, pady=5)

        IDs = [1,2,4,6,7,3,2,4]
        methods = ["Photoconversion","Primed Conversion","Photoconversion","Primed Conversion","Photoconversion","Primed Conversion","Primed Conversion","Primed Conversion",]
        prev_data_list = ["green_test_after.png","green_test_after.png","green_test_before.png","green_test_after.png","green_test_before.png","green_test_before.png","green_test_after.png","green_test_before.png"]

        #Previous images displayed in a grid format - .grid() can only be in frames that also use only .grid()
        col_num = 4 #Set to 4 columns
        for i,(num, method, filename) in enumerate(zip(IDs, methods, prev_data_list)):
            r = int(i/col_num) #Calculates row number
            c = i % col_num #Calculates column number
            photo = PIL.Image.open(filename).resize((150, 150), ANTIALIAS)
            render = ImageTk.PhotoImage(photo)
            img = Label(canvas, text=str(method) + " Test " + str(num), image=render, compound="bottom")
            img.image = render
            img.bind("<Button>",self.printName)
            img.grid(row=r, column=c, padx=5, pady=5)

        self.pack(fill="both", expand=True)
        b = Button(self, text="Options", command=lambda: (self.destroy(), buttonsPage()))
        b.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        h = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        h.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def printName(self, event):
        widget=event.widget
        out = widget.cget("text")
        grid_info=widget.grid_info()
        '''row_num = grid_info["row"]
        col_num = grid_info["column"]
        self.button_commands(row_num,col_num)'''
        self.convert_to_filename(out)

    def convert_to_filename(self, text):
        #Finds the numbers in the name -> must be converted into list format, but as there is only 1 number in the list, we take the first (0th) element
        ID = list(re.findall(r'\d+', text))[0]
        if "Photoconversion" in text:
            method = "pc"
        elif "Primed Conversion" in text:
            method = "pr"
        print("norm_" + method + "_green_" + ID + ".png")
        #return "norm_" + method + "_" + colour + "_" + ID + ".png"




class buttonsPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Options")

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        buttons = ["Take a Blank Photo (Green Channel)", "Green Excitation", "Take Photo",
                   "Undergo ", "Take a Blank Photo (Red Channel)", "Red Excitation", "Take Photo", "View Image Analysis"]
        r=2
        c=4
        for row_index in range(r):
            Grid.rowconfigure(frame, row_index, weight=1)
            for col_index in range(c):
                Grid.columnconfigure(frame, col_index, weight=1)
                btn = Button(frame,text=buttons[c*row_index+col_index], relief=RIDGE, bd=2)
                btn.bind("<Button>",self.showPosEvent)
                btn.grid(column=col_index, row=row_index, sticky=N+S+E+W)

        h = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        h.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        i = Button(self, text="Images", command=lambda: (self.destroy(), imagePage()))
        i.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def showPosEvent(self, event):
        widget=event.widget
        out = widget.cget("text")
        grid_info=widget.grid_info()
        row_num = grid_info["row"]
        col_num = grid_info["column"]
        self.button_commands(row_num,col_num)

    def button_commands(self, r,c):
        n = (4*r)+c
        if n==0:
            print("Green channel image")
        elif n==1:
            print("Green excitation")
        elif n==2:
            print("Post green photo")
        elif n==3:
            print("Undergoing")
            self.destroy()
            startPage()
        elif n==4:
            print("Red channel image")
        elif n==5:
            print("Red excitation")
        elif n==6:
            print("post red photo")
        elif n==7:
            print("analysis")


if __name__ == "__main__":
    startPage()
    root.mainloop()