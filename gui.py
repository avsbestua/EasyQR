import tkinter as tk
from tkinter import ttk
import qrcode as qr
from tkinter.messagebox import *
from PIL import Image

font = ("Segoe UI", 15)

class App:
        def __init__(self):
                root = tk.Tk()
                root.geometry("800x500+400+150") #Setting up window
                root['bg'] = 'snow'
                root.title("EasyQR")


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

                m_btn = tk.Button(root,
                        text="Make QR-Code",
                        bg='snow',
                        font=font,
                        command=self.generate,
                        width=25)

                m_btn.place(x=350, y=410)

                self.box_size = tk.Scale(root, from_= 1 ,to=21, bg='snow', tickinterval=5, orient=tk.HORIZONTAL, length=280)
                self.box_size.place(x=50, y=300)

                tk.Label(root, text='Select box size', bg='snow', font=("Segoe UI", 18)).place(x=110, y=362)

        def qr_code(self, error_cor): #Qr code generator
            data = self.inform.get()
            if data:
                img = qr.make(data=data, error_correction=error_cor, box_size=self.box_size.get())
                img.save("qr.png")
            else: showerror("Error", "Please enter information to code")

        def generate(self):     #Qr code generator
            print("work")
            eror_corect = self.er_c.get()
            if eror_corect:
                if eror_corect == '7%':
                    self.qr_code(qr.ERROR_CORRECT_L)
                elif eror_corect == '15%':
                    self.qr_code(qr.ERROR_CORRECT_M)
                elif eror_corect == '25%':
                    self.qr_code(qr.ERROR_CORRECT_Q)
                elif eror_corect == '30%':
                    self.qr_code(qr.ERROR_CORRECT_H)
            else: showerror("Error", "Select error correction level")

            showinfo("Save", "This QR-Code saved in app directory")
            img = Image.open("qr.png")
            img.show()

if __name__ == "__main__":
    t = App()
    tk.mainloop()