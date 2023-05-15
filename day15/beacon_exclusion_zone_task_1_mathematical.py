import re
x = 0
y = 1
d = 2
data = [row for row in open('input.txt', 'r').read().split('\n')]
sb_locations = []
answer = set()


def distance(sb):
    sensor_xy = sb[0]
    beacon_xy = sb[1]
    return abs(sensor_xy[x] - beacon_xy[x]) + abs(sensor_xy[y] - beacon_xy[y])


for pair in data:
    x_s = re.findall(r'x=([\-]*\d+)', pair)
    y_s = re.findall(r'y=([\-]*\d+)', pair)
    # 0 - sensor, 1 - beacon
    sb = [[int(x_s[0]), int(y_s[0])], [int(x_s[1]), int(y_s[1])]]
    sb.append(distance(sb))
    sb_locations.append(sb)


def write_signal_area(xy, line_of_interest):
    if line_of_interest != xy[y]:
        return

    area = [xy[x], xy[y]]
    if area not in beacons and area not in sensors:
        answer.add((xy[x], xy[y]))


def draw_sensor_area(sb, line_of_interest):
    s_xy = sb[0]
    d = sb[2]

    """
    for i_y in range(0, d + 1):
        if s_xy[y] + i_y == line_of_interest or s_xy[y] - i_y == line_of_interest:
            for j_x in range(0, d + 1 - i_y):
                write_signal_area([s_xy[x] + j_x, s_xy[y] + i_y], line_of_interest)
                write_signal_area([s_xy[x] - j_x, s_xy[y] + i_y], line_of_interest)
                write_signal_area([s_xy[x] + j_x, s_xy[y] - i_y], line_of_interest)
                write_signal_area([s_xy[x] - j_x, s_xy[y] - i_y], line_of_interest)

    """
    i_y = s_xy[y] - line_of_interest
    if 0 <= i_y <= d:
        if s_xy[y] + i_y == line_of_interest or s_xy[y] - i_y == line_of_interest:
            for j_x in range(0, d + 1 - i_y):
                write_signal_area([s_xy[x] + j_x, s_xy[y] - i_y], line_of_interest)
                write_signal_area([s_xy[x] - j_x, s_xy[y] - i_y], line_of_interest)

    i_y = line_of_interest - s_xy[y]
    if 0 <= i_y <= d:
        if s_xy[y] + i_y == line_of_interest or s_xy[y] - i_y == line_of_interest:
            print(i_y)
            for j_x in range(0, d + 1 - i_y):
                write_signal_area([s_xy[x] + j_x, s_xy[y] + i_y], line_of_interest)
                write_signal_area([s_xy[x] - j_x, s_xy[y] + i_y], line_of_interest)


print(sb_locations)
line_of_interest = 2000000
beacons = [sb[1] for sb in sb_locations]
sensors = [sb[0] for sb in sb_locations]

for sb in sb_locations:
    draw_sensor_area(sb, line_of_interest)


print(len(answer))
