from tkinter import * 
from tkinter import ttk

anaform = Tk()
anaform.geometry("300x400")
kur = {"USD":0.035,"EURO":0.033}
def hesapla():
    x = int(ent_miktar.get())*kur[cmb_kursec.get()]
    lbl_hesap_sonuc.configure(text="SONUÇ : "+str(x))
lbl_tlmiktar = Label(
    anaform,
    text="TL :",
    font="Helcetica 15 bold italic")

ent_miktar = Entry()

lbl_kursec = Label(anaform,
    text="Kur Seçiniz :",
    font="Helcetica 15 bold italic")
cmb_kursec = ttk.Combobox(anaform,
                          values=["USD","EURO"])

lbl_sonuc = Label(anaform,
                  text="SONUÇ: ")

lbl_hesap_sonuc = Label(anaform,
                        text="....")

btn_1 =Button(anaform,text="BTN1")
btn_hesapla = ttk.Button(anaform,
                         text="HESAPLA",command=hesapla)


"""lbl_tlmiktar.pack(expand=YES)
ent_miktar.pack(expand=YES)"""



lbl_tlmiktar.grid(row=0,column=0)
ent_miktar.grid(row=0,column=1)
lbl_kursec.grid(row=1,column=0)
cmb_kursec.grid(row=1,column=1)
lbl_sonuc.grid(row=2,column=0)
lbl_hesap_sonuc.grid(row=2,column=1)
btn_1.grid(row=3,column=0)
btn_hesapla.grid( row=3 , column=1)





anaform.mainloop()