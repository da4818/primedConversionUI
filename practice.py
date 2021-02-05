from tkinter import *
root = Tk()
root.geometry("650x600")
def message(L):
    L['text'] = 'Test 2'

def delay(L):
    root.after(2000, message(L))
def display():
    L = Label(root, text="Test 1")
    L.pack()
    root.after(2000, delay,L)

B = Button(root, text="button", command=display)
B.pack()

root.mainloop()
