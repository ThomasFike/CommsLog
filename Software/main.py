
from tinydb import TinyDB, Query
import time


class Contact:
    def __init__(self):
        self.time = 0
        self.transmiting = ""
        self.receiving = ""
        self.message = ""

    def log(self, db):
        db.insert({'time': self.time, 'Tx': self.transmiting,
                   'Rx': self.receiving, 'msg': self.message})

    def getContactInfo(self):
        self.transmiting = input("Station: ")
        self.time = time.time()
        self.message = input("Message: ")


db = TinyDB('./test.json')
db.purge()
contact = Contact()
User = Query()
contact.receiving = "NC"
while (input("Continue:").lower() == "y"):
    contact.getContactInfo()
    contact.log(db)

last = db.get(doc_id=len(db))
print("Last contact:")
print(
    f"Rx: {last['Rx']}\nTx: {last['Tx']}\nTime: {time.ctime(last['time'])}\nMessage: {last['msg']}")
