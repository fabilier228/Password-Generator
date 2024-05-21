import tkinter as tk

class PassGen(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()