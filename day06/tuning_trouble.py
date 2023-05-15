def find_unique_sublist(data, length_of_sublist):
    for i in range(length_of_sublist, len(data) + 1):
        if len(data[i-length_of_sublist:i]) == len(set(data[i-length_of_sublist:i])):
            return i


data = [c for c in open('input.txt', 'r').read()]
print(find_unique_sublist(data, 4))
# task1: 1850, example 7
print(find_unique_sublist(data, 14))
# task2: 2823, example 19