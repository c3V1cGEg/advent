def find_possible_steps(current_yx):
    y = current_yx[0]
    x = current_yx[1]
    possibles = []
    all_coordinates = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]

    for coordinate in all_coordinates:
        if len(data[0]) > coordinate[1] >= 0 and len(data) > coordinate[0] >= 0:
            possibles.append([coordinate[0], coordinate[1]])

    return possibles


def find_path_part_1(start_yx, end_yx):
    visited = set()
    queue = [(start_yx, 0)]

    while len(queue):
        yx, dist = queue.pop(0)

        #print(dist)
        yx_tup = (yx[0], yx[1])

        if yx_tup not in visited:
            print('%s:%s:%s' % (yx[0], yx[1], data[yx[0]][yx[1]]))
            visited.add((yx[0], yx[1]))

            if yx == end_yx:
                return dist
            else:
                steps = find_possible_steps(yx)
                for next_yx in steps:
                    if chr(ord(data[yx[0]][yx[1]]) - 1) <= data[next_yx[0]][next_yx[1]] <= data[yx[0]][yx[1]]:
                        queue.append((next_yx, dist + 1))

    return -1


def find_start_end_coords():
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == 'S':
                start_yx = [y, x]

            if col == 'E':
                end_yx = [y, x]

    return start_yx, end_yx


data = [[cell for cell in row] for row in open('input.txt', 'r').read().split('\n')]
start_yx, end_yx = find_start_end_coords()
data[start_yx[0]][start_yx[1]] = 'a'
data[end_yx[0]][end_yx[1]] = 'z'
print('Yee: ', find_path_part_1(end_yx, start_yx))
