#!/usr/local/bin/python3

import sys

def fuel_requirement(mass):
  fuel = (int(mass) // 3) - 2
  if (fuel <= 0):
    return 0
  return (fuel + fuel_requirement(fuel))

total = 0

with open(sys.argv[1]) as input:
  for line in input:
    total += fuel_requirement(line)

print(total)

