import tkinter as tk
from tkinter import ttk
import methods
from PIL import ImageTk, Image

leters = "BIPs"
font = ("BIPs", 15)

color = 'snow'
font_col = 'black'


class App:
        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry("800x520+400+150") #Setting up window
                self.root['bg'] = "snow"
                self.root.title("EasyQR")
                self.root.resizable(width=False, height=False)

                tk.Label(self.root,
                        text="Welcome to EasyQR",
                        font=(leters, 20),
                        bg=color, fg=font_col
                        ).place(x=280, y=0)

                self.inform = ttk.Entry(    #Entry for information to code (url, etc.)
                        self.root,
                        font=font
                        )
                self.inform.place(x=50, y=160)

                tk.Label(self.root,
                         text="Enter information for QR-Code\n(Url, etc.)",
                         bg=color,
                         font=font, fg=font_col
                        ).place(x=42, y=90)

                tk.Label(self.root,
                         text="Select error corection level",
                         bg=color,
                         font=font, fg=font_col
                        ).place(x=55, y=210)


                self.er_c = tk.StringVar()      #For ComboBox

                eror_cor = ttk.Combobox(self.root,     #ComboBox for % of loose
                                      textvariable=self.er_c,
                                      font=font,
                                      state='readonly',
                                      width=19
                                      )
                eror_cor['values'] = ("7%", "15%", "25%", "30%")
                eror_cor.place(x=50, y=250)
                eror_cor.set("7%")


                m_btn = tk.Button(self.root,
                        text="Make QR-Code",
                        bg=color,
                        font=font,
                        command=lambda : methods.generate(self), fg=font_col,
                        width=26)

                m_btn.place(x=350,
                            y=410)


                self.box_size = tk.Scale(self.root,
                                         from_= 1,
                                         to=21,
                                         bg=color,
                                         tickinterval=5,
                                         orient=tk.HORIZONTAL,
                                         length=280,
                                         fg=font_col,
                                         font=(leters, 8))
                self.box_size.place(x=50,
                                    y=295)

                self.box_size.set(10)


                tk.Label(self.root,
                         text='Select box size',
                         bg=color, fg=font_col,
                         font=(leters,18)).place(x=108,
                                                     y=362)

                self.border_size = tk.Scale(self.root,   #border size scaler
                                         from_=1,
                                         to=26,
                                         bg=color,
                                         tickinterval=5,
                                         orient=tk.HORIZONTAL,
                                         length=280,
                                         fg=font_col,
                                         font=(leters, 8))
                self.border_size.place(x=50,
                                    y=400)

                self.border_size.set(5)

                tk.Label(self.root,
                         text='Select border size',
                         bg=color, fg=font_col,
                         font=(leters, 18)).place(x=100,
                                                      y=467)


                read_qr = tk.Button(self.root,
                                    font=font,
                                    bg=color, fg=font_col,
                                    text="Read QR-Code",
                                    command=lambda :methods.read(self))     #QR-Code read button

                read_qr.place(x=350, y=352)

                save_qr = tk.Button(self.root,
                                    font=font,
                                    bg=color, fg=font_col,
                                    text="Save QR-Code",
                                    command=methods.save_qr)     #QR-Code save button

                save_qr.place(x=510, y=352)

                self.color_select = tk.BooleanVar()
                color_checkbox = tk.Checkbutton(self.root,
                                                 variable=self.color_select,
                                                 text="Select color manually?",
                                                 bg=color, fg=font_col,
                                                 font=(leters, 10))
                color_checkbox.place(x=125, y=195)


                default_img = Image.open("pics/defim.png")  # Putting default image to qr_label
                default_img = default_img.resize((250, 250),
                                                 Image.LANCZOS)
                self.default_tk_img = ImageTk.PhotoImage(default_img)


                self.qr_label = tk.Label(self.root, image=self.default_tk_img) #Label for image
                self.qr_label.place(x=380, y=70)