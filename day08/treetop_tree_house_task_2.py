data = [[int(item) for item in line]for line in open('input.txt').read().split('\n')]

print(data)
number_of_rows = len(data)
number_of_cols = len(data[0])
max_scenic_score = 0


def find_increasing_seq_count(items, current):
    if len(items) == 0:
        return 1

    max_val = -1
    count = 0
    for i in range(0,len(items)):
        count += 1
        if items[i] >= current:
            break

        if items[i] >= max_val:
            max_val = items[i]


    return count


def scenic_score_for_xy(row_idx, col_idx):
    row = data[row_idx]
    col = [data[i][col_idx] for i in range(0, number_of_rows)]
    x1 = find_increasing_seq_count(row[col_idx + 1:], data[row_idx][col_idx])
    left_side_row = row[:col_idx]
    left_side_row.reverse()
    x2 = find_increasing_seq_count(left_side_row, data[row_idx][col_idx])
    x3 = find_increasing_seq_count(col[row_idx + 1:], data[row_idx][col_idx])
    top_side_col = col[:row_idx]
    top_side_col.reverse()
    x4 = find_increasing_seq_count(top_side_col, data[row_idx][col_idx])
    return x1 * x2 * x3 * x4


for row_idx in range(0, number_of_rows):
    for col_idx in range(0, number_of_cols):
        if row_idx == 9 and col_idx == 9:
            print()


        scenic_score = scenic_score_for_xy(row_idx, col_idx)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
print(find_increasing_seq_count([3,3,3,5], 5))

# task2: 263670, example 8