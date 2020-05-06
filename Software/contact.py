import time
from tinydb import TinyDB, Query

class Contact:
    def __init__(self):
        self.time = 0
        self.transmitting = ""
        self.receiving = ""
        self.message = ""

    def log(self, db):
        db.insert({'time': self.time, 'Tx': self.transmitting,
                   'Rx': self.receiving, 'msg': self.message})

    def getContactInfo(self):
        self.transmitting = input("Station: ")
        self.time = time.time()
        self.message = input("Message: ")

    def print(self):
        print(
            f"Rx: {self.receiving}  Tx: {self.transmitting} Time: {time.ctime(self.time)}   Message: {self.message}")

    def load(self, doc):
        self.time = doc['time']
        self.transmitting = doc['Tx']
        self.receiving = doc['Rx']
        self.message = doc['msg']