#!/usr/local/bin/python3

import os
import sys

# class InvalidInputException(Exception): pass

def main():
    try:
        files = get_file_list()
        if len(files) == 0:
            print("No lists found!")
            add_file()
        else:
            show_lists(files)
    except (KeyboardInterrupt):
        quit()

def get_file_list():
    """
    Returns a list of ".lst" files in the current directory
    """
    all_files = os.listdir(".")
    list_files = list(filter(lambda x: ".lst" in x, all_files))
    return list_files

# def add_or_quit():
#     choice = "a"
#     while True:
#         try:
#             choice = str(input("[A]dd or [Q]uit [a]: ")).lower()
#             if choice not in {"a", "q"}:
#                 raise InvalidInputException("Invalid input {}".format(choice))
#             elif choice == "a":
#                 add_file()
#                 break
#             else:
#                 quit()
#         except InvalidInputException as iie:
#             print(iie)

def add_file():
    """
    Creates a new file, appending the ".lst" extension if necessary
    """
    ext = ".lst"
    while True:
        try:
            filename = str(input("New list name: "))
            if ext not in filename:
                filename += ext
            new_file = open(filename, "w", encoding="utf8")
            new_file.close()
            print("New list {} created!".format(filename))
            break;
        except ValueError:
            print("Invalid file name.")
        except OSError:
            print("Error writing file.")

def show_lists(files):
    """
    Print a list of ".lst" files
    """
    for i in range(len(files)):
        print("{}: {}".format(str(i + 1), files[i]))

def quit():
    """
    Exit the program
    """
    print("\nExiting...")
    sys.exit()

main()
