import json
import tkinter as tk
from PIL import Image, ImageTk
import functions as func
import customization as custom


# Creating the structure of an App
class PassGen(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        # Creating a container to hold all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, GenPage, SearchPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            self.geometry("600x400")

            frame.grid(row=0, column=0, sticky="nsew")

        # Making a MainPage the starting Page
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# Making and describing Main page which contains:
# - button to go to page with generator
# - button to go to page that provides a function to search for a specific code, then possibly delete it
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=custom.main_bg_color)
        self.controller = controller

        self.controller.title("Password Generator")

        # Creating the structure of a main/starting page

        head_label = tk.Label(self,
                              text="WELCOME TO PASSWORD GENERATOR",
                              font=custom.main_font,
                              bg=custom.main_bg_color,
                              fg=custom.main_f_color)

        start_button = tk.Button(self,
                                  text="START",
                                  command=lambda: controller.show_frame("GenPage"),
                                  font=custom.button_font,
                                  fg=custom.button_fc,
                                  bg=custom.button_bgc,
                                  width=20)

        #sp stands for searchpage
        sp_button = tk.Button(self,
                                 text="FIND CODE",
                                 command=lambda: controller.show_frame("SearchPage"),
                                 font=custom.button_font,
                                 fg=custom.button_fc,
                                 bg=custom.button_bgc,
                                 width=20)

        # packing and placing elements

        head_label.pack(side="top", fill="x", pady=40)
        start_button.pack(pady=20)
        sp_button.pack()


class GenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=custom.main_bg_color)
        self.controller = controller

        # structure of the GenPage

        title_label = tk.Label(self,
                         text="GENERATOR",
                         font=custom.main_font,
                         bg=custom.main_bg_color,
                         fg=custom.main_f_color)

        generate_button = tk.Button(self, text="BACK",
                                command=lambda: controller.show_frame("MainPage"),
                                font=custom.button_font,
                                fg=custom.button_fc,
                                bg=custom.button_bgc,
                                width=20)


        back_button = tk.Button(self, text="BACK",
                           command=lambda: controller.show_frame("MainPage"),
                           font=custom.button_font,
                           fg=custom.button_fc,
                           bg=custom.button_bgc,
                           width=20)

        # packing and placing the elements

        title_label.pack(side="top", fill="x", pady=10)
        back_button.pack(side="bottom", pady=10)


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()




if __name__ == "__main__":
    app = PassGen()
    app.mainloop()
