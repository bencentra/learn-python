#!/usr/local/bin/python3

#
# Create unique usernames from a list of uses (that may contain duplicate names)
#

import sys
import collections

# Constants for field names
ID, FIRST, MIDDLE, LAST, DEPT = range(5)

# User type
User = collections.namedtuple("User", "username first middle last id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        usage()
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.last.lower(), user.first.lower(), user.middle.lower(), user.id)] = user

    print_users(users)

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FIRST], fields[MIDDLE], fields[LAST], fields[ID])
    return user

def generate_username(fields, usernames):
    username = (fields[FIRST][0] + fields[MIDDLE][:1] + fields[LAST]).replace("-", "").replace("'", "")
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{}{}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

def print_users(users):
    namewidth = 32
    usernamewidth = 9
    print("{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth))
    for key in sorted(users):
        user = users[key]
        initial = " "
        if user.middle:
            initial += user.middle[0]
        name = "{0.last}, {0.first}{1}".format(user, initial)
        print("{0:.<{nw}} ({1.id}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))

def usage():
    print("usage: {} file1 [file2 [... fileN]]".format(sys.argv[0]))

main()
