import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import methods


font = ("Segoe UI", 15)




class App:
        def __init__(self):
                root = tk.Tk()
                root.geometry("800x520+400+150") #Setting up window
                root['bg'] = 'snow'
                root.title("EasyQR")
                root.resizable(width=False, height=False)

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
                eror_cor.set("7%")


                m_btn = tk.Button(root,
                        text="Make QR-Code",
                        bg='snow',
                        font=font,
                        command=lambda : methods.generate(self),
                        width=25)

                m_btn.place(x=350,
                            y=410)


                self.box_size = tk.Scale(root,
                                         from_= 1,
                                         to=21,
                                         bg='snow',
                                         tickinterval=5,
                                         orient=tk.HORIZONTAL,
                                         length=280)
                self.box_size.place(x=50,
                                    y=300)

                self.box_size.set(10)


                tk.Label(root,
                         text='Select box size',
                         bg='snow',
                         font=("Segoe UI",18)).place(x=110,
                                                     y=362)

                self.border_size = tk.Scale(root,   #border size scaler
                                         from_=1,
                                         to=26,
                                         bg='snow',
                                         tickinterval=5,
                                         orient=tk.HORIZONTAL,
                                         length=280)
                self.border_size.place(x=50,
                                    y=400)

                self.border_size.set(5)

                tk.Label(root,
                         text='Select border size',
                         bg='snow',
                         font=("Segoe UI", 18)).place(x=100,
                                                      y=462)


                read_qr = tk.Button(root,
                                    font=font,
                                    bg='snow',
                                    text="Read QR-Code",
                                    command=methods.read)     #QR-Code read button

                read_qr.place(x=350, y=352)

                self.color_select = tk.BooleanVar()
                color_checkbox = tk.Checkbutton(root,
                                                 variable=self.color_select,
                                                 text="Select color manually?",
                                                 bg='snow')
                color_checkbox.place(x=125, y=195)