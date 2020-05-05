from prettytable import PrettyTable
from tinydb import TinyDB, Query
from os import system, name
from main import Contact


def Last5Tx(db, User, TxSearch):
    Working = Contact()
    t = PrettyTable(['Rx', 'Tx', 'Time', 'Message'])
    contacts = db.search(User.Tx == TxSearch)
    if len(contacts) == 0:
        return
    elif len(contacts) < 5:
        for idoc_id in range(1, len(contacts) + 1):
            Working.load(contacts[idoc_id])
            t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    else:
        for idoc_id in range(len(contacts) - 4, len(contacts) + 1):
            Working.load(contacts[idoc_id])
            t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    print(t)


db = TinyDB('Database.json')
User = Query()
Last5Tx(db, User, 'ABC')
