import sys

with open(sys.argv[1], 'r') as f:
    input = [x for x in f.read().split('\n\n')]

crates = [x.split(' ') for x in input[0].split('\n')]
moves = [x.split(' ') for x in input[1].split('\n')]

# part 1
# for i in moves:
#     for j in range(int(i[0])):
#         crates[int(i[2]) - 1].append(crates[int(i[1]) - 1].pop())

# part 2
for i in moves:
    for j in crates[int(i[1]) - 1][-int(i[0]):]:
        crates[int(i[2]) - 1].append(j)
    del crates[int(i[1]) - 1][-int(i[0]):]

ans = [i[-1] for i in crates]
ans = ''.join(ans)
print(ans)