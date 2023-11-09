import tkinter as tk
from tkinter import ttk

def calculate():
    selected_currency = cmb_kurtikla.get()
    amount = ent_miktar.get()

    try:
        amount = float(amount)
        conversion_rates = {
            'USD': 28.48,
            'EURO': 30.45,
            'GBP': 38.20,
            'ETH': 2300,
            'BTC': 60000,
            'DOGE': 0.3
        }
        result = amount / conversion_rates[selected_currency]
        lbl_hesap_cikti.config(text=f"{result:.2f} {selected_currency}")
    except ValueError:
        lbl_hesap_cikti.config(text="Lütfen sayı giriniz...")

anaform = tk.Tk()
anaform.geometry("400x200")
anaform.title("Döviz Çevirici")
anaform.configure(bg='#FF69B4')  

lbl_tlmiktar = tk.Label(
    anaform,
    text="TL Miktarı ",
    font=("Helvetica", 12, "bold italic"),
    bg='#FF69B4'  
)
ent_miktar = tk.Entry()

lbl_kurtikla = tk.Label(
    anaform,
    text="Döviz veya Kripto Seçiniz",
    font=("Helvetica", 12, "bold italic"),
    bg='#FF69B4'  
)
cmb_kurtikla = ttk.Combobox(anaform, values=["USD", "EURO", "GBP", "ETH", "BTC", "DOGE"], background='#FF69B4')  

lbl_sonuc = tk.Label(anaform, text="Sonuç: ", font=("Helvetica", 12, "bold italic"), bg='#FF69B4')
lbl_hesap_cikti = tk.Label(anaform, text="...", bg='#FF69B4')

btn_hesapla = ttk.Button(anaform, text="Hesapla", command=calculate)

lbl_tlmiktar.grid(row=0, column=0)
ent_miktar.grid(row=0, column=1)
lbl_kurtikla.grid(row=1, column=0,padx=5, pady=5)
cmb_kurtikla.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0, )
lbl_hesap_cikti.grid(row=2, column=1)
btn_hesapla.grid(row=3, column=1)

anaform.mainloop()
