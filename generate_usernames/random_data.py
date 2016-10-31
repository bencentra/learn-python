#!/usr/local/bin/python3

#
# Create some random user data. Expect duplicates!
#

import sys
import random

first_names = ["Tom", "Bill", "Sarah", "Kelly", "Alex", "Chris"]
middle_names = ["", "", "", "Louis", "Reginald", "Picard"]
last_names = ["Smith", "Jones", "Abdullah", "Reynolds", "Jacobs", "Roberts"]
departments = ["Sales", "Legal", "HR", "Engineering"]

def main():
    count_firsts = len(first_names) - 1
    count_middles = len(middle_names) - 1
    count_lasts = len(last_names) - 1
    count_depts = len(departments) - 1
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        for i in range(start, end):
            random_first = first_names[random.randint(0, count_firsts)]
            random_middle = middle_names[random.randint(0, count_middles)]
            random_last = last_names[random.randint(0, count_lasts)]
            random_dept = departments[random.randint(0, count_depts)]
            print("{}:{}:{}:{}:{}".format(str(i), random_first, random_middle, random_last, random_dept))
    except IndexError as err1:
        print("IndexError: {}".format(err1))
        usage()
    except ValueError as err2:
        print("ValueError: {}".format(err2))
        usage()
    except:
        print("Uh-oh! Something else went wrong.")
        usage()

def usage():
    print("usage: random_data.py <start> <end>")

main()
