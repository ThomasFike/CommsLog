import tkinter as tk
import time
from contact import Contact
from tinydb import TinyDB, Query
from main import printLast5


class HelloWorld(tk.Frame):
    def getData(self, event):
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
        table.listLast5()
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


class Table(tk.Frame):
    def listLast5(self):
        Working = Contact()
        row = 0
        if len(db) == 0:
            pass
        elif len(db) < 5:
            for idoc_id in range(1, len(db) + 1):
                Working.load(db.get(doc_id=idoc_id))
                # RX
                tk.Label(self, text=Working.receiving,
                         background='white').grid(row=row, column=0)
                # TX
                tk.Label(self, text=Working.transmitting,
                         background='white').grid(row=row, column=1)
                # Time
                tk.Label(self, text=time.ctime(Working.time),
                         background='white').grid(row=row, column=2)
                # Message
                tk.Label(self, text=Working.message,
                         background='white').grid(row=row, column=3)
                row += 1
        else:
            for idoc_id in range(len(db) - 4, len(db) + 1):
                Working.load(db.get(doc_id=idoc_id))
                # RX
                tk.Label(self, text=Working.receiving, width=15, justify=tk.LEFT,
                         background='white').grid(row=row, column=0)
                # TX
                tk.Label(self, text=Working.transmitting, width=15, justify=tk.LEFT,
                         background='white').grid(row=row, column=1)
                # Time
                tk.Label(self, text=time.ctime(Working.time), width=20, justify=tk.LEFT,
                         background='white').grid(row=row, column=2)
                # Message
                tk.Label(self, text=Working.message, width=40, justify=tk.LEFT,
                         background='white').grid(row=row, column=3)
                row += 1

    def __init__(self, parent):
        super(Table, self).__init__(parent)
        self.header = tk.Label(self, text="Testing")
        self.listLast5()


if __name__ == "__main__":
    root = tk.Tk()
    root.title = 'Comms Log'
    db = TinyDB('./Database.json')
    main = HelloWorld(root)
    main.pack(fill="both", expand=True)
    table = Table(root)
    table.pack(fill="both", expand=True)

    root.mainloop()
