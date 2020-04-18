
class Contact:
    def __init__(self):
        self.time = 0
        self.transmiting = ""
        self.receiving = ""
        self.message = ""
    def log(self, db):
        db.insert({'time': self.time, 'Tx': self.transmiting, 'Rx': self.receiving, 'msg': self.message})

from tinydb import TinyDB, Query
import time
db = TinyDB('./test.json')
db.purge()
contact = Contact()
contact.time = time.time()
contact.receiving = "NC"
contact.transmiting = "Jackass Junction"
contact.message = "Hello"
contact.log(db)

User = Query()
print(db.all())

