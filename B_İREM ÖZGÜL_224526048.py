from tkinter import *
from tkinter import ttk
anaform= Tk()
anaform.geometry("400x600")
lbl_tlmiktar= Label(
    anaform,
    text=("TL: "),
    font= " irregularis 14 bold italic")

if baz alınan kur == "euro":
    sonuc= tlmiktar/euro_kuru
elif baz alınan kur == "usd"
    sonuc= tlmiktar/usd_kuru
else 
    sonuc="SONUÇ BULUNAMADI"

lbl_hesap_sonucu.config(text= str(sonuc))
except ValueError:
    lbl_hesap_sonucu.config(text="HATALI GİRİŞ")


txt_tlmiktar= Entry()
lbl_kursec= Label(anaform,
                 text="Kur Seçiniz"
                 )
cmb_kursec=ttk.Combobox(anaform,
                        values=["USD","EURO"])
lbl_sonuc=Label(anaform,
                text= "Sonuc")

lbl_hesap_sonucu:(anaform,
                text= ".....")

btn_1=Button(anaform,text="BTN1")
btn_hesapla=ttk.Button(anaform,
                       text="SONUCU BUL")

"""lbl_tlmiktar.pack(expand=YES)
txt_tlmiktar.pack(expand=YES)"""

lbl_tlmiktar.grid(row=0, coolumn=0)
txt_tlmiktar.grid(row=0, coolumn=1)
cmb_kursec.grid(row=1, coolumn=1)
lbl_sonuc.grid(row=2, coolumn=0)
lbl_hesap_sonucu.grid(row=2, coolumn=1)
btn_1.grid(row=3, coolumn=0)
btn_hesapla.grid(row=3, coolumn=1)
btn_sil=Button(anaform,text="HEPSİNİ SİL")
btn_sil.grid(row=5, column=2)


anaform.mainloop()

