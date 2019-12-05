#!/usr/local/bin/python3

import sys

# get bounds in format '123456-234567'
bounds = [int(i) for i in sys.argv[1].split('-')]
print(bounds)

def valid(password):
    # take advantage of python string iterability
    password = str(password)
    # sorted == list implies increasing order, 2 in count implies one value present exactly 2x
    return sorted(password) == list(password) and 2 in [password.count(i) for i in password]

count = sum(valid(p) for p in range(*bounds))

print(count)

