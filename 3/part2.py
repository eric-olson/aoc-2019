#!/usr/local/bin/python3

import sys

with open(sys.argv[1]) as input:
  lines = input.read().splitlines()

steps = [step.split(',') for step in lines]

all_points = []

for step in steps:
    # start at "central port" (0, 0)
    current_loc = (0, 0)
    distance = 0
    step_points = {}

    for point in step:
        # store each point we encounter as (x, y, distance)
        direction = point[0]
        assert direction in 'UDRL'
        amount = int(point[1:])
        if direction == 'U':
            new_locs = {(current_loc[0], current_loc[1] + i): distance + i for i in range(1, amount + 1)}
            current_loc = (current_loc[0], current_loc[1] + amount)
        if direction == 'D':
            new_locs = {(current_loc[0], current_loc[1] - i): distance + i for i in range(1, amount + 1)}
            current_loc = (current_loc[0], current_loc[1] - amount)
        if direction == 'R':
            new_locs = {(current_loc[0] + i, current_loc[1]): distance + i for i in range(1, amount + 1)}
            current_loc = (current_loc[0] + amount, current_loc[1])
        if direction == 'L':
            new_locs = {(current_loc[0] - i, current_loc[1]): distance + i for i in range(1, amount + 1)}
            current_loc = (current_loc[0] - amount, current_loc[1])

        step_points.update(new_locs)
        distance += amount

    all_points.append(step_points)

# find intersecting points
common_points = set(all_points[0].keys()).intersection(all_points[1].keys())

# compute manhattan dist on all common points
manhattan = [(abs(p[0]) + abs(p[1]), p[0], p[1]) for p in common_points]
print("Manhattan (m, x, y): {}".format(sorted(manhattan)[0]))

steps = [(all_points[0][p] + all_points[1][p], p[0], p[1]) for p in common_points]
print("Step (n, x, y): {}".format(sorted(steps)[0]))

