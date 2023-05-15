def create_range(pos):
    return set([i for i in range(pos[0], pos[1] + 1)])


section_pairs = [[create_range([int(pos) for pos in elf.split('-')]) for elf in pair.split(',')] for pair in open('input.txt', 'r').read().split('\n')]
fully_covered_pairs = sum([1 for pair in section_pairs if pair[0] <= pair[1] or pair[1] <= pair[0]])
print(fully_covered_pairs)
# task1: 462 or example: 2


partially_covered_pairs = sum([1 for pair in section_pairs if not pair[0].isdisjoint(pair[1])])
print(partially_covered_pairs)
# task2: 835 or example: 4
