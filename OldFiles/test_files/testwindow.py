import tkinter as tk
from tkinter import *
from tkinter import Frame, Button

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

        self.canvas = Canvas(frame)
        self.canvas.pack(side="left", expand=True, fill="both")

        self.buttonFrame = Frame(self.canvas)
        self.buttonFrame.configure(width=self.canvas.cget("width"))

        yscrollbar = Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        yscrollbar.pack(side="right", fill="y")
        self.canvasFrame = self.canvas.create_window((0,0), window=self.buttonFrame, anchor="nw")

        self.canvas.configure(yscrollcommand=yscrollbar.set)
        self.buttonFrame.bind('<Configure>', self.onFrameConfigure)
        self.canvas.bind('<Configure>', self.frameWidth)

        rows = 10
        columns = 3
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            #Grid.grid_rowconfigure(buttonFrame, i, weight=1)
            for j in range(0, columns):
                Grid.grid_columnconfigure(self.buttonFrame, j, weight=1)
                buttons[i][j] = tk.Button(self.buttonFrame, height=10, width=10, text=((columns*i)+j+1))
                buttons[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        self.pack(fill="both", expand=True)
        h = Button(self, text="Home", command=lambda: (self.destroy(), startPage()))
        h.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    def frameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvasFrame, width = canvas_width)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    startPage()
    root.mainloop()
