# asscii a=97 .. z=122 A=65 .. Z=90
# task a=1 .. z=26 A=27 .. Z=52
# difference: a=96 (lower), A=38 (upper)
data = open('input.txt', 'r').read().split('\n')


# task1: 7746 or example: 157
def get_priority(item):
    return ord(item) - (96 if 97 <= ord(item) <= 122 else 38)


print(sum([get_priority(set(sack[:int(len(sack)/2)]).intersection(sack[int(len(sack)/2):]).pop()) for sack in data]))

# task2: 2604 or example: 70
print(sum([get_priority(set.intersection(set(data[i]), set(data[i+1]), set(data[i+2])).pop()) for i in range(0, len(data), 3)]))