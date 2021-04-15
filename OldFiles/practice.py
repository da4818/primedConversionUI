from tkinter import *
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


class buttonsPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Options")

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        frame=Frame(self, relief=RAISED, borderwidth=1)
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