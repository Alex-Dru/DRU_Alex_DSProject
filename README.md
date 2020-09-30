# Dru Alex - Data Structure & Algorithms - Building a DataBase


### The PhoneBook


#### Class Person:


A Person is an entity with the following attributes: First & Last name, phone number.


The only method in this class is used to display a person's attributes.

```
def printPerson(self):
```

I made it so that the first name is in lower-case letters, the last name in capital letters and I handled these exceptions:

Phone numbers must be 10 digits long.

Names can't be longer than 30 characters.


#### Class PhoneBook:


A PhoneBook is only composed of a python list of entities from the Person class.


I implemented methods to add or delete a Person in a PhoneBook, as well as some methods to print a PhoneBook, look up for a phone number, a Last Name or a First Name in order to display all the Persons with the desired Number or Name.




### The Table



#### Class Table:


The Table Class is composed of a list of dictionaries. When adding an entity in this table, I make sure that the user can only enter the same attributes as the ones specified when the first entity was created. In the dictionaries, the keys are the attributes of an entity and the values are the corresponding value of the current entity. The Table being represented as a list, it can any number of rows.



#### Class Node:


The Node Class is used in the BST class. A Node is represented by its value, id and children (nextLeft & nextRight).



#### Class BST:


The BST Class is an ensemble of Nodes, sorted by their values when entered in the Tree. Searching in a BST uses a recursive function (searchIndex), as well as the printing method for Trees which is traversed in-order (parcours Infixe). My way of speeding up the search in the table is by using one BST per attribute in my table. An entity is found in the tree with its value, and the rest of its features are found in the Table using its .id, which is the index of its dictionary in the Table.
