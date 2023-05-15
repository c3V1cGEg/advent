moves = [row.split(' ') for row in open('input.txt').read().split('\n')]


def move_item(direction, curr_xh, curr_yh):
    if direction == 'R':
        curr_xh += 1
    elif direction == 'L':
        curr_xh -= 1
    elif direction == 'U':
        curr_yh += 1
    elif direction == 'D':
        curr_yh -= 1
    return curr_xh, curr_yh


def find_to_add(prev_coord, coord):
    return 1 if prev_coord > coord else -1


def move_tail_item(x, y, prev_x, prev_y):
    if x == prev_x:
        y += find_to_add(prev_y, y)
    elif y == prev_y:
        x += find_to_add(prev_x, x)
    return x, y


def move_item_diagonally(x, y, prev_x, prev_y):
    x += find_to_add(prev_x, x)
    y += find_to_add(prev_y, y)
    return x, y


def calculate_positions(tail_size):
    tail_position = set()
    length_of_rope = 1 + tail_size # head + tail
    xyt = [[0, 0] for i in range(0, length_of_rope)]

    for move in moves:
        for i in range(1, int(move[1])+1):
            xyt[0][0], xyt[0][1] = move_item(move[0], xyt[0][0], xyt[0][1])
            for j in range(1, length_of_rope):
                distance_ht = ((xyt[j-1][0] - xyt[j][0]) ** 2 + (xyt[j-1][1] - xyt[j][1]) ** 2) ** 0.5

                if distance_ht == 2:
                    xyt[j][0], xyt[j][1] = move_tail_item(xyt[j][0], xyt[j][1], xyt[j-1][0], xyt[j-1][1])
                elif distance_ht > 2:
                    xyt[j][0], xyt[j][1] = move_item_diagonally(xyt[j][0], xyt[j][1], xyt[j-1][0], xyt[j-1][1])

            tail_position.add(str(xyt[length_of_rope-1][0]) + ':' + str(xyt[length_of_rope-1][1]))
    print(len(tail_position))


calculate_positions(1)
# task1: 6190, example: 13
calculate_positions(9)
# task2: 2516, example: 36

