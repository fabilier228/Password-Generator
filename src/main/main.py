import json
import tkinter as tk
from PIL import Image, ImageTk
import customization as custom
import random


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


        #function createEntryWithPass() creates an entry with generated password in it
        def createEntryWithPass(password):
            entry_text = tk.StringVar()
            entry_text.set(password)

            entry = tk.Entry(self,
                             textvariable=entry_text,
                             font=custom.main_bg_color,
                             fg=custom.button_fc,
                             bg=custom.button_bgc,
                             width=20,
                             borderwidth=3
                             )
            entry.pack(pady=20)
            entry.place(x=206, y=180)


        # getValue() takes from the entry a value, then if it is an integer
        # creates a password of that length
        def getValue():
            try:
                value = int(entry_length.get())
                znaki = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                liczby = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                password = ""
                for i in range(value):
                    rand = random.randint(0, 1)
                    if rand == 0:
                        password += znaki[random.randint(0, len(znaki) - 1)]
                    else:
                        password += liczby[random.randint(0, len(liczby) - 1)]
                with open("../data/data.json", 'r') as file:
                    data = json.load(file)

                if password not in data:
                    data.append(password)
                    createEntryWithPass(password)
                with open("../data/data.json", "w") as dane:
                    json.dump(data, dane)
            except ValueError:
                errorpage = tk.Tk()
                errorpage.geometry("300x100")
                errorpage.title("ValueError")
                lbl = tk.Label(errorpage,
                               text="IT'S NOT A NUMBER",
                               font=("Arial", 18, "bold"),
                               fg="Black")

                lbl.pack()
                errorpage.mainloop()


        # structure of the GenPage

        title_label = tk.Label(self,
                         text="GENERATOR",
                         font=custom.main_font,
                         bg=custom.main_bg_color,
                         fg=custom.main_f_color)

        description_label = tk.Label(self,
                                     text="Define the length",
                                     font=custom.lower_basic_font,
                                     bg=custom.main_bg_color,
                                     fg=custom.main_f_color
                                     )

        back_button = tk.Button(self, text="BACK",
                           command=lambda: controller.show_frame("MainPage"),
                           font=custom.button_font,
                           fg=custom.button_fc,
                           bg=custom.button_bgc,
                           width=20)

        entry_length = tk.Entry(self,
                                font=custom.main_bg_color,
                                fg=custom.main_bg_color,
                                bg=custom.button_bgc,
                                width=20,
                                borderwidth=3
                                )

        generate_button = tk.Button(self, text="GENERATE",
                                command= getValue,
                                font=custom.button_font,
                                fg=custom.button_fc,
                                bg=custom.button_bgc,
                                width=20)
        # packing and placing the elements on GenPage

        title_label.pack(side="top", fill="x", pady=10)

        description_label.pack()
        description_label.place(x=240, y=100)

        back_button.pack(side="bottom", pady=10)

        entry_length.pack()
        entry_length.place(x=206,y=140)

        generate_button.pack()
        generate_button.place(x=206, y=230)




class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=custom.main_bg_color)
        self.controller = controller

        # functions
        def createTitle(sentence, x, y):
            label = tk.Label(self,
                                   text=sentence,
                                   font=custom.lower_basic_font,
                                   bg=custom.main_bg_color,
                                   fg=custom.main_f_color,
                                    height=300)

            label.pack()
            label.place(x=x, y=y)

        def findCode():
            code = code_entry.get().upper()
            with open("../data/data.json", 'r') as file:
                data = json.load(file)

            if code not in data:
                createTitle("THERE IS NO SUCH CODE", x=180, y=170)
            else:
                createTitle("DO YOU WANT TO DELETE IT?", x=180, y=170)

                no_button = tk.Button(self, text="NO",
                                command=lambda: controller.show_frame("MainPage"),
                                font=custom.button_font_small,
                                fg=custom.button_fc,
                                bg=custom.button_bgc,
                                width=20)
                yes_button = tk.Button(self, text="YES",
                                command=lambda: controller.show_frame("MainPage"),
                                font=custom.button_font_small,
                                fg=custom.button_fc,
                                bg=custom.button_bgc,
                                width=20)

                yes_button.pack()
                yes_button.place(x=180, y=210)

                no_button.pack()
                no_button.place(x=295, y=210)


        # structure of the SearchPage

        title_label = tk.Label(self,
                               text="FIND CODE",
                               font=custom.main_font,
                               bg=custom.main_bg_color,
                               fg=custom.main_f_color)

        code_entry = tk.Entry(self,
                                font=custom.main_bg_color,
                                fg=custom.main_bg_color,
                                bg=custom.button_bgc,
                                width=40,
                                borderwidth=3
                                )


        search_button = tk.Button(self, text="SEARCH",
                                command=findCode,
                                font=custom.button_font_small,
                                fg=custom.button_fc,
                                bg=custom.button_bgc,
                                width=20)


        back_button = tk.Button(self, text="BACK",
                                command=lambda: controller.show_frame("MainPage"),
                                font=custom.button_font,
                                fg=custom.button_fc,
                                bg=custom.button_bgc,
                                width=10)

        # packing and placing the elements on a SearchPage

        title_label.pack(side="top", fill="x", pady=10)

        code_entry.pack()
        code_entry.place(x=80, y=140)

        search_button.pack()
        search_button.place(x=455, y=141)

        back_button.pack(side="bottom", pady=10)


if __name__ == "__main__":
    app = PassGen()
    app.mainloop()
