# generate_usernames

A script for creating unique usernames. From Chapter 3 of "Programming in Python 3 (Second Edition)."

Given an input file of many users, possibly with duplicated names:

`./random_data.py 100 200 > users.txt`

```
100:Kelly::Reynolds:Engineering
101:Kelly::Reynolds:Legal
102:Kelly:Reginald:Reynolds:Sales
103:Bill:Louis:Jones:Legal
104:Tom::Abdullah:Engineering
...
```

Create a list of usernames unique to each user:

`./generate_usernames.py users.txt [users2.txt [... usersN.txt]]`

```
Name                               ID   Username
-------------------------------- ------ ---------
Abdullah, Alex ................. (159) aabdulla
Abdullah, Alex ................. (277) aabdulla1
Abdullah, Alex L................ (287) alabdull
Abdullah, Alex P................ (129) apabdull
Abdullah, Alex P................ (178) apabdull1
...
```
