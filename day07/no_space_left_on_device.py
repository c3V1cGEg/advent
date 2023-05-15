fs_items = [line.split(' ') for line in open('input.txt', 'r').read().split('\n')]
current_path = []
path_sizes = {}

for fs_item in fs_items:
    if fs_item[0] == '$' and fs_item[1] == 'cd':
        current_path.pop() if fs_item[2] == '..' else current_path.append(fs_item[2])
    elif fs_item[0] == '$' and fs_item[1] == 'ls':
        path_sizes[''.join([path_item + '/' for path_item in current_path])] = 0
    elif fs_item[0] != 'dir':
        sum_path = ''
        for path_item in current_path:
            sum_path += path_item + '/'
            path_sizes[sum_path] += int(fs_item[0])

print(sum([item for item in path_sizes.values() if item < 100000]))
# task1: 1206825, example 95437

currently_free = 70000000 - path_sizes['//']
print(min([item for item in path_sizes.values() if currently_free + item > 30000000]))
# task2: 9608311, example 24933642