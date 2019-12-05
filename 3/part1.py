#!/usr/local/bin/python3

import sys

with open(sys.argv[1]) as input:
  lines = input.read().splitlines()

steps = [step.split(',') for step in lines]

all_points = []

for step in steps:
    # start at "central port" (0, 0)
    current_loc = (0, 0)
    step_points = []

    for point in step:
        # store each point we encounter as (x, y)
        direction = point[0]
        amount = int(point[1:])
        if direction == 'U':
            new_locs = [(current_loc[0], current_loc[1] + i) for i in range(1, amount + 1)]
            current_loc = (current_loc[0], current_loc[1] + amount)
        if direction == 'D':
            new_locs = [(current_loc[0], current_loc[1] - i) for i in range(1, amount + 1)]
            current_loc = (current_loc[0], current_loc[1] - amount)
        if direction == 'R':
            new_locs = [(current_loc[0] + i, current_loc[1]) for i in range(1, amount + 1)]
            current_loc = (current_loc[0] + amount, current_loc[1])
        if direction == 'L':
            new_locs = [(current_loc[0] - i, current_loc[1]) for i in range(1, amount + 1)]
            current_loc = (current_loc[0] - amount, current_loc[1])

        step_points.extend(new_locs)

    all_points.append(step_points)

# find intersecting points
common_points = set(all_points[0]).intersection(all_points[1])

# compute manhattan dist on all common points
common_points = [(abs(p[0]) + abs(p[1]), p[0], p[1]) for p in common_points]

print(sorted(common_points)[0])

