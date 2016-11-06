# listkeeper

A program to manage several lists.

## Requirements

* When the program is run, it lists all `.lst` files in the current directory
  * If there are no `.lst` files, prompt the user for a name and create a file
* Print out a list of all lists, such as:

```
1. list1.lst
2. list2.lst
```

* The user is prompted to enter the number of the file to load
* Load the contents of the list:

```
1. Milk
2. Eggs
3. Whiskey
```

* If the list is empty, prompt to Add or Quit
* If the list has at least one item, prompt to Add, Delete, or Quit
  * If adding, prompt the user for an item to add
    * When adding, re-sort the list
  * If deleting, prompt the user for a number to delete
  * If quitting, prompt to save unsaved changes
* Also prompt to Save if the list has changed
