from create_lab import result

answer = {}
right_way = []


def find_way(position, flag, answer):
    ways = []
    if position[1] - 1 >= 0 and result[position[0]][position[1] - 1] == ' ' and flag != 1:
        ways.append((position[0], position[1] - 1))
        find_way((position[0], position[1] - 1), 2, answer)

    if position[1] + 1 < len(result[position[0]]) and result[position[0]][position[1] + 1] == ' ' and flag != 2:
        ways.append((position[0], position[1] + 1))
        find_way((position[0], position[1] + 1), 1, answer)

    if position[0] + 1 < len(result) and result[position[0] + 1][position[1]] == ' ' and flag != 4:
        ways.append((position[0] + 1, position[1]))
        find_way((position[0] + 1, position[1]), 3, answer)

    if position[0] - 1 >= 0 and result[position[0] - 1][position[1]] == ' ' and flag != 3:
        ways.append((position[0] - 1, position[1]))
        find_way((position[0] - 1, position[1]), 4, answer)

    if ways != []:
        answer[tuple(position)] = ways


def right_way_func(exit, right_way):
    for key, value in answer.items():
        if exit in value:
            right_way.append(key)
            right_way_func(key, right_way)


find_way((0, 5), 3, answer)

for i in range(len(result[-1])):
    if result[-1][i] == ' ':
        exit = i

right_way.append(((len(result)) - 1, exit))
right_way_func(right_way[0], right_way)
