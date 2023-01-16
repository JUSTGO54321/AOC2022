import sys

with open(sys.argv[1], 'r') as f:
    overlap = [[y.split('-') for y in x.split(',')] for x in f.read().split('\n')]

sum = 0
for x in overlap:
    x = [[int(j) for j in i] for i in x]
    # part 1
    # if x[0][0] <= x[1][0] and x[0][1] >= x[1][1] or x[1][0] <= x[0][0] and x[1][1] >= x[0][1]: 
    #     sum += 1

    # part 2
    if min(x[1][1], x[0][1]) - max(x[0][0], x[1][0]) >= 0:
        sum += 1
    
print(sum)