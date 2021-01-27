import os, time
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x250")
window.title("ImageConveter")


def convert():
    filename = askopenfilename()
    uzanti = z.get()
    try:
        os.system("convert "+filename+" output."+uzanti)
        messagebox.showinfo("Başarılı","Dosyanızın Formatı Başarıyla Değiştirildi")
        time.sleep(1)
        exit()
    except Exception:
        messagebox.showerror("Hata","Lüften Programı Yeniden Çalıştırınız")
        time.sleep(1)
        exit()

label = tk.Label(window, text="ImageConveter").pack()

list = ["png","jpg","bmp","ico","xbm","svg","webp"]

z = tk.StringVar()

formats = ttk.Combobox(window, values=list, textvariable=z).pack()

button = tk.Button(window, text="Dönüştür", command=convert).pack()

window.mainloop()