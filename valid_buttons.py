import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

number = tk.StringVar()
class aPage(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("A")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        e = Entry(self, textvariable=number)
        e.pack()
        b = Button(self, text="B", command=lambda: (self.newPage(number,frame)))
        #b = Button(self,text="B",command=lambda:(self.destroy(), bPage()))
        b.pack()

    def newPage(self, number, frame):
        if only_numbers(number.get()):
            display_LED_message(self,frame)
            #self.destroy(), bPage()
            #self.after(3000, self.destroy(), bPage())

        else:
            print("a")



class bPage(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("B")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        e = Entry(self, textvariable=number)
        e.pack()
        b = Button(self, text="A", command=lambda: (self.newPage1(number)))
        #b = Button(self,text="A",command=lambda:(self.destroy(), aPage()))
        b.pack()

    def newPage1(self, number):
        if only_numbers(number.get()):
            self.destroy()
            aPage()
        else:
            print("a")

def only_numbers(char):
    return char.isdigit()
def message(self,frame, label):
    label['text'] = "LED off..."
    frame.after(1000, remove_message, self, label)
def remove_message(self, label):
    label.forget()
    self.destroy(), bPage()
def display_LED_message(self, frame):
    label = Label(frame, text="LED on...")
    label.pack()
    frame.after(1000, message, self, frame, label)



'''class Application(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.text = tk.Text(self, width=40, height=2)
        self.text.pack(side="top", fill="both", expand=True)
        self.text.insert("end", "Please enter a number:")

        enter_name = tk.Entry(self)
        enter_name.pack()
        self.enter_0 = tk.Button(self, text="Enter", width=10, command=self.callback)
        self.enter_0.pack()

        enter_name.focus_set()
        self.pack()

    def callback(self):
        self.display_name = tk.Text(self, width=40, height=2)
        self.display_name.pack(side="top", fill="both", expand=True)
        self.display_name.insert("end", "Now please enter your tutor group.")
        tutor = tk.Entry(self)
        tutor.pack()
        tutor.focus_set()
        self.enter_0.config(state="disabled")

        Enter_0_2 = tk.Button(self, text="Enter", width=10, command=self.callback2)
        Enter_0_2.pack()

    def callback2(self):
        self.display_name = tk.Text(self, width=40, height=2)
        self.display_name.pack(side="top", fill="both", expand=True)
        self.display_name.insert("end", "Let's begin! Exit back to main screen.")'''


if __name__ == "__main__":
    aPage()
    root.mainloop()
    '''app = Application(root)
    app.mainloop()'''
