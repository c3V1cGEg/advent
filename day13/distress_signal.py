from itertools import zip_longest
from functools import cmp_to_key


def is_int(val):
    return isinstance(val, int)


def is_list(val):
    return isinstance(val, list)


def arr_has_idx(arr, idx):
    try:
        t = arr[idx]
        return True
    except IndexError:
        return False


def compx(left_val, right_val):
    print(left_val, right_val)
    return left_val <= right_val


def compare(left_arr, right_arr):
    for left, right in zip_longest(left_arr, right_arr):
        if left is None and right is not None:
            return True
        elif left is not None and right is None:
            return False
        if is_int(left) and is_int(right):
            if left < right:
                return True
            elif left > right:
                return False
            else:
                continue
        elif is_list(left) and is_list(right):
            result = compare(left, right)

            if result is None:
                continue

            return result
        elif is_int(left) and is_list(right):
            result = compare([left], right)

            if result is None:
                continue

            return compare([left], right)
        elif is_list(left) and is_int(right):
            result = compare(left, [right])

            if result is None:
                continue

            return compare(left, [right])


def comparator(left, right):
    c = compare(left, right)
    if c:
        return -1
    elif not c:
        return 1
    else:
        return 0


def task1():
    result = []
    for i in range(0, len(packets_by_two)):
        packet = packets_by_two[i]
        left = eval(packet[0])
        right = eval(packet[1])

        if compare(left, right):
            result.append(i + 1)

    print(sum(result))



def task2():
    all_packets.append([[2]])
    all_packets.append([[6]])
    sorted_packets = sorted(all_packets, key=cmp_to_key(comparator))
    decoder_key = []

    for i in range(0, len(sorted_packets)):
        if sorted_packets[i] == [[2]]:
            decoder_key.append(i+1)
        elif sorted_packets[i] == [[6]]:
            decoder_key.append(i + 1)

    print(decoder_key[0] * decoder_key[1])


packets_by_two = [chunk.split('\n') for chunk in open('input.txt', 'r').read().split('\n\n')]
all_packets = [eval(chunk) for chunk in open('input.txt', 'r').read().replace('\n\n', '\n').split('\n')]

task1()
# task1: 6623, example: 13
task2()
# task2: 23049, example: 140