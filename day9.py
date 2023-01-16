import numpy as np

with open("input.txt", 'r') as f:
    moves = [[y for y in x.split(' ')] for x in f.read().split('\n')]

for x in moves:
    x[1] = int(x[1])

plane = np.array([[1]])
string = np.zeros((10, 2))

for i in moves:
    for j in range(i[1]):
        if i[0] == 'U':
            if 1 - string[0][0] > 0:
                plane = np.vstack([np.zeros((1, len(plane[0]))), plane])
                string[0][0] = 0
                for x in string[1:]:
                    x[0] += 1
            else:
                string[0][0]-= 1
        elif i[0] == 'D':
            if 1 + string[0][0] > len(plane[0:, 0]) - 1:
                plane = np.vstack([plane, np.zeros((1, len(plane[0])))])
            string[0][0] += 1
        elif i[0] == 'R':
            if 1 + string[0][1] > len(plane[0]) - 1:
                plane = np.hstack([plane, np.zeros((len(plane[0:, 0]), 1))])
            string[0][1] += 1
        else:
            if 1 - string[0][1] > 0:
                plane = np.hstack([np.zeros((len(plane[0:, 0]), 1)), plane])
                string[0][1] = 0
                for x in string[1:]:
                    x[1] += 1
            else:
                string[0][1] -= 1
        
        for count, x in enumerate(string[1:]):
            rowDif = string[count][0] - x[0]
            colDif = string[count][1] - x[1]

            if abs(rowDif) > 1 or abs(colDif) > 1: #head not directly adjacent to tail
                if string[count][0] == x[0]: #left or right
                    if colDif == 2:
                        x[1] += 1
                    else:
                        x[1] -= 1
                elif string[count][1] == x[1]: #up or down
                    if rowDif == 2:
                        x[0] += 1
                    else:
                        x[0] -= 1
                else:
                    if rowDif == 1 and colDif == 2 or rowDif == 2 and colDif == 1 or rowDif == 2 and colDif == 2: #down 1 right 2 / down 2 right 1 / down 2 right 2
                        x[0] += 1
                        x[1] += 1
                    elif rowDif == 1 and colDif == -2 or rowDif == 2 and colDif == -1 or rowDif == 2 and colDif == -2: #down 1 left 2 / down 2 left 1 / down 2 left 2
                        x[0] += 1
                        x[1] -= 1
                    elif rowDif == -1 and colDif == 2 or rowDif == -2 and colDif == 1 or rowDif == -2 and colDif == 2: #up 1 right 2 / up 2 right 1 / up 2 right 2
                        x[0] -= 1
                        x[1] += 1
                    elif rowDif == -1 and colDif == -2 or rowDif == -2 and colDif == -1 or rowDif == -2 and colDif == -2: #up 1 left 2 / up 2 left 1 / up 2 left 2
                        x[0] -= 1
                        x[1] -= 1
        plane[int(string[9][0])][int(string[9][1])] = 1

print(plane)
print(f'{int(np.sum(plane)) = }')