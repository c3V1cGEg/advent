import re
x = 0
y = 1
d = 2


def distance(sb):
    sensor_xy = sb[0]
    beacon_xy = sb[1]
    return abs(sensor_xy[x] - beacon_xy[x]) + abs(sensor_xy[y] - beacon_xy[y])


def print_map():
    [print(row) for row in result]
    print('-' * 5 * len(result[0]))


data = [row for row in open('input.txt', 'r').read().split('\n')]
sb_locations = []

for pair in data:
    x_s = re.findall(r'x=([\-]*\d+)', pair)
    y_s = re.findall(r'y=([\-]*\d+)', pair)
    # 0 - sensor, 1 - beacon
    sb = [[int(x_s[0]), int(y_s[0])], [int(x_s[1]), int(y_s[1])]]
    sb.append(distance(sb))
    sb_locations.append(sb)

min_x = min(sb_locations, key=lambda sb: sb[0][x] - sb[2] if sb[0][x] - sb[2] < sb[1][x] else sb[1][x])
min_x = min_x[0][x] - min_x[d]
max_x = max(sb_locations, key=lambda sb: sb[0][x] + sb[2] if sb[0][x] + sb[2] > sb[1][x] else sb[1][x])
max_x = max_x[0][x] + max_x[d]
min_y = min(sb_locations, key=lambda sb: sb[0][y] - sb[2] if sb[0][y] - sb[2] < sb[1][y] else sb[1][y])
min_y = min_y[0][y] - min_y[d]
max_y = max(sb_locations, key=lambda sb: sb[0][y] + sb[2] if sb[0][y] + sb[2] > sb[1][y] else sb[1][y])
max_y = max_y[0][y] + max_y[d]
x_diff = 0 - min_x
y_diff = 0 - min_y
result = [['.' for x in range(0, max_x - min_x + 1)] for y in range(0, max_y - min_y + 1)]


def write_signal_area(xy):
    if result[xy[y]][xy[x]] != 'S' and result[xy[y]][xy[x]] != 'B':
        result[xy[y]][xy[x]] = '#'


def draw_sensor_area(sb):
    s_xy = sb[0]
    d = sb[2]

    for i_y in range(0, d + 1):
        for j_x in range(0, d + 1 - i_y):
            write_signal_area([s_xy[x] + j_x, s_xy[y] + i_y])
            write_signal_area([s_xy[x] - j_x, s_xy[y] + i_y])
            write_signal_area([s_xy[x] + j_x, s_xy[y] - i_y])
            write_signal_area([s_xy[x] - j_x, s_xy[y] - i_y])

print(sb_locations)
print("min_x: %s, max_x: %s, x_diff: %s, min_y: %s, max_y: %s, y_diff: %s" % (min_x, max_x, x_diff, min_y, max_y, y_diff))
# diff coordinates:
for sb in sb_locations:
    sb[0][x] = sb[0][x] + x_diff
    sb[0][y] = sb[0][y] + y_diff
    sb[1][x] = sb[1][x] + x_diff
    sb[1][y] = sb[1][y] + y_diff


for sb in sb_locations:
    sensor = sb[0]
    beacon = sb[1]
    distance = sb[2]

    result[sensor[y]][sensor[x]] = 'S'
    result[beacon[y]][beacon[x]] = 'B'
    draw_sensor_area(sb)

print_map()
print(sb_locations)
expected_y = 10
print(result[expected_y + y_diff])
print(len([x for x in result[expected_y + y_diff] if x == '#']))
