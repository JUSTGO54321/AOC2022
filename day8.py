import numpy as np

with open("input.txt", 'r') as f:
    row = [[int(y) for y in x] for x in f.read().split('\n')]
    row = np.array(row)


ans = 0
# part 1
# for counti, i in enumerate(row):
#     if counti == 0 or counti == len(row) - 1:
#         ans += len(i)
#     else:
#         for count, j in enumerate(i):
#             if count == 0 or count == len(i) - 1:
#                 ans += 1
#             elif j > max(i[count + 1:]) or j > max(i[0:count]) or j > max(row[:counti, count]) or j > max(row[counti + 1:, count]):
#                 ans += 1

# part 2

for counti, i in enumerate(row):
    if counti == 0 or counti == len(row) - 1:
        pass
    else:
        for count, j in enumerate(i):
            right = 0
            left = 0
            up = 0
            down = 0
            if count == 0 or count == len(i) - 1:
                pass
            else:
                for k in i[count + 1:]:
                    if k >= j:
                        right += 1
                        break
                    else:
                        right += 1
                for k in i[count - 1::-1]:
                    if k >= j:
                        left += 1
                        break
                    else:
                        left += 1
                for k in row[counti - 1::-1, count]:
                    if k >= j:
                        up += 1
                        break
                    else:
                        up += 1
                for k in row[counti + 1:, count]:
                    if k >= j:
                        down += 1
                        break
                    else:
                        down += 1
                if right * left * up * down > ans:
                    ans = right * left * up * down
print(ans)

