import sys

with open(sys.argv[1], 'r') as f:
    input = f.read()

sum = 0
for i in range(len(input) - 14):
    test = input[i:i + 14]
    if len(set(test)) == len(test):
        sum = i + 14
        break

print(sum)