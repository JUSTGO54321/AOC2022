map = []
with open("input.txt") as f:
    for row, line in enumerate(f):
        map.append([])
        for col, char in enumerate(line.strip()):
            map[row].append(char)
            if char == "S":
                start = (row, col)
                map[start[0]][start[1]] = "a"
            elif char == "E":
                end = (row, col)
                map[end[0]][end[1]] = "z"

print(end)
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = set()
q = []
q.append(end)
v = [[0 for j in range(len(map[0]))] for i in range(len(map))]

while (len(q) > 0):
    print(f'{q = }')
    p = q[0]
    q.pop(0)

    # part 1
    # if p == start:
        # print(v[start[0]][start[1]])
        # break

    # part 2
    if map[p[0]][p[1]] == 'a':
        print(v[p[0]][p[1]])
        break

    for i in range(4):
        a = p[0] + directions[i][0]
        b = p[1] + directions[i][1]

        if a >= 0 and b >= 0 and a < len(map) and b < len(map[0]) and (a, b) not in visited and (map[a][b] >= map[p[0]][p[1]] or ord(map[a][b]) + 1 == ord(map[p[0]][p[1]])): 
            q.append((a, b))
            visited.add((a, b))
            v[a][b] = v[p[0]][p[1]] + 1