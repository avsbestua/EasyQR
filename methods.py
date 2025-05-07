import qrcode
from tkinter.messagebox import *
from tkinter import colorchooser, filedialog
from PIL import Image
from cv2 import imread
from pyzbar.pyzbar import decode

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

        if self.color_select.get() == True:
            code_color = choose_color("Code color")
            back_color = choose_color("Background color")       #Checking flag "Select color manually"
        else:
            code_color = (0, 0, 0)
            back_color = (255, 255, 255)

        image = qr.make_image(fill_color=code_color, back_color=back_color)
        image.save(f"{self.name.get()}{self.formatsq.get()}")

        img = Image.open(f"{self.name.get()}{self.formatsq.get()}")
        img.show()

    else:
        showerror("Error", "Please enter information to code")


def generate(self):  # Qr code generator
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

def read():
    path = filedialog.askopenfilename(title="Select QR-Code",
                                      filetypes=[('Images', "*.png *.jpg *.bmp *.svg")])
    file = imread(path)         #OpenCv imread for opening qr code
    code = decode(file)

    if code:
        for c in code:
            data = c.data.decode('utf-8')
            showinfo("QR-Code reading", f"Information: {data}")

    else: showerror("Error", "QR-Code not found")
