#!/usr/local/bin/python3

import sys

with open(sys.argv[1]) as input:
  program = input.read().replace('\n','').split(',')

# convert to int
program = [int(x) for x in program]

for noun in range(99):
  for verb in range(99):
    pos = 0
    pgm = program[:]
    # update pos 1 and 2 with noun and verb
    pgm[1] = noun
    pgm[2] = verb

    while(pos < len(pgm)):
      opcode = pgm[pos]
      a, b, c = pgm[pos+1 : pos+4]
      if opcode == 99:
        break
      elif opcode == 1:
        pgm[c] = pgm[a] + pgm[b]
      elif opcode == 2:
        pgm[c] = pgm[a] * pgm[b]
      pos += 4

    if pgm[0] == 19690720:
      print("noun: {}, verb: {}".format(noun, verb))
      print("Solution: {}".format(100 * noun + verb))

