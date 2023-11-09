from tkinter import *
from tkinter import ttk

def hesapla():
    try:
        tlmiktar = float(txt_tlmiktarı.get())
        secilen_kur = cmb_kursec.get()

        usd_kuru = 29
        euro_kuru = 30

        if secilen_kur == "USD":
            sonuc = tlmiktar / usd_kuru
        elif secilen_kur == "EURO":
            sonuc = tlmiktar / euro_kuru
 

        lbl_hesap_sonucu.config(text=str(sonuc))
    except ValueError:
        lbl_hesap_sonucu.config(text="Geçersiz giriş")


anaform = Tk()
anaform.geometry("400x300")


lbl_tlmiktar = Label(anaform, text="TL Miktarı:", font="helvetcica 20 italic")
txt_tlmiktarı = Entry()
lbl_kursec = Label(anaform, text="Kur Seçiniz")
cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO"])
lbl_sonuc = Label(anaform, text="Sonuç")
lbl_hesap_sonucu = Label(anaform, text="....")
btn_sil = Button(anaform, text="Temizle")
btn_hesapla = Button(anaform, text="Hesapla", command=hesapla)


lbl_tlmiktar.grid(row=0, column=0)
txt_tlmiktarı.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonucu.grid(row=2, column=1)
btn_hesapla.grid(row=3, column=1)
btn_sil.grid(row=3, column=2)


anaform.mainloop()