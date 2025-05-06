import qrcode
from tkinter.messagebox import *
from tkinter import colorchooser
from PIL import Image

def choose_color(tittle):
    color = colorchooser.askcolor(title=tittle)
    return color[0]

def qr_code(self, error_cor):  # Qr code generator
    data = self.inform.get()
    if data:
        qr = qrcode.QRCode(version=1, error_correction=error_cor, box_size=self.box_size.get(),
                           border=self.border_size.get())
        qr.add_data(data)
        qr.make()

        image = qr.make_image(fill_color=choose_color("Fill color"), back_color=choose_color("Background color"))
        image.save(f"{self.name.get()}.png")

        img = Image.open(f"{self.name.get()}.png")
        img.show()

    else:
        showerror("Error", "Please enter information to code")


def generate(self):  # Qr code generator
    print("work")
    eror_corect = self.er_c.get()
    if eror_corect:
        if eror_corect == '7%':
            qr_code(self, qrcode.ERROR_CORRECT_L)
        elif eror_corect == '15%':
            qr_code(self, qrcode.ERROR_CORRECT_M)
        elif eror_corect == '25%':
            qr_code(self, qrcode.ERROR_CORRECT_Q)
        elif eror_corect == '30%':
            qr_code(self, qrcode.ERROR_CORRECT_H)


    else:
        showerror("Error", "Select error correction level")