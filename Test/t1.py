#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import main_Temp as mt


class t1:
    def __init__(self, master=None):
        # build ui
        frame1 = tk.Frame(master)
        frame1.configure(height=720, width=1280)
        labelframe1 = ttk.Labelframe(frame1)
        labelframe1.configure(height=200, text='labelframe1', width=200)
        self.entry_directory = ttk.Entry(labelframe1)
        self.entry_directory.configure(justify="center")
        _text_ = 'Generated_Problems'
        self.entry_directory.delete("0", "end")
        self.entry_directory.insert("0", _text_)
        self.entry_directory.pack(side="top")
        self.entry_pages = ttk.Entry(labelframe1)
        self.entry_pages.configure(justify="center")
        _text_ = 'Pages'
        self.entry_pages.delete("0", "end")
        self.entry_pages.insert("0", _text_)
        self.entry_pages.pack(side="top")
        self.checkbox_pdf = ttk.Checkbutton(labelframe1)
        global pdf
        pdf  = tk.StringVar()
        self.checkbox_pdf.configure(variable=pdf,offvalue="n", onvalue="y", text='PDF?')
        self.checkbox_pdf.pack(side="top")
        self.Generate = ttk.Button(labelframe1)
        self.Generate.configure(text='Generate', command=self.run_main())
        self.Generate.pack(side="top")
        labelframe1.pack(side="top")
        frame1.pack(side="top")

        # Main widget
        self.mainwindow = frame1
        
    def run_main(self):
        directory = self.entry_directory.get()
        times = int(self.entry_pages.get())
        
        mt.main(directory, times, pdf)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = t1
    app.run()
