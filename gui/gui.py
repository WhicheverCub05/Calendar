import tkinter as tk
from tkinter import ttk
from tkinter import dnd as tkdnd
from tkinterdnd2 import DND_FILES, TkinterDnD

from obj.engineer import Engineer
from obj.job import Job
from obj.schedule import Schedule

import web_parser.web_parser as wp

import os

# https://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/

class UI:
    input_file_l = None
    def __init__(self, master):
        self.root = master
        self.root.title("Octo-py")

        self.geometry = "700x350"
        self.root.minsize(500, 300)
        self.root.maxsize(800, 400)
        # self.root.iconbitmap("add one later")
        # self.drag_and_drop_label = tk.Label(text="Drag and drop html file into this window")
        
        self.main_frame = tk.Frame(self.root, bg="slate blue", height=300)
        self.main_frame.grid(row=0, column=0, sticky=("nsew"))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        input_label_stat = "Waiting"
        self.input_file_l = tk.Label(self.main_frame, text=input_label_stat, border=2)
        self.input_file_l.grid(column=0, row=0)

        self.main_frame.drop_target_register(DND_FILES)
        self.main_frame.dnd_bind("<<Drop>>", self.drop_inside_frame)
        

        """
        self.feet = tk.StringVar()
        self.feet_entry=ttk.Entry(self.main_frame, width=140, textvariable=self.feet)
        self.feet_entry.grid(column=2, row=3, sticky=("nsew"), paddy=2)

        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        https://www.reddit.com/r/learnpython/comments/8cwmjm/tkinter_frame_not_expanding_to_fit_window/

        self.grid = tk.Grid()

        pack all here.
        self.drag_and_drop_label.pack()
        self.main_frame.pack()
        self.grid.pack()"""

    def drop_inside_frame(self, event):
    
        # read file from path, parse file and then display organised calandar  
        # global input_file_l
        file_path = str(event.data)
        file_path = file_path.replace('{', '')
        file_path = file_path.replace('}', '')
        self.input_file_l.config(text="Dropped!")
        print(f"Trying to open {file_path}")

        if os.path.isfile(file_path):
            # add engineers from here
            engineer_soup = wp.open_file_from_path(file_path)
            engineer_list = wp.create_engineer_list(engineer_soup)

            # add engineer rows in the main_frame
            for engineer in engineer_list:
                self.add_engineer_row(parent=self.main_frame.grid,engineer=engineer)
        else:
            print("file is innaccessable")

        print("dropped")
        

    def set_schedule(self, schedule:Schedule):
        # add all the rows and columns one after the other
        pass
        
    def add_engineer_row(self, parent:tk.Widget, engineer:Engineer):
        """adds a row to the parent grid

        Args:
            parent (tkinter.Widget): the parent that has the grid
            engineer (Engineer): and engineer class object 
        """
        parent.tk_focusFollowsMouse()
        

        pass


class EngineerBox(tk.Frame):
    def __init__(self, parent, row, engineer: Engineer):
        super().__init__(parent=parent)
        self.main_frame_row = row
        self.bd = "00ff00"
        self.size = "50x50"
        self.name = engineer.name
        self.address = engineer.address

        self.name_label = tk.Label(self, text=self.name)
        self.address_label = tk.Label(self, text=self.address)
        self.name_label.pack()
        self.address_label.pack()
        # self.main_frame_row.pack()
        print(f"Engineer {engineer.__str__()} added")
        

    def collapse(self):
        self.size = "50x15"
        # all labels that show details can be hidden



class EngineerRow(tk.Grid):
    def __init__(self, parent, row, engineer: Engineer):
        super().__init__(parent=parent)
        self.bd = "ff00f0"
        self.size = "50x200"

        