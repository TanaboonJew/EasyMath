import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Python rock!")
greeting.pack()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()
window.mainloop()