def move_crate_task1(crates_struct, how_many, from_col, to_col):
    for i in range(0, how_many):
        crates_struct[to_col].insert(0, crates_struct[from_col].pop(0))


def move_crate_task2(crates_struct, how_many, from_col, to_col):
    sub_stack = crates_struct[from_col][0:how_many]
    del crates_struct[from_col][0:how_many]
    crates_struct[to_col] = sub_stack + crates_struct[to_col]


data = open('input.txt', 'r').read().split('\n\n')
# option: beginner
#crates = [[crate_line[i:i+4] for i in range(0, len(crate_line), 4)] for crate_line in [line for line in data[0].split('\n')]]
#crates_struct = [[] for item in crates.pop()]
#[[crates_struct[index].append(crate) for index, crate in enumerate(crate_line) if len(crate.strip()) > 0] for crate_line in crates]

# num of columns: int((data[0].find('\n')+1)/4)
# num of rows: data[0].count('\n')+1
# option: unreal
crates_struct = [[crate for crate in [x for x in data[0].replace('\n', ' ')[1::4]][i::data[0].count('\n')+1] if len(crate.strip()) > 0] for i in range(0,int((data[0].find('\n')+1)/4))]

for row in [command.split(' ') for command in data[1].split('\n')]:
    move_crate_task2(crates_struct, int(row[1]), int(row[3])-1, int(row[5])-1)

print("".join([column[0][1:2] for column in crates_struct]))

# task1: CWMTGHBDW, example CMZ
# task2: SSCGWJCRB, example MCD