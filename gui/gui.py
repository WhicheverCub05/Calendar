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
# https://tkdocs.com/tutorial/grid.html


class UI:
    input_file_l = None
    engineers = []
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
                self.engineers.append(engineer)
                self.add_engineer_row(parent=self.main_frame.grid,engineer=engineer)
                
                for job in engineer.jobs:
                    pass
        else:
            print("file is innaccessable")

        print("dropped")
        

    def add_job_to_row(self, row, column, job):
        # add all the rows and columns one after the other
        # create job Class thing
        job_box = JobBox(job)
        self.main_frame.grid(row=row, column=column)
        pass
        
    def add_engineer_row(self, parent:tk.Widget, engineer:Engineer):
        """adds a row to the parent grid

        Args:
            parent (tkinter.Widget): the parent that has the grid
            engineer (Engineer): and engineer class object 
        """
        tmp_engineer_box = EngineerBox(parent, engineer)
        tmp_engineer_box.grid(column=0, row=len(self.engineers)-1)
        print(f"adding engineer {str(engineer.name)} to grid")

        pass


class EngineerBox(tk.Frame):
    def __init__(self, container, engineer: Engineer):
        super().__init__(self, container=container)
        self.config(height=50, width=50, bd="00ff00")
        self.grid(row=0, column=0)

        self.name_label = tk.Label(self, text=engineer.name)
        self.address_label = tk.Label(self, text=engineer.address)
        
        self.name_label.grid(row=0, column=0)
        self.address_label.grid(row=1, column=0)
        

    def collapse(self):
        self.size = "50x15"
        # all labels that show details can be hidden

class JobBox(tk.Frame):
    def __init__(self, container, job:Job):
        super().__init__(self, container=container)
        self.config(height=50, width=70, bd="ff0000")
        self.grid(column=0, row=0)
        
        self.description_label = tk.Label(self, text=job.description)
        self.location_label = tk.Label(self, job.location)
        self.duration_label = tk.Label(self, text=job.duration)
        self.id_label = tk.Label(self, text=job.id)

        self.description_label.grid(row=0, column=0)
        self.location_label.grid(row=1, column=0)
        self.duration_label.grid(row=2, column=0)
        self.id_label.grid(row=3, column=0)
        