#!/usr/local/bin/python3

import sys

with open(sys.argv[1]) as input:
  program = input.read().replace('\n','').split(',')

# convert to int
program = [int(x) for x in program]

pos = 0

while(pos < len(program)):
  opcode = program[pos]
  if opcode == 99:
    break
  elif opcode == 1:
    program[program[pos + 3]] = program[program[pos + 1]] + program[program[pos + 2]]
  elif opcode == 2:
    program[program[pos + 3]] = program[program[pos + 1]] * program[program[pos + 2]]

  pos += 4

print(program)

