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

def printListOfContacts(contacts):
    clear()
    Working = Contact()
    if len(contacts) == 0:
        print("No contacts in Query")
        return
    t = PrettyTable(['Rx', 'Tx', 'Time', 'Message'])
    for ithContact in contacts:
        Working.load(ithContact)
        t.add_row([Working.receiving, Working.transmitting,
                       time.ctime(Working.time), Working.message])
    print(t)

def messageContains(db, User, searchTerm):
    contacts = db.search(User.msg.search(searchTerm + '*', flags=re.IGNORECASE))
    printListOfContacts(contacts)
    input("Press enter to continue")

def between(val, Earliest, Latest):
    return Earliest <= val <= Latest


def betweenTimes(db, User, Latest, Earliest):
    #Converting Strings to seconds after epoch
    try:
        if Latest.lower() == 'now':
            Latest = time.time()
        else:
            Latest = time.mktime(time.strptime(Latest,'%Y-%m-%d %H:%M'))
    except:
        print("Latest Time was not valid")
        input("Press enter to continue")
        return
    try:
        Earliest = time.mktime(time.strptime(Earliest,"%Y-%m-%d %H:%M"))
    except:
        print("Earliest Time was not valid")
        input("Press enter to continue")
        return
    if (Latest <= Earliest):
        print("Latest is earlier then earliest")
        input("Press enter to continue")
        return
    #Find those between
    contacts = db.search(User.time.test(between, Earliest, Latest))
    #Print List
    printListOfContacts(contacts)
    input("Press enter to continue")

def lookupDialog(db, User):
    print("Welcome to lookup please select and option:")
    print("1. Last 5 Contacts by Tx Station")
    print("2. Message contains word")
    print("3. Between Times")    

    action = input("Option: ")
    if (action.lower() == "1"):
        TxSearch = input("Tx Station: ")
        Last5Tx(db, User, TxSearch)
    elif (action.lower() == '2'):
        searchTerm = input('Word: ')
        messageContains(db, User, searchTerm)
    elif (action.lower() == '3'):
        print('Enter times in the format: yyyy-mm-dd hh:mm')
        print('you can also enter "now" to use the current time')
        Earliest = input('Earliest time: ')
        Latest = input('Latest time: ')
        betweenTimes(db, User, Latest, Earliest)
    else:
        pass