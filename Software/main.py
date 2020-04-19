
from tinydb import TinyDB, Query
from os import system, name
from prettytable import PrettyTable
import time


def clear():
    if (name == 'nt'):
        system('cls')
    # for mac and linux
    else:
        system('clear')


def printLast5():
    Working = Contact()
    t = PrettyTable(['Rx', 'Tx', 'Time', 'Message'])
    if len(db) == 0:
        return
    elif len(db) < 5:
        for idoc_id in range(1, len(db) + 1):
            Working.load(db.get(doc_id=idoc_id))
            t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    else:
        for idoc_id in range(len(db) - 4, len(db) + 1):
            Working.load(db.get(doc_id=idoc_id))
            t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    print(t)


def newContact(contact, db):
    contact.getContactInfo()
    contact.log(db)


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


# Init
db = TinyDB('./test.json')
User = Query()
WorkingContact = Contact()
clear()

# Initial Config
print("Welcome to Comms Log by Thomas Fike KG7FXT")
if (input("Do you want to start a new document? [Y/n]: ").lower() == "y"):
    db.purge()
Rx = input("What would you like to call your Receiving Station: ")
WorkingContact.receiving = Rx

while True:
    clear()
    printLast5()
    print("\nWhat action would you like to do?\nAdd (N)ew Contact, (Q)uit")
    action = input("Action: ").lower()
    if action == "n":
        print("")
        newContact(WorkingContact, db)
    elif action == "q":
        break

print("Thanks for using")
