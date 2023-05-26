#t1.py
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import main_Temp as mt

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "t1.ui"


class t1:
    def __init__(self, master=None):
        # 1: Create a builder and setup resources path (if you have images)
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('frame1', master)

        # 4: Connect callbacks
        builder.connect_callbacks(self)
        self.builder.get_object("Generate").configure(command=self.run_main)
    
    def run_main(self):
        directory = self.builder.get_object("entry_directory").get()
        times = int(self.builder.get_object("entry_pages").get())
        pdf = self.builder.get_object("checkbox_pdf").get()
        print(pdf)
        
        mt.main(directory, times, pdf)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = t1()
    app.run()
