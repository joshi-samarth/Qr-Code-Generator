import tkinter as tk
import qrcode as Qr
from PIL import Image,ImageTk
def generate_qr_code():
    text=entry.get()
    if text:
        qr=Qr.QRCode(version=1,box_size=10,border=5)
        qr.add_data(text)
        qr.make(fit=True)
        image=qr.make_image(fill="black",back_color="white")
        image=image.resize((200,200),Image.ANTIALIAS)
        image.save("qrcode.png")
        photo=ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image=photo
Window=tk.Tk()
Window.title("Qr code generator")
Window.geometry("500x500")
entry=tk.Entry(Window,font=("Arial,14"))
entry.pack(pady=10)
button=tk.Button(Window,text="generateQR code",command=generate_qr_code)
button.pack(pady=30)
label=tk.Label(Window)
label.pack(pady=40)
Window.mainloop()