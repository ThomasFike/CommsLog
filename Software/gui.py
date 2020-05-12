import tkinter as tk

def helloCallBack():
   print(self.text)

class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)
        self.text = ''
        self.Tx = tk.Entry(self, command=helloCallBack, textvariable=self.text)
        self.Tx.pack(padx=20, pady=20)
        
        
        
if __name__ == "__main__":
    root = tk.Tk()

    main = HelloWorld(root)
    main.pack(fill="both", expand=True)

    root.mainloop()