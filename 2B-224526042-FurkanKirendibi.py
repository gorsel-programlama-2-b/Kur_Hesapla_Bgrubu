from tkinter import * 
from tkinter import ttk

anaform = Tk()
anaform.geometry("350x450")
kur = {"USD":0.037,"EURO":0.032}

def hesapla():
    x = int(ent_miktar.get())*kur[cmb_kursec.get()]
    lbl_hesap_sonuc.configure(text="SONUÇ : "+str(x))

lbl_tlmiktar = Label(
    anaform,
    text="TL :",
    font="Arial 20 bold italic",
    fg="red",bg="white")
    
ent_miktar = Entry()

lbl_kursec = Label(anaform,
    text="Kur Seçiniz :",
    font="Arial 20 bold",
    fg="red",bg="white")


cmb_kursec = ttk.Combobox(anaform,
                          values=["USD","EURO"])

lbl_sonuc = Label(anaform,
                  text="SONUÇ: ",font="Arial 15 bold",bg="white")

lbl_hesap_sonuc = Label(anaform,
                        text="....")


btn_hesapla = ttk.Button(anaform,
                         text="HESAPLA",command=hesapla)

lbl_tlmiktar.grid(row=0,column=0)
ent_miktar.grid(row=0,column=1)
lbl_kursec.grid(row=1,column=0)
cmb_kursec.grid(row=1,column=1)
lbl_sonuc.grid(row=2,column=0)
lbl_hesap_sonuc.grid(row=2,column=1)
btn_hesapla.grid( row=3 , column=1)

anaform.mainloop()