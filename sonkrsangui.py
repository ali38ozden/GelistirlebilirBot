import tkinter as tk

class Example(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self, text="Button", command=self.button_clicked)
        self.button.pack()

    def button_clicked(self):
        print(self.button.winfo_id())
        print("Button clicked")

if __name__ == "__main__":
        root = tk.Tk()
        ex = Example(master=root)
        ex.mainloop()
        