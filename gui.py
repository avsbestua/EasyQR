import tkinter as tk
from tkinter import ttk

class App:
        root = tk.Tk()
        root.geometry("700x500+400+150") #Setting up window
        root['bg'] = 'snow'
        root.title("EasyQR")

        tk.mainloop()

App()