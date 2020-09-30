from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *

class PersonException(Exception):
    pass

class Person:
    def __init__(self, num, firstName, lastName):
        self.num = num
        if len(firstName)<30:
            self.firstName = firstName.lower()
        else:
            raise PersonException("error: firstname is too long")
        if len(lastName)<30:
            self.lastName = lastName.upper()
        else:
            raise PersonException("error: lastname is too long")

    def printPerson(self):
        print(self.num + "  " + self.firstName + "  " + self.lastName)
