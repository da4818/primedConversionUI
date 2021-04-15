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

class Test:
    def __init__(self,length,width=None):
        if width is not None:
            self.shape = "Square"
            print(self.shape,"-l:"+str(length)+" w:"+str(width))
        else:
            self.shape = "Circle"
            print(self.shape,"-r:"+str(length))

if __name__ == "__main__":
    t = Test(4,5)
    p = Test(2)