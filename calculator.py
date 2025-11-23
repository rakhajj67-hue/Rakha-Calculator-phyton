from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("RAKHA CALCULATOR")
root.geometry("340x480")
root.configure(bg="#222831")

myfont = font.Font(size=18, weight="bold")

e1 = Entry(root, width=18, borderwidth=0, justify="right")
e1["font"] = myfont
e1["bg"] = "#ececec"
e1["fg"] = "#222831"
e1.grid(row=0, column=0, columnspan=4, padx=20, pady=30, ipady=15)

def angka(nilai):
    sebelum = e1.get()
    # Jika entry hanya berisi operator, hapus dulu
    if sebelum in ["+", "-", "×", "÷"]:
        e1.delete(0,END)
        sebelum = ""
    e1.insert(END, str(nilai))
    print(nilai)

def tambah():
    nomor_awal = e1.get()
    global n_awal
    global matemat
    matemat = "penjumlahan"
    n_awal = int(nomor_awal)
    e1.delete(0,END)
    e1.insert(0, "+")
def kurang():
    nomor_awal = e1.get()
    global n_awal
    global matemat
    matemat = "pengurangan"
    n_awal = int(nomor_awal)
    e1.delete(0,END)
    e1.insert(0, "-")
def kali():
    nomor_awal = e1.get()
    global n_awal
    global matemat
    matemat = "perkalian"
    n_awal = int(nomor_awal)
    e1.delete(0,END)
    e1.insert(0, "×")
def bagi():
    nomor_awal = e1.get()
    global n_awal
    global matemat
    matemat = "pembagian"
    n_awal = int(nomor_awal)
    e1.delete(0,END)
    e1.insert(0, "÷")
def hapus():
    e1.delete(0,END)
def samadengan():
    nomor_akhir = e1.get()
    e1.delete(0,END)
    if matemat == "penjumlahan":
        e1.insert(0,n_awal + int(nomor_akhir))
    elif matemat == "pengurangan":
        e1.insert(0,n_awal - int(nomor_akhir))
    elif matemat == "perkalian":
        e1.insert(0,n_awal * int(nomor_akhir))
    elif matemat == "pembagian":
        try:
            hitung = n_awal / int(nomor_akhir)
            e1.insert(0,hitung)
        except ZeroDivisionError:
            e1.insert(0,'maaf sistem sedang error')




button_style = {
    "font": myfont,
    "bg": "#393e46",
    "fg": "#eeeeee",
    "activebackground": "#00adb5",
    "activeforeground": "#222831",
    "bd": 0,
    "width": 4,
    "height": 2,
    "relief": "flat"
}

btn1 = Button(root, text="1", command=lambda:angka(1), **button_style)
btn2 = Button(root, text="2", command=lambda:angka(2), **button_style)
btn3 = Button(root, text="3", command=lambda:angka(3), **button_style)
btn4 = Button(root, text="4", command=lambda:angka(4), **button_style)
btn5 = Button(root, text="5", command=lambda:angka(5), **button_style)
btn6 = Button(root, text="6", command=lambda:angka(6), **button_style)
btn7 = Button(root, text="7", command=lambda:angka(7), **button_style)
btn8 = Button(root, text="8", command=lambda:angka(8), **button_style)
btn9 = Button(root, text="9", command=lambda:angka(9), **button_style)
btn0 = Button(root, text="0", command=lambda:angka(0), **button_style)

tamb = Button(root, text="+", command=tambah, **button_style)
kurng = Button(root, text="-", command=kurang, **button_style)
kal = Button(root, text="×", command=kali, **button_style)
bag = Button(root, text="÷", command=bagi, **button_style)
haps = Button(root, text="C", command=hapus, font=myfont, bg="#ff5722", fg="#fff", activebackground="#ff784e", activeforeground="#222831", bd=0, width=4, height=2, relief="flat")
samadngn = Button(root, text="=", command=samadengan, font=myfont, bg="#00adb5", fg="#222831", activebackground="#00cfcf", activeforeground="#222831", bd=0, width=4, height=2, relief="flat")

btn7.grid(row=1, column=0, padx=5, pady=5)
btn8.grid(row=1, column=1, padx=5, pady=5)
btn9.grid(row=1, column=2, padx=5, pady=5)
bag.grid(row=1, column=3, padx=5, pady=5)

btn4.grid(row=2, column=0, padx=5, pady=5)
btn5.grid(row=2, column=1, padx=5, pady=5)
btn6.grid(row=2, column=2, padx=5, pady=5)
kal.grid(row=2, column=3, padx=5, pady=5)

btn1.grid(row=3, column=0, padx=5, pady=5)
btn2.grid(row=3, column=1, padx=5, pady=5)
btn3.grid(row=3, column=2, padx=5, pady=5)
kurng.grid(row=3, column=3, padx=5, pady=5)

haps.grid(row=4, column=0, padx=5, pady=5)
btn0.grid(row=4, column=1, padx=5, pady=5)
samadngn.grid(row=4, column=2, padx=5, pady=5)
tamb.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()