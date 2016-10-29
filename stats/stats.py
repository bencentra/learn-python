#!/usr/local/bin/python3

import math

count = 0
total = 0
entries = []

def get_int():
    msg = "Enter an integer: "
    try:
        i = int(input(msg))
        return i
    except ValueError as err:
        return None

def calculate_mean():
    try:
        mean = total / count
        return mean
    except ZeroDivisionError as err:
        return 0

def calculate_median():
    try:
        sorted_entries = sorted(entries)
        length = len(sorted_entries)
        index = math.ceil(length/2)
        if (length % 2 == 1):
            return sorted_entries[length - index]
        else:
            return (sorted_entries[length - index] + sorted_entries[index - 1]) / 2
    except IndexError as err1:
        return 0
    except ZeroDivisionError as err2:
        return 0


def print_results():
    output = "Results: \n"
    output += "\tCount: {}\n".format(str(count))
    output += "\tTotal: {}\n".format(str(total))
    output += "\tMean: {}\n".format(str(calculate_mean()))
    output += "\tMedian: {}\n".format(str(calculate_median()))
    print(output)

while True:
    print("Do some math on some integers! Press ^D to end.")
    try:
        value = get_int()
        if (value is not None):
            count += 1
            total += value
            entries.append(value)
        else:
            break
    except EOFError:
        break

print_results()
