import random

size = 0
while size < 10:
    try:
        size = int(input('Size(more then 10):'))
    except ValueError:
        print('Please enter a number more then 10 =)')
graf = {1: set()}


def find_way(h, w, ways):
    if len(ways) > 0:
        way = random.choice(ways)
        if way[0] == 'w':
            w += way[1] * 2
            if w < 0 or w >= len(field) or field[h][w] == ' ':
                w -= way[1] * 2
                ways.remove(way)
                way = find_way(h, w, ways)
            return way
        else:
            h += way[1] * 2
            if h < 0 or h >= len(field) or field[h][w] == ' ':
                h -= way[1] * 2
                ways.remove(way)
                way = find_way(h, w, ways)
            return way
    else:
        return None


def printer(g, h, w):
    for i in g:
        ways = [('w', -1), ('w', 1), ('h', -1), ('h', 1)]
        way = find_way(h, w, ways)
        if way == None:
            break

        if way[0] == 'w':
            for _ in range(2):
                w += way[1]
                field[h][w] = ' '
            if graf[i] != set():
                printer(graf[i], h, w)
            w -= way[1] * 2
        else:
            for _ in range(2):
                h += way[1]
                field[h][w] = ' '
            if graf[i] != set():
                printer(graf[i], h, w)
            h -= way[1] * 2


def create_layer():
    i = max(list(graf.keys()))
    for key, value in graf.items():
        if len(value) == 0:
            len_i = random.randint(1, 2)
            for _ in range(len_i):
                i += 1
                graf[key].add(i)

    for j in range(max(list(graf.keys())) + 1, i + 1):
        graf[j] = set()


for _ in range(int(size * 1.5)):
    create_layer()

field = []
for _ in range(size):
    field.append(['#'] * size)
h, w = 0, 4
field[h][w] = ' '

printer(graf[1], h, w)

while ' ' not in field[-1]:
    del field[-1]

exit = random.randint(1, size - 1)
while field[-1][exit] != ' ':
    exit = random.randint(1, size - 1)

result = []

result.append(list('#' * 5 + ' ' + '#' * (size - 4)))
for s in field:
    result.append(['#', *s, '#'])
result.append(list('#' * (exit + 1) + ' ' + '#' * (size - exit)))

for r in result:
    print(*r)
