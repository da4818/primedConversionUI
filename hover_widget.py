import tkinter as tk


class ButtonHoverExample:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("HoverExample")
        self.parent.geometry("160x60+10+10")
        self.buttons = {}

    def on_enter(self, name):
        button = self.buttons[name]
        # print(f"\nMouse Enter - name: {button['name']}, details: {button}")
        bgcolor = button["mouseexit"]
        button["button"].configure(bg=bgcolor)

    def on_exit(self, name):
        button = self.buttons[name]
        bgcolor = button["mouseenter"]
        button["button"].configure(bg=bgcolor)

    def new_button(self, name, mecolor, mxcolor, xpos, ypos):
        button = self.buttons
        parent = self.parent

        button[name] = {}
        button[name]["name"] = name
        button[name]["mouseenter"] = mecolor
        button[name]["mouseexit"] = mxcolor
        button[name]["xpos"] = xpos
        button[name]["ypos"] = ypos
        button[name]["button"] = tk.Button(
            parent, text=name, bg=button[name]["mouseenter"]
        )
        button[name]["button"].grid(row=xpos, column=ypos)

        # For binding options see Shipman 54.3. Event types
        button[name]["button"].bind("<Enter>", lambda event: self.on_enter(name))
        button[name]["button"].bind("<Leave>", lambda event: self.on_exit(name))

    def show_buttons(self, name):
        for key, value in self.buttons[name].items():
            print(f"{key}: {value}")


def main():
    root = tk.Tk()
    hx = ButtonHoverExample(root)

    # get colors here: https://www.w3schools.com/colors/colors_picker.asp
    hx.new_button(
        name="Button1", mecolor="#ccccff", mxcolor="#ffcccc", xpos=10, ypos=10
    )
    hx.new_button(
        name="Button2", mecolor="#ccffff", mxcolor="#ffffcc", xpos=10, ypos=100
    )

    # to show stored values:
    hx.show_buttons("Button1")

    root.mainloop()


if __name__ == "__main__":
    main()