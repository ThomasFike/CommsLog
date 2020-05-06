from os import system, name

def clear():
    if (name == 'nt'):
        system('cls')
    # for mac and linux
    else:
        system('clear')