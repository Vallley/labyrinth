from create_lab import result

answer = {}
right_way = []

def find_way(position, flag):
    ways = []
    if position[1]-1>=0 and result[position[0]][position[1]-1]==' ' and flag!=1:
        ways.append((position[0], position[1]-1))
        find_way((position[0],position[1]-1), 2)

    if position[1]+1<len(result[position[0]]) and result[position[0]][position[1]+1]==' ' and flag!=2:
        ways.append((position[0], position[1]+1))
        find_way((position[0],position[1]+1), 1)

    if position[0]+1<len(result) and result[position[0]+1][position[1]]==' ' and flag!=4:
        ways.append((position[0]+1, position[1]))
        find_way((position[0]+1,position[1]), 3)

    if position[0]-1>=0 and result[position[0]-1][position[1]]==' ' and flag!=3:
        ways.append((position[0]-1, position[1]))
        find_way((position[0]-1,position[1]), 4)

    if ways != []:
        answer[tuple(position)] = ways
    else:
        return None

def right_way_func(num):
    for key, value in answer.items():
        if num in value:
            right_way.append(key)
            right_way_func(key)  

find_way((0, 5), 3)

for i in range(len(result[-1])):
    if result[-1][i] == ' ':
        num = i
right_way.append(((len(result))-1, num))
right_way_func(right_way[0])
