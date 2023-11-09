from tkinter import *
from tkinter import ttk 

def hesapla():
    try:
        # Kullanıcının girdiği Tl miktarını ve seçtiği döviz kurunu al
        tlmiktar = float(txt_tlmiktar.get())
        secilen_kur = cmb_kursec.get()
        
        # Döviz kurlarını belirle (Gerçek değerler kullanılmalıdır)
        usd_kuru = 29
        euro_kuru = 30
        
        # Hesaplamayı gerçekleştir
        if secilen_kur == "USD":
            sonuc = tlmiktar / usd_kuru
        elif secilen_kur == "EURO":
            sonuc = tlmiktar / euro_kuru
        else:
            sonuc = "Geçersiz kur"
            
        # Sonucu etikete yazdır
        lbl_hesap_sonucu.config(text=str(sonuc))
    except ValueError:
        lbl_hesap_sonucu.config(text="Geçersiz giriş")

anaform = Tk()
anaform.geometry("400x600")

lbl_tlmiktar = Label(
    anaform,
    text="TL :",
    font="Helvetica 20 bold italic")

txt_tlmiktar = Entry()
lbl_kursec = Label(anaform, text="Kur Seçiniz" )
cmb_kursec = ttk.Combobox(anaform,
                          values=["USD","EURO"])

lbl_sonuc = Label(anaform,
                  text="Sonuç:")

lbl_hesap_sonucu = Label(anaform,
                         text="....")

btn_1 = Button(anaform, text="BTN1")
btn_hesapla = ttk.Button(anaform,
                         text="Hesapla",
                         command=hesapla)

lbl_tlmiktar.grid(row=0, column=0)
txt_tlmiktar.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonucu.grid(row=2, column=1)
btn_1.grid(row=3, column=0)
btn_hesapla.grid(row=3, column=1)

anaform.mainloop()
