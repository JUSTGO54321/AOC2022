import sys
from collections import defaultdict

cmd = []
with open(sys.argv[1], 'r') as f:
    cmd = [tuple(x.split()) for x in f] 

dir_dict = defaultdict()
dir_set = set()
dir_stack = []
current_dir_list = []
listmode = False

for i in cmd:
    if i[1] == "cd":
        if listmode:
            dir_dict[current_dir] = tuple(current_dir_list)
            current_dir_list.clear()
            listmode = False
        if i[2] == '..':
            dir_stack.pop()
            current_dir = tuple(dir_stack)
        else:
            dir_stack.append(i[2])
            current_dir = tuple(dir_stack)
            dir_set.add(current_dir)
    elif i[1] == 'ls':
        listmode = True
    elif i[0] == 'dir':
        dir_stack.append(i[1])
        current_dir_list.append(tuple(dir_stack))
        dir_stack.pop()
    else:
        current_dir_list.append(tuple((int(i[0]), "File", i[1])))

if listmode:
    dir_dict[current_dir] = tuple(current_dir_list)
    current_dir_list.clear()
    listmode = False

def CalculateDirSize(dir):
    dir_size = 0
    for j in dir_dict[dir]:
        if j[1] == "File":
            dir_size += j[0]
        else:
            dir_size += CalculateDirSize(j)
    return dir_size

ans = 0
for i in dir_set:
    dir_size = CalculateDirSize(i)
    if len(i) == 1:
        OuterShell = dir_size
    if dir_size <= 100000:
        ans += dir_size

needed_space = 30000000 - (70000000 - OuterShell) 
delete_space = 1000000000000

for i in dir_set:
    dir_size = CalculateDirSize(i)
    if dir_size - needed_space >= 0 and dir_size < delete_space:
        delete_space = dir_size
print(ans)
print(delete_space)
        