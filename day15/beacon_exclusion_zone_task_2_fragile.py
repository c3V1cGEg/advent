import re
from shapely import *

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


def get_polygon(sb):
    sb_x = sb[0][x]
    sb_y = sb[0][y]
    dist = sb[2]
    return Polygon([(sb_x, sb_y - dist), (sb_x + dist, sb_y), (sb_x, sb_y + dist), (sb_x - dist, sb_y)])


for pair in data:
    x_s = re.findall(r'x=([\-]*\d+)', pair)
    y_s = re.findall(r'y=([\-]*\d+)', pair)
    # 0 - sensor, 1 - beacon
    sb = [[int(x_s[0]), int(y_s[0])], [int(x_s[1]), int(y_s[1])]]
    sb.append(distance(sb))
    sb_locations.append(sb)

max_side = 4000000 # for example: 20
main_square = Polygon([(0, 0), (max_side, 0), (max_side, max_side), (0, max_side)])
p1 = get_polygon(sb_locations[0])

for i in range(1, len(sb_locations)):
    p_next = get_polygon(sb_locations[i])
    p1 = p1.union(p_next)

diff = main_square.difference(p1, grid_size=1) # fragile, different input needs different grid size, unclear
x = diff.centroid.x
y = diff.centroid.y

print((x * max_side) + y)
# task2: 13784551204480, example: 56000011





