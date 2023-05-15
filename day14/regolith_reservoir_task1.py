data = [[[int(coord) for coord in coords.split(',')] for coords in row.split(' -> ')] for row in open('input.txt', 'r').read().split('\n')]

x_all = [coords[0] for row in data for coords in row]
min_x, max_x = (min(x_all), max(x_all))
y_all = [coords[1] for row in data for coords in row]
min_y, max_y = (min(y_all), max(y_all))
min_x -= 1
max_x += 1
x_diff = max_x - min_x
result = [['.' for x in range(0, x_diff + 1)] for y in range(0, max_y + 1)]


def print_scan():
    [print(row) for row in result]
    print('-' * 5 * len(result[0]))


def fill_rock_path(start, end):
    if start[0] == end[0]:
        step = 1 if start[1] < end[1] else -1
        for y in range(start[1], end[1] + step, step):
            #print(start[0] - min_x, y)
            result[y][start[0] - min_x] = '#'

    else:
        step = 1 if start[0] < end[0] else -1
        for x in range(start[0], end[0] + step, step):
            #print(x - min_x, start[1])
            result[start[1]][x - min_x] = '#'


def initialize_rocks():
    for row in data:
        for j in range(1, len(row)):
            fill_rock_path(row[j-1], row[j])

    result[0][500 - min_x] = '+'


def is_abyss(y):
    return y > max_y


def can_move(xy):
    if is_abyss(xy[1] + 1):
        raise Exception("abyss")

    # in array [y-row][x-col]
    if result[xy[1] + 1][xy[0]] == '.':
        return True

    if result[xy[1] + 1][xy[0]] == '#':
        if xy[0] - 1 >= 0 and result[xy[1] + 1][xy[0] - 1] == '.':
            return True

        if xy[0] + 1 <= len(result[0]) - 1 and result[xy[1] + 1][xy[0] + 1] == '.':
            return True

        return False

    if result[xy[1] + 1][xy[0]] == 'o':
        if xy[0] - 1 >= 0 and result[xy[1] + 1][xy[0] - 1] == '.':
            return True

        if xy[0] + 1 <= len(result[0]) - 1 and result[xy[1] + 1][xy[0] + 1] == '.':
            return True

    return False


def move(xy):
    # in array [y-row][x-col]
    if result[xy[1] + 1][xy[0]] == '.':
        return [xy[0], xy[1] + 1]

    if result[xy[1] + 1][xy[0]] == '#':
        if xy[0] - 1 >= 0 and result[xy[1] + 1][xy[0] - 1] == '.':
            return [xy[0] - 1, xy[1] + 1]

        if xy[0] + 1 <= len(result[0]) - 1 and result[xy[1] + 1][xy[0] + 1] == '.':
            return [xy[0] + 1, xy[1] + 1]

        return xy

    if result[xy[1] + 1][xy[0]] == 'o':
        if xy[0] - 1 >= 0 and result[xy[1] + 1][xy[0] - 1] == '.':
            return [xy[0] - 1, xy[1] + 1]

        if xy[0] + 1 <= len(result[0]) - 1 and result[xy[1] + 1][xy[0] + 1] == '.':
            return [xy[0] + 1, xy[1] + 1]

    return xy


def drop_sand():
    start = [500 - min_x, 0]

    while can_move(start):
        start = move(start)
    else:
        result[start[1]][start[0]] = 'o'


initialize_rocks()
counter = 0

while True:
    try:
        drop_sand()
        counter += 1
    except Exception as e:
        if str(e) == 'abyss':
            print(counter)
            break

# task1: 618, example: 24