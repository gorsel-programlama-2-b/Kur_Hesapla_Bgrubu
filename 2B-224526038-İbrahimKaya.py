from tkinter import *
from tkinter import ttk  
import requests
from bs4 import BeautifulSoup

def hesapla():
       link = f"https://valuta.exchange/try-to-{cmb_kursec.get()}?amount={ent_miktar.get()}"
       dönen_sayfa = requests.get(link)
       soup = BeautifulSoup(dönen_sayfa.text, 'html.parser')
       sonuc = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
       lbl_hesap_sonucu.configure(text = "Sonuç : " + sonuc["value"])


anaform = Tk()
anaform.geometry("400x600")

lbl_tlmiktar = Label(
    anaform,
    text="TL :",
    font=("Helvectia 20 bold"))

ent_miktar = Entry(anaform)
lbl_kursec = Label(anaform, 
                   text="Kur Seçiniz :",
                   font=("Helvectia 20 bold"))
cmb_kursec = ttk.Combobox(anaform,
                          values=["USD","EUR"])
lbl_sonuc = Label(anaform,
                  text="Sonuç :",
                  font=("Helvectia 20 bold"))

lbl_hesap_sonucu = Label(anaform,
                         text="............")


btn_1 = Button(anaform,
               text="BTN1",
               font=("Helvectia 10 bold"))

btn_hesapla = ttk.Button(anaform,
                         text="Hesapla",command=hesapla)

                         
                         
                         
                        


"""lbl_tlmiktar.pack(expand=TRUE)
ent_miktar.pack(expand=TRUE)"""

lbl_tlmiktar.grid(row=0,column=0)
ent_miktar.grid(row=0,column=1)
lbl_kursec.grid(row=1,column=0)
cmb_kursec.grid(row=1,column=1)
lbl_sonuc.grid(row=2,column=0)
lbl_hesap_sonucu.grid(row=2,column=1)
btn_1.grid(row=3,column=0)
btn_hesapla.grid(row=3,column=1)


anaform.mainloop()