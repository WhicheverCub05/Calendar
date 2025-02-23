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


class UI(TkinterDnD.Tk):
    input_file_l = None
    engineers = []
    def __init__(self):
        super().__init__()
        self.title("Octo-p y")

        self.geometry = "700x350"
        self.minsize(500, 300)
        self.maxsize(800, 800)
        
        self.configure(background="slate blue")


        self.mf = tk.Frame(self, bg='blue')
        
        self.canvas = CanvasFrame(self.mf)
        

        self.canvas.drop_target_register(DND_FILES)
        self.canvas.dnd_bind("<<Drop>>", self.drop_inside_frame)

        input_file_l = tk.Label(self, text="Waiting", border=2)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.mf.grid(sticky='nsew')
        self.mf.columnconfigure(0, weight=1)
        self.mf.rowconfigure(0, weight=1)
        
        self.canvas.grid(sticky='nsew')
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.rowconfigure(0, weight=1)
        
        # scrollbars 
        scrollbar_h = ttk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
        scrollbar_v = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        
        self.canvas.configure(yscrollcommand = scrollbar_v.set)
        self.canvas.configure(xscrollcommand = scrollbar_h.set)
        self.canvas.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), "units"))
        self.canvas.bind('<Control MouseWheel>', lambda event: self.canvas.xview_scroll(-int(event.delta/60), "units"))


        scrollbar_v.place(relx=1, rely=0, relheight=1, anchor='ne')
        scrollbar_h.place(relx=0, rely=1, relwidth=1, anchor='sw')
        

        self.mainloop()


    def drop_inside_frame(self, event):
    
        # read file from path, parse file and then display organised calandar  
        # global input_file_l
        file_path = str(event.data)
        file_path = file_path.replace('{', '')
        file_path = file_path.replace('}', '')
        #self.input_file_l.config(text="Dropped!")
        print(f"Trying to open {file_path}")

        if os.path.isfile(file_path):
            # add engineers from here
            engineer_soup = wp.open_file_from_path(file_path)
            engineer_list = wp.create_engineer_list(engineer_soup)
            # add engineer rows in the main_frame
            engineers_added = 0
            for engineer in engineer_list:
                self.engineers.append(engineer)
                self.add_engineer_row(parent=self.canvas, engineer=engineer)
                
                jobs_added = 0
                for job in engineer.jobs:
                    self.add_job_to_row(parent=self.canvas, row=engineers_added+1, column=jobs_added+1, job=job)
                    jobs_added += 1
                
                engineers_added += 1

        else:
            print("file is innaccessable")

        print("dropped")
        

    def add_job_to_row(self, parent, row, column, job):
        # add all the rows and columns one after the other
        # create job Class thing
        job_box = JobBox(parent=parent, job=job)
        job_box.grid(row=row, column=column)
        
        
    def add_engineer_row(self, parent, engineer:Engineer):
        """adds a row to the parent grid

        Args:
            parent (tkinter.Widget): the parent that has the grid
            engineer (Engineer): and engineer class object 
        """
        tmp_engineer_box = EngineerBox(parent=parent, engineer=engineer)
        tmp_engineer_box.grid(column=0, row=len(self.engineers))
        print(f"adding engineer {str(engineer.name)} to grid")



class CanvasFrame(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, scrollregion = (0, 0, 2000, 5000), bg='red')
        self.create_line(0, 0, 2000, 5000, fill='black', width=10)


class EngineerBox(tk.Frame):
    def __init__(self, parent, engineer: Engineer):
        super().__init__(parent)
        self.config(height=50, width=100, background="grey")

        self.grid(row=0, column=0)
        
        self.name_label = tk.Label(self, text=engineer.name)
        self.address_label = tk.Label(self, text=f"{engineer.name[0]}.address")
        
        self.name_label.grid(row=0, column=0)
        self.address_label.grid(row=1, column=0)
        

    def collapse(self):
        self.size = "50x15"
        # all labels that show details can be hidden


class JobBox(tk.Frame):
    def __init__(self, parent, job:Job):
        super().__init__(parent)
        self.config(height=50, width=70, background="blue")
        
        self.grid(column=0, row=0)
        self.description_label = tk.Label(self, text=job.description)
        self.location_label = tk.Label(self, text=job.location)
        self.duration_label = tk.Label(self, text=job.duration)
        self.id_label = tk.Label(self, text=job.id)

        self.description_label.grid(row=0, column=0)
        self.location_label.grid(row=1, column=0)
        self.duration_label.grid(row=2, column=0)
        self.id_label.grid(row=3, column=0)
        