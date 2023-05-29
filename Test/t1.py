#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import main_Temp as mt
import threading


class t1:
    def __init__(self, master=None):
        # build UI
        frame1 = tk.Frame(master)
        frame1.configure(height=720, width=1280)
        
        self.entry_directory = ttk.Entry(frame1)
        self.entry_directory.configure(justify="center")
        _text_ = 'Generated_Problems'
        self.entry_directory.delete("0", "end")
        self.entry_directory.insert("0", _text_)
        self.entry_directory.pack(side="top")
        
        self.entry_pages = ttk.Entry(frame1)
        self.entry_pages.configure(justify="center")
        _text_ = 'Pages'
        self.entry_pages.delete("0", "end")
        self.entry_pages.insert("0", _text_)
        self.entry_pages.pack(side="top")
        
        global pdf
        pdf = tk.StringVar()
        self.checkbox_pdf = ttk.Checkbutton(frame1)
        self.checkbox_pdf.configure(variable=pdf, offvalue="n", onvalue="y", text='PDF?')
        self.checkbox_pdf.pack(side="top")
        
        self.button_generate = ttk.Button(frame1)
        self.button_generate.configure(text='Generate', command=self.run_main)
        self.button_generate.pack(side="top")
        
        frame1.pack(side="top")

        # Main widget
        self.mainwindow = frame1

    def run_main(self):
        directory = self.entry_directory.get()
        times = int(self.entry_pages.get())

        # Create a new thread to run the document generation task
        t = threading.Thread(target=self.generate_documents, args=(directory, times))
        t.start()

    def generate_documents(self, directory, times):
        try:
            mt.main(directory, times, pdf.get())
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = t1(root)
    app.run()
