data = [[cell for cell in row] for row in open('input.txt', 'r').read().split('\n')]
max_x = len(data[0]) - 1
max_y = len(data) - 1
solution_steps_min = 0
by_letter_coords = {}
closest_next_height_distances = [[[] for cell in row] for row in data]
visited_paths = []

def coord(c):
    return c - 1 if c > 0 else 0


def distance_ab(point_a, point_b):
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) ** 0.5


def print_list_chars(coords):
    return ''.join([data[coord[1]][coord[0]] for coord in coords])
    #return ''.join([str(data[coord[1]][coord[0]]) + str(coord[0]) + ':' + str(coord[1]) for coord in coords])


def find_possible_steps(current_xy, prev_steps):
    x = current_xy[0]
    y = current_xy[1]
    result = []
    current_h = data[y][x]
    #possibles = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    possibles = []
    all_coordinates = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

    for coordinate in all_coordinates:
        if max_x >= coordinate[0] >= 0 and max_y >= coordinate[1] >= 0:
            possibles.append([coordinate[0], coordinate[1], data[coordinate[1]][coordinate[0]], closest_next_height_distances[coordinate[1]][coordinate[0]]])#find closest current_h + 1 distance

    possibles = sorted(possibles, key=lambda x: x[2], reverse=True)

    for possible in possibles:
        if (current_h >= data[possible[1]][possible[0]] >= chr(ord(current_h) - 1) and data[possible[1]][possible[0]] != 'S') or (current_h in ['b', 'a'] and data[possible[1]][possible[0]] == 'S'):
            #print('current: %s <= possible: %s' % (data[possible[1]][possible[0]], chr(ord(current_h)+1)))
            if [possible[0], possible[1]] not in prev_steps:
                result.append([possible[0], possible[1]])
                #print(possible)
    return result


def do_step(start_xy, prev_steps, level):
    global solution_steps_min
    if len(prev_steps) > solution_steps_min and solution_steps_min != 0:
        return
    prev_steps.append(start_xy)

    print(print_list_chars(prev_steps))


    next_steps = find_possible_steps(start_xy, prev_steps)

    for next_step in next_steps:
        #print('Steps: %s, next: %s' % (prev_steps, next_step))

        if data[next_step[1]][next_step[0]] == 'S':
            print('Steps: %s, next: %s, solution: %s' % (len(prev_steps), next_step, prev_steps))
            if solution_steps_min == 0 or len(prev_steps) < solution_steps_min:
                solution_steps_min = len(prev_steps)
        else:
            print(level, start_xy, data[start_xy[1]][start_xy[0]], next_step, data[next_step[1]][next_step[0]])
            do_step(next_step, prev_steps, level+1)
    prev_steps.pop()


def initialize_by_letter_coors():
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            cell = data[y][x]
            if cell not in by_letter_coords:
                by_letter_coords[cell] = [[x, y]]
            else:
                by_letter_coords[cell].append([x, y])


def find_start_end_coords():
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == 'S':
                start_xy = [x, y]

            if col == 'E':
                end_xy = [x, y]

    return start_xy, end_xy


def initialize_closest_distances():
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            cell = data[y][x]
            if cell == 'E' or cell == 'S' or cell == 'z':
                closest_next_height_distances[y][x] = 0
                continue

            next_level_coords = by_letter_coords[chr(ord(cell) + 1)]
            distances = []
            from_coord = [x, y]
            for to_coord in next_level_coords:
                if from_coord != to_coord:
                    distances.append(distance_ab(from_coord, to_coord))

            closest_next_height_distances[y][x] = min(distances)


initialize_by_letter_coors()
initialize_closest_distances()
start_xy, end_xy = find_start_end_coords()
data[end_xy[1]][end_xy[0]] = 'z'
do_step(end_xy, [], 0)
print(solution_steps_min)
