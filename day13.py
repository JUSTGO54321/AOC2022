import ast

def findRightOrder(left, right, depth):
    for count, i in enumerate(left):
        if count == len(right):
            return False

        print(f'{count = } {len(right) = }')
        print(f'left = {i}')
        print(f'right = {right[count]}')
        
        if type(i) == int and type(right[count]) == int:
            if i < right[count]:
                return True
            elif i > right[count]:
                return False
        elif type(i) == list and type(right[count]) == list:
            test = findRightOrder(i, right[count], depth + 1)
            if test == True:
                return True
            elif test == False:
                return False
        else:
            if type(i) == list and type(right[count]) == int:
                test = findRightOrder(i, list(map(int, str(right[count]))), depth + 1)
                if test == True:
                    return True
                elif test == False:
                    return False
            else:
                test = findRightOrder(list(map(int, str(i))), right[count], depth + 1)
                if test == True:
                    return True
                elif test == False:
                    return False
        if count + 1 == len(left) and len(left) < len(right):
                return True
    if len(left) == 0 and len(right) != 0:
        return True
    if depth == 1:
        if left == right:
            return False
        return True
with open('input.txt', 'r') as f:
    packet = [x.split('\n') for x in f.read().split('\n\n')]

packet_list = []
correct_packet = []
for index, i in enumerate(packet):
    left = ast.literal_eval(i[0])
    right = ast.literal_eval(i[1])
    print(f'{left = } \n{right = }')
    if findRightOrder(left, right, 1):
        correct_packet.append(index + 1)
    print(f'{correct_packet = }')
    
a, b = packet[149]
print(a)
print(b)
print(sum(correct_packet))

