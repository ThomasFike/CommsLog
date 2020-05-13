import tkinter as tk
import time
from contact import Contact
from tinydb import TinyDB, Query
from main import printLast5

class HelloWorld(tk.Frame):
    def getData(self,event):
        contact = Contact()
        contact.receiving = 'Test'
        contact.transmitting = self.Tx.get()
        contact.message = self.Msg.get()
        contact.time = time.time()
        contact.log(db)
        contact.print()
        self.Tx.delete(0, tk.END)
        self.Msg.delete(0, tk.END)
        self.Tx.focus_set()
        printLast5(db)

    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)
        self.L1 = tk.Label(self, text="Tx Station")
        self.L2 = tk.Label(self, text="Message")
        self.Tx = tk.Entry(self)
        self.Msg = tk.Entry(self, width=45)
        self.L1.grid(row=0, column=0, padx=5, pady=5)
        self.Tx.grid(row=0, column=1, padx=20, pady=5, sticky=tk.W)
        self.L2.grid(row=1, column=0, padx=5, pady=5)
        self.Msg.grid(row=1, column=1, padx=20, pady=5)
        self.Msg.bind('<Return>', self.getData)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title = 'Comms Log'
    db = TinyDB('./Database.json')
    main = HelloWorld(root)
    main.pack(fill="both", expand=True)

    root.mainloop()