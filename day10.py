import sys
import numpy as np

with open("input.txt", 'r') as f:
    cmd = [[y for y in x.split(' ')] for x in f.read().split('\n')]

def determineAns (count):
    if count == 20:
        return 20 * x
    elif count == 60:
        return 60 * x
    elif count == 100:
        return 100 * x
    elif count == 140:
        return 140 * x
    elif count == 180:
        return 180 * x
    elif count == 220:
        return 220 * x
    
x = 1
# part 1
# ans = 0
# count = 1
# for i in cmd:
#     if i[0] == 'noop':
#         count += 1
#         if (count - 20) % 40 == 0:
#             ans += determineAns(count)
#     if i[0] == 'addx':
#         for j in range(2):
#             if j == 1:
#                 x += int(i[1])
#             count += 1
#             if (count - 20) % 40 == 0:
#                 ans += determineAns(count)

# part 2
crt = np.empty([6, 40], dtype=str)

def drawImage(crtCol, crtRow):
    if crtCol == x - 1 or crtCol == x or crtCol == x + 1:
        crt[crtRow][crtCol] = '#'
    else:
        crt[crtRow][crtCol] = ' '

crtCol = 0
crtRow = 0
for i in cmd:
    
    if i[0] == 'noop':
        drawImage(crtCol, crtRow)
        crtCol += 1
    
    elif i[0] == 'addx':
        for j in range(2):
            drawImage(crtCol, crtRow)
            crtCol += 1
            if crtCol == 40: 
                crtRow += 1
                crtCol = 0
            if j == 1:
                x += int(i[1])
    
    if crtCol == 40: 
        crtRow += 1
        crtCol = 0
    if crtRow == 6:
        break

for i in crt:
    print(' '.join(i))