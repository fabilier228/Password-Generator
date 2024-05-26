import tkinter as tk

#Show a frame for the given page name

def show_frame(self, page_name):
    frame = self.frames[page_name]
    frame.tkraise()