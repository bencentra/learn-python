#!/usr/local/bin/python3

import os
import sys

def main():
    try:
        # Load all ".lst" files, or create one if none exist
        files = get_files()
        if len(files) == 0:
            print("No lists found!")
            create_list()
            files = get_files()
        print_list(files)
        # Select the file to load
        index = 0
        if (len(files) > 1):
            index = get_int("Load file number: ") - 1
        items = read_file(files[index])
        print_list(items)
        changed = False
        # Interact with the list
        while True:
            action = get_action(items, changed)
            if action == 'a':
                print('Add')
                changed = True
            elif action == 'd':
                print('Delete')
            elif action == 's':
                print('Save')
                changed = False
            elif action == 'q':
                print('Quit')
            else:
                print("Invalid action.")
    except ValueError as err:
        print(err)
    except KeyboardInterrupt:
        quit()

def get_files():
    """
    Returns a list of ".lst" files in the current directory
    """
    all_files = os.listdir(".")
    list_files = list(filter(lambda x: ".lst" in x, all_files))
    return list_files

def create_list():
    """
    Create a new list file, appending the ".lst" extension if needed
    """
    ext = ".lst"
    filename = get_string("New list name: ")
    if ext not in filename:
        filename += ext
    write_file(filename)

def print_list(my_list):
    """
    Print out a list data structure as an ordered list
    """
    try:
        for i in range(len(my_list)):
            print("{}. {}".format(str(i + 1), my_list[i]));
    except TypeError:
        print("That list is empty!")

def write_file(filename, content=""):
    """
    Write a file <filename> with the given <content>
    """
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write(content)
    except EnvironmentError as err:
        print("Error writing file:", err)
    else:
        print("Saved file")
    finally:
        if fh is not None:
            fh.close()

def read_file(filename):
    """
    Open a file and read the contents into a list
    """
    fh = None
    lines = []
    try:
        fh = open(filename, "r")
        for line in fh:
            lines.append(line.strip())
    except EnvironmentError as err:
        print("Error reading file:", err);
    finally:
        if fh is not None:
            fh.close()
    return sorted(lines)

def get_action(items=[], changed=False):
    """
    Get the next command from the user
    """
    msg = "[A]dd"
    if len(items) > 0:
        msg += ", [D]elete"
    if changed is not False:
        msg += ", [S]ave"
    msg += ", or [Q]uit: "
    action = get_string(msg)
    return action.lower()

def get_string(msg):
    """
    Get a string input from the user
    """
    while True:
        try:
            string = str(input(msg))
            return string
        except ValueError as err:
            print("Invalid input:", err)

def get_int(msg):
    """
    Get an integer input from the user
    """
    while True:
        try:
            integer = int(input(msg))
            return integer
        except ValueError as err:
            print("Invalid input:", err)

def quit():
    """
    Exit the program
    """
    print("\nQuitting...")
    sys.exit()

main()
