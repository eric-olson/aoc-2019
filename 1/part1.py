#!/usr/local/bin/python3

import sys

total = 0

with open(sys.argv[1]) as input:
  for line in input:
    total += (int(line) // 3) - 2

print(total)

