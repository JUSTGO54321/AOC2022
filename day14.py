import numpy as np

with open("input.txt", 'r') as f:
    rocks = [[[int(z) for z in y.split(',')] for y in x.split()] for x in f.read().split('\n')]

rock_row = set()
rock_col = set()
for i in rocks:
    for j in i:
        rock_row.add(j[1])
        rock_col.add(j[0])

num_rows = max(rock_row) - min(rock_row)
num_cols = max(rock_col) - min(rock_col)

array = np.zeros([int(num_rows), int(num_cols)], dtype = str)

#print(len(array))
#print(len(array[0]))
for i in rocks:
    for count, j in enumerate(i):
        #print(f'{row = } {min(rock_row) = }')
        row = j[1] - min(rock_row) - 1
        col = j[0] - min(rock_col) - 1

        if count + 1 == len(i):
            array[row, col] = '#'
            break
        else:
            next_row = i[count + 1][1] - min(rock_row) - 1
            next_col = i[count + 1][0] - min(rock_col) - 1
            #print(row, next_row, col, next_col)
            if row == next_row:
                for k in range(abs(col - next_col)):
                    array[row, min(col, next_col) + k] = '#'
            elif col == next_col:
                for k in range(abs(row - next_row)):
                    array[min(row, next_row) + k, col] = '#'
# for count, i in enumerate(array):
#     print('.'.join(i))

sand = 0
while True:
    rowlmao = 0
    collmao = 500 - min(rock_col) - 1
    while True:
        if array[rowlmao + 1, collmao] == '#' or array[rowlmao + 1, collmao] == 'o':
            if array[rowlmao + 1, collmao - 1] == '0':
                collmao -= 1
            elif array[rowlmao + 1, collmao + 1] == '0':
                collmao += 1
            else:
                array[rowlmao, collmao] = 'o'
                break
        rowlmao += 1
    sand += 1
    print(sand)
    if (rowlmao > len(array)):
        break
print(min(rock_row), max(rock_row), min(rock_col), max(rock_col))



