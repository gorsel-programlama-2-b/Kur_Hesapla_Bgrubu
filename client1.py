#Client
from socket import * 
from threading import *
from tkinter import *
from tkinter import filedialog


def onEnterPress(event):
    sendMessage()
    

client = socket(AF_INET, SOCK_STREAM)
#ip adresinizi bulmak için cmd komut istemcisine ipconfig yazınız
ip = '10.100.5.133'
port = 55555

client.connect((ip, port))

pencere = Tk()
pencere.title('Bağlandı :' + ip + ":" + str(port))

messages = Text(pencere, width=50)
messages.grid(row=0, column=0, padx=10, pady=10)

yourMessage = Entry(pencere, width=50)
yourMessage.insert(0, 'Isminiz')
yourMessage.grid(row=1, column=0, padx=10, pady=10)
yourMessage.focus()
yourMessage.selection_range(0, END)

def sendFile():
    file_path = filedialog.askopenfilename()
    messages.insert(END, '\n' + 'Dosya' + file_path)
    
gözat= Button(pencere, text = 'Gözat', width=20, command=sendFile)
gözat.grid(row=5, column=0, padx=10, pady=10)    


def sendMessage():
    clientMessage = yourMessage.get()
    messages.insert(END, '\n' + 'Sen: ' + clientMessage)
    client.send(clientMessage.encode('utf8'))
    yourMessage.delete(0, END)

bmessageGonder = Button(pencere, text='Gönder', width=20, command=sendMessage)
bmessageGonder.grid(row=2, column=0, padx=10, pady=10)

yourMessage.bind("<Return>", onEnterPress)


def recvMessage():
    while True:
        serverMessage = client.recv(1024).decode('utf8')
        messages.insert(END, '\n' + serverMessage)

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

pencere.mainloop()