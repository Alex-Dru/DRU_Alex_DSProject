from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *

class Node:
    def __init__(self, value, id, nextRight = None, nextLeft = None):
        self.value = value
        self.id = id
        self.nextLeft = nextLeft
        self.nextRight = nextRight
