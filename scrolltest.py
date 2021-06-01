import tkinter as tk
from tkinter import *
from tkinter import Frame, Button, LabelFrame
root = Tk()
root.geometry("700x600")
class dataPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Home")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0,weight=1)

        wrapper = LabelFrame(frame)

        canvas = Canvas(wrapper,bg="bisque")
        canvas.pack(side="left", expand=True, fill="both")

        yscrollbar = Scrollbar(wrapper, orient="vertical", command=canvas.yview)
        yscrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=yscrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

        buttonFrame = Frame(canvas)
        canvas.create_window((0,0), window=buttonFrame, anchor="nw")

        wrapper.pack(fill="both", expand=True, padx=10, pady=10)

        rows = 10
        columns = 3
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            #Grid.grid_rowconfigure(buttonFrame, i, weight=1)
            for j in range(0, columns):
                Grid.grid_columnconfigure(buttonFrame, j, weight=1)
                buttons[i][j] = tk.Button(buttonFrame, height=10, width=10, text=((columns*i)+j+1))
                buttons[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        self.pack(fill="both", expand=True)
        photoButton = Button(self, text="Photo Conversion")
        photoButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        primedButton = Button(self, text="Primed Conversion")
        primedButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        dataButton = Button(self, text="Load Previous Data")
        dataButton.pack(side="left", fill="both", expand=True, padx=5, pady=5)


if __name__ == "__main__":
    dataPage()
    root.mainloop()




'''canvas = Canvas(frame, height = 300, width = 300, scrollregion=(0,0,500,500), bg = "bisque")
        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.pack (side="right", fill="y")
        scrollbar.config(command = canvas.yview)

        canvas.config(yscrollcommand=scrollbar.set)
        canvas.pack(expand=True, fill="both")'''


'''TBox = tk.Text(frame, height = 500, width = 500, yscrollcommand = scrollbar.set, wrap = "none")
TBox.pack(expand = 0, fill = tk.BOTH)
TBox.insert(tk.END, Num_Horizontal)
TBox.insert(tk.END, Num_Vertical)
scrollbar.config(command = TBox.yview)'''


'''
rows = 9
columns = 5
buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
for i in range(0, rows):
    Grid.grid_rowconfigure(buttons_frame, i, weight=1)
    for j in range(0, columns):
        Grid.grid_columnconfigure(buttons_frame, j, weight=1)
        buttons[i][j] = tk.Button(buttons_frame,  text=((columns*i)+j+1))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

canvas.create_window((0,0), window=buttons_frame, anchor=tk.CENTER)
buttons_frame.update_idletasks()

canvas.configure(scrollregion=canvas.bbox("all"))'''