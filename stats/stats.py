#!/usr/local/bin/python3

import math

def get_int():
    msg = "Enter an integer: "
    try:
        i = int(input(msg))
        return i
    except ValueError as err:
        return None

def calculate_sum(entries):
    sum = 0
    for i in entries:
        sum += i
    return sum;

def calculate_mean(total, count):
    try:
        mean = total / count
        return mean
    except ZeroDivisionError as err:
        return 0

def calculate_median(entries, count = None):
    try:
        sorted_entries = sorted(entries)
        count = count or len(entries)
        index = math.ceil(count/2)
        if (count % 2 == 1):
            return sorted_entries[count - index]
        else:
            return (sorted_entries[count - index] + sorted_entries[index - 1]) / 2
    except IndexError as err1:
        return "None"
    except ZeroDivisionError as err2:
        return "None"

def calculate_mode(entries):
    occurrences = {}
    for i in entries:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    mode = -1
    amount = 0
    for key, value in occurrences.items():
        if value > amount:
            mode = key
            amount = value
    if mode == -1:
        return "None"
    else:
        return mode

def print_results(entries):
    count = len(entries)
    sum = calculate_sum(entries)
    output = "Results: \n"
    output += "\tCount: {}\n".format(str(count))
    output += "\tSum: {}\n".format(str(sum))
    output += "\tMean: {}\n".format(str(calculate_mean(sum, count)))
    output += "\tMedian: {}\n".format(str(calculate_median(entries)))
    output += "\tMode: {}\n".format(str(calculate_mode(entries)))
    print(output)

values = []

print("Do some math on some integers! Use ^D empty entry to end input.")

while True:
    try:
        value = get_int()
        if (value is not None):
            values.append(value)
        else:
            break
    except EOFError:
        break

print_results(values)
