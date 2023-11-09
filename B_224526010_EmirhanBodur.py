# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:21:10 2023

@author: Emirhan
"""

import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests


def get_currency(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currency = soup.find("div", class_=class_name).text.strip()
    a = currency.replace(",",".")
    return round(float(a))

url_usd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
url_euro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

rounded_dolar = get_currency(url_usd, "YMlKec fxKbKc")
rounded_euro = get_currency(url_euro, "YMlKec fxKbKc")

def hesapla():
    tl_miktar = float(ent_miktar.get())
    secilen_kur = cmb_kursec.get()
    if secilen_kur == "USD":
        if rounded_dolar != 0:
            sonuc = tl_miktar / rounded_dolar
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
        else:
            lbl_hesap_sonuc.config(text="Değer alınmadı!")
    elif secilen_kur == "EURO":
        if rounded_euro != 0:
            sonuc = tl_miktar / rounded_euro
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")
        else:
            lbl_hesap_sonuc.config(text="Değer alınmadı!")


anasayfa = tk.Tk()
anasayfa.geometry("300x200")
anasayfa.title("Döviz Çevirici")

lbl_tlmiktar = tk.Label(anasayfa,text="TL Miktarı ",font=("Helvetica 10 bold "))

ent_miktar = tk.Entry()


lbl_kursec = tk.Label(anasayfa,text="Döviz Kuru Seçiniz",font=("Helvatica 10 bold "))

cmb_kursec = ttk.Combobox(anasayfa, values=["USD", "EURO"])

lbl_sonuc = tk.Label(anasayfa, text="Sonuç: ", font=("Helvatica 10 bold "))
lbl_hesap_sonuc = tk.Label(anasayfa, text="")

btn_hesapla = ttk.Button(anasayfa, text="Hesapla")

btn_hesapla.config(command=hesapla)
lbl_tlmiktar.grid(row=0, column=0)
ent_miktar.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonuc.grid(row=2, column=1)
btn_hesapla.grid(row=3, column=0)

anasayfa.mainloop()