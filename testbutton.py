from tkinter import *

#Create & Configure root
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
        photoButton = Button(self, text="A", command=lambda: (self.destroy(), methodPage()))
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="B", command=lambda: (self.destroy(), methodPage()))
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="C", command=lambda: (self.destroy(), testPage()))
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)

class methodPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Home")

        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        #Create & Configure frame
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        #frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.pack(fill="both", expand=True)
        #Create a 5x10 (rows x columns) grid of buttons inside the frame
        buttons = ["Take a Blank Photo (Green Channel)", "Green Excitation", "Take Photo",
                   "Undergo ", "Take a Blank Photo (Red Channel)", "Red Excitation", "Take Photo", "View Image Analysis"]
        r=2
        c=4

        for row_index in range(r):
            Grid.rowconfigure(frame, row_index, weight=1)
            for col_index in range(c):
                Grid.columnconfigure(frame, col_index, weight=1)
                btn = Label(frame,text=buttons[(r*row_index)+col_index], relief=RIDGE, bd=2) #create a button inside frame
                btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                btn.bind('<Button>', out)

        '''for row_index in range(r):
            Grid.rowconfigure(frame, row_index, weight=1)
            for col_index in range(c):
                Grid.columnconfigure(frame, col_index, weight=1)
                btn = Button(frame,text=buttons[(r*row_index)+col_index]) #create a button inside frame
                btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)'''
def y(event):

    # for every label.
    entry = event.widget
    pad = 0
    pad += int(str(entry['bd']))
    pad += int(str(entry['padx']))
    pad *= 2
    entry.configure(wraplength = event.width - pad)

def p(event):
    widget = event.widget
    j = widget.winfo_fpixels
    print(j)

class testPage(Frame):
    def __init__(self):
        super().__init__()
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
                btn = Button(frame, text="a") #create a button inside frame
                btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                #btn.bind('<Button>', out)
                print(btn.winfo_fpixels())
                btn.bind("<Button>", p)

            '''entry = Label(frame, text="text example a b c ffjfgbsibfdgdgd df nmfkgbsies", width=30, anchor=NW, justify=LEFT, relief=RIDGE, bd=2)
            entry.bind("<Configure>", y)
            entry.pack(side="left", padx=5, pady=5)'''

def out(event):
    widget = event.widget
    labelText = widget.cget("text")
    print(labelText)


if __name__ == "__main__":
    startPage()
    root.mainloop()