# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:56:46 2023

@author: iremb
"""

from tkinter import *
from tkinter import ttk

def hesapla():
    try:
        miktar = float(txt_tlmiktar.get())
        kur_secimi = cmb_kursec.get()
        
        if kur_secimi == "USD":
            sonuc = miktar / USD_KUR  
        elif kur_secimi == "EURO":
            sonuc = miktar / EURO_KUR  
        else:
            sonuc = "Geçersiz kur seçimi"
        
        lbl_hesap_sonucu.config(text=sonuc)
    except ValueError:
        lbl_hesap_sonucu.config(text="Hatalı giriş")

anaform = Tk()
anaform.geometry("400x600")

lbl_tlmiktar = Label(
    anaform,
    text="TL : ",
    font="Helvatica 20 bold italic")

txt_tlmiktar = Entry()
lbl_kursec = Label(anaform,
                   text="Kur Seçiniz"
                   )
cmb_kursec = ttk.Combobox(anaform,
                          values=["USD", "EURO"])

lbl_sonuc = Label(anaform,
                  text="Sonuç:")

lbl_hesap_sonucu = Label(anaform,
                         text=".....")

btn_1 = Button(anaform, text="BTN1")
btn_hesapla = ttk.Button(anaform,
                         text="Hesapla",
                         command=hesapla)

USD_KUR = 28.46  
EURO_KUR = 30.36  

lbl_tlmiktar.grid(row=0, column=0)
txt_tlmiktar.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonucu.grid(row=2, column=1)
btn_1.grid(row=3, column=0)
btn_hesapla.grid(row=3, column=1)

anaform.mainloop()
