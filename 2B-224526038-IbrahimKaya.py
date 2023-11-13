from tkinter import *
from tkinter import ttk  

def hesapla():
    dolar = 0.035
    euro = 0.033

    if cmb_kursec.get() == "USD":
        cevrilmis_kur =  int(ent_miktar.get()) * dolar
        lbl_hesap_sonucu.configure(text=cevrilmis_kur)

    if cmb_kursec.get() == "EUR":
        cevrilmis_kur =  int(ent_miktar.get()) * euro
        lbl_hesap_sonucu.configure(text=cevrilmis_kur) 

pencere = Tk()
pencere.geometry("400x600")

lbl_tlmiktar = Label(
    pencere,
    text="TL :",
    font=("Helvectia 20 bold"))

ent_miktar = Entry(pencere)
lbl_kursec = Label(pencere, 
                   text="Kur Seçiniz :",
                   font=("Helvectia 20 bold"))
cmb_kursec = ttk.Combobox(pencere,
                          values=["USD","EUR"])
lbl_sonuc = Label(pencere,
                  text="Sonuç :",
                  font=("Helvectia 20 bold"))

lbl_hesap_sonucu = Label(pencere,
                         text="............")


btn_1 = Button(pencere,
               text="BTN1",
               font=("Helvectia 10 bold"))

btn_hesapla = ttk.Button(pencere,
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

pencere.mainloop()