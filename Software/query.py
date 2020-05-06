from prettytable import PrettyTable
from tinydb import TinyDB, Query
from os import system, name
from contact import *
from functions import clear
import re


def Last5Tx(db, User, TxSearch):
    clear()
    Working = Contact()
    t = PrettyTable(['Rx', 'Tx', 'Time', 'Message'])
    contacts = db.search(User.Tx.matches(TxSearch, flags=re.IGNORECASE))
    if len(contacts) == 0:
        return
    elif len(contacts) < 5:
        for idoc_id in range(0, len(contacts)):
            Working.load(contacts[idoc_id])
            t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    else:
        for idoc_id in range(len(contacts) - 5, len(contacts)):
            Working.load(contacts[idoc_id])
            t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    print(t)
    input("Press enter to continue")

def messageContains(db, User, searchTerm):
    clear()
    Working = Contact()
    contacts = db.search(User.msg.search(searchTerm + '*', flags=re.IGNORECASE))
    if len(contacts) == 0:
        return
    t = PrettyTable(['Rx', 'Tx', 'Time', 'Message'])
    for ithContact in contacts:
        Working.load(ithContact)
        t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    print(t)
    input("Press enter to continue")


def lookupDialog(db, User):
    print("Welcome to lookup please select and option:")
    print("1. Last 5 Contacts by Tx Station")
    print("2. Message contains word")

    action = input("Option: ")
    if (action.lower() == "1"):
        TxSearch = input("Tx Station: ")
        Last5Tx(db, User, TxSearch)
    elif (action.lower() == '2'):
        searchTerm = input('Word: ')
        messageContains(db, User, searchTerm)
    else:
        pass