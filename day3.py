import sys

sum = 0
with open(sys.argv[1], 'r') as f:
    for count, x in enumerate(f.read().split('\n')):
        if count % 3 == 0:
            group1 = x
        elif count % 3 == 1:
            group2 = x
        else:
            group3 = x

            common = ''.join(set(group1).intersection(group2, group3))
            if ord(common) < 91:
                sum += ord(common) - 38
            else:
                sum += ord(common) - 96 
        
print(sum)