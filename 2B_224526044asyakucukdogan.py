from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def get_currency(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currency = soup.find("div", class_=class_name).text.strip()
    a = currency.replace(",", ".")
    return round(float(a), 4)

url_usd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
url_euro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

rounded_dolar = get_currency(url_usd, "YMlKec fxKbKc")
rounded_euro = get_currency(url_euro, "YMlKec fxKbKc")

def hesapla():
    try:
        tl_miktar = float(ent_miktar.get())
        secilen_kur = cmb_kursec.get()
        
        if secilen_kur == "USD":
            if rounded_dolar != 0:
                sonuc = tl_miktar / rounded_dolar
                lbl_hesap_sonucu.config(text="{:.2f} dolar".format(sonuc))
            else:
                lbl_hesap_sonucu.config(text="Değer alınmadı!")
        elif secilen_kur == "EURO":
            if rounded_euro != 0:
                sonuc = tl_miktar / rounded_euro
                lbl_hesap_sonucu.config(text="{:.2f} euro".format(sonuc))
            else:
                lbl_hesap_sonucu.config(text="Değer alınmadı!")
    except ValueError:
        lbl_hesap_sonucu.config(text="Geçersiz miktar")

anaform = Tk()
anaform.geometry("400x600")
anaform.configure(bg="#FFCBDB")

lbl_tlmiktar = Label(
    anaform,
    text="TL :",
    font=("Comic Sans MS", 20, "bold italic"),
    bg="#FFCBDB")

ent_miktar = Entry(anaform)
lbl_kursec = Label(anaform,
                   text="Kur Seçiniz",
                   font=("Comic Sans MS", 12),
                   bg="#FFCBDB")
cmb_kursec = ttk.Combobox(anaform,
                          values=["USD", "EURO"],
                          font=("Comic Sans MS", 12),
                          state="readonly",
                          background="#FFCBDB")
lbl_sonuc = Label(anaform,
                  text="Sonuç:",
                  font=("Comic Sans MS", 12),
                  bg="#FFCBDB")
lbl_hesap_sonucu = Label(anaform,
                         text=".........",
                         font=("Comic Sans MS", 12, "bold"),
                         bg="#FFCBDB")
btn_hesapla = ttk.Button(anaform,
                         text="Hesapla",
                         command=hesapla,
                         style="TButton",
                         cursor="hand2")


style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 12),
                background="#FFCBDB")

lbl_tlmiktar.grid(row=0, column=0)
lbl_sonuc.grid(row=2, column=0)
ent_miktar.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_hesap_sonucu.grid(row=2, column=1)
btn_hesapla.grid(row=3, column=1)

anaform.mainloop()
