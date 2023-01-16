import sys

with open(sys.argv[1], 'r') as f:
    hand = [x.split(" ") for x in f.read().split("\n")]

sum = 0
for x in hand:
    x[1] = int(x[1])
    x[0] = int(x[0])
    if x[1] == 2:
        sum += 3
    elif x[1] == 3:
        sum += 6
    
    if x[1] == 2:
        if x[0] == 1:
            sum += 1
        elif x[0] == 2:
            sum += 2
        else:
            sum += 3
    elif x[1] == 1:
        if x[0] == 1:
            sum += 3
        elif x[0] == 2:
            sum += 1
        else:
            sum += 2
    else:
        if x[0] == 1:
            sum += 2
        elif x[0] == 2:
            sum += 3
        else:
            sum += 1

print(sum)