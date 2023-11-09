import tkinter as tk
from tkinter import ttk

def calculate():
    selected_currency = cmb_kursec.get()
    amount = ent_miktar.get()

    try:
        amount = float(amount)
        if selected_currency == 'USD':
            result = amount / 28.48  
        elif selected_currency == 'EURO':
            result = amount / 30.45  
        elif selected_currency == 'ETH':
            result = amount / 2300  
        elif selected_currency == 'BTC':
            result = amount / 60000  
        lbl_hesap_sonuc.config(text=f"{result:.8f} {selected_currency}")
    except ValueError:
        lbl_hesap_sonuc.config(text="Lütfen sayı giriniz")

anaform = tk.Tk()
anaform.geometry("350x200")
anaform.title("Döviz ve Kripto Çevirici")

lbl_tlmiktar = tk.Label(
    anaform,
    text="Miktarı Giriniz ",
    font=("Helvetica 10 bold"),
)

ent_miktar = tk.Entry()

lbl_kursec = tk.Label(
    anaform,
    text="Döviz/Kripto Seçiniz",
    font=("Helvetica 10 bold"),
)
cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO", "ETH", "BTC"])

lbl_sonuc = tk.Label(anaform, text="Sonuç: ", font=("Helvetica 10 bold"))
lbl_hesap_sonuc = tk.Label(anaform, text="")

btn_hesapla = ttk.Button(anaform, text="Hesapla", command=calculate)

lbl_tlmiktar.grid(row=0, column=0, padx=5, pady=5)
ent_miktar.grid(row=0, column=1, padx=5, pady=5)
lbl_kursec.grid(row=1, column=0, padx=5, pady=5)
cmb_kursec.grid(row=1, column=1, padx=5, pady=5)
lbl_sonuc.grid(row=2, column=0, padx=5, pady=5)
lbl_hesap_sonuc.grid(row=2, column=1, padx=5, pady=5)
btn_hesapla.grid(row=3, column=1, padx=5, pady=5)

anaform.mainloop()
