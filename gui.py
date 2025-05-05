import tkinter as tk
from tkinter import ttk

font = ("Segoe UI", 15)

class App:
        def __init__(self):
                root = tk.Tk()
                root.geometry("800x500+400+150") #Setting up window
                root['bg'] = 'snow'
                root.title("EasyQR")

                style = ttk.Style()
                style.theme_use('xpnative')

                tk.Label(root,
                        text="Welcome to EasyQR",
                        font=("Segoe UI Bold", 20),
                        bg='snow'
                        ).place(x=280, y=0)

                self.inform = ttk.Entry(    #Entry for information to code (url, etc.)
                        root,
                        font=font
                        )
                self.inform.place(x=80, y=160)

                tk.Label(root,
                         text="Enter information for QR-Code\n(Url, etc.)",
                         bg='snow',
                         font=font
                        ).place(x=62, y=90)

                tk.Label(root,
                         text="Select error corection level",
                         bg='snow',
                         font=font
                        ).place(x=75, y=210)


                self.er_c = tk.StringVar()      #For ComboBox

                eror_cor = ttk.Combobox(root,     #ComboBox for % of loose
                                      textvariable=self.er_c,
                                      font=font,
                                      state='readonly'
                                      )
                eror_cor['values'] = ("7%", "15%", "25%", "30%")
                eror_cor.place(x=70, y=250)
                tk.mainloop()


