from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *

def createTestTable():
    list = []

    list.append({"First Name":"Bruce", "Last Name":"Wayne"})
    list.append({"First Name":"Jack", "Last Name":"Nickolson"})
    list.append({"First Name":"Alex", "Last Name":"Turner"})
    list.append({"First Name":"Lewis", "Last Name":"Hamilton"})
    list.append({"First Name":"Jack", "Last Name":"Brabham"})
    list.append({"First Name":"Jean", "Last Name":"Alesi"})
    list.append({"First Name":"Jack", "Last Name":"Miller"})
    list.append({"First Name":"Johann", "Last Name":"Zarco"})
    list.append({"First Name":"Andrea", "Last Name":"Dovizioso"})
    list.append({"First Name":"Michelle", "Last Name":"Obama"})
    list.append({"First Name":"Danilo", "Last Name":"Petrucci"})
    list.append({"First Name":"Iker", "Last Name":"Lecuona"})
    list.append({"First Name":"Takaaki", "Last Name":"Nakagami"})
    list.append({"First Name":"Brad", "Last Name":"Binder"})
    list.append({"First Name":"Joan", "Last Name":"Mir"})
    list.append({"First Name":"Bradley", "Last Name":"Smith"})
    list.append({"First Name":"Valentino", "Last Name":"Rossi"})
    list.append({"First Name":"Tito", "Last Name":"Rabat"})
    list.append({"First Name":"Marc", "Last Name":"Marquez"})
    list.append({"First Name":"Miguel", "Last Name":"Oliveira"})


    return Table(list)
