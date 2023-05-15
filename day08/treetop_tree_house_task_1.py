data = open('input.txt').read()
num_of_rows = data.count('\n') + 1
num_of_cols = data.find('\n')

data = data.replace('\n', '')
mapping = [[1 if rowIdx in [0, num_of_rows - 1] or colIdx in [0, num_of_cols - 1] else 0 for colIdx in range(0,num_of_cols)] for rowIdx in range(0,num_of_rows)]


def calculate_visible_trees(row, mapper, first_index):
    max = row[0]
    for idx, item in enumerate(row):
        if item > max:
            max = item
            mapper(mapping, first_index, idx)

    max = row[len(row)-1]
    for idx, item in reversed(list(enumerate(row))):
        if item > max:
            max = item
            mapper(mapping, first_index, idx)


def map_by_row(mapping, x, y):
    mapping[x][y] = 1


def map_by_column(mapping, x, y):
    mapping[y][x] = 1


for i in range(0,num_of_rows):
    row = data[i*num_of_cols:(i+1)*num_of_cols:1]
    calculate_visible_trees(row, map_by_row, i)

for i in range(0,num_of_cols):
    row = data[i::num_of_cols]
    calculate_visible_trees(row, map_by_column, i)

print(sum([j for sub in mapping for j in sub]))
# task1: 1835, example 21

