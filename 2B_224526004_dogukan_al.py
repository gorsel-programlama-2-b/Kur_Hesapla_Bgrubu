import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_monet_type():
    x = requests.get("https://www.forbes.com/advisor/money-transfer/currency-converter/try-usd/")
    soup = BeautifulSoup(x.text, 'html.parser')
    
    type_list = []
    
    for i in soup.find(id="to_currency").find_all("option"):
        type_list.append(i["value"])
    return type_list

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x400")
        self.columnconfigure((0,1,2,3),weight = 1, uniform = "x")
        self.rowconfigure((0,1,2,3), weight = 1, uniform = "x")
        self.title("app")
        self.value = tk.StringVar(value = "USD")
        self.type_list = get_monet_type()
        self.setup()
        self.mainloop()
        
    def setup(self):
        tk.Label(self,text= "TL Miktar").grid(row = 0, column = 1, sticky="nswe")
        tk.Label(self,text="Kur Seç").grid(row = 1, column = 1)
        
        self.price = tk.Entry(self)
        self.type = tk.OptionMenu(self,self.value,*self.type_list)
        
        self.price.grid(row = 0, column = 2)
        self.type.grid(row = 1, column = 2)
        
        self.result = tk.Label(self,text = "Sonuç : ")
        self.result.grid(row = 2, column = 1, columnspan=2, sticky="nswe")
        
        tk.Button(self,text = "Hesapla",command = self.hesapla).grid(row = 3, column = 1, columnspan = 2, sticky="we")
        
    def hesapla(self):
        link = f"https://valuta.exchange/try-to-{self.value.get()}?amount={self.price.get()}"
        y = requests.get(link)
        soup = BeautifulSoup(y.text, 'html.parser')
        i = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
        self.result.configure(text = "Sonuç : " + i["value"])
        
if __name__ == '__main__':
    app = App()
