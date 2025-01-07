import os
import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title('QrCode Generator')
root.geometry('350x400')
root.configure(bg='#3f3f3f')
frm = ttk.Frame(root, padding=10)

def Qr():
    img = qrcode.make(str(entry_var.get()))
    img.save('QrCode.png')
    image_qr = ImageTk.PhotoImage(Image.open('QrCode.png'))
    label_qr.config(image=image_qr)
    label_qr.image = image_qr
    label_qr.pack()

def Focus():
    entry.focus_set()

def Dellete():
    if os.path.exists('QrCode.png'):
        os.remove('QrCode.png')
    entry.delete(0, END) 
    Focus()       
    label_qr.config(image='')
    label_qr.image = None

def check_entry(*args):
    if entry_var.get().strip() == '':
        btn['state'] = 'disabled'
    else:
        btn['state'] = 'normal'

label = ttk.Label(text='Введите ссылку и программа сгенерирует Qr код ')

entry_var = StringVar()
entry_var.trace_add('write', check_entry)

entry = ttk.Entry(width=30, textvariable=entry_var)
btn = ttk.Button(text='Сгенерировать', command=Qr, width=30, state='disabled')
btn2 = ttk.Button(text='Удалить', command=Dellete, width=30)
label_qr = Label(root)

label.pack(side=TOP)
entry.pack(side=TOP, pady=5)
btn.pack(side=TOP, pady=3)
btn2.pack(side=TOP)
label_qr.pack()

if __name__ == '__main__':
    root.mainloop()
