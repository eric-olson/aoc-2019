#!/usr/local/bin/python3

import sys

# get bounds in format '123456-234567'
bounds = [int(i) for i in sys.argv[1].split('-')]
print(bounds)

def valid(password):
    # take advantage of python string iterability
    password = str(password)
    # sorted == list implies increasing order, len > len(set) implies at least one duplicate
    return sorted(password) == list(password) and len(password) > len(set(password))

count = sum(valid(p) for p in range(*bounds))

print(count)

