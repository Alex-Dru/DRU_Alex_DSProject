from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *
from test import *
import time

def demoPB():
    print("This is an example of a Phonebook:\n")
    a = Person("0612457845", "Alex", "Dru")
    b = Person("0614785478","Jack", "Nicolson")
    c = Person("0614782478","Michelle", "Obama")
    d = Person("0644785478","John", "Doe")
    e = Person("0614785458","John", "Lennon")
    dataPB = []
    myPB = PhoneBook(dataPB)
    myPB.addPerson(a)
    myPB.addPerson(b)
    myPB.addPerson(c)
    myPB.addPerson(d)
    myPB.addPerson(e)
    myPB.printPB()
    time.sleep(2)
    print("\nWe can add a new Person in the PhoneBook database, for example:\n")
    print("We are adding Gregor Jouet to the Phonebook\n")
    f = Person("4206942504","Gregor", "Jouet")
    myPB.addPerson(f)
    time.sleep(3)
    myPB.printPB()
    print()
    time.sleep(3)
    print("You can now try it yourself!")
    time.sleep(1)
    a = str(input("What is the desired First Name?"))
    b = str(input("What is the desired Last Name?"))
    c = str(input("What is the desired phone number?"))
    myPB.addPerson(Person(c,a,b))
    myPB.printPB()
    print("You are now in the PhoneBook!\n\n\n\n")
    print("Now, we will look up for a phone number in the database")
    d = input("What is the wanted phone number?")
    myPB.lookUpNumber(d)

def demoTable():
    tableTest = createTestTable()
    print("This is an example of a table with 2 attributes:\n")
    tableTest.printTable()
    print("\n\nWe are now going to create your own database!")
    list = []
    myTable = Table(list)
    i = int(input("How many entities will you need in your table?"))
    for n in range(1,i+1):
        print("Entity number " + str(n) + ":\n")
        myTable.addEntity()
        print()
    print("This is how your table currently looks like:")
    myTable.printTable()
    print("\n\nNow we are sorting your table in diffrent indexes\n\n")
    myTableTrees = myTable.buildAllBST()
    for arbre in myTableTrees:
        print(arbre.affInfixe())
    print("\n")
    print("Now we are going to use these indexes to look up for a value in your table")
    j = int(input("How many times will you want to try to find a value?"))
    for n in range (1 , j+1):
        k = input("Desired Value: \n")
        for arbre in myTableTrees:
            index = arbre.searchIndex(k)
            if index != -1:
                result = myTable.data[index]
                break
            else:
                result = "\nNothing was found for this value\n\n"
        print(result)
    print("\n\nWe are now going to rebuild an index in order to update it")
    print("Here are the indexes so far \n")
    for arbre in myTableTrees:
        print(arbre.affInfixe())
    print("Let's add a new entity in your Table")
    myTable.addEntity()
    print("\n\nNow let's see how the indexes look like ->\n\n")
    for arbre in myTableTrees:
        myTable.delBST(arbre)
    myTableTrees = myTable.buildAllBST()
    for arbre in myTableTrees:
        print(arbre.affInfixe())
    print("As a last test, we are going to rebuild a specific index")
    print("Let's add another entity")
    myTable.addEntity()
    print(myTable.rebuildBSTUser().affInfixe())
    print("\n\n\n\n\t\t\t\tThanks for playing!")

def demoMode():
    demoPB()
    demoTable()


demoMode()
