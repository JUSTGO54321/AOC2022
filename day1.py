import sys

with open(sys.argv[1], 'r') as f:
    elves = [x.split('\n') for x in f.read().split('\n\n')]

calories = sorted([sum([int(x) for x in y if x.isdigit()]) for y in elves])

print(max(calories))
print(sum(calories[-3:]))