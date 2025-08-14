import threading
import webbrowser
import winsound
import numpy as np
import qrcode, io
from tkinter.messagebox import *
from tkinter import colorchooser, filedialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import cv2

def choose_color(tittle): #choose color function
    color = colorchooser.askcolor(title=tittle)
    return color[0]

image = None
def qr_code(self, error_cor):  # Qr code generator
    data = self.inform.get()
    if data:
        qr = qrcode.QRCode(version=1, error_correction=error_cor, box_size=self.box_size.get(),
                           border=self.border_size.get())
        qr.add_data(data)
        qr.make()

        if self.color_select.get() == True:
            code_color = choose_color("Code color")
            back_color = choose_color("Background color")       #Checking flag "Select color manually?"
        else:
            code_color = (0, 0, 0)
            back_color = (255, 255, 255)

        global image

        image = qr.make_image(fill_color=code_color, back_color=back_color)

        img = image.resize((250, 250), Image.LANCZOS) #Size fo preview

        tk_img = ImageTk.PhotoImage(img)

        self.qr_label.config(image=tk_img)
        self.qr_label.image = tk_img

    else:
        showerror("Error", "Please enter information to code")

def save_qr():
    if image:
        path = filedialog.asksaveasfilename(title="Save as...",
                                            defaultextension=".png",
                                            filetypes=[("PNG", "*.png"), ('JPG', "*.jpg"),
                                                       ("BMP", "*.bmp")],
                                            initialfile="qr_code")
        image.save(path)

    else: showerror("Error", "Please generate QR-Code before saving")


def generate(self):  # Error correction
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


def code_decode(code, self):
    for c in code:
        data = c.data.decode('utf-8')
        if data.startswith("http://") or data.startswith("https://"):
            if askyesno("Link detected", f"Should open {data} in browser?"):  # Should open if link detected?
                webbrowser.open(data)
        else:
            if askyesno("QR-Code reading", f"Information: {data}, should copy into clipboard"):
                self.root.clipboard_append(data)



def read(self=None, cam_mode=False, cap=None):

    if not cam_mode:
        path = filedialog.askopenfilename(title="Select QR-Code",
                                          filetypes=[('Images', "*.png *.jpg *.bmp")])
        if path:
            file = Image.open(path)

            img_ocv = np.array(file.convert("L"))

            _, binary = cv2.threshold(
                img_ocv, 0, 255,
                cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            file = binary

    else:
        file = Image.fromarray(cap)

    code = decode(file)

    if code:
        winsound.Beep(900, 350)
        code_decode(code, self)
    else:
        showerror("Code not Found", "QR-Code not found on this image")


def scan_qr():
    showinfo("Info", "Please wait a few seconds, camera is starting. Press q to exit")

    cam = cv2.VideoCapture(0) #You can write other camera index instead 0, usually 0 is main camera
    while True:
        ret, cap = cam.read()

        if not ret:
            showerror("Error", "Please check your camera")
            break

        cv2.putText(cap,
                    "Press Q to exit",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA)

        cv2.imshow("EasyQR", cap)
        read(cam_mode=True, cap=cap)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def start_cam_thread():
    threading.Thread(target=scan_qr, daemon=True).start()